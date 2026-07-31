def solve(s: str, k: int) -> int:
    remaining = k
    required = 1
    factor = 2

    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        if exponent:
            required *= factor ** ((exponent + 1) // 2)
        factor += 1

    if remaining > 1:
        required *= remaining

    period = 2 * required
    vowels = set("aeiou")
    balance = 0
    answer = 0
    frequency = {(0, 0): 1}

    for end, character in enumerate(s, start=1):
        balance += 1 if character in vowels else -1
        state = (balance, end % period)
        answer += frequency.get(state, 0)
        frequency[state] = frequency.get(state, 0) + 1

    return answer
