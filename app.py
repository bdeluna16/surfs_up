from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(use_reloader=True)

@app.route('/Page2')
def bye_world():
    return 'Goodbye World'
