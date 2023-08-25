# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    total_sum = sum(A)
    left_sum = 0
    min_diff = float('inf')

    for num in A[:-1]:
        left_sum += num
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff

