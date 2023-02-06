import asyncio
from itertools import product

from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist, distri_kw, distri_kw2, opti_kw, opti_kw2, robust_kw2
from example import main

keywords = Keywords()
keywords.add_word_rules(*opti_kw, *distri_kw)
keywords.add_rule_list(
    *list(product(*robust_kw2)),
    *list(product(*distri_kw2)),
    *list(product(*opti_kw2)),
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
