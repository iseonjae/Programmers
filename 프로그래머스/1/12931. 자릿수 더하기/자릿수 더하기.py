def solution(n):
    n_str = str(n)
    num_sum = 0
    for i in range(0, len(n_str)):
        num_sum += int(n_str[i])
    return num_sum