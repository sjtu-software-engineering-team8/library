#生成楼层
import os
import pymysql
from db import user1
import hashlib
import time

cur = user1.db.cursor()

for num in range(1, 5):
    floor = num
    number_max = 25
    number_now = 0
    #sql = "insert into floor (num,number_max,number_now) values (%d,%d,%d)",(floor,number_max,number_now)

    cur.execute("insert into floor(floor, max, now) values (%s,%s,%s)",
                ([floor, number_max, number_now]))

    user1.db.commit()

user1.db.close()
