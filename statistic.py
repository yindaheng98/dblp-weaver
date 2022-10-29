import json

years_to_be_stat = list(range(2012, 2023))


def stat(data):  # d = data['nodes'][0]['data']或data['edges'][0]['data']
    ccf_count = {'A': 0, 'B': 0, 'C': 0, 'N': 0}
    journal_count = {ccf: {} for ccf in ccf_count}
    year_count = {ccf: {year: 0 for year in years_to_be_stat} for ccf in ccf_count}
    for k, pub in data['detail'].items():
        ccf_count[pub["CCF"]] += 1
        if pub["journal"] not in journal_count[pub["CCF"]]:
            journal_count[pub["CCF"]][pub["journal"]] = 0
        journal_count[pub["CCF"]][pub["journal"]] += 1
        if pub["year"] in year_count[pub["CCF"]]:
            year_count[pub["CCF"]][pub["year"]] += 1
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


def is_noob(data):
    return data['detail']['ccf_count']['A'] < 20


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
