def solution(N):
    binary_representation = bin(N)[2:]  # Convert to binary and remove the '0b' prefix
    max_gap = 0
    current_gap = 0
    counting = False
    
    for digit in binary_representation:
        if digit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                counting = True
        elif counting:
            current_gap += 1
    
    return max_gap

# Example usage
N = 1041
print("Longest binary gap:", solution(N))
