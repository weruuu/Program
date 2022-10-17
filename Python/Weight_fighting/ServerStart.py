from flask import Flask, request, render_template ,jsonify
import time
import json

app = Flask(__name__,template_folder='./static/templates')
testInfo = {}
@app.route('/', methods=['GET', 'POST'])
def home():
    ip = request.remote_addr
    fbl = open('ipblack.txt', 'r+')
    abl = fbl.read().splitlines()
    logallow = 1
    for i in abl:
        print(i)
        if ip == i:
            logallow = 0
            break
    print(ip)
    if logallow == 1 :
        return render_template('biview.html')
    return 0


@app.route('/echarts.js',methods = ['GET', 'POST'])
def echartsJs():
    return render_template('echarts.js')

@app.route('/data_log',methods = ['GET', 'POST'])
def data_log():
    username = request.form['username']
    weight = request.form['Weight']
    print(username,weight)
    if len(username)>0 :
        f = open('weight1.txt', 'r')
        a = f.readlines()
        f = open('weight1.txt', 'w')

        insert = (username+','+weight).split(',')
        is_new = 1
        for i in range(len(a)):

            if a[i].split(',')[2].strip().find(time.strftime("%Y-%m-%d", time.localtime())) != -1 and insert[0] == 'Nancy':
                a[i] = insert[1] + ',' + a[i].split(',')[1] + ',' + a[i].split(',')[2]
                is_new = 0
                print('uN',insert,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            if a[i].split(',')[2].strip().find(time.strftime("%Y-%m-%d", time.localtime())) != -1 and insert[0] == 'SXA':
                a[i] = a[i].split(',')[0] + ',' + insert[1] + ',' + a[i].split(',')[2]
                is_new = 0
                print('uX',insert,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        if is_new == 1 and insert[0] == 'Nancy':
            a.append(insert[1] + ',,' + time.strftime("%Y-%m-%d", time.localtime()) + '\n')
            print('iN',insert,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if is_new == 1 and insert[0] == 'SXA':
            a.append(',' + insert[1] + ',' + time.strftime("%Y-%m-%d", time.localtime()) + '\n')
            print('iS',insert,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write(''.join(a))
        f.close()
        return render_template('biview.html')
    return 0

@app.route('/search_data', methods=['GET', 'POST'])
def test_post():
    f = open('weight1.txt', 'r')
    a = f.readlines()
    row_id = 1
    for i in a:
        testInfo[row_id] = {"Nweight":i.split(',')[0],"Sweight":i.split(',')[1],"date":i.split(',')[2]}
        row_id = row_id + 1
    return json.dumps(testInfo)

@app.route('/echart', methods=['GET', 'POST'])
def index():
    return render_template('biview.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)