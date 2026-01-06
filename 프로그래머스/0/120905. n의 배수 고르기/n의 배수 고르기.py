def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

#리스트를 요구하는 문제에서는 리스트로 답변이 가장 pythonic
def solution(n,numlist):
    return [i for i in numlist if i%n == 0]














def solution(n,numlist):
    return list(filter(lambda x: x%n == 0, numlist))






