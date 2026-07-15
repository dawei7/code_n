def solve(low, high):
    digits = "123456789"
    answer = []
    for length in range(2, 10):
        for start in range(10 - length):
            value = int(digits[start:start + length])
            if low <= value <= high:
                answer.append(value)
    return answer
