


def solve():
    class Solution:
        def findRepeatingAndMissing(self, arr):
            n = len(arr)
            freq = [0] * (n + 1)

            # Count frequency of each number
            for num in arr:
                freq[num] += 1

            repeating = -1
            missing = -1

            for i in range(1, n + 1):
                if freq[i] == 2:
                    repeating = i
                elif freq[i] == 0:
                    missing = i

            return [repeating, missing]


if __name__ == "__main__":
    solve()
