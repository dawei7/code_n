class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        frequencies = [0] * 26
        left = 0
        qualifying = 0
        answer = 0

        for character in s:
            index = ord(character) - ord("a")
            frequencies[index] += 1
            if frequencies[index] == k:
                qualifying += 1

            while qualifying:
                left_index = ord(s[left]) - ord("a")
                if frequencies[left_index] == k:
                    qualifying -= 1
                frequencies[left_index] -= 1
                left += 1

            answer += left

        return answer
