function get_ccfpie_option(id, ccfpie_data) {
    return {
        series: [
            {
                type: "pie",
                data: ccfpie_data[id],
                label: {
                    formatter: 'CCF {b}: {c}篇',
                    position: 'inside'
                }
            }
        ]
    }
}
function get_conpie_option(id, conpie_data) {
    return {
        series: [
            {
                type: "pie",
                data: conpie_data[id],
                label: {
                    formatter: '{b}: {c}篇'
                }
            }
        ]
    }
}
function get_line_option(id, line_data) {
    return {
        legend: {
            orient: 'vertical',
            right: 10,
            top: 'center',
        },
        xAxis: {
            name: '年份',
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            data: line_data.years,
        },
        yAxis: {
            name: '论文数'
        },
        series: [
            {
                name: "CCF A",
                id: "A",
                data: line_data.data[id].A,
                type: 'line',
            },
            {
                name: "CCF B",
                id: "B",
                data: line_data.data[id].B,
                type: 'line',
            },
            {
                name: "CCF C",
                id: "C",
                data: line_data.data[id].C,
                type: 'line',
            },
            {
                name: "CCF N",
                id: "N",
                data: line_data.data[id].N,
                type: 'line',
            }
        ]
    }
}
function get_pub_text(id, person_data, pub_data) {
    text = person_data[id] + "\n\n" + pub_data[id].join('\n\n')
    return text.replaceAll('\n', '<br>').replaceAll('\t', '&emsp;')
}

function get_person_cat_data(id, cat_data) {
    return cat_data[id]
}

ccfpie = echarts.init(document.getElementById("ccfpie"));
conpie = echarts.init(document.getElementById("conpie"));
line = echarts.init(document.getElementById("line"));
pub = document.getElementById("publications")

var person_cat_data;
var years;
var ccfs;
var journals;

function change_person(id) {
    ccfpie.setOption(get_ccfpie_option(id, ccfpie_data))
    conpie.setOption(get_conpie_option(id, conpie_data))
    line.setOption(get_line_option(id, line_data))
    pub.innerHTML = get_pub_text(id, person_data, pub_data)

    person_cat_data = cat_data[id]
    years = line_data.years
    ccfs = ccfpie_data[id].map(function (i) { return i['name'] })
    journals = conpie_data[id].map(function (i) { return i['name'] })
}

function show_person_cat_data(years, ccfs, journals, person_cat_data) {
    text = ''
    for (year of years.slice().reverse()) {
        if (!person_cat_data[year])
            continue
        for (ccf of ccfs) {
            if (!person_cat_data[year][ccf])
                continue
            for (journal of journals) {
                if (!person_cat_data[year][ccf][journal])
                    continue
                text += '<b>' + year + ', (CCF ' + ccf + ') ' + journal + "</b>\n\n"
                text += person_cat_data[year][ccf][journal].join('\n\n') + "\n\n"
            }
        }
    }
    return text.replaceAll('\n', '<br>').replaceAll('\t', '&emsp;')
}

ccfpie.on("click", function (properties) {
    pub.innerHTML = show_person_cat_data(years, [properties.name], journals, person_cat_data)
});
conpie.on("click", function (properties) {
    pub.innerHTML = show_person_cat_data(years, ccfs, [properties.name], person_cat_data)
});
line.on("click", function (properties) {
    pub.innerHTML = show_person_cat_data([properties.name], properties.seriesId, journals, person_cat_data)
});