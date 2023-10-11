def solution(x):
    #runtime error -> 맞지 않은 풀이
    num = 0;X=x;
    while X>10:
        num+=X%10
        X=x//10
    if x%num == 0:
        return True
    else:
        return False
print(solution(12))


def solution1(x):
    answer = True
    num=str(x)
    k=0
    for i in num:
        k+=int(i)
    if x%k == 0:
        return True
    else:
        return False
print(solution1(12))


def solution2(x):
    return x % sum(int(i) for i in str(x) )==0

def solution3(n):
    return n % sum(map(int, str(n))) == 0

def is_harshad(x):
    return x % sum(int(d) for d in str(x) if d.isdigit()) == 0
