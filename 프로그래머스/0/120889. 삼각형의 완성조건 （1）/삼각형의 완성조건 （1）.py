def solution(sides):
    a = 0
    sides.sort()
    if sides[2] >= sides[0]+sides[1]:
        a = 2
    else:
        a = 1
    return a


def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2





