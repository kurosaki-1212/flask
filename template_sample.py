from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>hello flask</h1></body></html>'

@app.route('/tmpl_sample1/')
def message():
    q1 = request.args.get('param1', '')
    return render_template('message.html', message=q1)

# パスパラメータ
@app.route('/param/<test>')
def template_ex1(test):
    return render_template('message2.html', p=test)

@app.route('/tmpl_sample2/')
def select_page():
    q1 = request.args.get('pid', '')
    q2 = request.args.get('uname', '')

    if q2=='admin':
        return render_template('template4.html', username=q2, userid=q1)
    elif q1=='1':
        return render_template('template2.html', username=q2)
    elif q1=='2':
        return render_template('template3.html', username=q2)
    else:
        return 'エラー'

if __name__ == '__main__':
    app.run(debug=True)
