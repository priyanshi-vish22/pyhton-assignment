amount = int(input())
start = int(input())
denoms = [100, 50, 20, 10, 5, 2, 1]
idx = denoms.index(start)
use_denoms = denoms[idx:]
for d in use_denoms:
    match d:
        case 100:
            cnt = amount 
        case 50:
            cnt = amount 
        case 20:
            cnt = amount 
        case 10:
            cnt = amount 
        case 5:
            cnt = amount 
        case 2:
            cnt = amount 
        case 1:
            cnt = amount 
    print(f"{d} rupees note: {cnt}")
    amount %= d