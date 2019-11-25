# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
import json
import pymysql

app = Flask(__name__)  # 实例化app对象

testInfo = {}

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='Eviless',
    passwd='demo1029',
    db='mysql',
    charset='utf8'
)
cursor = connect.cursor()

@app.route('/test_post/nn', methods=['GET', 'POST'])  # 路由
def test_post():
    row_id = 1
    sql = 'select * from web_user'
    cursor.execute(sql)
    for i in cursor.fetchall():
        print(i)
        ele_id = i[0]
        ele_pw = i[1]
        testInfo[row_id] = {"ID":ele_id,"PASSWORD":ele_pw}
        row_id = row_id + 1
    print(testInfo)
    return json.dumps(testInfo)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',  # 任何ip都可以访问
            port=7777,  # 端口
            debug=True
            )
