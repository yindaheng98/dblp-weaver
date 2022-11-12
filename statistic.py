import json
from config import years_to_be_stat, ccf_to_be_stat, is_noob, is_weak, node_value, edge_value, node_color

print("正在统计")


def stat(data):
    ccf_count = {ccf: 0 for ccf in ccf_to_be_stat}
    journal_count = {ccf: {} for ccf in ccf_count}
    year_count = {year: {ccf: 0 for ccf in ccf_count} for year in years_to_be_stat}
    for k, pub in data['detail'].items():
        if pub["year"] not in year_count:
            continue
        if pub["journal"] not in journal_count[pub["CCF"]]:
            journal_count[pub["CCF"]][pub["journal"]] = 0
        journal_count[pub["CCF"]][pub["journal"]] += 1
        year_count[pub["year"]][pub["CCF"]] += 1
        ccf_count[pub["CCF"]] += 1
    data['detail'] = dict(
        ccf_count=ccf_count,
        journal_count=journal_count,
        year_count=year_count,
    )
    return data


def cat(data):
    c = {}
    for k, pub in data['detail'].items():
        if pub["year"] not in years_to_be_stat:
            continue
        if pub["year"] not in c:
            c[pub["year"]] = {}
        if pub["CCF"] not in c[pub["year"]]:
            c[pub["year"]][pub["CCF"]] = {}
        if pub["journal"] not in c[pub["year"]][pub["CCF"]]:
            c[pub["year"]][pub["CCF"]][pub["journal"]] = []
        c[pub["year"]][pub["CCF"]][pub["journal"]].append("%s\n\t%s\n\t%s" % (k, pub['authors'], pub['title']))
    return c


def stat_all(data):
    for node in data['nodes']:
        node['category'] = cat(node['data'])
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
        if is_noob(n):
            drop_nodes.add(n["id"])
        else:
            nodes.append(n)
    edges = []
    for e in data['edges']:
        if e['from'] in drop_nodes or e['to'] in drop_nodes:
            pass
        elif is_weak(e):
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
        ccfpie_data[n['id']] = [dict(name=ccf, value=n['data']['detail']['ccf_count'][ccf]) for ccf in ccf_to_be_stat]
    return ccfpie_data


def export_conpie_data(data):
    conpie_data = {}
    for n in data['nodes']:
        d = []
        for ccf in ccf_to_be_stat:
            d_ccf = []
            for journal, journal_count in n['data']['detail']['journal_count'][ccf].items():
                d_ccf.append(dict(name=journal, value=journal_count))
            d_ccf.sort(key=lambda x: x['value'], reverse=True)
            d.extend(d_ccf)
        conpie_data[n['id']] = d
    return conpie_data


def export_line_data(data):
    line_data = {}
    for n in data['nodes']:
        d = {ccf: [] for ccf in ccf_to_be_stat}
        for year in years_to_be_stat:
            for ccf in ccf_to_be_stat:
                d[ccf].append(n['data']['detail']['year_count'][str(year)][ccf])
        line_data[n['id']] = d
    return dict(data=line_data, years=years_to_be_stat)


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


def export_cat_data(data):
    cat_data = {n['id']: n['category'] for n in data['nodes']}
    return cat_data


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
    cat_data = export_cat_data(j)
    ranking_data = export_ranking_data(j)
    with open("summary.js", 'w', encoding='utf8') as fw:
        fw.write("let data = " + json.dumps(graph_data, indent=2) + ";\n")
        fw.write("let person_data = " + json.dumps(person_data, indent=2) + ";\n")
        fw.write("let pub_data = " + json.dumps(pub_data, indent=2) + ";\n")
        fw.write("let ccfpie_data = " + json.dumps(ccfpie_data, indent=2) + ";\n")
        fw.write("let conpie_data = " + json.dumps(conpie_data, indent=2) + ";\n")
        fw.write("let line_data = " + json.dumps(line_data, indent=2) + ";\n")
        fw.write("let cat_data = " + json.dumps(cat_data, indent=2) + ";\n")
        fw.write("let ranking_data = " + json.dumps(ranking_data, indent=2) + ";\n")
