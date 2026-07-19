def solve(n: int, k: int) -> list[int]:
    cap = 10**18
    factorial = [1] * (n + 1)
    for value in range(1, n + 1):
        factorial[value] = min(cap, factorial[value - 1] * value)

    def count_with_next(odd_count: int, even_count: int, next_parity: int) -> int:
        length = odd_count + even_count
        next_slots = (length + 1) // 2
        other_slots = length // 2
        required_odd = next_slots if next_parity == 1 else other_slots
        required_even = length - required_odd
        if odd_count != required_odd or even_count != required_even:
            return 0
        return min(cap, factorial[odd_count] * factorial[even_count])

    numbers = list(range(1, n + 1))
    odd_count = (n + 1) // 2
    even_count = n // 2
    answer: list[int] = []
    previous_parity: int | None = None

    while numbers:
        chosen = False
        for index, value in enumerate(numbers):
            parity = value & 1
            if previous_parity is not None and parity == previous_parity:
                continue
            next_odd = odd_count - parity
            next_even = even_count - (1 - parity)
            ways = (
                count_with_next(next_odd, next_even, 1 - parity)
                if next_odd + next_even
                else 1
            )
            if k > ways:
                k -= ways
                continue
            answer.append(value)
            numbers.pop(index)
            odd_count = next_odd
            even_count = next_even
            previous_parity = parity
            chosen = True
            break
        if not chosen:
            return []
    return answer
