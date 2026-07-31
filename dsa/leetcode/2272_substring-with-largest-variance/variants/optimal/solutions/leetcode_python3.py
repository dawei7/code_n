from collections import Counter


class Solution:
    def largestVariance(self, s: str) -> int:
        totals = Counter(s)
        answer = 0

        for major in totals:
            for minor in totals:
                if major == minor:
                    continue

                major_count = 0
                minor_count = 0
                remaining_minor = totals[minor]

                for character in s:
                    if character == major:
                        major_count += 1
                    elif character == minor:
                        minor_count += 1
                        remaining_minor -= 1
                    else:
                        continue

                    if minor_count > 0:
                        answer = max(answer, major_count - minor_count)

                    if major_count < minor_count and remaining_minor > 0:
                        major_count = 0
                        minor_count = 0

        return answer
