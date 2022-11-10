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
function get_person_raw_data(id, raw_data) {
    return raw_data[id]
}

ccfpie = echarts.init(document.getElementById("ccfpie"));
conpie = echarts.init(document.getElementById("conpie"));
line = echarts.init(document.getElementById("line"));
pub = document.getElementById("publications")
var person_raw_data;
function change_person(id) {
    ccfpie.setOption(get_ccfpie_option(id, ccfpie_data))
    conpie.setOption(get_conpie_option(id, conpie_data))
    line.setOption(get_line_option(id, line_data))
    pub.innerText = get_pub_text(id, person_data, pub_data)
    person_raw_data = get_person_raw_data(id, raw_data)
}

function search_person_raw_data(year, ccf, journal, person_raw_data) {
    for (raw in person_raw_data) {

    }
}