def solution(my_string):
    k = []
    for i in my_string:
        for u in i:
            if u.isdigit():
                k.append(int(u))
    k.sort()
                
    return k

