def solution(num_list):
    if num_list[-1] > num_list[-2]:
        tmp = num_list[-1] - num_list[-2]
        num_list.append(tmp)
        return num_list
    else:
        tmp2 = num_list[-1]*2
        num_list.append(tmp2)
    return num_list