from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        balls = 0
        moves = 0
        for index in range(len(boxes)):
            answer[index] += moves
            balls += boxes[index] == "1"
            moves += balls

        balls = 0
        moves = 0
        for index in range(len(boxes) - 1, -1, -1):
            answer[index] += moves
            balls += boxes[index] == "1"
            moves += balls

        return answer
