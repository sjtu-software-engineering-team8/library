<template>
  <div id="app">
    <div class="container">
      <router-view name="left"></router-view>
      <router-view name="main"></router-view>
    </div>
  </div>
</template>

<script>
</script>


<style lang="scss" scoped>
html,
body {
  margin: 0;
  padding: 0;
  background-color: white;
}
.container {
  display: flex;
  height: 100%;
  background-color: white;
}
</style>
