import json
from filter import *
from draw import *
from dblp_crawler.summarizer.networkx import *
from dblp_crawler.data import CCF_A, CCF_B, CCF_C
from dblp_crawler.keyword import Keywords
import networkx as nx
from dblp_crawler import DBLPPerson, Publication


def construct_detail(publications):
    detail = {}

    def get_detail(pub, ccf):
        return dict(
            year=pub.year(), CCF=ccf, journal=pub.journal(), title=pub.title(),  # maybe too large
            authors=", ".join(str(author) for author in pub.authors()))

    for publication in publications:
        detail[publication.key()] = get_detail(publication, 'N')
    for publication in filter_publications_by_journals(publications, CCF_A):
        detail[publication.key()] = get_detail(publication, 'A')
    for publication in filter_publications_by_journals(publications, CCF_B):
        detail[publication.key()] = get_detail(publication, 'B')
    for publication in filter_publications_by_journals(publications, CCF_C):
        detail[publication.key()] = get_detail(publication, 'C')
    return detail


class GG(NetworkxGraph):
    def __init__(self, keywords: Keywords = None, blacklist: [str] = [], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keywords = keywords
        self.blacklist = blacklist

    def filter_publications_at_crawler(self, publications):
        # publications = filter_publications_after(publications, 2016)  # 6年内
        publications = filter_publications_after(publications, 2019)  # 3年内
        publications = filter_publications_by_journals(publications, CCF_A + CCF_B)
        if self.keywords:
            publications = filter_publications_by_title_with_func(publications, self.keywords.match_words)
        publications = drop_publications_by_journals(publications, self.blacklist)
        return publications

    def filter_publications_at_output(self, publications):
        publications = filter_publications_after(publications, 2019)  # 3年内
        publications = filter_publications_by_journals(publications, CCF_A)
        if self.keywords:
            publications = filter_publications_by_title_with_func(publications, self.keywords.match)
        publications = drop_publications_by_journals(publications, self.blacklist)
        return publications

    def summary_person(self, person, publications):
        return dict(
            **super().summary_person(person, publications),
            detail=construct_detail(list(person.publications())),
        )

    def summary_cooperation(self, a, b, publications):
        all_publications = {}
        for pub in a.publications():
            if pub.key() in all_publications:
                continue
            if b.pid() in list(author.pid() for author in pub.authors()):
                all_publications[pub.key()] = pub
        for pub in b.publications():
            if pub.key() in all_publications:
                continue
            if a.pid() in list(author.pid() for author in pub.authors()):
                all_publications[pub.key()] = pub
        return dict(
            **super().summary_cooperation(a, b, publications),
            detail=construct_detail(list(all_publications.values())),
        )


def networkx_drop_noob_once(g, filter_min_publications=3):
    for node, data in list(g.nodes(data=True)):
        if data is None or 'publications' not in data or len(data['publications']) < filter_min_publications:
            # 文章数量太少？
            g.remove_node(node)  # 应该不是老师吧
    return g


def networkx_drop_thin_edge(g: nx.Graph, filter_min_publications=3):
    for a, b, data in list(g.edges(data=True)):
        if data is None or 'publications' not in data or len(data['publications']) < filter_min_publications:
            # 文章数量太少？
            g.remove_edge(a, b)  # 那应该不是紧密协作
    return g


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DBLPPerson):
            return obj.pid() + "\n" + str(obj.person())
        if isinstance(obj, Publication):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


async def main(summary_path, paper_path, limit: int = 0,
               drop_noob_node=True, drop_thin_edge=True,
               *args, **kwargs):
    g = GG(*args, **kwargs)
    while min(*(await g.bfs_once())) > 0 and (limit != 0):
        print("Still running......")
        limit -= 1
    summary = g.graph_summary()
    if drop_noob_node:
        summary = networkx_drop_noob_once(summary, filter_min_publications=1)
    if drop_thin_edge:
        summary = networkx_drop_thin_edge(summary, filter_min_publications=1)
    with open(summary_path, 'w', encoding='utf8') as f:
        json.dump(summary_to_json(summary), fp=f, cls=JSONEncoder, indent=2)
    dump_papers_in_summary(summary, paper_path)
