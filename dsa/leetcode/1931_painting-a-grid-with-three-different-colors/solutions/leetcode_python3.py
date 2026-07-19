class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        modulo = 1_000_000_007
        states = []

        def build(row: int, state: tuple[int, ...]) -> None:
            if row == m:
                states.append(state)
                return
            for color in range(3):
                if not state or state[-1] != color:
                    build(row + 1, state + (color,))

        build(0, ())
        compatible = [
            [
                next_index
                for next_index, next_state in enumerate(states)
                if all(first != second for first, second in zip(state, next_state))
            ]
            for state in states
        ]

        counts = [1] * len(states)
        for _ in range(1, n):
            next_counts = [0] * len(states)
            for state_index, count in enumerate(counts):
                for next_index in compatible[state_index]:
                    next_counts[next_index] = (
                        next_counts[next_index] + count
                    ) % modulo
            counts = next_counts

        return sum(counts) % modulo
