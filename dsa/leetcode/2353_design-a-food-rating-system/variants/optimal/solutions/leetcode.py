import heapq
from collections import defaultdict
from typing import List


class FoodRatings:
    def __init__(
        self,
        foods: List[str],
        cuisines: List[str],
        ratings: List[int],
    ):
        self.cuisine_by_food = {}
        self.rating_by_food = {}
        self.heaps = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_by_food[food] = cuisine
            self.rating_by_food[food] = rating
            heapq.heappush(self.heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating_by_food[food] = newRating
        cuisine = self.cuisine_by_food[food]
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while -heap[0][0] != self.rating_by_food[heap[0][1]]:
            heapq.heappop(heap)
        return heap[0][1]
