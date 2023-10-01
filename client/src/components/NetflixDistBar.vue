<script setup lang="ts">
import { watch, ref, onMounted } from 'vue';
import { useConfig } from '../stores/vaConfig';
import { useNetflixStore, type DistCount } from '../stores/netflix';
import { useStaticNetflixStore } from '../stores/netflixStatic';

// acquire color from pinia store
const vaConfig = useConfig();
const netflixStore = vaConfig.hasServer
  ? useNetflixStore()
  : useStaticNetflixStore(); // define data source according to the environment

// button configurations
const buttonList = [
  { name: 'tracks', get: netflixStore.get_year_distribution },
  { name: 'artists', get: netflixStore.get_country_distribution },
];
const selectedButton = ref<string>('tracks');
function onSelectButton(button: any) {
  selectedButton.value = button.name;
  button.get();
}

// The mounted option
onMounted(() => {
  // init and render bar chart
  netflixStore.get_year_distribution(); // default with year distribution
});




</script>

<template>
  <div class="netflix-dist">
    <div class="button-group">
      <a-button
        class="button"
        v-for="button in buttonList"
        :key="button.name"
        :type="button.name === selectedButton ? 'primary' : ''"
        @click="onSelectButton(button)"
      >
        {{ `Top ${netflixStore.displayMax} ${button.name}` }}
      </a-button>
    </div>
    <img src="../assets/top_10_artists.png" v-if="selectedButton=='artists'">
    <img src="../assets/top_10_tracks.png" v-if="selectedButton=='tracks'">

  </div>
</template>

<style scoped>
.netflix-dist {
  height: calc(100% - 2px);
  width: 999px;
  display: flex;
  flex-direction: column;
  border: 1px solid black;
}

.button-group {
  padding: 5px;
  display: flex;
  flex: 0 1 auto;
  flex-flow: row wrap;
}

.button {
  flex: auto;
}

img{
  height:90%;
  width:100%
}


</style>
