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

def dec_to_hex(num):
    ls = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    final_num = []
    
    left_num = num % 16
    div_num = num // 16
    
    if num > 255:
        return "Invalid decimal number"
    
    # მოვამზადოთ ათობითი ნაწილი
    if div_num > 9:
        final_num.append(ls[div_num])
    elif div_num < 10:
        final_num.append(str(div_num)) 
    if left_num > 9:
        final_num.append(ls[left_num])
    elif left_num < 10:
        final_num.append(str(left_num))  

    return "".join(final_num)

print(dec_to_hex(251))
