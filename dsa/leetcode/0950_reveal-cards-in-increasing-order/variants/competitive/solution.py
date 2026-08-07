from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        positions = deque(range(len(deck)))
        answer = [0] * len(deck)
        for value in sorted(deck):
            answer[positions.popleft()] = value
            if positions:
                positions.append(positions.popleft())
        return answer
