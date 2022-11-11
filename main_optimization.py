from itertools import product
from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist
from example import main

keywords = Keywords()
keywords.add_word_rules(
    "accelerate", "accelerated", "acceleration", "accelerator",
    "quantize", "quantization",
    "compress", "compression", "compressive",
    "normalization", "normalize",
    "binarization", "binarize", "binarized", "binary",
    "QAT", "PTQ",
    "tune", "tuning",
)
keywords.add_rule_list(
    *list(product({"adversarially", "adversarial"},
                  {"attack", "attacking",
                   "robust", "robustness",
                   "example", "examples", })),
    {"communication", "efficient", "distributed", "distribute", "distribution"},
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
        pid_list=vips,
        journal_list=CCF_A
    ))
