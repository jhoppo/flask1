from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    print("SS")
    return "Hello World1"

@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    return f"String => {name}"

@app.route('/text')
def text():
    return '<html><body><h1>HELLO WORLD</h1></body></html>'

@app.route('/home')
def home():
    return render_template('homt.html')