<script setup lang="ts">
import { neovis_show, ShowNeoVisType } from './state'
import PaperAuthorsGraph from './PaperAuthorsGraph.vue'

const props = defineProps<{ limit: number }>()
</script>

<template>
  <div v-if="neovis_show.type == ShowNeoVisType.None">Please select a starting point</div>
  <PaperAuthorsGraph
    v-else-if="neovis_show.type == ShowNeoVisType.AuthorByPaper"
    :id="neovis_show.id"
    :limit="props.limit"
  />
</template>
