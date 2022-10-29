import json
from config import colors

print("正在统计")

years_to_be_stat = list(range(2016, 2023))


def stat(data):  # d = data['nodes'][0]['data']或data['edges'][0]['data']
    ccf_count = {'A': 0, 'B': 0, 'C': 0, 'N': 0}
    journal_count = {ccf: {} for ccf in ccf_count}
    year_count = {year: {ccf: 0 for ccf in ccf_count} for year in years_to_be_stat}
    for k, pub in data['detail'].items():
        if pub["journal"] not in journal_count[pub["CCF"]]:
            journal_count[pub["CCF"]][pub["journal"]] = 0
        journal_count[pub["CCF"]][pub["journal"]] += 1
        if pub["year"] in year_count:
            year_count[pub["year"]][pub["CCF"]] += 1
            ccf_count[pub["CCF"]] += 1
    data['detail'] = dict(
        ccf_count=ccf_count,
        journal_count=journal_count,
        year_count=year_count,
    )
    return data


def stat_all(data):
    for node in data['nodes']:
        node['data'] = stat(node['data'])
    for edge in data['edges']:
        edge['data'] = stat(edge['data'])
    return data


with open("summary.json", 'r', encoding='utf8') as fr:
    j = json.load(fr)
    j = stat_all(j)
    with open("statistic_full.json", 'w', encoding='utf8') as fw:
        json.dump(j, fw, indent=2)

print("正在筛选文章多的老师")


def is_noob(data):
    return data['detail']['ccf_count']['A'] < 32


def drop_noob(data):
    nodes = []
    drop_nodes = set()
    for n in data['nodes']:
        if is_noob(n["data"]):
            drop_nodes.add(n["id"])
        else:
            nodes.append(n)
    edges = []
    for e in data['edges']:
        if e['from'] in drop_nodes or e['to'] in drop_nodes:
            pass
        else:
            edges.append(e)
    return dict(nodes=nodes, edges=edges)


with open("statistic_full.json", 'r', encoding='utf8') as fr:
    j = json.load(fr)
    j = drop_noob(j)
    with open("statistic.json", 'w', encoding='utf8') as fw:
        json.dump(j, fw, indent=2)

print("正在转换成vis数据")


def export_ccfpie_data(data):
    ccfpie_data = {}
    for n in data['nodes']:
        ccfpie_data[n['id']] = [
            dict(name="CCF A", value=n['data']['detail']['ccf_count']['A']),
            dict(name="CCF B", value=n['data']['detail']['ccf_count']['B']),
            dict(name="CCF C", value=n['data']['detail']['ccf_count']['C']),
        ]
    return ccfpie_data


def export_conpie_data(data):
    conpie_data = {}
    for n in data['nodes']:
        d = []
        for ccf in ['A', 'B', 'C']:
            for journal, journal_count in n['data']['detail']['journal_count'][ccf].items():
                d.append(dict(name=journal, value=journal_count))
        conpie_data[n['id']] = d
    return conpie_data


def export_line_data(data):
    line_data = {}
    for n in data['nodes']:
        d = {'A': [], 'B': [], 'C': [], 'years': years_to_be_stat}
        for year in years_to_be_stat:
            d['A'].append(n['data']['detail']['year_count'][str(year)]['A'])
            d['B'].append(n['data']['detail']['year_count'][str(year)]['B'])
            d['C'].append(n['data']['detail']['year_count'][str(year)]['C'])
        line_data[n['id']] = d
    return line_data


def node_value(node):
    return node['data']['detail']['ccf_count']['A']


def edge_value(edge):
    return edge['data']['detail']['ccf_count']['A']


def node_color(node):
    if len(node['data']['publications']) < 2:  # 透明掉相关文章数小于2的
        return 'rgba(97,195,238,0.2)'
    for color, who in colors.items():
        if node['id'] in who:
            return color
    return 'rgb(97,195,238)'


def export_graph_data(data):
    graph_data = dict(nodes=[], edges=[])
    for n in data['nodes']:
        graph_data['nodes'].append({
            'id': n['id'], 'label': n['label'], 'value': node_value(n),
            'color': node_color(n),
            'data': {
                'publications': n['data']['publications'],
                'person': n['data']['person']
            }
        })
    for e in data['edges']:
        graph_data['edges'].append({
            'from': e['from'], 'to': e['to'], 'value': edge_value(e),
            'data': {'publications': e['data']['publications']}
        })
    return graph_data


with open("statistic.json", 'r', encoding='utf8') as fr:
    j = json.load(fr)
    graph_data = export_graph_data(j)
    ccfpie_data = export_ccfpie_data(j)
    conpie_data = export_conpie_data(j)
    line_data = export_line_data(j)
    with open("summary.js", 'w', encoding='utf8') as fw:
        fw.write("let data = " + json.dumps(graph_data, indent=2) + ";\n")
        fw.write("let ccfpie_data = " + json.dumps(ccfpie_data, indent=2) + ";\n")
        fw.write("let conpie_data = " + json.dumps(conpie_data, indent=2) + ";\n")
        fw.write("let line_data = " + json.dumps(line_data, indent=2) + ";\n")
