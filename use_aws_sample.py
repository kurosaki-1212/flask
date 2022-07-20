from flask import Flask
from flask import render_template
from flask import request

import trans_text_ja_2

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>hello flask</h1></body></html>'

# 直接URLを開いてパラメータが無い場合は、空欄のまま表示する
@app.route('/aws/', methods=['GET'])
def trans_top():
    return render_template('translate.html', input_text='', output_text='')

# パラメータがある場合は、翻訳して表示する
@app.route('/aws/', methods=['POST'])
def trans():
    # リクエストパラメータを読み込む
    in_text = request.form['input_text']

    # trans_text_ja_2のtrans関数を呼び出す
    result = trans_text_ja_2.translate(in_text)
    return render_template('translate.html', input_text=in_text, output_text=result['TranslatedText'])

if __name__ == '__main__':
    app.run()
