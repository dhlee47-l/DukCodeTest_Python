def solution(array, commands):
    answer = []
    result = []
    for i,j,k in commands:
        result = sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer

def solution2(array, command):
    answer =[]
    for i, j, k in command:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


# 테스트 코드
def test_solution():
    # 입출력 예시에 따른 테스트 케이스
    test_cases = [
        ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5, 6, 3]),
    ]

    for array, commands, expected in test_cases:
        result = solution(array, commands)
        assert result == expected, f"Expected {expected}, but got {result}"

def test_solution2():
    # 입출력 예시에 따른 테스트 케이스
    test_cases = [
        ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5, 6, 3]),
    ]

    for array, commands, expected in test_cases:
        result = solution2(array, commands)
        assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_solution()
    test_solution2()
    print("All tests passed!")