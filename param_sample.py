from flask import Flask, request
app = Flask(__name__)
 
# パスパラメータ
@app.route('/user/<user_id>')
def get_path_param(user_id):
    return '<html><body><h1>パスパラメータ:' + user_id + '</h1></body></html>'

@app.route('/city/<city_id>')
def path_param_ex1(city_id):
    return '<html><body><h1>こんにちは、{}に住んでいる皆さん！'.format(city_id) + '</h1></body></html>'

@app.route('/user')
def get_query_param():
    user_id = request.args.get('id')
    return '<html><body><h1>クエリパラメータ:' + user_id + '</h1></body></html>'

@app.route('/data')
def get_query_param_ex1():
    user_countory = request.args.get('country')
    return '<html><body><h1>Hello ' + user_countory + '</h1></body></html>'

@app.route('/user', methods=['POST'])
def get_request_param():
    user_id = request.form['id']
    return '<html><body><h1>リクエストパラメータ:' + user_id + '</h1></body></html>'

@app.route('/info', methods=['POST'])
def get_request_param_ex():
    user_id = request.form['id']
    user_name = request.form['name']
    return '<html><body><h1>' + user_name + 'さん(' + user_id + ')こんにちは！' + '</h1></body></html>'

@app.route('/calc', methods=['POST'])
def get_request_param_ex2():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    return '<html><body><h1>{}*{}の結果は{}です。'.format(num1, num2, num1 * num2) + '</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
