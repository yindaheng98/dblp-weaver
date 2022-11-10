import json
from config import years_to_be_stat, is_noob, is_weak, node_value, edge_value, node_color

print("正在统计")


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
        raw_data=data['detail'],
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
        elif is_weak(e["data"]):
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


def export_graph_data(data):
    graph_data = dict(nodes=[], edges=[])
    for n in data['nodes']:
        graph_data['nodes'].append({
            'id': n['id'], 'label': n['label'], 'value': node_value(n),
            'color': node_color(n),
        })
    for e in data['edges']:
        graph_data['edges'].append({
            'from': e['from'], 'to': e['to'], 'value': edge_value(e),
            'data': {'publications': e['data']['publications']}
        })
    return graph_data


def export_person_data(data):
    person_data = {n['id']: n['data']['person'] for n in data['nodes']}
    return person_data


def export_pub_data(data):
    pub_data = {n['id']: n['data']['publications'] for n in data['nodes']}
    return pub_data


def export_raw_data(data):
    raw_data = {n['id']: n['data']['detail']['raw_data'] for n in data['nodes']}
    return raw_data


import numpy as np


def export_ranking_data(data):
    ranking_value = np.array([node_value(n) for n in data['nodes']])
    ranking_value_colors = np.array([
        dict(value=node_value(n), itemStyle=dict(color=node_color(n)))
        for n in data['nodes']])
    ranking_label = np.array([n['label'] for n in data['nodes']])
    ranking_id = np.array([n['id'] for n in data['nodes']])
    sort_arg = ranking_value.argsort()
    ranking_data = dict(
        id=ranking_id[sort_arg].tolist(),
        label=ranking_label[sort_arg].tolist(),
        data=ranking_value_colors[sort_arg].tolist()
    )
    return ranking_data


with open("statistic.json", 'r', encoding='utf8') as fr:
    j = json.load(fr)
    graph_data = export_graph_data(j)
    person_data = export_person_data(j)
    pub_data = export_pub_data(j)
    ccfpie_data = export_ccfpie_data(j)
    conpie_data = export_conpie_data(j)
    line_data = export_line_data(j)
    raw_data = export_raw_data(j)
    ranking_data = export_ranking_data(j)
    with open("summary.js", 'w', encoding='utf8') as fw:
        fw.write("let data = " + json.dumps(graph_data, indent=2) + ";\n")
        fw.write("let person_data = " + json.dumps(person_data, indent=2) + ";\n")
        fw.write("let pub_data = " + json.dumps(pub_data, indent=2) + ";\n")
        fw.write("let ccfpie_data = " + json.dumps(ccfpie_data, indent=2) + ";\n")
        fw.write("let conpie_data = " + json.dumps(conpie_data, indent=2) + ";\n")
        fw.write("let line_data = " + json.dumps(line_data, indent=2) + ";\n")
        fw.write("let raw_data = " + json.dumps(raw_data, indent=2) + ";\n")
        fw.write("let ranking_data = " + json.dumps(ranking_data, indent=2) + ";\n")
