import re
def solution(my_string):
    pattern = r'\d'
    answer1 = re.findall(pattern, my_string)
    answer2 = [int(x) for x in answer1]
    answer = sum(answer2)
    return answer