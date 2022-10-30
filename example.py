from dblp_crawler import *
from dblp_crawler.data import CCF_A, CCF_B, CCF_C
from dblp_crawler.keyword import *


def construct_detail(publications):
    detail = {}

    def get_detail(pub, ccf):
        return dict(
            year=pub.year(), CCF=ccf, journal=pub.journal(),  # title=pub.title(), # too large
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


class GG(Graph):
    def __init__(self, pid_list: [str], journal_list: [str], keywords: Keywords, blacklist: [str]):
        super().__init__(pid_list, journal_list)
        self.keywords = keywords
        self.blacklist = blacklist

    def filter_publications_at_crawler(self, publications):
        publications = filter_publications_after(publications, 2019)
        publications = filter_publications_by_journals(publications, CCF_A + CCF_B)
        publications = filter_publications_by_title_with_func(publications, self.keywords.match_words)
        publications = drop_publications_by_journals(publications, self.blacklist)
        return publications

    def filter_publications_at_output(self, publications):
        publications = filter_publications_after(publications, 2020)
        publications = filter_publications_by_journals(publications, CCF_A)
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
