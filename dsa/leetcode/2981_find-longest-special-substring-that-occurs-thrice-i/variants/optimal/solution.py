class Solution:
    def maximumLength(self, s: str) -> int:
        longest_runs = [[0, 0, 0] for _ in range(26)]

        start = 0
        for end in range(1, len(s) + 1):
            if end == len(s) or s[end] != s[start]:
                runs = longest_runs[ord(s[start]) - ord("a")]
                runs.append(end - start)
                runs.sort(reverse=True)
                runs.pop()
                start = end

        answer = 0
        for first, second, third in longest_runs:
            answer = max(
                answer,
                first - 2,
                min(first - 1, second),
                third,
            )
        return answer if answer > 0 else -1
