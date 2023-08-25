# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    expected_sum = ((n+1)*(n+2))//2
    actual_sum = sum(A)
    missing_element = expected_sum - actual_sum
    return missing_element
