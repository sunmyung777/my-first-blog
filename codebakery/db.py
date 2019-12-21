import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='tjsaud7001!!',
                     db='codebakery',
                     charset='utf8')

cursor=db.cursor()

cursor.execute("show tables;")
db.commit
db.close