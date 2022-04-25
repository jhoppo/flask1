import app
@app.app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name)", type(name))
    return f"String => {name}"