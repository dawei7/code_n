def solve(n: int, k: int) -> str:
    characters = ['a'] * n
    remaining = k - n

    for index in range(n - 1, -1, -1):
        increase = min(25, remaining)
        characters[index] = chr(ord('a') + increase)
        remaining -= increase
        if remaining == 0:
            break

    return ''.join(characters)
