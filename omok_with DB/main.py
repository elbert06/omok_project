import timeclock
import omok
import data
import start
import os
current = os.path.dirname(__file__)
os.environ["Path"] = os.environ["Path"] + current+"/instantclient_19_11"+";"
os.environ["ORACLE_HOME"] = current+"/instantclient_19_11"+";"
os.environ["TNS_ADMIN"] = current+"/instantclient_19_11/network/admin"+";"
print(os.environ.get("ORACLE_HOME"))
print(os.environ.get("TNS_ADMIN"))
print("program started - ",end="")
timeclock.check()
data.DB_CHECK()
start.start()
