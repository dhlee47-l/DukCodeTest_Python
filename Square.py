def solution(n):
    x = int(n ** 0.5)  
    if x * x == n: 
        return (x + 1) ** 2
    else:
        return -1


print("입출력 예#1")
n1 = 121
print(f"n={n1}, return {solution(n1)}")

print("입출력 예#2")
n2 = 3
print(f"n={n2}, return {solution(n2)}")