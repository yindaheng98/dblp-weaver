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