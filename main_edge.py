from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist, edge_kw
from example import main

# 视频的关键词
keywords = Keywords()
keywords.add_word_rules(*edge_kw)

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(
        summary_path="summary_edge.json",
        paper_path="papers_edge.txt",
        keywords=keywords,
        blacklist=blacklist,
        pid_list=vips,
        journal_list=CCF_A
    ))
