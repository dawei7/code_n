import heapq
from collections import defaultdict
from typing import List


class FoodRatings:
    def __init__(
        self,
        foods: List[str],
        cuisines: List[str],
        ratings: List[int],
    ) -> None:
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


def solve(operations, arguments):
    ratings = None
    output = []

    for operation, values in zip(operations, arguments):
        if operation == "FoodRatings":
            ratings = FoodRatings(*values)
            output.append(None)
        elif operation == "changeRating":
            output.append(ratings.changeRating(*values))
        elif operation == "highestRated":
            output.append(ratings.highestRated(*values))

    return output
