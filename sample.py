from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_flask ():
    return '<html><body><h1>hello flask</h1></body></html>'

@app.route('/ciao')
def ciao_flask ():
    return '<html><body><h1>ciao flask</h1></body></html>'

if __name__ == '__main__':
    app.run()