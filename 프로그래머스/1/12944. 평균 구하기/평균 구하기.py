def solution(arr):
    num_sum = 0
    for i in range(0, len(arr)):
        num_sum += arr[i]
        mean_arr = num_sum / len(arr)
    return mean_arr