def solve(n: int) -> int:
    words = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    parity = 0

    while n:
        for letter in words[n % 10]:
            parity ^= 1 << (ord(letter) - ord("a"))
        n //= 10

    return parity.bit_count()
