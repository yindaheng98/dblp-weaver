import { reactive } from 'vue'
import { type IdType } from 'vis-network'

export const enum ShowNeoVisType {
    None = 1,
    PaperAuthorsGraph,
    PaperCitesGraph,
}
export const stateGraphPanel = reactive<{
    type: ShowNeoVisType,
    id: IdType,
    showPaperAuthorsGraph(id: IdType): void
    showPaperCitesGraph(id: IdType): void
}>({
    type: ShowNeoVisType.None,
    id: 0,
    showPaperAuthorsGraph(id: IdType) {
        this.type = ShowNeoVisType.PaperAuthorsGraph
        this.id = id
    },
    showPaperCitesGraph(id: IdType) {
        this.type = ShowNeoVisType.PaperCitesGraph
        this.id = id
    }
})

export const stateAuthorPapersStat = reactive<{
    visible: boolean,
    id: IdType,
    show(id: IdType): void
}>({
    visible: false,
    id: 0,
    show(id: IdType) {
        this.visible = true
        this.id = id
    }
})

export const statePaperList = reactive<{
    visible: boolean,
    id: IdType,
    filter: {
        year?: number, journal?: string, ccf?: string
    }
    show(id?: IdType, year?: number, journal?: string, ccf?: string): void
}>({
    visible: false,
    id: 0,
    filter: {},
    show(id?: IdType, year?: number, journal?: string, ccf?: string) {
        this.visible = true
        if (id) this.id = id
        if (year) this.filter.year = year
        else this.filter.year = undefined
        if (journal) this.filter.journal = journal
        else this.filter.journal = undefined
        if (ccf) this.filter.ccf = ccf
        else this.filter.ccf = undefined
    }
})