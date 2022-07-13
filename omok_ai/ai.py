import key
from keras.models import load_model
def analyze(gameboard_list,black_position,white_position):
    model = load_model("omok_white.h5")
    r = list(model.predict([gameboard_list])[0])
    
    while True:
        e = (r.index(max(r)))-1
        c = int(e/15)
        d = int(e%15)
        if(black_position.__contains__([50*d+35,50*c+35]) or white_position.__contains__([50*d+35,50*c+35]) ):
            r[r.index(max(r))] = 0
        else:
            return d,c
def analyze_black(gameboard_list,black_position,white_position):
    print("analyzing...")
    gameboard_list2 = gameboard_list
    model = load_model("omok_black.h5")
    r = list(model.predict([gameboard_list])[0])
    g = []
    for im in r:
        for ik in im:
            g.append(ik)
    m = []
    n = []
    k = []
    for gi in range(0,225):
        if(gameboard_list[int(gi/15)][int(gi%15)] == 0):
            gameboard_list[int(gi/15)][int(gi%15)] = 1
            if(key.check(gameboard_list)[0] == True):
                return int(gi%15),int(gi/15)
            urgent = check(gameboard_list)
            if(urgent == True):
                n.append(int(gi/15)*15+int(gi%15))
            gameboard_list[int(gi/15)][int(gi%15)] = -1
            if(key.check(gameboard_list)[0] == True):
                k.append([int(gi%15),int(gi/15)])
            urgent = check(gameboard_list)
            if(urgent == True):
                m.append(int(gi/15)*15+int(gi%15))
            gameboard_list[int(gi/15)][int(gi%15)] = 0
    print("evaluating...")
    while True:
        e = (g.index(max(g)))
        c = int(e/15)
        d = int(e%15)
        possibleto = check2(gameboard_list2,d,c)
        if(possibleto == False):
            g[g.index(max(g))] = -1
        else:
            if(len(k)!= 0):
                return k[0][0],k[0][1]
            elif(len(m) == 0):            
                return d,c
            elif(len(m) != 0):
                rm = []
                for i in m:
                    rm.append(g[i])
                e = (g.index(max(rm)))
                c = int(e/15)
                d = int(e%15)
                return d,c
            else:
                rm = []
                for i in n:
                    rm.append(g[i])
                e = (g.index(max(rm)))
                c = int(e/15)
                d = int(e%15)
                return d,c
def check(gameboard_list):
    m = []
    ss = 0
    for i in range(len(gameboard_list)):
        for s in gameboard_list[i]:
            m.append(s)
    for h in range(0,len(m)):
        try:
            if m[h] == m[h+1] and m[h+2] == m[h+1] and m[h+3] == m[h+2] and m[h] != 0 and (m[h-1] == 0 and m[h+4] == 0):
                return True
            if m[h] == m[h+15] and m[h+30] == m[h+45] and m[h+15] == m[h+30] and m[h] != 0 and (m[h-15] == 0 and m[h+60] == 0):
                return True

            if m[h] == m[h+16] and m[h+32] == m[h+48] and m[h+16] == m[h+32] and m[h] != 0 and (m[h-16] == 0 and m[h+64] == 0):
                return True

            if m[h] == m[h+14] and m[h+28] == m[h+42] and m[h+14] == m[h+28] and m[h] != 0 and (m[h-14] == 0 and m[h+56] == 0):
                return True
        except:
            continue
    return False
def check2(gameboard_list,x,y):
    if(gameboard_list[y][x] == 0):
        gameboard_list[y][x] = 1
        real = 0
        m = []
        for i in range(len(gameboard_list)):
            for s in gameboard_list[i]:
                m.append(s)
        for h in range(1,len(m)):
            try:
                if m[h] == m[h+1] and m[h+2] == m[h+1] and m[h] == 1 and (m[h-1] == 0 and m[h+3] == 0):
                    real += 1
                if m[h] == m[h+15] and m[h+15] == m[h+30] and m[h] == 1 and (m[h-15] == 0 and m[h+45] == 0):
                    real += 1
                if m[h] == m[h+16] and m[h+16] == m[h+32] and m[h] == 1 and (m[h-16] == 0 and m[h+48] == 0):
                    real += 1
                if m[h] == m[h+14] and m[h+14] == m[h+28] and m[h] == 1 and (m[h-14] == 0 and m[h+42] == 0):
                    real += 1
            except:
                continue
        gameboard_list[y][x] = 0
        if(real < 2):
            return True
    return False