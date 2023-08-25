import math

def solution(X, Y, D):
    min_jumps = math.ceil((Y - X) / D)
    return min_jumps
