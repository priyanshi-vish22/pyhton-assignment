#a, b, c = map(int, input().split())
#print(max(a, b, c))

# a, b, c = map(int, input().split())
# max_num = a if (a >= b and a >= c) else (b if b >= c else c)
# print(max_num)


# Find maximum of three numbers

a, b, c = map(int, input("Enter three numbers: ").split())

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

print("Maximum number is:", max_num)