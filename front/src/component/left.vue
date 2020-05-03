<template>
  <div class="left">
    <!-- 定义左侧图的容器 -->
    <div class="leftcontainer">
      <!-- 定义查询这两个字的样式 -->
      <router-link to="/">
        <h1>root</h1>
      </router-link>
      <router-link to="/query">
        <h1>查询信息</h1>
      </router-link>
      <router-link to="/reserve">
        <h1>预约座位</h1>
      </router-link>
      <router-link to="/renew">
        <h1>续约座位</h1>
      </router-link>
      <router-link to="/cancel">
        <h1>取消预约</h1>
      </router-link>
    </div>
  </div>
</template>

<script>
</script>
<style lang="scss" scoped>
.left {
  background-color: white;
  flex: 2;
}
.leftcontainer {
  text-align: center;
  margin: 0 auto;
  padding-top: 200px;
}
h1 {
  color: black;
  font-size: 22px;
  padding-top: 15px;
}
h1:hover {
  color: red;
}
</style>