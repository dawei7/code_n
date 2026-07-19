from collections import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        eligible = sorted(
            character
            for character, frequency in Counter(s).items()
            if frequency >= k
        )

        def is_repeated(candidate: str) -> bool:
            index = 0
            completed = 0

            for character in s:
                if character != candidate[index]:
                    continue
                index += 1
                if index == len(candidate):
                    completed += 1
                    if completed == k:
                        return True
                    index = 0

            return False

        frontier = [""]
        answer = ""

        while frontier:
            following = []
            for prefix in frontier:
                for character in eligible:
                    candidate = prefix + character
                    if is_repeated(candidate):
                        following.append(candidate)

            if not following:
                break
            answer = max(following)
            frontier = following

        return answer
