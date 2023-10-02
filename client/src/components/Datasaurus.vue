<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from "axios";


const buttonList = [
  { name: 'us' },
  { name: 'jp' },
  { name: 'gb' },
  { name: 'fr' },
  { name: 'de' },
  { name: 'ca' },
  { name: 'au' },
];
const selectedButton = ref<string>('us');
const imgURL = ref<string>("/src/assets/keyword_us.png");
async function onSelectButton(button: any) {
  selectedButton.value = button.name;
  const res = await axios.post("http://localhost:5000/get_keyword", {country: button.name})
  if (res.data.status == "success"){
    console.log(res.data.data)
  }
  else{
    console.log("error")
  }
  imgURL.value = "/src/assets/keyword_"+button.name+".png";
}


</script>

<template>
  <div class="datasaurus">
    <h4>Keyword in Different Countries</h4>
    <div class="button-group">
      <a-button
          class="button"
          v-for="button in buttonList"
          :key="button.name"
          :type="button.name === selectedButton ? 'primary' : ''"
          @click="onSelectButton(button)"
      >
        {{ ` ${button.name}` }}
      </a-button>
    </div>
    <img :src="imgURL">
  </div>
</template>

<style scoped>
.datasaurus {
  height: calc(100% - 2px);
  width: 100%;
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  padding :10px;
  box-sizing:border-box;
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
  height:100%;
}

</style>
