def check(lis):
    if lis[0] == lis[3] and lis[3] == lis[6] and lis[6] != "a":
        return 1,0
    if lis[1] == lis[4] and lis[4] == lis[7] and lis[7] != "a":
        return 1,1
    if lis[2] == lis[5] and lis[5] == lis[8] and lis[8] != "a":
        return 1,2
    if lis[0] == lis[1] and lis[1] == lis[2] and lis[2] != "a":
        return 1,0
    if lis[3] == lis[4] and lis[3] == lis[5] and lis[4] != "a":
        return 1,3
    if lis[6] == lis[7] and lis[6] == lis[8] and lis[8] != "a":
        return 1,6
    if lis[2] == lis[4] and lis[4] == lis[6] and lis[4] != "a":
        return 1,2
    if lis[0] == lis[4] and lis[4] == lis[8] and lis[8] != "a":
        return 1,0
    else:
        return 0,0
def real(rs,lis):
    pin = lis
    for sr in range(0,len(pin)):
        if pin[sr] == "a":
            pin[sr] = "x"
            sc,ch = check(pin)
            if sc == 1:
                return sr
            else:
                pin[sr] = "a"
    for sr in range(0,len(pin)):
        if pin[sr] == "a":
            pin[sr] = "o"
            sc,ch = check(pin)
            if sc == 1:
                return sr
            else:
                pin[sr] = "a"
    return rs
def real2(rs,lis):
    pin = lis
    for sr in range(0,len(pin)):
        if pin[sr] == "a":
            pin[sr] = "o"
            sc,ch = check(pin)
            if sc == 1:
                return sr+1
            else:
                pin[sr] = "a"
    for sr in range(0,len(pin)):
        if pin[sr] == "a":
            pin[sr] = "x"
            sc,ch = check(pin)
            if sc == 1:
                return sr
            else:
                pin[sr] = "a"
    return rs