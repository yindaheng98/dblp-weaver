import json

years_to_be_stat = list(range(2010, 2023))


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
    with open("statistic.json", 'w', encoding='utf8') as fw:
        json.dump(j, fw, indent=2)
