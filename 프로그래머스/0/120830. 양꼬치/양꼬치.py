def solution(n, k):
    tmp = n // 10
    answer = n*12000 + (k-tmp)*2000
    return answer