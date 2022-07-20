from flask import Flask
from flask import render_template
from flask import request
# menu.htmlはBootstrapを使っているのでimport
from flask_bootstrap import Bootstrap

import trans_text_ja_2

app = Flask(__name__)
bootstrap = Bootstrap(app)

# 直接アクセスした場合もメニューに強制遷移
@app.route('/')
def index():
    return render_template('menu.html')

# メニュー画面
@app.route('/menu/')
def trans_menu():
    return render_template('menu.html')

# ==================================
# 翻訳へ
# @app.route('/trans/', methods=['GET'])
@app.route('/trans/')
def trans_top():
    return render_template('translate.html', input_text='', output_text='')

# パラメータがある場合は、翻訳して表示する
@app.route('/trans/', methods=['POST'])
def trans():
    # リクエストパラメータを読み込む
    in_text = request.form['input_text']
    # リクエストパラメータが空ならinput_textとoutput_textは空表示のままtranslate.htmlを表示する
    if in_text == '':
        return render_template('translate.html', input_text='', output_text='')
    # trans_text_ja_2のtrans関数を呼び出す
    result = trans_text_ja_2.translate(in_text)
    return render_template('translate.html', input_text=in_text, output_text=result['TranslatedText'])
# ==================================

# プログラムの実行
if __name__ == '__main__':
    app.run(debug=True)
