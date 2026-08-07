class Solution:
    def minimumOperations(self, num: str) -> int:
        length = len(num)
        answer = length - 1 if "0" in num else length

        for target in ("00", "25", "50", "75"):
            index = length - 1
            deletions = 0

            while index >= 0 and num[index] != target[1]:
                index -= 1
                deletions += 1

            index -= 1
            while index >= 0 and num[index] != target[0]:
                index -= 1
                deletions += 1

            if index >= 0:
                answer = min(answer, deletions)

        return answer
