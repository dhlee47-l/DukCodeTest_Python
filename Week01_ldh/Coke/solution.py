def solution(a, b, n):
    answer = 0

    while n >= a:
        full_bottles = n // a
        answer += full_bottles * b
        n = full_bottles * b + n % a

    return answer

# 입출력 예 #1
a1, b1, n1 = 2, 1, 20
print(solution(a1, b1, n1))

# 입출력 예 #2
a2, b2, n2 = 3, 1, 20
print(solution(a2, b2, n2))
