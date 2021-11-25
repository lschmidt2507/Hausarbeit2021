import math
import scipy.special

def frequency_test(data,min_value,max_value):
    n=len(data)
    frequencies = {}
    for val in data:
        if val in frequencies:
            frequencies[val]+=1
        else:
            frequencies[val]=1
    max_freq=max(frequencies,key=frequencies.get)
    print(f"{max_freq = }")
    print(f"{frequencies[max_freq]=}")
    
    p_binom=1/(max_value-min_value+1)
    p=0
    for i in range(frequencies[max_freq],n+1):
        p+=scipy.special.binom(n, i)*(p_binom**i)*(1-p_binom)**(n-i)
    return p

