def reverse_num(n):
    return int(str(n)[::-1])

N = int(input().strip())

for _ in range(N):
    a, b = input().split()
    ra = reverse_num(a)
    rb = reverse_num(b)
    rs = ra + rb
    print(reverse_num(rs))