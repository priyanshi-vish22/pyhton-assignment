N = int(input())
i = 1
stones = N
while True:
    if stones < i:
        print("Ramesh")
        break
    stones -= i
    if stones < 2 * i:
        print("Suresh")
        break
    stones -= 2 * i
    i += 1