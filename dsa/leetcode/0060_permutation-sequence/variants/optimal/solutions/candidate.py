def solve(n: int, k: int) -> str:
    digits = [str(x) for x in range(1, n + 1)]
    block_size = 1
    for x in range(2, n):
        block_size *= x

    rank = k - 1
    answer: list[str] = []
    while digits:
        i, rank = divmod(rank, block_size)
        answer.append(digits.pop(i))
        if digits:
            block_size //= len(digits)
    return "".join(answer)
