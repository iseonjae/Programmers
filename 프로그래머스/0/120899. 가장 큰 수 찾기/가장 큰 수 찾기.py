def solution(array):
    tmp = max(array)
    answer = [tmp, array.index(tmp)]
    return answer