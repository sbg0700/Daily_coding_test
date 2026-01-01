def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)




def solution(array,height):
    count = 0
    array.append(height)
    for i in array:
        if height <i:
            count += 1

    return count


