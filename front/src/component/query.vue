<template>
    <div class="main">
        <div v-if="this.$store.state.cookie">
            <div>
            <h1 style="color:#ffffff;font-size:30px">查询界面</h1>
            
            <input type="button"  value="查询" @click="query" class="btn btn-primary">
            <div>
                <!--想在这里画一个下拉列表，但是不确定未知选项个数的下拉列表怎么画-->
                <!--于是demo里就用插值表达式简单显示了-->
                <!--这里还缺一个v-if,只当点击查询按钮的时候显示查询信息。-->
                <!--另外关于v-if的使用，如何使用v-if调用这里的flag属性？-->
                <p style="color:#ffffff;font-size:15px">空座信息{{message}}</p>
                <p style="color:#ffffff;font-size:15px">预约信息{{rent_record}}</p>
            </div>
            </div>
        </div>
        <div v-else>
            <h1 style="color:#ffffff;font-size:30px;padding-bottom:50px ">您还未验证，请前往验证</h1>
            <router-link to="/"><button>前往验证</button></router-link>
        </div>
    </div>
</template>

<script>
export default{
  data(){
    return{
      flag:"false",     // 是否已经点击了查询按钮
      message:[],       // 空座信息，数组形式
      rent_record:{}    //账户预约记录
    };
  },
  methods:{
    query(){
      this.flag="true";
      this.$http.get('searchAPI').then(result=>
      {
        if(result.body.status==0) //查询成功
          {
            this.message=result.body.message;
            this.rent_record=result.body.rent;
          }
        else
          alert("查询失败！")
      })
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