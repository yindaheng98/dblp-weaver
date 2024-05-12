import { reactive } from 'vue'
import { type IdType } from 'vis-network'

export const enum ShowContentType {
    None = 1,
    Author,
}
export const content_show = reactive<{
    type: ShowContentType,
    id: IdType,
    author(id: IdType): void
}>({
    type: ShowContentType.None,
    id: 0,
    author(id: IdType) {
        console.log(id)
        this.type = ShowContentType.Author
        this.id = id
    }
})

export const enum ShowNeoVisType {
    None = 1,
    AuthorByPaper,
}
export const neovis_show = reactive<{
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