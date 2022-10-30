from itertools import product
from pprint import pprint

from dblp_crawler import *
from dblp_crawler.data import CCF_A
from dblp_crawler.keyword import *
from example import GG

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
sr_kw2 = {{"super"}, {"resolution"}}
# 模型的关键词
model_kw = {"model", "models", "transformer", "transformers"}
model_kw2 = {{"pre"}, {"train", "trained", "training"}}

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
opti_kw2 = {{"real"}, {"time"}}

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

blacklist = [
    "CVPR Workshops"
]


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
    g = GG(init, CCF_A, keywords, blacklist)
    while (await g.bfs_once()) > 0:
        print("Still running......")
    summary = g.networkx_summary()
    summary = networkx_drop_noob_once(summary, filter_min_publications=1)
    summary = networkx_drop_thin_edge(summary, filter_min_publications=1)
    pprint(dropped_journal)
    with open("summary.json", 'w', encoding='utf8') as f:
        json.dump(summary_to_json(summary), fp=f, cls=JSONEncoder, indent=2)
    dump_papers_in_summary(summary, "papers.txt")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
