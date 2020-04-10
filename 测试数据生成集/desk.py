

import os
import MySQLdb
from db import user1
import hashlib
import time

cur = user1.db.cursor()


for num in range(1, 10):
    desk_number = str(num)
    floor = str(1)
    plug_state = 'false'
    sql = "insert into login_desk(desk_number,floor,plug_state) values ('" + \
        desk_number+"','"+floor+"',"+plug_state+")"
    cur.execute(sql)
    user1.db.commit()

for num in range(11, 20):
    desk_number = str(num)
    floor = str(2)
    plug_state = 'false'
    sql = "insert into login_desk(desk_number,floor,plug_state) values ('" + \
        desk_number+"','"+floor+"',"+plug_state+")"
    cur.execute(sql)
    user1.db.commit()

for num in range(21, 30):
    desk_number = str(num)
    floor = str(3)
    plug_state = 'false'
    sql = "insert into login_desk(desk_number,floor,plug_state) values ('" + \
        desk_number+"','"+floor+"',"+plug_state+")"
    cur.execute(sql)
    user1.db.commit()
user1.db.close()
