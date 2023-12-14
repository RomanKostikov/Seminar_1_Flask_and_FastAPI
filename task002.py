# Задание №1
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".
# Задание №2
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/contact')
def contact():
    return 'This is the contact page'


if __name__ == '__main__':
    app.run(debug=True)
