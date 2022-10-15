from pprint import pprint
from itertools import product, combinations

from dblp_crawler import *
from dblp_crawler.data import CCF_A, CCF_B, CCF_C
from dblp_crawler.keyword import *

keywords = Keywords()
keywords.add_rule_list(
    *list(product(
        {"video", "live", "stream", "streaming", "feature", "vision", "resolution", "qoe", "360", "vr"},
        {"delivery", "deliver", "cached", "cache", "caching", "communication", "communicate",
         "quality", "code", "coding", "encode", "encoding", "decode", "decoding",
         "adaptive", "adaption", 'super', 'high', 'low', 'bit', 'bitrate', 'bandwidth',
         "denoising", "denoise", "deblur", "deblurring", "dehaze", "dehazing",
         "restoration", "restore", "enhance", "enhancement", "interpolation", "interpolate", "inpaint", "inpainting",
         'mec', 'edge', "neural", "fog", "mobile", "accelerate", "parallel"}
    )),
    *list(combinations(
        {"video", "live", "stream", "streaming", "feature", "vision", "resolution", "360", "vr"}, 2
    )),
    *list(product(
        {'content', 'quality'},
        {"aware"}
    )),
    """
    *list(product(
        {'mec', 'edge', "fog"},
        {"compute", "computing", "base", "based", "assist", "assisted", "assisting"}
    )),
    """
)
keywords.add_word_rules('hdr', 'uhd', "VSR", 'in-network', 'dash', 'offload', 'offloading')

blacklist = [
    "CVPR Workshops"
]


class GG(Graph):
    def filter_publications_at_crawler(self, publications):
        publications = filter_publications_after(publications, 2019)
        publications = filter_publications_by_journals(publications, CCF_A + CCF_B)
        publications = filter_publications_by_title_with_func(publications, keywords.match_words)
        publications = drop_publications_by_journals(publications, blacklist)
        return publications

    def filter_publications_at_output(self, publications):
        publications = filter_publications_after(publications, 2020)
        publications = filter_publications_by_journals(publications, CCF_A)
        publications = filter_publications_by_title_with_func(publications, keywords.match)
        publications = drop_publications_by_journals(publications, blacklist)
        return publications

    def summary_person(self, person, publications):
        detail = {}

        def get_detail(pub, ccf):
            return dict(
                year=pub.year(), CCF=ccf, journal=pub.journal(),  # title=pub.title(), # too large
                authors=", ".join(str(author) for author in pub.authors()))

        for publication in person.publications():
            detail[publication.key()] = get_detail(publication, 'N')
        for publication in filter_publications_by_journals(person.publications(), CCF_A):
            detail[publication.key()] = get_detail(publication, 'A')
        for publication in filter_publications_by_journals(person.publications(), CCF_B):
            detail[publication.key()] = get_detail(publication, 'B')
        for publication in filter_publications_by_journals(person.publications(), CCF_C):
            detail[publication.key()] = get_detail(publication, 'C')
        return dict(
            **super().summary_person(person, publications),
            detail=detail,
        )


async def main():
    init = [
        # 港中文、港大、南阳理工 多媒体联合实验室 http: // mmlab.ie.cuhk.edu.hk/people.html
        '54/4989-2',  # 香港大学 罗平 http://luoping.me
        '01/5855',  # 南洋理工 吕健勤 模型研究方向
        '16/1278',  # 中科院深圳先进技术研究所 董超, 2016年博士毕业 http://xpixel.group/people.html

        '91/6236-1',  # 港中文 Xiaogang Wang

        # 待整理
        '142/0351',  # 港中文深圳 Fangxin Wang https://mypage.cuhk.edu.cn/academics/wangfangxin/index.html
        '78/1467-1',  # 华为 Qi Tian
        'q/YuQiao1',  # Yu Qiao
        # 清华大学深圳研究院
        '74/1552-1',  # 清深 江勇
        '95/6543',  # 清华 王智
    ]
    g = GG(init, CCF_A)
    for _ in range(32):
        await g.bfs_once()
    summary = g.networkx_summary()
    summary = networkx_drop_noob_once(summary, filter_min_publications=1)
    summary = networkx_drop_thin_edge(summary, filter_min_publications=1)
    pprint(dropped_journal)
    with open("summary.json", 'w', encoding='utf8') as f:
        json.dump(summary_to_json(summary), fp=f, cls=JSONEncoder, indent=2)
    with open("summary.json", 'r', encoding='utf8') as fr:
        j = json.load(fr)
        with open("summary.js", 'w', encoding='utf8') as fw:
            fw.write("let data = " + json.dumps(j, indent=2))
    dump_papers_in_summary(summary, "papers.txt")
    # draw_summary(summary)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
