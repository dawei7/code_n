from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)
        return sum(candies)
