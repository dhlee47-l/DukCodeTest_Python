def solution(ingredients):
    answer = 0
    stack = []

    for ingredient in ingredients:
        stack.append(ingredient)

        while len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1

    return answer

# 입출력 예 #1
ingredients1 = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredients1))

# 입출력 예 #2
ingredients2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredients2))
