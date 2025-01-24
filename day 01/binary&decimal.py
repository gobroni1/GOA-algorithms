def binary_to_decimal(n):
    sum = 0
    for i in range (1,len(str(n))+1):
        sum += int(str(n)[i-1])*(2**(len(str(n))-i))
    return sum

print(binary_to_decimal(11010))


def decimal_to_binary (n):
    bi = []
    res = n
    while res > 0:
        if n % 2 == 0:
            bi.append("0")
            n = n / 2
            res = n
        else:
            bi.append("1")
            n = (n-1) / 2
            res = n
    return "".join(bi[::-1])

print(decimal_to_binary(26))