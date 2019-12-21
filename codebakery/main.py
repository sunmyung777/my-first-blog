from flask import Flask, request, redirect,render_template,url_for,session
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='tjsaud7001!!',
                     db='codebakery',
                     charset='utf8')

cursor=db.cursor()

app=Flask(__name__)

app.secret_key='secret_key'

@app.route('/')
def home():
    if('username' in session):
        username='hello, '+session['username']
    else :
        username='not login'
    return render_template('index.html',username=username)

@app.route('/login', methods=['GET','POST'])
def login():
    if(request.method=='POST'):
        userid=request.form['id']
        pwd=request.form['pwd']
        cursor.execute('select userid from user where userid="'+userid+'"')
        req=cursor.fetchall()
        if(len(req)==0):
            session['username']='no id'
            return redirect('/')
        else:
            cursor.execute('select password from user where userid="'+userid+'"')
            req=cursor.fetchall()
            if(req[0][0]==pwd):
                session['username']=userid;
                return redirect('/')
    else:
        return'''
        <form action="/login" method="POST">
        <input type="text" name="id" placehorder="아이디">
        <input type="password" name="pwd" placehorder="비밀번호">
        <input type="submit" value="login">
        </form>
         '''
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect('/')

@app.route('/register',methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        userid=request.form['id']
        password=request.form['pwd']
        cursor.execute('insert into user(userid,password) values('+str(userid)+','+str(password)+')')
        db.commit()
        redirect('/')
    else :
        return'''
        <form action="/register" method="POST">
        <input type="text" name="id" placehorder="아이디">
        <input type="password" name="pwd" placehorder="비밀번호">
        <input type="submit" value="login">
        </form>
        '''
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    db.close()