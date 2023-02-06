import asyncio
from itertools import product

from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist, video_kw, video_kw2
from example import main

# 视频的关键词
keywords = Keywords()
keywords.add_word_rules(*video_kw)
keywords.add_rule_list(*list(product(*video_kw2)))

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(
        summary_path="summary_video.json",
        paper_path="papers_video.txt",
        keywords=keywords,
        blacklist=blacklist,
        pid_list=vips,
        journal_list=CCF_A
    ))
