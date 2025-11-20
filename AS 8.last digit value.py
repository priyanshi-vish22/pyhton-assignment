def last_digit(a, b):
    last = a % 10
    if last in {0, 1, 5, 6}:
        return last
    cycles = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    cycle = cycles[last]
    idx = (b - 1) % len(cycle)   
    return cycle[idx]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(last_digit(a, b))