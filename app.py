from flask import Flask
import random

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello'

# 랜덤 함수를 문자로 변환해서 리턴
@app.route('/')
def index():
    # return 'random : <strong>'+str(random.random())+'</strong>'
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

# @app.route('/read/<int:post_id>/')
# @app.route('/read/<path:subpath>/')
@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+str(id)

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)

app.run(port=5001, debug=True)

