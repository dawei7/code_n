def solve(n: int, l: int, r: int) -> int:
    modulus = 1_000_000_007
    value_count = r - l + 1
    state = list(range(value_count))
    transition = [
        [0] * (value_count - value) + [1] * value
        for value in range(value_count)
    ]

    def apply(matrix: list[list[int]], vector: list[int]) -> list[int]:
        return [
            sum(coefficient * count for coefficient, count in zip(row, vector))
            % modulus
            for row in matrix
        ]

    def multiply(
        left: list[list[int]], right: list[list[int]]
    ) -> list[list[int]]:
        right_columns = list(zip(*right))
        return [
            [
                sum(a * b for a, b in zip(row, column)) % modulus
                for column in right_columns
            ]
            for row in left
        ]

    exponent = n - 2
    while exponent:
        if exponent & 1:
            state = apply(transition, state)
        exponent >>= 1
        if exponent:
            transition = multiply(transition, transition)

    return 2 * sum(state) % modulus
