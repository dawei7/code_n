def solve(num: int) -> int:
    digits = str(num)
    odd = sorted(character for character in digits if int(character) % 2)
    even = sorted(character for character in digits if int(character) % 2 == 0)
    return int(
        "".join(
            odd.pop() if int(character) % 2 else even.pop()
            for character in digits
        )
    )
