from typing import List


class Solution:
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]],
    ) -> List[List[int]]:
        first = 0
        second = 0
        answer = []

        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])
            if start <= end:
                answer.append([start, end])

            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1

        return answer
