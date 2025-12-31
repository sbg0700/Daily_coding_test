def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer



def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))




