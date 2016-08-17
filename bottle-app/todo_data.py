import sqlite3

db = sqlite3.connect('todo.db')
db.execute("CREATE TABLE todo (id integer PRIMARY KEY autoincrement, task char(100) NOT NULL, status bool NOT NULL)")
db.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
db.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
db.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
db.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
db.commit()