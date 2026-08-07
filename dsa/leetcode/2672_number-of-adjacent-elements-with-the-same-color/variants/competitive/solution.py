from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        adjacent_pairs = 0
        answer = []

        for index, new_color in queries:
            old_color = colors[index]
            if old_color != 0:
                if index > 0 and colors[index - 1] == old_color:
                    adjacent_pairs -= 1
                if index + 1 < n and colors[index + 1] == old_color:
                    adjacent_pairs -= 1

            colors[index] = new_color
            if index > 0 and colors[index - 1] == new_color:
                adjacent_pairs += 1
            if index + 1 < n and colors[index + 1] == new_color:
                adjacent_pairs += 1
            answer.append(adjacent_pairs)

        return answer
