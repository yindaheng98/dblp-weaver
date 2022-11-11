from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist
from example import main

# 视频的关键词
keywords = Keywords()
keywords.add_word_rules(
    "video", "live", "livecast", "livecast", "crowdcast", "crowdcasting",
    "resolution", "360", "vr", "camera", "hdr", 'uhd', "VSR"
)

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
