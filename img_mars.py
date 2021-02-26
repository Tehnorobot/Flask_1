from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index_2():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    strings = '</br>'.join(['Человечество вырастает из детства.',
    'Человечеству мала одна планета.', 'Мы сделаем обитаемыми безжизненные пока планеты.',
    'И начнем с Марса!', 'Присоединяйся!'])
    return strings


@app.route('/image_mars')
def image_mars():
    res = '</br>'.join(['<title>Привет, Марс!</title>', 
                        '<h1>Жди нас, Марс!</h1>',
                        f'''<img src="{url_for('static', filename='img/mars.png')}"''',
                        '<br>Вот она какая, красная планета.</br>'])
    return res


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')