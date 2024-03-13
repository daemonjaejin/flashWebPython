from flask import Flask, request, redirect

app = Flask(__name__)

def getContents():
    litags = ''
    for topic in topics:
        litags += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return litags

def template(contents, content, id=None):
    contextUI = ''
    if(id != None):
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
        '''
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
                    {contextUI}
                </ul>
            </body>
        </html>
    '''    

nextId = 4
topics = [
    {'id': 1, 'title': 'HTML', 'body': 'HTML is ...'},
    {'id': 2, 'title': 'CSS', 'body': 'CSS is ...'},
    {'id': 3, 'title': 'JavaScript', 'body': 'JavaScript is ...'},
]

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello'

# 랜덤 함수를 문자로 변환해서 리턴
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    print('request.method', request.method)
    # if request.method == 'POST':
    #     return ''''''
    # else:
    #     return ''''''
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = f'/read/{nextId}/'
        nextId = nextId + 1
        return redirect(url)
    
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if topic['id'] == id:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = f'/read/{id}/'
        return redirect(url)

# @app.route('/read/<int:post_id>/')
# @app.route('/read/<path:subpath>/')
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if topic['id'] == id:
            title = topic['title']
            body = topic['body']
            break
            
    # return 'random : <strong>'+str(random.random())+'</strong>'
    # return 'Welcome'
    # 작은따옴표 ''' 3개는 여러줄을 표시하기 위해서이다.
    print(title, body)
    return template(getContents(), f'<h2>{title}</h2>{body}', id)

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)

app.run(port=5001, debug=True)

