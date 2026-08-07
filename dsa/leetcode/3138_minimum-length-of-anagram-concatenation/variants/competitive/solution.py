class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)

        for length in range(1, n + 1):
            if n % length != 0:
                continue

            target = [0] * 26
            for index in range(length):
                target[ord(s[index]) - ord("a")] += 1

            valid = True
            for start in range(length, n, length):
                counts = [0] * 26
                for index in range(start, start + length):
                    counts[ord(s[index]) - ord("a")] += 1
                if counts != target:
                    valid = False
                    break

            if valid:
                return length

        return n
