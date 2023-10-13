def solution(x):
    digit_sum = sum(map(int, str(x)))
    
    if x % digit_sum == 0:
        answer = True
    else:
        answer = False
    
    return answer

# 입출력 예 #1
x = 10
result = solution(x)
print(f"If x={x}, return {result}")

# 입출력 예 #2
x = 12
result = solution(x)
print(f"If x={x}, return {result}")

# 입출력 예 #3
x = 11
result = solution(x)
print(f"If x={x}, return {result}")

# 입출력 예 #4
x = 13
result = solution(x)
print(f"If x={x}, return {result}")