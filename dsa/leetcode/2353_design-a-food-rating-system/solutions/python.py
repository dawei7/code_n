import heapq
from collections import defaultdict
from typing import List, Any, Union

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            # Negate rating for max-heap behavior. 
            # Lexicographical order of food names is naturally handled in ascending order.
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            neg_rating, food = heap[0]
            # If the rating in the heap matches the current rating, it is valid
            if -neg_rating == self.food_to_rating[food]:
                return food
            # Otherwise, it is a stale entry; discard it
            heapq.heappop(heap)
        return ""

def solve(commands: List[str], inputs: List[List[Any]]) -> List[Union[None, str]]:
    """
    Simulates the FoodRatings class operations.
    """
    if not commands:
        return []
    
    # The first command is always the constructor
    foods, cuisines, ratings = inputs[0]
    obj = FoodRatings(foods, cuisines, ratings)
    results = [None]
    
    for i in range(1, len(commands)):
        cmd = commands[i]
        args = inputs[i]
        if cmd == "changeRating":
            obj.changeRating(args[0], args[1])
            results.append(None)
        elif cmd == "highestRated":
            results.append(obj.highestRated(args[0]))
            
    return results
