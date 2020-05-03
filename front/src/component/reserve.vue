<template>
  <div class="main">
    <div v-if="this.$store.state.cookie">
      <div>
        <el-container style=" width: 600px; border: 1px solid #eee">
          <el-header style="text-align: center; font-size: 12px;">
            <h1 class="mainTitle">预约页面</h1>
          </el-header>
          <!--我电脑的element-ui并不能很好地显示，但是范例写日历是这么写的-->
          <el-calendar v-model="calendar"></el-calendar>
          <el-main>
            <el-form label-width="80px">
              <el-form-item label="座位号" size="mini">
                <el-input v-model="desk_num"></el-input>
              </el-form-item>
              <el-form-item label="预约日期">
                <el-date-picker
                  v-model="date"
                  type="date"
                  placeholder="选择日期"
                  format="yyyy 年 MM 月 dd 日"
                  value-format="yyyy-MM-dd"
                ></el-date-picker>
              </el-form-item>
              <el-form-item label="开始时间">
                <el-input v-model="start_time"></el-input>
              </el-form-item>
              <el-form-item label="结束时间">
                <el-input v-model="end_time"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submit">提交</el-button>
                <el-button type="primary" @click="reset">重置</el-button>
              </el-form-item>
            </el-form>
          </el-main>
        </el-container>
      </div>
    </div>
    <div v-else>
      <h1 style="color:blackf;font-size:30px;padding-bottom:50px ">您还未验证，请前往验证</h1>
      <router-link to="/">
        <button>前往验证</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_no: "",
      desk_num: "",
      start_time: "",
      end_time: "",
      date: "",
      calendar: new Date()
    };
  },
  methods: {
    submit() {
      console.log(this.user_no);
      console.log(this.desk_num);
      console.log(this.start_time);
      console.log(this.end_time);
      console.log(this.date);
      //url可能还有点问题
      this.$http
        .post(
          "seats/rent",
          {
            No: this.$store.state.No,
            desk_number: this.desk_num,
            start_time: this.start_time,
            end_time: this.end_time,
            date: this.date
          },
          { emulateJSON: true }
        )
        .then(function(result) {
          if (result.body.status == 0) alert("预约成功！");
          else if (result.body.status == 1)
            alert("预约失败：输入数据有误，请检查！");
          else if (result.body.status == 2)
            alert("预约失败：已有其他预约数据！");
          else if (result.body.status == 3)
            alert("预约失败：该座位已被他人预约！");
          else if (result.body.status == 4) alert("预约失败：输入未完整！");
        });
    },
    reset() {
      this.desk_num = "";
      this.start_time = "";
      this.end_time = "";
      this.date = "";
      console.log(this.desk_num);
      alert("testReset");
    }
  }
};
</script>
<style lang="scss" scoped>
.main {
  background-color: white;
  flex: 8;
  padding-top: 80px;
  padding-left: 200px;
}
.main .mainTitle {
  text-shadow: 5px 5px 5px #ff0000;
  font-family: "楷体";
  font-size: "40px";
}

h1 {
  margin: 0;
  padding: 0;
  font-size: 16px;
}
div {
  position: relative;
}
.cssfx {
  float: left;
  input {
    width: 20em;
    color: black;
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
    color: black;
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
  content: "";
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
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>