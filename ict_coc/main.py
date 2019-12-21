from flask import Flask,render_template
import pymysql
app=Flask(__name__)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='tjsaud7001!!',
                     db='ict_coc',
                     charset='utf8')
cursor=db.cursor()

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/beamaps')
def search_beacon():
	cursor.execute('select * from beacon')
	data=cursor.fetchall()
	return render_template('beacon_search.html',data=data)

@app.route('/beaorder')
def order_beacon():
	return render_template('beacon_order.html')

if __name__ == '__main__':
	app.run(port='5000',debug=True)