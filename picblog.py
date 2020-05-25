from bottle import Bottle, run, request, static_file, template, redirect
from datetime import datetime
import datalayer as datalayer
import os

#vytvorim server
app = Bottle()


@app.get('/')
def home():
    return show_list()


@app.get('/tag/<tagname>')
def tag(tagname):
    return show_list(tagname)


def show_list_test(filter=None):
    imgs = [
        {
            'title': 'Jablko',
            'url': '/img/1.jpg'
        },
        {
            'title': 'Tim Barners-Lee',
            'url': '/img/2.jpg'
        },
        {
            'title': 'Racci',
            'url': '/img/3.jpg'
        },
        {
            'title': 'Talk Code',
            'url': '/img/4.png'
        }
    ]
    return template('list', {'imgs': imgs})


def show_list(filter=None):
    imgs = datalayer.get_pictures(20)
    return template('list', {'imgs': imgs})


@app.get('/add')
def add_form():
    return template('addform')


@app.post('/add')
def add_form_post():
    title = request.forms.get('txtitle')
    upload = request.files.get('upload')

    upload.save(os.path.join('imgs', upload.filename))
    datalayer.add_picture(upload.filename, title)
    redirect('/', 302)


@app.get('/img/<file_name>')
def images(file_name):
    return static_file(file_name, 'imgs')


#spustim server na adrese localhost a portu 8080...url tedy bude http://localhost:8080
#run(app, host='localhost', port=8080, debug=True)