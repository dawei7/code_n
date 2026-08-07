### Approach: Greedy

#### Intuition

**Hint $1$**

We can minimize the total cost of purchasing the candies using the following strategy:

Sort the candy prices in descending order. Then, for every group of three candies, pay for the first two and obtain the third one for free.

**Hint $1$ Explaination**

Assume the number of candies is $n$. Then, the maximum possible number of free candies is $\lfloor n / 3 \rfloor$. Under the strategy described in Hint 1, the number of free candies is exactly equal to this upper bound. Therefore, we can divide the proof into two parts:

1. An optimal purchase plan must maximize the number of free candies obtained.

2. Among all purchase plans that obtain the maximum number of free candies, the plan described in Hint 1 is optimal.

For the first part, consider any purchase plan in which the number of free candies is less than $\lfloor n / 3 \rfloor$. In this case, there must exist at least three candies that have not been grouped together. Among these three candies, the cheapest one can always be obtained for free by grouping them into a valid purchase. Therefore, any such plan cannot be optimal, and proposition 1 holds.

For the second part, assume that the array $\textit{cost}$ has already been sorted in descending order. By the rules of the promotion, the most expensive candy that can be obtained for free is at most $\textit{cost}[2]$ (assuming such an index exists). Similarly, the $k$-th most expensive free candy, where $0 \le k < \lfloor n / 3 \rfloor$, is at most $\textit{cost}[3k + 2]$.

Under the strategy in Hint 1, all of these upper bounds are achieved exactly. Since the number of free candies is already maximized, this strategy also maximizes the total value of the free candies. Therefore, proposition 2 holds.

Combining the above results, we conclude that the purchase plan described in Hint 1 yields the minimum possible total cost.

According to Hint 1, we first sort the array $\textit{cost}$ in descending order. Then, every candy whose index is congruent to $2$ modulo $3$ is obtained for free. We traverse the array and compute the total cost while skipping these free candies. Finally, we return the resulting total cost.

#### Implementation

```python
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(key=lambda x: -x)
        res = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                res += cost[i]
        return res
```

#### Complexity Analysis

Let $n$ be the length of $\textit{cost}$.

- Time complexity: $O(n \log n)$.

  This is the time required to sort the candy prices.

- Space complexity: $O(\log n)$.

  This is the auxiliary space used by the sorting algorithm's recursion stack.

---