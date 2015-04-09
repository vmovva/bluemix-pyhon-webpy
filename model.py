import web
from dbutils import connect2clearDB,initDB

db= connect2clearDB()

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())

# code to create table if it doesn't exist
try:
    db.select('todo')
except:
   initDB()
