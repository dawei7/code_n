from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_u, first_v = edges[0]
        second_u, second_v = edges[1]
        if first_u == second_u or first_u == second_v:
            return first_u
        return first_v
