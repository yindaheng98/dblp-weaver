import asyncio
from itertools import product, combinations

from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist, video_kw, video_kw2, sr_kw, sr_kw2, opti_kw, opti_kw2, edge_kw, edge_kw2
from example import main

# 模型的关键词
model_kw = {"model", "models", "transformer", "transformers"}
model_kw2 = [{"pre"}, {"train", "trained", "training"}]

# 传输的关键词
trans_kw = {"stream", "streaming", "delivery", "deliver", "cached", "cache", "caching",
            "adapt", "adaptive", "adaption", 'bit', 'bitrate', 'bandwidth', "qoe", "dash"}

# 视频处理的关键词
proc_kw = {"processing", "analytics"}

# 应用的关键词
app_kw = {"communication", "communicate", "conference", "conferencing", "stream", "streaming", "crowdcast"}

keywords = Keywords()
keywords.add_rule_list(
    *list(product(video_kw, *video_kw2)),
    *list(product(video_kw, sr_kw)),
    *list(product(video_kw, *sr_kw2)),
    *list(product(video_kw, model_kw)),
    *list(product(video_kw, *model_kw2)),
    *list(product(video_kw, opti_kw)),
    *list(product(video_kw, *opti_kw2)),
    *list(product(video_kw, trans_kw)),
    *list(product(video_kw, proc_kw)),
    *list(product(video_kw, app_kw)),
    *list(product(video_kw, edge_kw)),
    *list(product(video_kw, *edge_kw2)),
    *list(combinations(video_kw, 2)),
    *list(product(video_kw, {'content', 'quality'}, {"aware"})),
    *list(product(video_kw, {'super'}, {'resolution'})),
)
keywords.add_word_rules('hdr', 'uhd', "VSR")

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(
        summary_path="summary.json",
        paper_path="papers.txt",
        keywords=keywords,
        blacklist=blacklist,
        pid_list=vips,
        journal_list=CCF_A
    ))
