import os
import pymysql
#import MySQLdb

class user1:
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        #db='user'
        db='mylibrary'
    )
