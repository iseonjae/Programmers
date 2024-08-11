def solution(numbers):
    max_num = max(numbers)
    numbers.remove(max_num)
    second_num = max(numbers)
    answer = max_num * second_num
    return answer