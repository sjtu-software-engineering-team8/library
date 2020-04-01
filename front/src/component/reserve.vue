<template>
    <div class="main">
        <div v-if="this.$store.state.cookie">
            <div>
            <h1 style="color:#ffffff;font-size:30px">预约界面</h1>
            </div>
        </div>
        <div v-else>
            <h1 style="color:#ffffff;font-size:30px;padding-bottom:50px ">您还未验证，请前往验证</h1>
            <router-link to="/"><button>前往验证</button></router-link>
        </div>
    </div>
</template>

<script>
    
</script>
<style lang="scss" scoped>
.main {
            background-color: #090821;
            flex: 8;
            padding-top:80px;
            padding-left: 200px;
            height:800px;
        }
        h1 {
            margin: 0;
            padding: 0;
            font-size: 16px;
        }
div {
  position: relative;
}
.cssfx{
    float: left;
    input {
  width: 20em;
  color: hsla(0, 0%, 100%, 0.6);
  font-size: inherit;
  font-family: inherit;
  background-color: transparent;
  border: 1px solid transparent;
  border-bottom-color: hsla(185, 100%, 62%, 0.2);
}

input:focus {
  outline: none;
}

input::placeholder {
  color: hsla(0, 0%, 100%, 0.6);
}

span {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background-color: #3cefff;
  transform-origin: bottom right;
  transform: scaleX(0);
  transition: transform 0.5s ease;
}

input:focus ~ span {
  transform-origin: bottom left;
  transform: scaleX(1);
}
}




button {
  z-index: 1;
  position: relative;
  font-size: inherit;
  font-family: inherit;
  color: white;
  padding: 0.5em 1em;
  outline: none;
  border: none;
  background-color: hsl(236, 32%, 26%);
  overflow: hidden;
  transition: color 0.4s ease-in-out;
}

button::before {
  content: '';
  z-index: -1;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #3cefff;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale3d(0, 0, 0);
  transition: transform 0.45s ease-in-out;
}

button:hover {
  cursor: pointer;
  color: #161616;
}

button:hover::before {
  transform: translate3d(-50%, -50%, 0) scale3d(15, 15, 15);
}
</style>