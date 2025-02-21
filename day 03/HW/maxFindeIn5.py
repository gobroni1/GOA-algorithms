# 5! = 2*3*4*5 = 120

# inefficient code 
def maxFinde (a,b,c,d,e):
    MAX = a
    if b > MAX:
        MAX = b
    if c > MAX:
        MAX = c
    if d > MAX:
        MAX = d
    if e > MAX:
        MAX = e
    return MAX

# efficient code
def maxFinde2 (a,b,c,d,e):  # მაქსიმალური მინიჭება - 0; მაქსიმალური შედარება - 4; მინიმალური შედარება - 
    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return a
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
        else: # c > [a,b]
            if c > d:
                if c > e:
                    return c
                else:
                    return e
            else: # d > [a,b,c]
                if d > e:
                    return d
                else:
                    return e
    else: # b > a
        if b > c:
            if b > d:
                if b > e:
                    return b
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
        else: # c > [a,b]
            if c > d:
                if c > e:
                    return c
                else:
                    return e
            else:
                if d > e:
                   return d
                else:
                    return e
             
            
 
# print(maxFinde2(1,2,3,4,5))
# print(maxFinde2(1,5,2,3,4))
# print(maxFinde2(1,2,5,3,4))
# print(maxFinde2(1,2,3,5,4))

# i did same proses for all other max posibilities bit by hand 

# all 24 possible arrangments of 4 numbers (a,b,c,d) because e is largest, every list has same arrangment of a,b,c,d witch is a,b,c,d 
# ls1 = [100, 90, 80, 70]
# ls2 = [100, 90, 70, 80]
# ls3 = [100, 80, 90, 70]
# ls4 = [100, 70, 90, 80]
# ls5 = [100, 80, 70, 90]
# ls6 = [100, 70, 80, 90]
# ls7 = [90, 100, 80, 70]
# ls8 = [90, 100, 70, 80]
# ls9 = [80, 100, 90, 70]
# ls10 = [70, 100, 90, 80]
# ls11 = [80, 100, 70, 90]
# ls12 = [70, 100, 80, 90]
# ls13 = [90, 80, 100, 70]
# ls14 = [90, 70, 100, 80]
# ls15 = [80, 90, 100, 70]
# ls16 = [70, 90, 100, 80]
# ls17 = [80, 70, 100, 90]
# ls18 = [70, 80, 100, 90]
# ls19 = [90, 80, 70, 100]
# ls20 = [90, 70, 80, 100]
# ls21 = [80, 90, 70, 100]
# ls22 = [70, 90, 80, 100]
# ls23 = [80, 70, 90, 100]
# ls24 = [70, 80, 90, 100]


# same list in 2d list for looping over 
lst = [
    [100, 90, 80, 70],
    [100, 90, 70, 80],
    [100, 80, 90, 70],
    [100, 70, 90, 80],
    [100, 80, 70, 90],
    [100, 70, 80, 90],
    [90, 100, 80, 70],
    [90, 100, 70, 80],
    [80, 100, 90, 70],
    [70, 100, 90, 80],
    [80, 100, 70, 90],
    [70, 100, 80, 90],
    [90, 80, 100, 70],
    [90, 70, 100, 80],
    [80, 90, 100, 70],
    [70, 90, 100, 80],
    [80, 70, 100, 90],
    [70, 80, 100, 90],
    [90, 80, 70, 100],
    [90, 70, 80, 100],
    [80, 90, 70, 100],
    [70, 90, 80, 100],
    [80, 70, 90, 100],
    [70, 80, 90, 100]
]

res = []
e= 101

for ls in lst:
    assignment = 0
    MAX = ls[0]  # Fix: Initialize MAX with the first element of ls
    assignment += 1
    if ls[1] > MAX:
        MAX = ls[1]
        assignment += 1
    if ls[2] > MAX:
        MAX = ls[2]
        assignment += 1
    if ls[3] > MAX:
        MAX = ls[3]
        assignment += 1

    res.append([ls, assignment])

print(res)
# same list but paierd with number of ssignments they took

[[[100, 90, 80, 70], 1], 
 [[100, 90, 70, 80], 1],
 [[100, 80, 90, 70], 1], 
 [[100, 70, 90, 80], 1], 
 [[100, 80, 70, 90], 1], 
 [[100, 70, 80, 90], 1], 
 [[90, 100, 80, 70], 2], 
 [[90, 100, 70, 80], 2], 
 [[80, 100, 90, 70], 2], 
 [[70, 100, 90, 80], 2], 
 [[80, 100, 70, 90], 2], 
 [[70, 100, 80, 90], 2], 
 [[90, 80, 100, 70], 2], 
 [[90, 70, 100, 80], 2], 
 [[80, 90, 100, 70], 3], 
 [[70, 90, 100, 80], 3],
 [[80, 70, 100, 90], 2],
 [[70, 80, 100, 90], 3], 
 [[90, 80, 70, 100], 2], 
 [[90, 70, 80, 100], 2],
 [[80, 90, 70, 100], 3], 
 [[70, 90, 80, 100], 3], 
 [[80, 70, 90, 100], 3], 
 [[70, 80, 90, 100], 4]]

#same lists but converted in to a,b,c,d and gruped by number assignments they took
# 1 assignment:
# [['a', 'b', 'c', 'd'],
#  ['a', 'b', 'd', 'c'],
#  ['a', 'c', 'b', 'd'],
#  ['a', 'd', 'b', 'c'],
#  ['a', 'c', 'd', 'b'],
#  ['a', 'd', 'c', 'b']]

# 2 assignments:
# [['b', 'a', 'c', 'd'],
#  ['b', 'a', 'd', 'c'],
#  ['c', 'a', 'b', 'd'],
#  ['d', 'a', 'b', 'c'],
#  ['c', 'a', 'd', 'b'],
#  ['d', 'a', 'c', 'b'],
#  ['b', 'c', 'a', 'd'],
#  ['b', 'd', 'a', 'c'],
#  ['c', 'b', 'a', 'd'],
#  ['d', 'b', 'a', 'c']]

# 3 assignments:
# [['c', 'b', 'd', 'a'],
#  ['d', 'b', 'c', 'a'],
#  ['c', 'd', 'a', 'b'],
#  ['d', 'c', 'a', 'b'],
#  ['c', 'd', 'b', 'a'],
#  ['d', 'c', 'b', 'a']]

# 4 assignments:
# [['d', 'c', 'b', 'a']]