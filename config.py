import re

from sets import vips, normal, others, pure_sota, important_keywords

years_to_be_stat = list(range(2016, 2023))
ccf_to_be_stat = ['A', 'B', 'C', 'N']


def is_noob(node):
    if node["id"] in vips:
        return False
    year_count = node['data']['detail']["year_count"]
    return year_count["2022"]['A'] + year_count["2021"]['A'] + year_count["2020"]['A'] < 16


def is_weak(edge):
    if edge["from"] in vips or edge["to"] in vips:
        return False
    year_count = edge['data']['detail']["year_count"]
    return sum([
        sum(year_count["2022"].values()),
        sum(year_count["2021"].values()),
        sum(year_count["2020"].values()),
    ]) < 4


def node_value(node):
    return node['data']['detail']['ccf_count']['A']


def edge_value(edge):
    return sum(edge['data']['detail']['ccf_count'].values())


colors = {
    'red': vips,
    'green': normal,
    'rgba(192,192,192,0.5)': others.union(pure_sota)
}


def node_color(node):
    for color, who in colors.items():
        if node['id'] in who:
            return color
    for pub in node['data']['publications']:
        if important_keywords.match(pub):
            return 'rgb(255,69,0)'
    journal_count = node['data']['detail']['journal_count']['A']
    cv_count = 0  # 统计纯模型研究的发表数
    if 'CVPR' in journal_count:
        cv_count += journal_count['CVPR']
    if 'CVPR Workshops' in journal_count:
        cv_count += journal_count['CVPR Workshops']
    if 'ICCV' in journal_count:
        cv_count += journal_count['ICCV']
    if 'IEEE Trans. Image Process.' in journal_count:
        cv_count += journal_count['IEEE Trans. Image Process.']
    for key in journal_count:
        if re.search(r"^ACL", key):
            cv_count += journal_count[key]
    if 'IEEE Trans. Image Process.' in journal_count:
        cv_count += journal_count['IEEE Trans. Image Process.']
    if cv_count / node['data']['detail']['ccf_count']['A'] > 0.2:
        return 'rgba(192,192,192,0.5)'
    if len(node['data']['publications']) < 2:  # 透明掉相关文章数小于2的
        return 'rgba(97,195,238,0.2)'
