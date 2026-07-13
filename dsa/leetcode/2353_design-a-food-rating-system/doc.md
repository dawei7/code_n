# Design a Food Rating System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2353 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-a-food-rating-system](https://leetcode.com/problems/design-a-food-rating-system/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-a-food-rating-system/).

### Goal
Design a system that tracks food items, their cuisines, and their ratings. The system must support updating a food's rating and querying the highest-rated food for a given cuisine. If there is a tie in ratings, the food with the lexicographically smaller name should be prioritized.

### Function Contract
**Inputs**
- `commands`: `List[str]` - A list of method names to execute: `"FoodRatings"` (constructor), `"changeRating"`, or `"highestRated"`.
- `inputs`: `List[List[Any]]` - A list of arguments corresponding to each command.

For `"FoodRatings"`, the arguments are `[foods, cuisines, ratings]`, where `foods`
contains food names, `cuisines` contains the cuisine for each food, and `ratings`
contains the initial ratings. For `"changeRating"`, the arguments are
`[food, newRating]`. For `"highestRated"`, the arguments are `[cuisine]`.

**Return value**
- `List[Union[None, str]]` - A list of return values from each method call. The constructor and `"changeRating"` return `None`, while `"highestRated"` returns the name of the highest-rated food as a string.

### Examples
**Example 1**

- **Input**:
  - `commands = ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]`
  - `inputs = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]`
- **Output**: `[None, "kimchi", "ramen", None, "sushi", None, "ramen"]`
- **Explanation**:
  1. Initialize foods with their cuisines and ratings.
  2. `highestRated("korean")` returns `"kimchi"` (rating 9 is higher than bulgogi's 7).
  3. `highestRated("japanese")` returns `"ramen"` (rating 14 is higher than miso's 12 and sushi's 8).
  4. `changeRating("sushi", 16)` updates sushi's rating to 16.
  5. `highestRated("japanese")` returns `"sushi"` (rating 16 is now the highest).
  6. `changeRating("ramen", 16)` updates ramen's rating to 16.
  7. `highestRated("japanese")` returns `"ramen"` (both sushi and ramen have rating 16, but `"ramen"` is lexicographically smaller than `"sushi"`).

---

## Solution
### Approach
To implement this system efficiently, we use a combination of **Hash Maps** and **Priority Queues (Heaps)**:
1. **Hash Maps**:
   - `food_to_cuisine`: Maps each food name to its cuisine for $O(1)$ lookup.
   - `food_to_rating`: Maps each food name to its current rating.
2. **Priority Queues (Heaps)**:
   - For each cuisine, we maintain a min-heap storing tuples of `(-rating, food)`.
   - Negating the rating allows us to use Python's built-in min-heap as a max-heap.
   - If ratings are equal, Python compares the second element of the tuple (`food`), which naturally sorts them lexicographically in ascending order. This perfectly satisfies the tie-breaking condition.
3. **Lazy Deletion**:
   - Instead of searching and updating elements inside the heap (which is an expensive $O(N)$ operation), we perform **lazy deletion**.
   - When `changeRating` is called, we simply push the new `(-newRating, food)` tuple onto the heap and update the `food_to_rating` map.
   - When `highestRated` is called, we peek at the top of the heap. If the rating in the heap entry does not match the current rating in `food_to_rating`, it is a stale entry. We pop it and continue checking until we find a valid entry.

### Complexity Analysis
- **Time Complexity**:
  - **Initialization**: $O(N \log N)$ where $N$ is the number of foods, as we push each food into its cuisine's heap.
  - **`changeRating`**: $O(\log(N + M))$ where $M$ is the number of rating updates, to push the new rating into the heap.
  - **`highestRated`**: $O(K \log(N + M))$ amortized, where $K$ is the number of stale entries popped. Since each update adds at most one stale entry, the total time spent popping stale entries across all operations is bounded by $O(M \log(N + M))$. Thus, the amortized time complexity per query is $O(\log(N + M))$.
- **Space Complexity**: $O(N + M)$ to store the mappings and the heap elements (including stale entries).

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
