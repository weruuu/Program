from flask import Flask, request, render_template ,jsonify
import pymysql
import json

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='demo1029',
    db='mysql',
    charset='utf8'
)
cursor = connect.cursor()
app = Flask(__name__)
testInfo = {}
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    sql = "select count(*) from web_user where userid = '" + username + "'"
    cursor.execute(sql)
    if cursor.fetchone()[0] == 0 :
        return render_template('form.html', message='User not exists', username=username)
    sql = "select password from web_user where userid = '" + username + "'"
    cursor.execute(sql)
    s_password = cursor.fetchone()[0]
    if s_password != '' and password == s_password:
        return render_template('signok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    password1 = request.form['password1']
    sql = "select count(*) from web_user where userid = '" + username + "'"
    cursor.execute(sql)
    if cursor.fetchone()[0] > 0:
        return render_template('signup.html', message='User already exists', username=username)
    if username != '' and password != '' and password==password1:
        sql = "insert into web_user values('"+username+"','"+password+"')"
        cursor.execute(sql)
        connect.commit()
        return render_template('form.html', username=username)
    return render_template('signup.html', message='Invalid username or password', username=username)

@app.route('/search_data', methods=['GET', 'POST'])  # 路由
def test_post():
    row_id = 1
    sql = 'select * from web_user'
    cursor.execute(sql)
    for i in cursor.fetchall():
        ele_id = i[0]
        ele_pw = i[1]
        testInfo[row_id] = {"ID":ele_id,"PASSWORD":ele_pw}
        row_id = row_id + 1
    print(testInfo)
    return json.dumps(testInfo)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)