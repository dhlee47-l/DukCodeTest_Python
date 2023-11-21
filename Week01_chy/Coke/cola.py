def solution(a, b, n):
    answer = 0
    if n==1:
        return 0;
    while n > 1:
        answer += b*(n/a)
        n = n//a +n%a
    return answer


print(solution(2,1,20))