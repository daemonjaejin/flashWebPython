from flask import Flask
import random
import pymysql
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Session

# from flaskext.mysql import MySQL

# mysql = MySQL()

app = Flask(__name__)

# app.config['MYSQL_DATABASE_USER'] = ''
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = ''
# app.config['MYSQL_DATABASE_HOST'] = ''
# mysql.init_app(app)

_host = '3.37.55.65'
_user = 'svc'
_password = 'svc123$%^'
_db = 'python'
_charset = 'utf8'

db = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)

cursor = db.cursor()

sql = "SELECT * FROM topics"

cursor.execute(sql)

topics = cursor.fetchall()

cursor.close()

# conn = mysql.connect()
# cursor = conn.cursor()
# sql = """SELECT * FROM topics"""
# value = (_user, _password, _db, _charset)
# cursor.execute('set names utf8')
# cursor.execute(sql, value)

# topics = cursor.fetchall()
# cursor.close()
# conn.close()

print(f'topics : {topics}')
for topic in topics:
    print(f'topic : {topic[0]}')

def getContents():
    litags = ''
    for topic in topics:
        # litags += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        litags = litags + f'<li><a href="/read/{topic[0]}/">{topic[1]}</a></li>'
    # return 'random : <strong>'+str(random.random())+'</strong>'
    # return 'Welcome'
    # 작은따옴표 ''' 3개는 여러줄을 표시하기 위해서이다.
    return litags

def template(contents, content):
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                    <li><a href="/create/">create</a></li>
                </ul>
            </body>
        </html>
    '''    

# topics = [
#     {'id': 1, 'title': 'HTML', 'body': 'HTML is ...'},
#     {'id': 2, 'title': 'CSS', 'body': 'CSS is ...'},
#     {'id': 3, 'title': 'JavaScript', 'body': 'JavaScript is ...'},
# ]

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello'

# 랜덤 함수를 문자로 변환해서 리턴
@app.route('/')
def index():
    # litags = ''
    # for topic in topics:
        # litags += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        # litags = litags + f'<li><a href="/read/{topic[0]}/">{topic[1]}</a></li>'
    # return 'random : <strong>'+str(random.random())+'</strong>'
    # return 'Welcome'
    # 작은따옴표 ''' 3개는 여러줄을 표시하기 위해서이다.
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''

    return template(getContents(), content)

# @app.route('/read/<int:post_id>/')
# @app.route('/read/<path:subpath>/')
@app.route('/read/<int:id>/')
def read(id):
    # print(type(id))
    # litags = ''
    # for topic in topics:
        # litags += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        # litags = litags + f'<li><a href="/read/{topic[0]}/">{topic[1]}</a></li>'

    title = ''
    body = ''
    for topic in topics:
        if topic[0] == id:
            title = topic[1]
            body = topic[2]
            break;
            
    # return 'random : <strong>'+str(random.random())+'</strong>'
    # return 'Welcome'
    # 작은따옴표 ''' 3개는 여러줄을 표시하기 위해서이다.
    print(title, body)
    return template(getContents(), f'<h2>{title}</h2>{body}')

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)

app.run(port=5001, debug=True)

