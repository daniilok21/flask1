from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')