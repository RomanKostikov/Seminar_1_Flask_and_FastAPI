# Задание №5
# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return ("<head><title>Моя первая HTML страница</title></head>"
            "<body><h1>Моя первая HTML страница</h1><p>Привет, мир!</p></body>")


if __name__ == '__main__':
    app.run(debug=True)
