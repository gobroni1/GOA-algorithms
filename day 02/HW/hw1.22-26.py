# ს.თოფურია 1, მაგალითები 1.22 - 1.26.  (გვ. 179-180)

#1.22 (1)

def partial (frac,num):
    ls = frac.split("/")
    return (num/int(ls[0])) * int(ls[1])

print(partial("2/3",50))

#1.22 (2)

