from typing import List


class Solution:
    def platesBetweenCandles(
        self,
        s: str,
        queries: List[List[int]],
    ) -> List[int]:
        length = len(s)
        plates = [0] * (length + 1)
        nearest_left = [-1] * length
        last_candle = -1

        for index, character in enumerate(s):
            plates[index + 1] = plates[index] + (character == "*")
            if character == "|":
                last_candle = index
            nearest_left[index] = last_candle

        nearest_right = [-1] * length
        next_candle = -1
        for index in range(length - 1, -1, -1):
            if s[index] == "|":
                next_candle = index
            nearest_right[index] = next_candle

        answer = []
        for left, right in queries:
            first_candle = nearest_right[left]
            last_candle = nearest_left[right]
            if first_candle == -1 or first_candle >= last_candle:
                answer.append(0)
            else:
                answer.append(plates[last_candle] - plates[first_candle])
        return answer
