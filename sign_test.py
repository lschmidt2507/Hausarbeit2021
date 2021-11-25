import math
import scipy.special

def sign_test(data):
    diffs = []
    # get differences
    for idx, val in enumerate(data[:-1]):
        diffs.append(val-data[idx+1])
    # last difference
    diffs.append(data[-1]-data[0])
    # compute
    n=len(diffs)
    r_plus=0
    r_minus=0
    zeros=0
    for value in diffs:
        if value>0:
            r_plus+=1
        elif value<0:
            r_minus+=1
        elif value==0:
            zeros+=1
    r_plus+=math.floor(zeros/2)
    r_minus+=math.floor(zeros/2)
    r=max(r_plus,r_minus)
    print(f"r_plus: {r_plus}")
    print(f"r_minus: {r_minus}")
    print(f"n: {n}")
    p=0
    
    for i in range(r,n+1):
        p+=scipy.special.binom(n, i)*(0.5**n)
    return p
