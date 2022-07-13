import tecto
import random
import time
import data
def tectoc():
    bye = 0
    for sf in range(10000):
        print(sf)
        bye = 0
        if sf % 100 == 0:
            print(sf)
        lis = ["a"]*9
        sh = []
        for sss in range(0,5):
            inp = 4
            inp_data = inp-1
            while lis[inp_data] != "a":
                inp = random.randint(1,9)
                inp_data = inp-1
            inp = tecto.real2(inp,lis)
            inp_data = inp-1
            lis[inp_data] = "o"
            ra = inp_data
            bye,ch = tecto.check(lis)
            sh.append(inp_data+1)
            if bye == 1:
                while len(sh) != 9:
                    sh.append(0)
                s = lis[ch]
                sh.append("l")
                data.DB_insert(sh)
                break
            if sss == 4:
                sh.append("t")
                break
            while lis[ra] != "a":
                ra = random.randint(0,8)
            ra = tecto.real(ra,lis)
            lis[ra] = "x"
            sh.append(ra+1)
            bye,ch = tecto.check(lis)
            if bye == 1:
                while len(sh) != 9:
                    sh.append(0)
                s = lis[ch]
                sh.append("w")
                data.DB_insert(sh)
                break
        data.find()
        time.sleep(1)


