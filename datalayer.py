from sqlite3 import connect, Error
from logger import log
import config
from datetime import datetime
from os import path


def connectdb():
    cfg = config.get()
    connection = connect(cfg['db_lite'])
    return connection

def handle_error(err):
    log(err)


def execute_select(query, data={}, multi=False):
    result = []
    try:
        connection = connectdb()
        cursor = connection.cursor()
        cursor.execute(query, data)
        for row in cursor:
            result.append(row)
        return result
    except Error as err:
        handle_error(err)
    else:
        connection.close()


def execute_nonquery(query, params, multi=False):
    try:
        connection = connectdb()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
    except Error as err:
        handle_error(err)
    else:
        connection.close()


def ensure_db():
    cfg = config.get()
    if not path.isfile(cfg['db_lite']):
        create_db()


def create_db():
    try:
        connection = connectdb()
        c = connection.cursor()
        c.execute('''CREATE TABLE pictures (picId INTEGER, picFile TEXT, picTitle TEXT, picInserted INTEGER)''')
        connection.commit()
    except Error as err:
        handle_error(err)
    else:
        connection.close()


def get_pictures(max):
    return map(lambda t: {'id': t[0], 'url': '/img/'+t[1], 'title': t[2], 'inserted': t[3]},
               execute_select("SELECT picId, picFile, picTitle, picInserted FROM pictures ORDER BY picInserted DESC LIMIT %d" % max))


def add_picture(filename, title):
    execute_nonquery("INSERT INTO pictures(picId, picFile, picTitle, picInserted) VALUES(?, ?, ?, ?)", [datetime.now().timestamp(), filename, title, datetime.now().timestamp()])


ensure_db()