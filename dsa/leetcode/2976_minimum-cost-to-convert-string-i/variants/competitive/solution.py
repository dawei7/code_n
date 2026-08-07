from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        alphabet = 26
        infinity = 10**30
        distance = [[infinity] * alphabet for _ in range(alphabet)]
        for letter in range(alphabet):
            distance[letter][letter] = 0

        for start, end, price in zip(original, changed, cost):
            first = ord(start) - ord("a")
            second = ord(end) - ord("a")
            distance[first][second] = min(distance[first][second], price)

        for middle in range(alphabet):
            for first in range(alphabet):
                through_middle = distance[first][middle]
                if through_middle == infinity:
                    continue
                for second in range(alphabet):
                    candidate = through_middle + distance[middle][second]
                    if candidate < distance[first][second]:
                        distance[first][second] = candidate

        answer = 0
        for start, end in zip(source, target):
            price = distance[ord(start) - ord("a")][ord(end) - ord("a")]
            if price == infinity:
                return -1
            answer += price
        return answer
