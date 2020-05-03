<template>
  <div class="main">
    <div v-if="this.$store.state.cookie">
      <el-container style=" width: 800px; border: 1px solid #eee">
        <el-header style="text-align: center; font-size: 12px;">
          <h1 style="text-shadow: 5px 5px 5px #ff0000;font-family: 楷体; font-size: 40px;">欢迎来到续约界面</h1>
        </el-header>
        <div v-if="flag">
          <h1 style="color:black;font-size:20px">您预约的座位信息如下：</h1>
          <h1
            style="color:black;font-size:20px"
          >您预约了{{ rent_record[0].date}}位于主图书馆的{{rent_record[0].desk_number_id_id}}号座位</h1>
          <h1
            style="color:black;font-size:20px"
          >从{{rent_record[0].start_time}}点到{{rent_record[0].end_time}}点</h1>
          <h1 style="color:black;font-size:20px">请输入您想续约到什么时候？？</h1>
          <form>
            <input type="text" v-model="end_time" placeholder="结束时间" />
          </form>
          <el-button type="text" @click="open" style="margin-top:200px">续约</el-button>
        </div>
        <div v-else>
          <h1 style="color:black;font-size:20px">你还没有预约记录，请先预约</h1>
        </div>
      </el-container>
    </div>
    <div v-else>
      <h1 style="color:black;font-size:30px;padding-bottom:50px ">您还未验证，请前往验证</h1>
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
      end_time: "",
      message: [], // 空座信息，数组形式
      rent_record: [{ desk_number_id_id: "1", floor: "3", plug_state: "0" }],
      flag: false
    };
  },
  methods: {
    open() {
      this.$confirm("是否确定续约?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.$http
            .post(
              "seats/renew",
              { No: this.$store.state.No, end_time: this.end_time },
              { emulateJSON: true }
            )
            .then(function(result) {
              if (result.body.status === 0) {
                this.$message({
                  type: "success",
                  message: "续约成功"
                });
                this.query();
                this.end_time = "";
              } else if (result.body.status === 1)
                this.$message({
                  type: "success",
                  message: "续约失败，该位置后面已经已经有人预约了"
                });
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "续约操作未完成"
          });
        });
    },
    query() {
      this.$http
        .get("seats/search?" + "No=" + this.$store.state.No)
        .then(result => {
          console.log(result);
          if (result.body.status === 0) {
            //查询成功
            this.flag = true;
            this.message = result.body.message;
            this.rent_record = result.body.rent;
            console.log(this.rent_record);
          } else if (result.body.status === 1) {
            this.flag = false;
            this.message = [{ msg: "你没有预约的信息" }];
          }
        });
    }
  },
  created() {
    this.query();
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
    border-bottom-color: black;
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
</style>