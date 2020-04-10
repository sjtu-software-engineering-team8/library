import os
import MySQLdb 
class user1:
    db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='',
        db='user'
    )
