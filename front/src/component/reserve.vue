<template>
    <div class="main">
        <div v-if="this.$store.state.cookie">
            <div>
            <h1 style="color:#ffffff;font-size:30px">预约界面</h1>
              <div class="panel-body form-inline">
                <form>
                  <input type="text" v-model=user_no placeholder="账号">
                  <input type="text" v-model=desk_num placeholder="预约座位号">
                  <input type="text" v-model=start_time placeholder="开始时间">
                  <input type="text" v-model=end_time placeholder="结束时间">
                  <input type="text" v-model=date placeholder="预约日期">
                </form>
              </div>
              <input type="button"  value="提交" @click="submit" class="btn btn-primary">
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
    return {
        user_no:"",
        desk_num:"",
        start_time:"",
        end_time:"",
        date:"",
    };
  },
  methods:{
    submit(){
        console.log(this.user_no);
        console.log(this.desk_num);
        console.log(this.start_time);
        console.log(this.end_time);
        console.log(this.date);
        //url可能还有点问题
        this.$http    
          .post("http://127.0.0.1:8000/seat/rent",{user_no:this.user_no, desk_num:this.desk_num, start_time:this.start_time, 
          end_time:this.end_time, date: this.date},{emulateJSON:true})  
          .then(function(result)
          {
            if (result.body.status==0)
              alert("预约成功！")
            else if(result.body.status==1)
              alert("预约失败：输入数据有误，请检查！")
            else if(result.body.status==2)
              alert("预约失败：已有其他预约数据！")
            else if(result.body.status==3)
              alert("预约失败：该座位已被他人预约！")
            else if(result.body.status==4)
              alert("预约失败：输入未完整！")
          } 
            );
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