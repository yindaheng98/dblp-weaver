from sets import vips, normal, others, pure_sota

years_to_be_stat = list(range(2016, 2023))


def is_noob(node):
    if node["id"] in vips:
        return False
    year_count = node['data']['detail']["year_count"]
    return year_count["2022"]['A'] + year_count["2021"]['A'] + year_count["2020"]['A'] < 16


def is_weak(edge):
    if edge["from"] in vips or edge["to"] in vips:
        return False
    year_count = edge['data']['detail']["year_count"]
    return year_count["2022"]['A'] + year_count["2021"]['A'] + year_count["2020"]['A'] < 3


def node_value(node):
    return len(node['data']["publications"])


def edge_value(edge):
    return edge['data']['detail']['ccf_count']['A']


colors = {
    'red': vips,
    'green': normal,
    'rgba(192,192,192,0.5)': others.union(pure_sota)
}


def node_color(node):
    for color, who in colors.items():
        if node['id'] in who:
            return color
    if len(node['data']['publications']) < 2:  # 透明掉相关文章数小于2的
        return 'rgba(97,195,238,0.2)'
