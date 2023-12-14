# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # context students
    students = [
        {'first_name': 'John', 'last_name': 'Doe', 'age': 20, 'average_score': 85},
        {'first_name': 'Jane', 'last_name': 'Smith', 'age': 22, 'average_score': 90},
        {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 21, 'average_score': 95}
    ]
    return render_template('task006.html', students=students)


if __name__ == '__main__':
    app.run()
