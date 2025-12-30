def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    if sides[0] < sides[1]+sides[2]:
        answer = 1
    else:
        answer = 2
    return answer


def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2




