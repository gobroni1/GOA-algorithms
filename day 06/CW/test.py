ls = [1,6,1,670,48,3]
v = 1
n = len(ls)
for i in range(n):
    if v == ls[i]:
        if i == n:
            print("not found")
            break
        else:
            print(f"found at index {i}")
            break
print("not found")
            
            