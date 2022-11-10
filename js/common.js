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
            data: line_data[id].years,
        },
        yAxis: {
            name: '论文数'
        },
        series: [
            {
                name: "CCF A",
                id: "A",
                data: line_data[id].A,
                type: 'line',
            },
            {
                name: "CCF B",
                id: "B",
                data: line_data[id].B,
                type: 'line',
            },
            {
                name: "CCF C",
                id: "C",
                data: line_data[id].C,
                type: 'line',
            }
        ]
    }
}
function get_pub_text(id, person_data, pub_data) {
    return person_data[id] + "\n\n" + pub_data[id].join('\n\n')
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
    pub.innerText = get_pub_text(id, person_data, pub_data)

    person_cat_data = cat_data[id]
    years = line_data[id].years
    ccfs = ccfpie_data[id].map(function (i) { return i['name'] })
    journals = conpie_data[id].map(function (i) { return i['name'] })
}

function search_person_cat_data(years, ccfs, journals, person_cat_data) {
    d = {}
    for (year of years) {
        d[year] = {}
        for (ccf of ccfs) {
            d[year][ccf] = {}
            for (journal of journals) {
                d[year][ccf][journal] = person_cat_data[year][ccf][journal]
            }
        }
    }
    return d
}

ccfpie.on("click", function (properties) {
    pub.innerText = search_person_cat_data(years, [properties.name], journals, person_cat_data)
});
conpie.on("click", function (properties) {
    pub.innerText = search_person_cat_data(years, ccfs, [properties.name], person_cat_data)
});
line.on("click", function (properties) {
    pub.innerText = search_person_cat_data([properties.name], properties.seriesId, journals, person_cat_data)
});