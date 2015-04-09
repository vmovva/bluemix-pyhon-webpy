# Parase VCAP_SERVICES

import os
import json
import web
import MySQLdb

appservices_json    = os.environ.get('VCAP_SERVICES')
decoded_appservices = json.loads(appservices_json)
clearDB_service     = decoded_appservices['cleardb'][0]
clearDB_credentials = clearDB_service['credentials']
clearDB_host        = clearDB_credentials['hostname']
clearDB_port        = int(clearDB_credentials['port'])
clearDB_dbname      = clearDB_credentials['name']
clearDB_username    = clearDB_credentials['username']
clearDB_password    = clearDB_credentials['password']

def connect2clearDB() :

  db = web.database(dbn='mysql', db=clearDB_dbname , user=clearDB_username , pw=clearDB_password , host=clearDB_host , port=clearDB_port)
  return db

def initDB():
   dbinit=MySQLdb.connect(host=clearDB_host,port=clearDB_port,passwd=clearDB_password,db=clearDB_dbname,user=clearDB_username)
   cursorVar=dbinit.cursor()
   sql= ''' CREATE TABLE todo (
                               id INT AUTO_INCREMENT,
                               title TEXT,
                               primary key (id)
                              ) '''
   cursorVar.execute(sql)
   dbinit.commit()
   dbinit.close()

