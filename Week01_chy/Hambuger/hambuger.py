
def solution(ingredient):
    answer = 0
    ham=[]
    for i in ingredient:
        ham.append(i)
        if ham[-4:]==[1,2,3,1]:
            answer+=1
            del ham[-4:]

    return answer
def test_solution():
    test_cases = [
        ([2, 1, 1, 2, 3, 1, 2, 3, 1], 2),
        ([1, 3, 2, 1, 2, 1, 3, 1, 2], 0)
    ]

    for ingredient, expected in test_cases:
        result = solution(ingredient)
        assert result == expected, f"For ingredient {ingredient}, expected {expected}, but got {result}"

if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
