
<template>
  <div class="main">
    <div v-if="this.$store.state.cookie">
      <div>
        <h1 style="color:black;font-size:30px">欢迎来到取消预约界面</h1>
        <input type="button" value="取消预约" @click="cancel" class="btn btn-primary" />

        <div class="panel-body form-inline">
          <form>
            <input type="text" v-model="user_no" placeholder="账号" />
          </form>
        </div>
        <input type="button" value="提交" @click="submit" class="btn btn-primary" />
      </div>
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
      user_no: ""
    };
  },
  methods: {
    submit() {
      console.log(this.user_no);

      //url暂时还不知道该怎么写，这儿先随便写了一个

      this.$http
        .post(
          "http://127.0.0.1:8000/seat/cancel",
          { user_no: this.user_no },
          { emulateJSON: true }
        )
        .then(function(result) {
          if (result.body.status == 0) alert("您的预约取消了！");
          else if (result.body.status == 1) alert("您的预约没有成功取消");
        });
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
  color: black;
  padding: 0.5em 1em;
  outline: none;
  border: none;
  background-color: white;
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
