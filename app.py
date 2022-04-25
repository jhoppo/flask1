from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello World1"

@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    return f"String => {name}"

@app.route('/data/appInfo/<int:id>', methods=['GET'])
def queryDataMessageByID(id):
    return f"String => {id}"

@app.route('/data/appInfo/<version>', methods=['GET'])
def queryDataMessageByVersion(version):
    return f"String => {version}"

@app.route('/data/appInfo/<author>', methods=['GET'])
def queryDataMessageByAuthor(author):
    return f"String => {author}"

@app.route('/data/appInfo/<remark>', methods=['GET'])
def queryDataMessageByRemark(remark):
    return f"String => {remark}"

@app.route('/text')
def text():
    return '<html><body><h1>HELLO WORLD</h1></body></html>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page/text')
def PageText():
    return render_template('page.html', text="Python Flask !")

@app.route('/page/app')
def PageAppInfo():
    appInfo={
        'id': 5,
        'name': 'Python - Flask',
        'version': '0.0.1',
        'author': 'JieHong',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text 01',
        '02': 'Text 02',
        '03': 'Text 03',
        '04': 'Text 04',
        '05': 'Text 05'
    }
    return render_template('page.html', data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

