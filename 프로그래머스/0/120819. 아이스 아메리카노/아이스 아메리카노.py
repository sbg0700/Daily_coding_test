def solution(money):
    count = money // 5500
    rem = money % 5500
    return [count,rem]