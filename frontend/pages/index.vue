<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { Vue3Marquee } from 'vue3-marquee';

const config = useRuntimeConfig();
const apiBase = config.public.apiBase;

const initData = ref([]);

const loadInitData = async () => {
  const res = await $fetch(`${apiBase}/init`);
  initData.value = res;
};

onMounted(() => { loadInitData(); });
</script>
<template>
  <div>
    {{ initData }}
  </div>
</template>
<style scoped>
</style>