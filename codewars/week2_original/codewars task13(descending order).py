def descending_order(num):
    ar = []
    mult = 1
    sum = 0
    while num >= 1:
        ar.append(num%10)
        num = num//10
        round(num)
    ar.sort()
    for i in range(len(ar)):
        sum += ar[i]*mult
        mult *= 10
    return sum
        