import math
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    g = math.gcd(X, Y)
    l = (X * Y) 
    print(g, l)