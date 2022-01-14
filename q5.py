def solution(numbers):
    numbers.sort()
    return numbers[(len(numbers)-1)//2]

numbers = [1,49,51,52,101]
answer = solution(numbers)
print(answer)
