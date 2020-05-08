
<template>
  <div class="main">
    <div v-if="this.$store.state.cookie">
      <el-container style=" width: 800px; border: 1px solid #eee">
        <el-header style="text-align: center; font-size: 12px;">
          <h1 style="text-shadow: 5px 5px 5px #ff0000;font-family: 楷体; font-size: 40px;">积分系统界面</h1>
        </el-header>
        <h3>您的积分为:{{score}}</h3>
        <el-header style="text-align: center; font-size: 12px">
          <h3>积分排名</h3>
        </el-header>
        <!--<div>
          <el-table
            style="width: 493%; height: 72px; font-size: 13px; line-height: 0px;"
            :data="rent_record"
            border
            stripe
            fit="false"
            show-header="false"
          >
            <el-table-column label="排名" prop="desk_number" width="100"></el-table-column>
            <el-table-column label="姓名" prop="floor" width="180"></el-table-column>
            <el-table-column label="身份" prop="plug_state"></el-table-column>
            <el-table-column label="积分" prop="start_time"></el-table-column>
          </el-table>
        </div>-->
        <el-table :data="msg" stripe style="width: 100%">
          <el-table-column prop="ID" label="排名" width="180"></el-table-column>
          <el-table-column prop="name" label="姓名" width="180"></el-table-column>
          <el-table-column prop="identity" label="身份"></el-table-column>
          <el-table-column prop="score" label="积分"></el-table-column>
        </el-table>
        <el-pagination layout="prev, pager, next" :total="50"></el-pagination>
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
      score: "",
      msg: []
    };
  },
  methods: {
    getcredit() {
      this.$http
        .get("credit/getcredit?No=" + this.$store.state.No)
        .then(result => {
          if (result.body.status === 0) console.log(result);
          this.score = result.body.credit;
        });
    },
    getall() {
      this.$http.get("credit/getall").then(result => {
        if (result.body.status === 0) console.log(result);
        this.msg = result.body.msg;
      });
    }
  },
  created() {
    this.getcredit();
    this.getall();
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
