import tecto
import random
import time
import data
import checks
def pro(lis):
    print(lis[0],lis[1],lis[2],sep=" ")
    print(lis[3],lis[4],lis[5],sep=" ")
    print(lis[6],lis[7],lis[8],sep=" ")
def tectoc():
    bye = 0
    for sf in range(1):
        lis = ["a"]*9
        sh = []
        pro(lis)
        for sss in range(0,5):
            inp = int(input())
            inp_data = inp-1
            while lis[inp_data] != "a":
                inp = int(input())
                inp_data = inp-1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            lis[inp_data] = "o"
            ra = inp_data
            bye,ch = tecto.check(lis)
            sh.append(inp_data+1)
            if bye == 1:
                while len(sh) != 9:
                    sh.append(0)
                pro(lis)
                print("o의 승리")
                sh.append("l")
                break
            pro(lis)
            print("\n")
            if sss == 4:
                sh.append("t")
                data.DB_insert(sh)
                break
            while lis[ra] != "a":
                ra = checks.checking(sh)
            ra = tecto.real(ra, lis)
            lis[ra] = "x"
            bye,ch = tecto.check(lis)
            sh.append(ra+1)
            if bye == 1:
                while len(sh) != 9:
                    sh.append(0)
                pro(lis)
                print("x의 승리")
                sh.append("w")
                data.DB_insert(sh)
                break
            pro(lis)
        if sss == 4 and bye != 1:
            print("tie")


