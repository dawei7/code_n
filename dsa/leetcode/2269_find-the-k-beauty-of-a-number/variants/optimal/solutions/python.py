def solve(num: int, k: int) -> int:
    digits = str(num)
    answer = 0
    for start in range(len(digits) - k + 1):
        divisor = int(digits[start:start + k])
        if divisor != 0 and num % divisor == 0:
            answer += 1
    return answer
