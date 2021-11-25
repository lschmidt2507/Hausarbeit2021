import math

def runs_test(data):
    last_sign=""
    sign=""
    r=0
    #loop over data
    for k in range(1,len(data)):
        if data[k]==data[k-1]:
            sign="0"
        elif data[k]>data[k-1]:
            sign="+"
        else:
            sign="-"
        # test if resulting sign matches previous
        if not last_sign==sign:
            # if not, a new run started
            r+=1
            last_sign=sign
    print(f"r: {r}")
    
    return r
