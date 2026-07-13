"""Deterministic rand7-stream adapter for LeetCode 470."""


def solve(rand7_values: list[int], draws: int) -> list[int]:
    stream_index = 0

    def rand7() -> int:
        nonlocal stream_index
        value = rand7_values[stream_index % len(rand7_values)]
        stream_index += 1
        return value

    output = []
    for _ in range(draws):
        while True:
            cell = (rand7() - 1) * 7 + rand7()
            if cell <= 40:
                output.append(1 + (cell - 1) % 10)
                break
    return output
