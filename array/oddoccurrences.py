def solution(A):
    result = 0
    for num in A:
        result ^= num  # XOR operation
    return result

# Example usage
A = [9, 3, 9, 7, 3]
unpaired_element = solution(A)
print("Unpaired element:", unpaired_element)
