def solution(myString, pat):
    str1 = myString.upper()
    pat1 = pat.upper()
    
    if pat1 in str1:
        return 1
    else:
        return 0