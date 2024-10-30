# 한 자리 정수로 이루어진 문자열 `num_str` 이 주어질 때, 각 자리수의 합을 return

def solution(num_str):

    int_num = sum(int(digit) for digit in num_str)

    return int_num