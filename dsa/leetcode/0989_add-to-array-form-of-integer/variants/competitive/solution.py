from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        answer = []
        index = len(num) - 1
        carry = k

        while index >= 0 or carry:
            total = carry
            if index >= 0:
                total += num[index]
            answer.append(total % 10)
            carry = total // 10
            index -= 1

        answer.reverse()
        return answer
