import sqlite3
from bottle import route, run, debug, template, request, error, CherryPyServer

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = template('todo_list', rows=result)
    return output

@route('/new', method='GET')
def new_item():
    if request.GET.get('save', '').strip():
        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        query = "INSERT INTO todo (task,status) VALUES ('%s',1)" %new
        c.execute(query)
        conn.commit()
        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        return '<p>The new task was inserted into the database, the ID is %s</p>' %new_id
    else:
        return template('new_todo')

@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        query = "UPDATE todo SET task = '%s', status = '%s' WHERE id LIKE '%s'" % (edit,status,no)
        c.execute(query)
        conn.commit()

        return '<p>The item number %d was successfully updated</p>' %no

    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        query = "SELECT task, status FROM todo WHERE id LIKE '%d'" %no
        c.execute(query)
        cur_data = c.fetchone()

        return template('edit_todo', old = cur_data, no = no)

@error(404)
@error(403)
def mistake404(code):
    return 'The parameter you passed has the wrong format!'

@error(500)
def mistake500(code):
    return '500 error!'

debug(True)
run(server=CherryPyServer, host='0.0.0.0', port=8888)