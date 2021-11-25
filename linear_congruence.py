import math

def linear_congruence(k,l,m,x,j):
    random_nums=[]
    for count in range(j):
        x = x*k+l
        z = (x % m)/m
        random_nums.append(z)
    return random_nums

def to_range(a,b,random_nums):
    return [a+math.floor(random_nums[idx]*(b-a+1)) for idx in range(len(random_nums))]

