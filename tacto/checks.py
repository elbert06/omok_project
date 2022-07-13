import statistics as st
import data
import random
def checking(sh):
    dict_ = data.find()
    m = ["FIR","SEC","THR","FO","FIF","SIX","SEV","EIG","NINE","STATUS"]
    ss = []
    for i in range(0,len(dict_)):
        s = dict(dict_[i])
        if len(sh) == 1:
            if s.get(m[0]) == sh[0] and s.get(m[9]) == 'w':
                ss.append(int(s.get(m[1])))
        elif len(sh) == 2:
            if s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[9]) == 'l':
                ss.append(int(s.get(m[2])))
        elif len(sh) == 3:
            if s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2] and s.get(m[9]) == 'w':
                ss.append(int(s.get(m[3])))
        elif len(sh) == 4:
            if (s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2]
            and s.get(m[3]) == sh[3] and s.get(m[9]) == 'l'):
                ss.append(int(s.get(m[4])))
        elif len(sh) == 5:
            if (s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2]
            and s.get(m[3]) == sh[3] and s.get(m[4]) == sh[4] and s.get(m[9]) == 'w'):
                ss.append(int(s.get(m[5])))
        elif len(sh) == 6:
            if (s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2]
            and s.get(m[3]) == sh[3] and s.get(m[4]) == sh[4] and s.get(m[5]) == sh[5] and s.get(m[9]) == 'l'):
                ss.append(int(s.get(m[6])))
        elif len(sh) == 7:
            if (s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2]
            and s.get(m[3]) == sh[3] and s.get(m[4]) == sh[4] and s.get(m[5]) == sh[5] and s.get(m[6]) == sh[6] and s.get(m[9]) == 'w'):
                shs = int(str(s.get(m[7])))
                ss.append(shs)
        elif len(sh) == 8:
            if (s.get(m[0]) == sh[0] and s.get(m[1]) == sh[1] and s.get(m[2]) == sh[2]
            and s.get(m[3]) == sh[3] and s.get(m[4]) == sh[4] and s.get(m[5]) == sh[5]
            and s.get(m[6]) == sh[6] and s.get([m[8]]) == sh[8] and s.get(m[9]) == 'l'):
                ss.append(int(s.get(m[8])))
    if len(ss) != 0:
        if ss.__contains__(0):
            ss.remove(0)
        return int(st.mode(ss)) - 1
    else:
        return random.randint(0,8)