from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Nope'


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div class="text-center">                           
                                <h2>Анкета претендета</h2>
                                <h4>на участии в миссии</h4>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div class="form-group">
                                        <label for="classSelect"></label>
                                        <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть проффессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="en_is" value="en_is" checked>
                                          <label class="form-check-label" for="en_is">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="pilot" value="pilot">
                                          <label class="form-check-label" for="en_st">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="builder" value="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="ekzobiol" value="ekzobiol">
                                          <label class="form-check-label" for="ekzobiol">
                                            Экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="en_ter" value="en_ter">
                                          <label class="form-check-label" for="en_ter">
                                            Инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="klimat" value="klimat">
                                          <label class="form-check-label" for="klimat">
                                            Климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="spez_rad_protect" value="spez_rad_protect">
                                          <label class="form-check-label" for="spez_rad_protect">
                                            Cпециалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="astreolog" value="astreolog">
                                          <label class="form-check-label" for="astreolog">
                                            Астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="glaziolog" value="glaziolog">
                                          <label class="form-check-label" for="glaziolog">
                                            Гляциолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="en_shizn" value="en_shizn">
                                          <label class="form-check-label" for="en_shizn">
                                            Инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="meteo" value="meteo">
                                          <label class="form-check-label" for="meteo">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="op_marshod" value="op_marshod">
                                          <label class="form-check-label" for="op_marshod">
                                            Оператор марсохода
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="kiber_en" value="kiber_en">
                                          <label class="form-check-label" for="kiber_en">
                                            Киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="shtyrman" value="shtyrman">
                                          <label class="form-check-label" for="shtyrman">
                                            Штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="proffesion" id="pilot_dron" value="pilot_dron">
                                          <label class="form-check-label" for="pilot_dron">
                                            Пилот дронов
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссие?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['proffesion'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])

        return "Форма отправлена"


@app.route('/index')
def rout():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    list = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    countdown_list = [x for x in list]
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <h4>Вот она какая, красная планета.</h4>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-secondary" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h2>Мое предложение: {planet_name}</h2>
                        <h4>Эта планета близка к Земле;</h4>
                        <div class="alert alert-success" role="alert">
                          На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-warning" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Наконец, она просто красива!
                        </div>
                      </body>
                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h2>Результат отбора</h2>
                        <h4>Претендента на участие в миссии {nickname}:</h4>
                        <div class="alert alert-success" role="alert">
                          Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </div>
                        <div class="card mb-3">
                          <div class="card-body">
                            составляет {rating}!
                          </div>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Желаем удачи!
                        </div>
                      </body>
                    </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f"""<html>
                        <head>
                        <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Загрузка фотографии</title>
                        </head>
                        <body>
                            <div class="text-center">  
                                <h2>Загрузка фотографии</h2>
                            </div>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </body>
                    </html>"""
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
            return "Файл не выбран."
        if f:
            try:
                filename = f.filename
                file_path = os.path.join('static/img', filename)
                file_path2 = f'img/{filename}'
                print(file_path2)
                f.save(file_path)
                return f"""<html>
                            <head>
                            <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Загрузка фотографии</title>
                            </head>
                            <body>
                                <div class="text-center">  
                                    <h2>Загрузка фотографии</h2>
                                </div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="{url_for('static', filename=file_path2)}" 
           alt="здесь должна была быть картинка, но не нашлась">
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </body>
                        </html>"""
            except Exception as e:
                return f"Произошла ошибка: {str(e)}"
        else:
            return "Файл не выбран."


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
