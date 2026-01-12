def solution(num_list):
    a = 0  # 짝수 개수
    b = 0  # 홀수 개수
    answer = []
    
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    
    answer.append(a)
    answer.append(b)
    return answer

