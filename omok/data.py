import cx_Oracle
import timeclock
def DB_CHECK():
    try:
        db = cx_Oracle.connect("system", "1234", "210.94.95.68:1521/orcl")        
        cursor = db.cursor()
        print("DB was connected - ",end="")
        timeclock.check()
    except:
        print("failed")
def find():
    m = []
    db = cx_Oracle.connect("system", "1234", "localhost:1521/orcl")        
    cursor = db.cursor()
    retain = "SELECT * from TIC"
    cursor.execute(retain)
    for row in cursor:
        s = ({"FIR":row[0],"SEC":row[1],"THR":row[2],"FO":row[3],"FIF":row[4],"SIX":row[5],"SEV":row[6],"EIGH":row[7],"NINE":row[8],"STATUS":row[9]})
        m.append(s)
    db.commit()
    return m
def DB_insert(sh):
    db = cx_Oracle.connect("system", "1234", "localhost:1521/orcl")        
    cursor = db.cursor()
    put = """
    INSERT INTO TIC(FIR,SEC,THR,FO,FIF,SIX,SEV,EIG,NINE,STATUS)
        VALUES ("""
    for i in range(0,9):
        put = put + str(sh[i])+","
    put = put + "'" + str(sh[9]) +"'" +")"
    cursor.execute(put)
    db.commit()
    # print("data was inserted")