import math
def solution(n):
    if (float(n**(1/2)).is_integer()):
        return int((n**(1/2)+1)**2)
    else:
        return -1

def solution1(n):
    n = n**0.5
    return int(n+1)**2 if n.is_integer()  else -1

def solution2(n):
    return -1 if int(math.sqrt(n)) != math.sqrt(n) else (math.sqrt(n) + 1) ** 2

if __name__ == "__main__":
    print(solution(121))
    print(solution(3))
    print(solution1(121))
    print(solution1(3))
    print(solution2(121))
    print(solution2(3))


