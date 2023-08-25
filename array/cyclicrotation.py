def solution(A, K):
    if not A:
        return A

    N = len(A)
    K = K % N  # Handle cases where K is greater than N
    if K == 0:
        return A

    result = [0] * N
    for i in range(N):
        new_index = (i + K) % N
        result[new_index] = A[i]

    return result

# Example usage
A = [3, 8, 9, 7, 6]
K = 3
rotated_array = solution(A, K)
print("Original array:", A)
print("Array after rotation:", rotated_array)
