from itertools import product

from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from sets import vips, blacklist
from example import main

# 视频的关键词
video_kw = {
    "video", "live", "livecast", "livecast", "crowdcast", "crowdcasting",
    "feature", "vision", "visual", "resolution",
    "360", "vr", "camera", "hdr", 'uhd', "VSR"
}

# 超分的关键词
sr_kw = {"denoise", "denoising", "deblur", "deblurring", "dehaze", "dehazing", "restoration", "restore", "restoring",
         "interpolation", "interpolate", "inpaint", "inpainting",
         "enhance", "enhancement", "neural", "deep", "learn", "learning", "intelligent", "transformer"}
sr_kw2 = [{"super"}, {"resolution"}]
# 模型的关键词
model_kw = {"model", "models", "transformer", "transformers"}
model_kw2 = [{"pre"}, {"train", "trained", "training"}]

# 传输的关键词
trans_kw = {"stream", "streaming", "delivery", "deliver", "cached", "cache", "caching",
            "adapt", "adaptive", "adaption", 'bit', 'bitrate', 'bandwidth', "qoe", "dash"}

# 视频处理的关键词
proc_kw = {"processing", "analytics"}

# 优化的关键词
opti_kw = {"optimize", "optimization",
           "quantize", "quantization",
           "compress", "compression",
           "distillate", "distilling", "distillation",
           "normalization", "real-time"}
opti_kw2 = [{"real"}, {"time"}]

# 应用的关键词
app_kw = {"communication", "communicate", "conference", "conferencing", "stream", "streaming", "crowdcast"}

# 边缘的关键词
edge_kw = {'mec', 'edge', 'in-network', "fog", "mobile"}
# 计算的关键词
comp_kw = {'offload', 'offloading', "accelerate", "parallel", "compute", "computing", "assist", "assisted"}
# 边缘计算的关键词
edge_comp_kw = edge_kw.union(comp_kw)

keywords = Keywords()
keywords.add_rule_list(
    *list(product(video_kw, sr_kw)),
    *list(product(video_kw, *sr_kw2)),
    *list(product(video_kw, model_kw)),
    *list(product(video_kw, *model_kw2)),
    *list(product(video_kw, opti_kw)),
    *list(product(video_kw, *opti_kw2)),
    *list(product(video_kw, trans_kw)),
    *list(product(video_kw, proc_kw)),
    *list(product(video_kw, app_kw)),
    *list(product(video_kw, edge_comp_kw)),
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
