def solution(num1, num2):
    result = (num1 == num2)
    dict1 = {True:1, False:-1}
    return dict1[result]