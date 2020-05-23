/* eslint-disable */
<template>
  <div class="query">
    <div v-if="this.$store.state.cookie">
      <el-container style="height: 1000px; width: 850px; border: 1px solid #eee">
        <el-header style="text-align: center; font-size: 12px;">
          <h1 class="mainTitle">查询页面</h1>
        </el-header>
        <div>
          <el-button
            type="primary"
            @click.native="query"
            icon="el-icon-search"
            style="float:right"
          >查询</el-button>
        </div>
        <el-main>
          <el-container style="height: 100px; border: 1px solid #eee">
            <el-header style="text-align: center; font-size: 12px">
              <h3>预约结果</h3>
            </el-header>
            <div>
              <el-table
                style="width: 493%; height: 150px; font-size: 13px;"
                :data="rent_record"
                border
                stripe
                fit="false"
                show-header="false"
              >
                <el-table-column label="座位号" prop="desk_number_id_id" width="100"></el-table-column>
                <el-table-column label="开始时间" prop="start_time"></el-table-column>
                <el-table-column label="结束时间" prop="end_time"></el-table-column>
                <el-table-column label="预约日期" prop="date"></el-table-column>
                <el-table-column align="right"></el-table-column>
              </el-table>
            </div>
          </el-container>
          <br />
          <br />
          <div style="height: 174px; border: 1px solid rgb(238, 238, 238);margin-top:70px">
            <div style="text-align: center; font-size: 12px;top-padding:10px;">
              <h3>图书馆空座情况</h3>
            </div>
            <el-col style="height: 125px; width: 49.8914%;" :xs="12" :sm="12">
              <div class="grid-content" v-for="rowNum in row">
                {{rowNum}}.
                <!--对应desk_id:rowNum*5-4-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor1_row1(rowNum)"></i>
                <!--对应desk_id:rowNum*5-3-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor1_row2(rowNum)"></i>
                <!--对应desk_id:rowNum*5-2-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor1_row3(rowNum)"></i>
                <!--对应desk_id:rowNum*5-1-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor1_row4(rowNum)"></i>
                <!--对应desk_id:rowNum*5-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor1_row5(rowNum)"></i>
              </div>
              <p style="text-align:center;">第一层</p>
            </el-col>
            <el-col style="height: 126px;" :xs="12" :sm="12">
              <div class="grid-content" v-for="rowNum in row">
                {{rowNum}}.
                <!--对应desk_id:rowNum*5+21-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor2_row1(rowNum)"></i>
                <!--对应desk_id:rowNum*5+22-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor2_row2(rowNum)"></i>
                <!--对应desk_id:rowNum*5+23-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor2_row3(rowNum)"></i>
                <!--对应desk_id:rowNum*5+24-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor2_row4(rowNum)"></i>
                <!--对应desk_id:rowNum*5+25-->
                <i class="el-icon-reading" style="width:20px;" :id="generateId_floor2_row5(rowNum)"></i>
              </div>
              <p style="text-align:center;">第二层</p>
            </el-col>
            <el-row style="height: 366px;">
              <el-col style="height: 144px; padding-top: 0px; margin-top: 80px;" :xs="12" :sm="12">
                <div class="grid-content" v-for="rowNum in row">
                  {{rowNum}}.
                  <!--对应desk_id:rowNum*5+46-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor3_row1(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+47-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor3_row2(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+48-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor3_row3(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+49-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor3_row4(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+50-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor3_row5(rowNum)"
                  ></i>
                </div>
                <p style="text-align:center;">第三层</p>
              </el-col>
              <el-col style="height: 143px; margin-top: 80px; margin-left: 0px;" :xs="12" :sm="12">
                <div class="grid-content" v-for="rowNum in row">
                  {{rowNum}}.
                  <!--对应desk_id:rowNum*5+71-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor4_row1(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+72-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor4_row2(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+73-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor4_row3(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+74-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor4_row4(rowNum)"
                  ></i>
                  <!--对应desk_id:rowNum*5+75-->
                  <i
                    class="el-icon-reading"
                    style="width:20px;"
                    :id="generateId_floor4_row5(rowNum)"
                  ></i>
                </div>
                <p style="text-align:center;">第四层</p>
              </el-col>
            </el-row>
            <div></div>
          </div>
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
export default {
  name: "manageStudents",
  data() {
    return {
      flag: false, // 是否查询成功

      message: [], // 全部座位信息，数组形式
      rent_record: [], //账户预约记录
      colorStatus: [], //保存对应每个座位的颜色信息，如：[{desk_id:1,color:'red'},{desk_id:2,color:'green'},...]
      row: [1, 2, 3, 4, 5]
    };
  },
  methods: {
    query() {
      this.$http
        .get("seats/search?" + "No=" + this.$store.state.No)
        .then(result => {
          if (result.body.status === 0 || result.body.status === 1) {
            //查询成功
            this.flag = true;
            console.log(result.body.rent);
            this.message = result.body.message;
            this.rent_record = result.body.rent;
            console.log(this.rent_record);
            this.getColorStatus();
            this.changeColor();
          } else {
            this.flag = false;
            alert("查询失败！");
          }
        });
    },
    getColorStatus() {
      if (!this.flag) {
        return;
      }
      for (var i = 0; i < this.message.length; i++) {
        if (this.message[i].rent_state == 1) {
          // 若unavailable则标红
          var tmp = { desk_id: this.message[i].desk_id, color: "#F56C6C" };
          this.colorStatus.push(tmp);
        } else {
          if (this.message[i].plug_state == 0) {
            //若有插座则标绿
            var tmp = { desk_id: this.message[i].desk_id, color: "#67C23A" };
            this.colorStatus.push(tmp);
          } else {
            // 若无插座则标白
            var tmp = { desk_id: this.message[i].desk_id, color: "#FFFFFF" };
            this.colorStatus.push(tmp);
          }
        }
      }
    },
    changeColor() {
      alert("before change!");
      // 第i个id对应colorStatus里第i个对象
      for (var i = 1; i < this.colorStatus.length + 1; i++) {
        document.getElementById(i).style.color = this.colorStatus[i - 1].color;
      }
      alert("changed!");
    },
    generateId_floor1_row1(index) {
      return index * 5 - 4;
    },
    generateId_floor1_row2(index) {
      return index * 5 - 3;
    },
    generateId_floor1_row3(index) {
      return index * 5 - 2;
    },
    generateId_floor1_row4(index) {
      return index * 5 - 1;
    },
    generateId_floor1_row5(index) {
      return index * 5;
    },
    generateId_floor2_row1(index) {
      return index * 5 + 21;
    },
    generateId_floor2_row2(index) {
      return index * 5 + 22;
    },
    generateId_floor2_row3(index) {
      return index * 5 + 23;
    },
    generateId_floor2_row4(index) {
      return index * 5 + 24;
    },
    generateId_floor2_row5(index) {
      return index * 5 + 25;
    },
    generateId_floor3_row1(index) {
      return index * 5 + 46;
    },
    generateId_floor3_row2(index) {
      return index * 5 + 47;
    },
    generateId_floor3_row3(index) {
      return index * 5 + 48;
    },
    generateId_floor3_row4(index) {
      return index * 5 + 49;
    },
    generateId_floor3_row5(index) {
      return index * 5 + 50;
    },
    generateId_floor4_row1(index) {
      return index * 5 + 71;
    },
    generateId_floor4_row2(index) {
      return index * 5 + 72;
    },
    generateId_floor4_row3(index) {
      return index * 5 + 73;
    },
    generateId_floor4_row4(index) {
      return index * 5 + 74;
    },
    generateId_floor4_row5(index) {
      return index * 5 + 75;
    }
  }
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
  border-radius: 10px;
  min-height: 0px;
  height: 0px;
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
