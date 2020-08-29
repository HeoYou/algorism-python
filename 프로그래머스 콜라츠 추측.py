def solution(num):
    answer = 0
    while True:
        if num == 1:
            return answer
        elif answer >= 500:
            return -1

        if num % 2 == 0:
            num //= 2
            answer += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            answer += 1
    return answer