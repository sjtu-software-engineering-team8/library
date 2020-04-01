<template>
    <div class="main">
      <div v-if="this.$store.state.flag">
            <div>
              <h1 style="color:#ffffff;font-size:30px">为确保本人操作，请输入您的账号名</h1>
            </div>
 
            <div style="overflow:hidden;padding-top:100px">
              <div style="float:left;padding:11px;color:#ffffff" >账号</div>
              <div class="cssfx">
              <input type="text" placeholder="input your account" v-model="usercookie" @keyup.enter="confirmuser">
              <span></span>
              </div>
            </div>
            <div><button @click="confirmuser">确认</button></div>
      </div>
      <div v-else>
        <h1 style="color:#ffffff;font-size:30px">欢迎回来{{this.$store.state.cookie}},请选择服务</h1>
      </div>
    </div>
</template>

<script>
    export default{
        data(){
            return {
              usercookie:''
            }
        },
        methods:{
          confirmuser(){
          this.$store.state.cookie=this.usercookie
          this.check()
          },
          check()
          {
            if(this.$store.state.cookie==='')
            this.$store.state.flag=true
            else
            this.$store.state.flag=false
          },
          created () {
            this.check()
          }
        }
        }
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