def solution(price, money, count):
    answer = -1
    while count>0:
        money -= count*price
        count-=1
    if money > 0:
        return 0
    else:
        return abs(money)
        