<script setup lang="ts">
import { watch, ref, onMounted } from 'vue';
import axios from "axios";


const buttonList = [
  { name: 'tracks' },
  { name: 'artists'},
];
const selectedButton = ref<string>('tracks');
function onSelectButton(button: any) {
  selectedButton.value = button.name;
  selectedContinent.value = 'All';
  imgURL.value = button.name === 'tracks' ? '/src/assets/top_10_tracks.png' : '/src/assets/top_10_artists.png';
}

const continentList = [
  { name: 'All'},
  { name: 'North America'},
  { name: 'South America'},
  { name: 'Europe'},
  { name: 'Asia'},
  { name: 'Oceania'},
]

const selectedContinent = ref<string>('All');
function onSelectContinent(continent: any) {
  selectedContinent.value = continent.name;
  let continentName;
  if (selectedContinent.value == 'North America') continentName = 'na'
  else if (selectedContinent.value == 'South America') continentName = 'sa'
  else if (selectedContinent.value == 'Europe') continentName = 'europe'
  else if (selectedContinent.value == 'Asia') continentName = 'asia'
  else if (selectedContinent.value == 'Oceania') continentName = 'oceania'
  if (continentName == undefined) imgURL.value = `/src/assets/top_10_${selectedButton.value}.png`;
  else imgURL.value = `/src/assets/top_10_${selectedButton.value}_in_${continentName}.png`;
}

onMounted(async () => {
  await axios.post("http://localhost:5000/get_data");
});

const imgURL = ref<string>('/src/assets/top_10_tracks.png');


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
        {{ `Top 10 ${button.name}` }}
      </a-button>
    </div>
    <div class="button-group">
      <a-button
          class="button"
          v-for="button in continentList"
          :key="button.name"
          :type="button.name === selectedContinent ? 'primary' : ''"
          @click="onSelectContinent(button)"
      >
        {{ `${button.name}` }}
      </a-button>
    </div>
    <img :src="imgURL">

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
  height:85%;
  width:100%
}


</style>
