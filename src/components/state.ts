import { reactive } from 'vue'
import { type IdType } from 'vis-network'

export const enum ShowNeoVisType {
    None = 1,
    AuthorByPaper,
}
export const neovisShow = reactive<{
    type: ShowNeoVisType,
    id: IdType,
    authorsbypaper(id: IdType): void
}>({
    type: ShowNeoVisType.None,
    id: 0,
    authorsbypaper(id: IdType) {
        console.log(id)
        this.type = ShowNeoVisType.AuthorByPaper
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
    show(id: IdType, year?: number, journal?: string, ccf?: string): void
}>({
    visible: false,
    id: 0,
    filter: {},
    show(id: IdType, year?: number, journal?: string, ccf?: string) {
        this.visible = true
        this.id = id
        if (year) this.filter.year = year
        if (journal) this.filter.journal = journal
        if (ccf) this.filter.ccf = ccf
    }
})