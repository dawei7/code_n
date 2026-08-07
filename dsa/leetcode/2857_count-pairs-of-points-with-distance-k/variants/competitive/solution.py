class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        answer = 0
        seen = {}

        for x, y in coordinates:
            for x_distance in range(k + 1):
                partner = (x ^ x_distance, y ^ (k - x_distance))
                answer += seen.get(partner, 0)
            seen[(x, y)] = seen.get((x, y), 0) + 1

        return answer
