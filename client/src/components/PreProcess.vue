<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from "axios";


const buttonList = [
  { name: 'day' },
  { name: 'dayofweek' },
  { name: 'month' },
];
const selectedButton = ref<string>('day');
const imgURL = ref<string>("/src/assets/2017 day Cnt.png");
onMounted(async () => {
  const res = await axios.post("http://localhost:5000/pre_process", )
  if (res.data.status == "success"){
    console.log(res.data.data)
  }
  else{
    console.log("error")
  }
})

function onSelectButton(button: any) {
  selectedButton.value = button.name;
  imgURL.value = "/src/assets/2017 "+button.name+" Cnt.png";
}


</script>

<template>
  <div class="datasaurus">
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
  height: calc(100% - 0px);
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
  height:92%;
}

</style>
