### Approach: Simulation

#### Intuition

Since the input size is small, we can simulate the process directly. We iterate over each fruit from left to right and try to find a basket that can hold it. A fruit can only be placed in a basket if the basket’s capacity is greater than or equal to the fruit's requirement. Once a fruit is placed in a basket, that basket is marked as used and cannot be used again.

There are two possibilities for each fruit:

1. If a basket with enough capacity is found, we use that basket and mark it as unavailable by setting its capacity to `0`.
2. If no such basket is found, we increment the counter `count` to indicate this fruit couldn't be placed.

#### Implementation

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        n = len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break
            count += unset
        return count
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{fruits}$.

- Time complexity: $O(n^2)$.

  Every time a fruit is encountered, the basket array needs to be traversed.

- Space complexity: $O(1)$.

  Only a few additional variables were used.

---