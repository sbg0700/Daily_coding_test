def solution(numbers):
    num = 0
    numbers.sort()
    a = numbers[0]*numbers[1]
    b = numbers[-1]*numbers[-2]
    
    return max(a,b)