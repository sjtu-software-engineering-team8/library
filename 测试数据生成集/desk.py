

import os
# import MySQLdb
import pymysql
from db import user1
import hashlib
import time

cur = user1.db.cursor()


for num in range(1, 26):
    desk_id = num
    floor = 1
    plug_state = 0
    rent_state =0

    cur.execute("insert into Desk(desk,floor,plug,status) values (%s,%s,%s,%s)",
                ([desk_id,floor,plug_state,rent_state]))
    user1.db.commit()


for num in range(26, 51):
    desk_id = num
    floor = 2
    plug_state = 0
    rent_state =0

    cur.execute("insert into Desk(desk,floor,plug,status) values (%s,%s,%s,%s)",
                ([desk_id,floor,plug_state,rent_state]))
    user1.db.commit()

for num in range(51, 76):
    desk_id = num
    floor = 3
    plug_state = 0
    rent_state =0

    cur.execute("insert into Desk(desk,floor,plug,status) values (%s,%s,%s,%s)",
                ([desk_id,floor,plug_state,rent_state]))
    user1.db.commit()

for num in range(76, 101):
    desk_id = num
    floor = 4
    plug_state = 0
    rent_state =0

    cur.execute("insert into Desk(desk,floor,plug,status) values (%s,%s,%s,%s)",
                ([desk_id,floor,plug_state,rent_state]))
    user1.db.commit()

user1.db.close()
