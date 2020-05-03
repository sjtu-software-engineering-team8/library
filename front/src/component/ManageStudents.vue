/* eslint-disable */
<template>
  <div class="query">
    <div v-if="this.$store.state.cookie">
      <el-container style=" width: 850px; border: 1px solid #eee">
        <el-header style="text-align: center; font-size: 12px;">
          <h1 class="mainTitle">查询页面</h1>
        </el-header>
        <el-main>
          <!--<el-button type="primary" size="mini" icon="el-icon-search" @click.native= "query">查询</el-button>-->
          <el-container style="height: 150px; border: 1px solid #eee">
            <el-header style="text-align: center; font-size: 12px">
              <h3>预约结果</h3>
            </el-header>
            <div>
              <el-table :data="rent_record" border stripe style="width: 100%">
                <el-table-column label="座位号" prop="desk_number_id_id" width="100"></el-table-column>
                <el-table-column label="楼层号" prop="floor" width="180"></el-table-column>
                <el-table-column label="插座情况" prop="plug_state"></el-table-column>
                <el-table-column align="right"></el-table-column>
              </el-table>
            </div>
          </el-container>
          <el-row>
            <el-col :span="24">
              <div class="grid-content bg-purple-dark"></div>
            </el-col>
          </el-row>
          <!--
          <div>
            <el-container style="height: 500px; border: 1px solid #eee">
              <el-header style="text-align: center; font-size: 12px">
                <h3>图书馆空座情况</h3>
              </el-header>
              <el-form :inline="true">
                <el-form-item style="float:left">
                  <el-input v-model="searchInfo" placeholder="搜索需要的内容" prefix-icon="el-icon-search"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button
                    type="primary"
                    size="mini"
                    icon="el-icon-search"
                    @click.native="search()"
                  >搜索</el-button>
                </el-form-item>
              </el-form>
              <el-row>
                <el-col :span="24">
                  <div class="grid-content bg-purple-dark"></div>
                </el-col>
              </el-row>
              <el-table :data="message" border stripe style="width: 100%">
                <el-table-column label="座位号" prop="desk_number" width="100"></el-table-column>
                <el-table-column label="楼层号" prop="floor" width="180"></el-table-column>
                <el-table-column label="插座情况" prop="plug_state"></el-table-column>
                <el-table-column align="right"></el-table-column>
              </el-table>
            </el-container>
          </div>
          -->

          <el-container style="height: 120px; border: 1px solid #eee">
            <el-header style="text-align: center; font-size: 12px">
              <h3>图书馆空座情况</h3>
            </el-header>
            <el-main>
              <el-form :inline="true">
                <el-form-item style="float:left">
                  <el-input v-model="searchInfo" placeholder="搜索需要的内容" prefix-icon="el-icon-search"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button
                    type="primary"
                    size="mini"
                    icon="el-icon-search"
                    @click.native="search()"
                  >搜索</el-button>
                </el-form-item>
              </el-form>
            </el-main>
          </el-container>
          <el-container>
            <el-aside style="float:left; width:180px">
              <el-container style="border: 1px solid #eee">
                <el-header>
                  <h5>第一层</h5>
                </el-header>
                <div v-for="rowNum in row">
                  <img :src="imageUrl" style="width:10%" />
                  <img :src="imageUrl" style="width:10%" />
                  <img :src="imageUrl" style="width:10%" />
                  <img :src="imageUrl" style="width:10%" />
                  <img :src="imageUrl" style="width:10%" />
                </div>
              </el-container>
            </el-aside>
            <el-main style="width:800px">
              <!--剩下三个区域-->
              <el-container style="border: 1px solid #eee">
                <el-aside style="float:left;width:180px">
                  <el-container style="border: 1px solid #eee">
                    <el-header>
                      <h5>第二层</h5>
                    </el-header>
                    <div v-for="rowNum in row">
                      <input type="checkbox" />
                      <input type="checkbox" />
                      <input type="checkbox" />
                      <input type="checkbox" />
                      <input type="checkbox" />
                    </div>
                  </el-container>
                </el-aside>
                <el-main>
                  <!--剩下两个区域-->
                  <el-container style="border: 1px solid #eee">
                    <el-aside style="float:left; width:180px">
                      <el-container>
                        <el-header>
                          <h5>第三层</h5>
                        </el-header>
                        <div v-for="rowNum in row">
                          <input type="checkbox" />
                          <input type="checkbox" />
                          <input type="checkbox" />
                          <input type="checkbox" />
                          <input type="checkbox" />
                        </div>
                      </el-container>
                    </el-aside>
                    <el-main>
                      <el-container style="border: 1px solid #eee">
                        <el-header>
                          <h5>第四层</h5>
                        </el-header>
                        <el-aside style="float:left; width:180px">
                          <div v-for="rowNum in row">
                            <input type="checkbox" />
                            <input type="checkbox" />
                            <input type="checkbox" />
                            <input type="checkbox" />
                            <input type="checkbox" />
                          </div>
                        </el-aside>
                      </el-container>
                    </el-main>
                  </el-container>
                </el-main>
              </el-container>
            </el-main>
          </el-container>
        </el-main>
        <el-footer></el-footer>
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
import imageU from "../img/seatIcon.jpg";
export default {
  name: "manageStudents",
  data() {
    return {
      imageUrl: imageU,
      message: [
        { desk_number: "1", floor: "1", plug_state: "0" },
        { desk_number: "2", floor: "3", plug_state: "1" }
      ], // 空座信息，数组形式
      rent_record: [{ desk_number_id_id: "1", floor: "3", plug_state: "0" }], //账户预约记录
      searchInfo: "",
      row: [1, 2, 3, 4, 5],
      col: [1, 2, 3, 4, 5],
      floor: [1, 2, 3, 4]
    };
  },
  methods: {
    query() {
      alert("testQuery");
      this.$http
        .get("seats/search?" + "No=" + this.$store.state.No)
        .then(result => {
          if (result.body.status === 0) {
            //查询成功
            this.message = result.body.message;
            this.rent_record = result.body.rent;
            console.log(this.message);
            console.log(this.rent_record);
          } else alert("查询失败！");
        });
    },
    created() {
      this.query();
      alert("testCreate");
    },
    search() {
      alert("testSearch");
      console.log(this.message);
    }
  } //,
  /*
  created() {
    this.query();
  }*/
};
</script>

<style>
.query {
  background-color: white;
  flex: 8;
  padding-top: 80px;
  padding-left: 200px;
}

.query .title {
  text-align: center;
  margin-bottom: 50px;
  margin-left: -80px;
  font-size: 20px;
}

.query .addBtn {
  position: absolute;
  top: 0px;
  right: 20px;
}

.query .row_style {
  color: blue;
  border-top: 1px solid #6699cc; /*上框线*/
  border-bottom: 1px solid #6699cc; /*下框线*/
  border-left: 1px solid #6699cc; /*左框线*/
  border-right: 1px solid #6699cc; /*右框线*/
}
.query .mainTitle {
  text-shadow: 5px 5px 5px #ff0000;
  font-family: "楷体";
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
