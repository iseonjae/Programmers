def solution(s):
    list1 = list(map(int, s.split() ))
    return str(min(list1)) + ' ' + str(max(list1))

# .split() : 문자열을 공백 기준으로 리스트로 변환
# map(int, list) : 리스트 원소들을 정수형으로 변환