import timeit  
old = int(timeit.default_timer())
def check():
    new = int(timeit.default_timer())
    times = new-old
    minu = int(times / 60)
    secs = times % 60
    print(str(minu)+"m "+str(secs)+"s")
