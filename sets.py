vips_ai = {
    # 模型优化
    '28/10261-1',  # 上海交通大学 Weinan Zhang
    '43/5685-1',  # 上海交通大学 俞勇
    # 视频相关的模型优化
    '54/4989-2',  # 香港大学 罗平
    '91/6236-1',  # 港中文 Xiaogang Wang 但只招博后和RA
    '28/4556-1',  # 香港中文大学 余備
    '172/4863',  # 香港科技大学 广州 Yuzhe Ma
    '176/1445',  # 香港大学 Xiaojuan Qi
    '117/4819',  # 香港中文大学 陳启峰
    # 图片相关的模型优化
    '64/5666-6',  # 香港理工 Lei Zhang
    # 机器学习理论
    '82/6362-1',  # 香港科技大学 Qiang Yang
    '06/4171',  # 香港中文大学 James Cheng
    '50/2644-1',  # 清华大学 朱军
    '94/3104-1',  # 中科院 王颖 太硬件了
}
vips_app = {
    # 无人机+图像
    '07/9968',  # 香港科技大学 沈劭劼
    # 边缘计算
    '99/4094',  # 清华大学 院士 张尧学
    '01/267-1',  # 香港理工大学 Song Guo
    '27/2403',  # 清华大学 刘云浩
    '59/5806-2',  # 清华大学 杨铮
    '93/2334-8',  # 清华大学 Yong Li
    '142/0351',  # 港中文 Fangxin Wang 21年刚招生
    '74/1552-1',  # 清华大学深圳研究院 江勇
    '95/6543',  # 清华大学深圳研究院 王智
    '49/8398',  # 芝加哥大学 Junchen Jiang
    # 分布式机器学习理论
    '82/6362-1',  # 香港科技大学 Qiang Yang
    '06/4171',  # 香港中文大学 James Cheng
    '181/2839',  # 香港科技大学 Kai Chen
    # 交叉
    '165/784',  # 香港中文大学 Qi DOU
    # 多媒体
    'l/JiangchuanLiu',  # Simon Fraser University Jiangchuan (JC) LIU
    'l/BaochunLi',  # 多伦多大学 Baochun Li
    '97/6308-1',  # 清华大学 朱文武
    '312/6561',  # 港中文 Jianwei Huang
    'c/KwangTingCheng',  # 香港科技大学 Kwang-Ting (Tim) Cheng
    '55/3521',  # 清华大学 刘云新
    # 边缘计算
    '142/0351',  # 港中文 Fangxin Wang 21年刚招生
    '48/4914',  # 港中文 Shuguang Cui 研究院FNii的leader https://fnii.cuhk.edu.cn/
    '73/8637',  # 北邮 Shangguang Wang
    'c/JiannongCao',  # 香港理工 Jiannong Cao
    '181/2839',  # 香港科技 Kai Chen
    'l/JohnCSLui',  # 香港中文
    '60/6865',  # 纽约州立大学布法罗分校 Chunming Qiao
    '59/1232',  # Arizona State University  Junshan Zhang
    '00/468',  # 清华大学 任炬
    '97/6589-1',  # 何强
    '34/4445',  # 香港科技 伍楷舜 三年4篇Mobicom的大佬
    # 实时视频流
    '06/2128',  # 孙立峰 清华大学计算机科学与技术系，视频传输
    '91/2346-1',  # 崔勇 清华大学计算机科学与技术系
    '84/2519-2', '42/5105-1',  # 北美的，唐安然的参考博导
}
vips = vips_ai.union(vips_app)
vips_thu = {  # 清华的
    "67/3001",  # 杨广文, 高性能计算
    "51/3710-5",  # 刘洋, NLP的
}
normal = {
    # 边缘计算+视频
    'w/JieWu1',  # 吴杰 Temple University 吴杰教授是中国计算机学会海外杰出贡献奖获得者,跟国内各大高校都有密切的合作关系
    'c/GuohongCao',  # Guohong Cao,宾夕法尼亚州立大学
    '21/1550-1',  # 女教授
    '33/4854-1',  # 悉尼大学
    '84/8277',  # 京东
    '155/3173',  # 海康威视
    '64/146',  # 北京理工
    '31/1277',  # 澳大利亚的
    '31/5772',  # INFOCOM太多
    # 北大 数字视频编解码技术国家工程实验室
    'g/WenGao',  # 实验室主任 北大 高文院士
    '38/559',  # 北大刘云淮
    # 面向机器的视频编解码
    '12/7627-1',  # 计算所 张新峰 副教授
    '40/5402',  # 北大 马思伟
    '126/4540',
    '58/9145-1',  # 香港城市大学 Shiqi Wang, 2014 年博士毕业，视频编码+超分
    # https://www.zhihu.com/question/22814279/answer/1798183969
    '156/2359',  # 南阳理工 杨文瀚, 2018 年博士毕业带点超分辨率 北大王选计算机研究所
    '38/559',  # 北大刘云淮
    '18/30',

    '55/3521',  # 清华刘云新

    # 模型优化加速
    '86/896', '63/8217-1',  # 华为的
    '150/6667', '97/2966-2',  # 悉尼大学的
    '93/6765-1',  # 合肥科技
    '45/7737', 's/TajanaSimunic', '14/2770', 'x/YuanXie',  # 美国的
    '50/2644-1',  # 手头一堆6年的博士
    '56/8278',  # 南洋理工大佬
    '03/281',  # 匹兹堡大学
    '127/6999',  # 阿里巴巴的
    '84/2644',  # 微软的
    '20/612', '96/5144',  # 中科大
    '86/5681',  # 厦门大学
    '97/1213-1',  # 德国的
    '39/8969',  # IBM的
    '94/7236',  # 美国的
    '98/4156',  # 杭州科技
    '12/5444-1',  # 京东的
    '12/5444-1',  # 牛津
    '38/5435',  # 北理工
    'd/LarrySDavis',  # 美国

    # 偏通信
    '25/3972-1',

    # 边缘计算+视频
    '49/8398',
    '84/6614',  # 华科的
    '45/2091-1',  # 北京交通大学
    '17/6315',  # 日本的，体积视频研究（国内少见的新方向）
    'l/JiangchuanLiu',  # 国外的
    '35/7092',  # 字节的
    '72/628-1',  # 国外的
    '83/514',

    # 偏系统的模型研究
    'd/FernandoDelaTorre', '07/954',

    # 光场（新方向）
    '23/1818', '54/6827', '136/9389',

    # 体积视频研究（国内少见的新方向）
    'w/ChaoliWang', '54/476-1', '08/5351', 's/RameshKSitaraman', '64/10521', '35/1211', '90/4174', '81/5358', '37/8397',
    '12/5388',
    # 大连理工
    '61/4041', '65/2749',
    # 南京大学
    '69/6137-1', '96/2572', '24/3318', '124/6911',
    # 德国的？
    '55/3346', '232/2002', 's/HansPeterSeidel', '180/6438',
    '117/4311',  # 20篇SIGCOMM，牛逼
    '29/4638',  # 港理工深圳的院长

    '133/3824',  # 新加坡管理大学
}
pure_sota = {  # 纯模型研究
    '24/8616', '176/4020', '00/5815-1', '166/2763', '61/5017', '06/10816', '119/0230',
    '01/5855', '127/0477', '79/3711', '14/6655', '24/4105-8', '97/8704-54', '46/5881', '17/1926',
    '33/4058', '158/1384', '53/520', '77/6697', '51/3185', '31/5649', '16/1278', '205/3991', '23/2089',
    '05/6300-2', '46/3391', '126/3420', '39/3695', '59/4859', '179/6089', '99/4522', '17/2703-1',
    '10/8359-1', '64/2916', '139/6983', '19/3230', 'c/LiChen21', '75/2339', '13/322', '00/5012',
    '10/239-2', '97/3742', '84/4965', 's/HTShen', '92/10934', '172/1282', '75/1030', '40/566',
    '45/7592', '09/1365-5', '92/2954', '75/1030', '45/7592', 'y/JianYang3', '69/4250', '40/566',
    '16/8313', '75/1281', 'v/AntonvandenHengel', '51/5804', '56/1673', '23/8653', '17/1152-5',
    'c/AmitKRoyChowdhury', '126/4457', '84/7019', '42/5677', '63/34', '79/1442-6', '55/957-8',
    '151/8848', '56/2053-1', '78/1123', '119/9269', '51/1815', '39/2152', '89/5820', '65/7804',
    '49/3441', 'w/KwanYeeKennethWong', '16/9879', '117/4770', '93/2671', '43/9044', '98/1737-2',
    '54/6827', '136/9389', '23/1818', '95/3056', '24/5818', '27/7402-1', '17/7992', '53/6088',
    'q/YuQiao1', '16/1278', '31/5649', '90/6896', '46/999', '07/4227-1', '185/7848', '24/6606',
    '119/4026', '64/6896', '68/4388', '10/10313', '136/0900', '51/3710', '74/4917', '139/6993',
    '70/10575', '123/9849', '76/834-1', '23/8015', '205/3148',
}
others = {
    # 视频质量检测
    '20/5353', 'b/ACBovik', '13/3788', '92/6630', '01/8056', '03/5833', '14/3737', '122/2673', '00/5012-1',
    # 纯ABR研究
    '93/347', '91/2346-1', '10/5630-1', '49/8116', '09/6350', '200/2255',
    # 通信研究
    '46/3359-1',
    # 可视化研究
    '49/6702', '65/1792', '38/803',
    # 不相关
    '26/6037', '86/7615', 'm/SamuelMadden', 's/MichaelStonebraker', '27/6045', '41/1662-1', '84/3254-1', '78/1467-1',
    '11/5357-1', '218/7793', '10/2717', '75/7785', '78/713-2', '51/3710-3',
    # 北大 数字视频编解码技术国家工程实验室
    '02/894', 's/JunSun12', '02/2683', '32/197', 'd/LingyuDuan',
    '38/2763',  # 清华 王生进 机器视觉机器人
    '58/5750-1'  # 博士平均毕业时间》=6年
    '59/1007',  # 推荐系统
    # 计算机图形学
    '23/4197',
    # 图数据库
    'y/JXuYu',  # 香港中文大学 Jeffrey Xu Yu, 于旭
    'm/ChunyanMiao',  # 南洋理工 Chunyan Miao
    '94/1128',
    'c/LeiChen0002',  # 香港科技 Lei Chen
    # 水
    '181/2834',
}

