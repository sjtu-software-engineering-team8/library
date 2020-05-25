# 软工第八组的项目

##### 注释：本项目采用的python版本需要大于3.6，采用anaconda环境，django版本为2.x，如果不适用anaconda环境需要在下面步骤3之前使用pip安装一些依赖包

### 1. front文件夹为前端vue.js的项目

### 2. rear文件夹为后端django项目

### 3. testdata文件夹为后端测试数据生成集

### 4. unittest文件夹为单元测试的框架和结果

### 5. pushlog.md文件为历次组员的提交记录，方便后续同学整合，是阶段性成果的展示



## 项目的使用方式

### 1.在文件rear/mysite/settings.py中配置database，将用户名和账号设置为本地数据库mysql的账号和密码

### 2.安装django-cors-headers，在终端执行下面的指令

```
pip install django-cors-headers
```



### 3. 在rear文件夹下执行数据库迁移指令和创建超级用户的指令

```
python manage.py makemigrations   #生成数据库迁移文件
python manage.py migrate          #数据库迁移
python manage.py createsuperuser  #创建超级用户
```

### 4.依次运行testdata文件夹下的user.py和desk.py生成测试数据

### 5.在rear文件夹下执行下面的指令启动项目

```
python manage.py runserver 8000
```

### 6.在浏览器输入 http://127.0.0.1:8000/credit/insert 生成user.py中新增的用户的积分信息

### 7.项目初始化完成

