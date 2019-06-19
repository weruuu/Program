from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    requestJsonString = request.form.dict()
    requestDict = eval(requestJsonString.keys()[0])
    username = requestDict.get('username')
    password = requestDict.get('password')
    print(username,password)
    # username = request.form['username']
    # password = request.form['password']
    # if username=='admin' and password=='password':
    #     return render_template('./ServerDevelop/signinok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()