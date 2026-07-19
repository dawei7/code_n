class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            n = len(s)
            doubled = s + s
            first = 0
            second = 1
            offset = 0

            while first < n and second < n and offset < n:
                left = doubled[first + offset]
                right = doubled[second + offset]
                if left == right:
                    offset += 1
                    continue

                if left > right:
                    first += offset + 1
                    if first == second:
                        first += 1
                else:
                    second += offset + 1
                    if first == second:
                        second += 1
                offset = 0

            start = min(first, second)
            return doubled[start : start + n]

        counts = [0] * 26
        for character in s:
            counts[ord(character) - ord("a")] += 1
        return "".join(
            chr(ord("a") + index) * count for index, count in enumerate(counts)
        )
