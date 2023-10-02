<script setup lang="ts">
import Datasaurus from './components/Datasaurus.vue';
import NetflixDistBar from './components/NetflixDistBar.vue';

</script>

<template>
  <a-row>
    <a-col :span="9">
      <a-row class="row-half">
      </a-row>
      <a-row class="row-half">
        <Datasaurus id="datasaurus_container" />
      </a-row>
    </a-col>
    <a-col :span="15">
      <a-row class="row-one-third">
        <a-col>
        </a-col>
      </a-row>
      <a-row class="row-two-third">
        <a-col style="height:600px">
          <NetflixDistBar />
        </a-col>
      </a-row>
    </a-col>
  </a-row>
</template>

<style>
#app {
  font-family: 'Open Sans', Helvetica, 'PingFang SC', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 1600px;
  height: 900px;
  margin: 10px;
  border: 1px solid #455a64;
  box-sizing: border-box;
}

a-row{
  height:900px;
}

.row-one-third {
  height: 300px;
  width: 100%;
}

.row-half {
  height: 450px;
}

.row-two-third {
  height: 600px;
  width: 100%;
}
img{
  position:relative;
  z-index:-1;

}


a-col{
  height: inherit;
  width: inherit;
}

.noselect {
  user-select: none;
}
</style>
