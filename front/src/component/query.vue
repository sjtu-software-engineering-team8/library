<template>
    <div class="main">
        <div v-if="this.$store.state.cookie">
            <div>
            <h1 style="color:#ffffff;font-size:30px">查询界面</h1>
            
            <div>
                <!--空座信息display-->
                <div>\n</div>
                <div class="container-fluid">
                   <h1 style="color:#ffffff;front-size:30px">空余座位</h1>
                   <div>\n</div>
                   <div class="row">
                      <div class="block col-md-4" style="color:#ffffff;front-size:15px;">座位号</div>
                      <div class="block col-md-4" style="color:#ffffff;front-size:15px;">所在楼层</div>
                   </div>
                     <div class="row" v-for="(seat,i) in message">
                        <div class="block col-md-4" style="color:#ffffff;front-size:15px;">{{seat.desk_number}}</div>
                        <div class="block col-md-4" style="color:#ffffff;front-size:15px;">{{seat.floor}}</div>
                     </div>
                </div>
                
                <!--预约信息display-->
                <div>\n</div>
                <div class="container-fluid">
                   <h1 style="color:#ffffff;front-size:30px">已预约的信息</h1>
                   <div>\n</div>
                   <div class="row">
                      <div class="block col-md-4" style="color:#ffffff;front-size:15px;">座位号</div>
                      <div class="block col-md-4" style="color:#ffffff;front-size:15px;">所在楼层</div>
                   </div>
                     <div class="row">
                        <div class="block col-md-4" style="color:#ffffff;front-size:15px;">{{rent_record.desk_number}}</div>
                        <div class="block col-md-4" style="color:#ffffff;front-size:15px;">{{rent_record.floor}}</div>
                     </div>
                </div>
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
  },
  created(){
    this.query();
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