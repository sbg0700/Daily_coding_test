def solution(my_string, letter):
    a = ""
    for i in my_string:
        if i not in letter:
            a += i
    return a



