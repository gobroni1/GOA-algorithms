# exomple 1 (3 შედარება, 0 მინიჭება, 4 ცვლადი)    
a = 8
b = 3
c = 5
d = 9
if a > b: 
    if a > c:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
else:
    if b > c:
        if b > d:
            print(b)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)

# exomple 2 (3 შედარება, min-1 მინიჭება, 5   ცვლადი)       
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
print(largest)