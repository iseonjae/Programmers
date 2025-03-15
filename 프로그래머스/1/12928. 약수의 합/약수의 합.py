def solution(n):
    num_sum = 0 
    for i in range(1, n+1):
        if n%i == 0:
            num_sum += i
    return num_sum