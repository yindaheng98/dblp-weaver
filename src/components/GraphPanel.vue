<script setup lang="ts">
import { neovisShow, ShowNeoVisType } from './state'
import PaperAuthorsGraph from './PaperAuthorsGraph.vue'

const props = defineProps<{ limit: number }>()
</script>

<template>
  <div v-if="neovisShow.type == ShowNeoVisType.None">Please select a starting point</div>
  <PaperAuthorsGraph
    v-else-if="neovisShow.type == ShowNeoVisType.AuthorByPaper"
    :id="neovisShow.id"
    :limit="props.limit"
  />
</template>
