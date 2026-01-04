def solution(n):
    ls = []
    for i in range(1,n+1):
        if n % i ==0:
            ls.append(i)
    return len(ls)

def solution(n):
    return len([i for i in range(1,n+1) if n%i == 0])





