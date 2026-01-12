def solution(my_string):
    a = "aeiou"
    answer = ''
    for i in my_string:
        if i not in a:
            answer += i
    return answer

