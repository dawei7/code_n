class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {1: 0}

        def power(start):
            value = start
            path = []
            while value not in powers:
                path.append(value)
                value = value // 2 if value % 2 == 0 else 3 * value + 1

            steps = powers[value]
            while path:
                value = path.pop()
                steps += 1
                powers[value] = steps
            return powers[start]

        ordered = sorted(
            range(lo, hi + 1),
            key=lambda value: (power(value), value),
        )
        return ordered[k - 1]
