class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        answer = 0

        for text in strs:
            value = int(text) if text.isdigit() else len(text)
            answer = max(answer, value)

        return answer
