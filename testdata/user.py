
import os
# import MySQLdb
import pymysql
from db import user1
import hashlib
import time
from hashencode import hash_code


cur = user1.db.cursor()


for num in range(1, 30):
    number = str(num)
    username = str(num)+'hhh'
    password1 = str(num)+str(num)+str(num)
    sh = hash_code(password1)
    email = str(num)+'@qq.com'
    time = '2020-04-10 08:46:21.533721'
    sql = "insert into user (name,number,password,email,identity,c_time,has_confirmed) values ('" + \
        username+"',"+number+",'"+sh+"','"+email+"','student','"+time+"',True)"

    cur.execute(sql)
    user1.db.commit()

user1.db.close()
