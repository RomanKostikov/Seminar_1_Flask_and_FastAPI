# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def news_page():
    news = [
        {
            'title': 'Заголовок новости 1',
            'description': 'Описание новости 1',
            'date': '2023-01-01'
        },
        {
            'title': 'Заголовок новости 2',
            'description': 'Описание новости 2',
            'date': '2023-01-02'
        }
    ]

    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()
