"""Reference solution for LeetCode 1388."""


def solve(slices: list[int]) -> int:
    choose = len(slices) // 3

    def best_linear(values: list[int]) -> int:
        impossible = float("-inf")
        previous_two = [impossible] * (choose + 1)
        previous_one = [impossible] * (choose + 1)
        previous_two[0] = 0
        previous_one[0] = 0

        for value in values:
            current = previous_one.copy()
            for count in range(1, choose + 1):
                current[count] = max(
                    previous_one[count],
                    previous_two[count - 1] + value,
                )
            previous_two, previous_one = previous_one, current

        return previous_one[choose]

    return max(
        best_linear(slices[:-1]),
        best_linear(slices[1:]),
    )
