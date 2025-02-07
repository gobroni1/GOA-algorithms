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
             
            
 
print(maxFinde2(1,2,3,4,5))
print(maxFinde2(1,5,2,3,4))
print(maxFinde2(1,2,5,3,4))
print(maxFinde2(1,2,3,5,4))
