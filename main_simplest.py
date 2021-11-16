from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def root():
    return '<h1>Pybcn</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
