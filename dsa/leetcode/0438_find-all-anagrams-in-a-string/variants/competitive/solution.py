from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_length = len(p)
        if window_length > len(s):
            return []

        pattern_counts = [0] * 26
        window_counts = [0] * 26
        for index in range(window_length):
            pattern_counts[ord(p[index]) - ord("a")] += 1
            window_counts[ord(s[index]) - ord("a")] += 1

        answer = [0] if window_counts == pattern_counts else []
        for right in range(window_length, len(s)):
            left = right - window_length
            window_counts[ord(s[left]) - ord("a")] -= 1
            window_counts[ord(s[right]) - ord("a")] += 1
            if window_counts == pattern_counts:
                answer.append(left + 1)
        return answer