blacklist = {
    r".* workshop[s]*"
}

# 视频的关键词
video_kw = {
    "video", "live", "livecast", "livecast", "crowdcast", "crowdcasting",
    "vision", "visual", "resolution", "streaming",
    "360", "vr", "ar", "camera", "hdr", 'uhd', "VSR"
}
video_kw2 = [{"augmented", "augment", "virtual"}, {"reality"}]

# 超分的关键词
sr_kw = {"denoise", "denoising", "deblur", "deblurring", "dehaze", "dehazing", "restoration", "restore", "restoring",
         "interpolation", "interpolate", "inpaint", "inpainting"}
sr_kw2 = [{"super", "neural", "video"}, {"resolution", "enhance", "enhancement"}]

# 优化的关键词
opti_kw = {
    "accelerate", "accelerated", "acceleration", "accelerator",
    "quantize", "quantization",
    "compress", "compression", "compressive",
    "normalization", "normalize",
    "binarization", "binarize", "binarized", "binary",
    "QAT", "PTQ",
    "tune", "tuning",
}
opti_kw2 = [{"real"}, {"time"}]

# 模型稳定性的关键词
robust_kw2 = [{"adversarially", "adversarial"},
              {"attack", "attacking",
               "robust", "robustness",
               "example", "examples", }]
# 分布式计算的关键词
distri_kw = {"distributed", "distribute", "distribution", "parallel", "compute", "computing"}
distri_kw2 = [{"communication"}, {"efficient"}]

# 边缘的关键词
edge_kw = {'mec', 'edge', 'in-network', "fog", 'offload', 'offloaded', 'offloading'}
edge_kw2 = [{'mobile'}, {"accelerate", "acceleration"}]

from dblp_crawler.keyword import Keywords

important_keywords = Keywords()
important_keywords.add_word_rules("live", "livecast", "livecasting", "fog", "quantization", "quantize")
