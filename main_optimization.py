from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from example import main
from main import blacklist

# 视频的关键词
keywords = Keywords()
keywords.add_word_rules(
    "quantize", "quantization",
    "compress", "compression",
    "distillate", "distilling", "distillation",
    "normalization",
    "adversarial", "adversarially",
)

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(
        summary_path="summary_optimization.json",
        paper_path="papers_optimization.txt",
        keywords=keywords,
        blacklist=blacklist,
        pid_list=[],
        journal_list=CCF_A
    ))
