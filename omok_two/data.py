import cx_Oracle
import timeclock
import os
def DB_CHECK():
    current = os.path.dirname(__file__)
    cx_Oracle.init_oracle_client(current+"/instantclient_19_11")
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    print("DB was connected - ",end="")
    timeclock.check()
def find_wait():
    m = []
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    retain = "SELECT * from USERWAIT"
    cursor.execute(retain)
    for row in cursor:
        s = ({"USERID":row[0],"PINNUM":row[1]})
        m.append(s)
    db.commit()
    return m
def DB_insert(sh):
    print(sh)
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    put = """
    INSERT INTO USERWAIT(USERID,PINNUM)
        VALUES ("""
    put = put + "'" + str(sh[0]) +"'"+","
    put = put + str(sh[1]) +")"
    cursor.execute(put)
    db.commit()
    # print("data was inserted")
def DB_delete(sh):
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    put = """
    DELETE USERWAIT
      WHERE USERID = """
    put += "'"+str(sh)+"'"
    cursor.execute(put)
    db.commit()
def CRE(mama):
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    put = """CREATE TABLE """+mama+""" (
    NO NUMBER(10),
    X NUMBER(10),
    Y NUMBER(10)
)"""
    print(mama)
    cursor.execute(put)
    db.commit()
def drop(sh):
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    put = """
    DROP TABLE """
    put += sh
    cursor.execute(put)
    db.commit()
def DB_insert2(sh,mama):
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    put = """INSERT INTO """+mama+"""(NO,X,Y)
                VALUES ("""
    put = put  + str(sh[0]) +","
    put = put + str(sh[1]) +","
    put = put + str(sh[2]) +")"
    cursor.execute(put)
    db.commit()
    # print("data was inserted")
def find_wait2(mama):
    m = []
    db = cx_Oracle.connect("system", "1234", "211.243.158.233:1521/orcl")        
    cursor = db.cursor()
    retain = "SELECT * from "+mama
    cursor.execute(retain)
    for row in cursor:
        s = ({"NO":row[0],"X":row[1],"Y":row[2]})
        m.append(s)
    db.commit()
    return m