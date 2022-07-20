from flask import Flask
app = Flask(__name__)
 
@app.route('/hello')
def hello_flask ():
    a = '''
        <html>
            <body>
                <h1>
                    hello world
                </h1>
                <h2>
                    this is test page.
                </h2>
            </body>
        </html>
    '''
    return '<html><body><h1>hello world!!</h1><h2>this is test page.</h2></body></html>'

@app.route('/morning')
def morning_flask ():
    return '<html><body><h1>good morning</h1><h2>this is test page.</h2></body></html>'

if __name__ == '__main__':
    app.run(debug=True)