# Candy Distribution Problem

| | |
|---|---|
| **ID** | `greedy_08` |
| **Category** | greedy |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Candy](https://leetcode.com/problems/candy/) |

## Problem statement

There are `N` children standing in a line. Each child is assigned a rating value given in an integer array `ratings`.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating must get *more* candies than their immediate neighbors.

Find the absolute minimum total number of candies you need to distribute.

**Input:** An integer array `ratings` of size `N`.
**Output:** An integer representing the minimum number of candies.

## When to use it

- The classic "Two-Pass Greedy Array Sweep" problem.
- To resolve interdependent local relationships (where an element depends on both its left and right neighbors simultaneously).

## Approach

**1. The Interdependency Problem:**
If we just iterate from left to right, we might give Child 2 more candies than Child 1. But what if Child 3 has a lower rating than Child 2? We have to ensure Child 2 *also* has more candies than Child 3! Adjusting Child 2 might break their relationship with Child 1!
Trying to solve both the Left and Right relationships in a single pass is highly error-prone.

**2. The Two-Pass Solution (Divide and Conquer the Rules):**
Instead of solving both constraints at once, we decouple them!
**Pass 1 (Left-to-Right):** We only care about ensuring a child has more candies than their **LEFT** neighbor.
- Initialize a `candies` array with `1` for every child.
- Loop `i` from 1 to N-1: If `ratings[i] > ratings[i-1]`, set `candies[i] = candies[i-1] + 1`.

**Pass 2 (Right-to-Left):** We only care about ensuring a child has more candies than their **RIGHT** neighbor, *without breaking the left rule*.
- Loop `i` from N-2 down to 0: If `ratings[i] > ratings[i+1]`, the child deserves more candies than the right neighbor.
- **The Catch:** What if `candies[i]` is ALREADY greater than `candies[i+1]` because of the first pass? We don't want to lower it! We only update it if necessary: `candies[i] = max(candies[i], candies[i+1] + 1)`.

**3. The Result:**
By doing one pass strictly observing left-neighbors, and a second reverse-pass strictly observing right-neighbors (using `max`), the final array perfectly satisfies both constraints! Just sum the array.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_08: Candy Distribution.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(ratings, n):
    if n == 0:
        return 0
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    total = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        total += candies[i]
    return total
```

</details>

## Walk-through

`ratings = [1, 0, 2, 5, 3]`. Length 5.
`candies = [1, 1, 1, 1, 1]`.

**Pass 1 (Left to Right):**
- `i=1`: `ratings[1] > ratings[0]`? (0 > 1) NO.
- `i=2`: `ratings[2] > ratings[1]`? (2 > 0) YES. `candies[2] = 1 + 1 = 2`.
- `i=3`: `ratings[3] > ratings[2]`? (5 > 2) YES. `candies[3] = 2 + 1 = 3`.
- `i=4`: `ratings[4] > ratings[3]`? (3 > 5) NO.
`candies` after Pass 1: `[1, 1, 2, 3, 1]`.

**Pass 2 (Right to Left):**
- `i=3`: `ratings[3] > ratings[4]`? (5 > 3) YES.
  - `candies[3] = max(3, candies[4] + 1)` -> `max(3, 2) = 3`.
- `i=2`: `ratings[2] > ratings[3]`? (2 > 5) NO.
- `i=1`: `ratings[1] > ratings[2]`? (0 > 2) NO.
- `i=0`: `ratings[0] > ratings[1]`? (1 > 0) YES.
  - `candies[0] = max(1, candies[1] + 1)` -> `max(1, 2) = 2`.

`candies` after Pass 2: `[2, 1, 2, 3, 1]`.
Sum = `2 + 1 + 2 + 3 + 1 = 9`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

We iterate through the array exactly three times (Left-to-Right pass, Right-to-Left pass, and a final `sum()` pass). The operations at each step are $O(1)$. Total time complexity is strictly $O(N)$.
Space complexity is $O(N)$ because we must instantiate the `candies` array to store the intermediate states between passes.

## Variants & optimizations

- **Single Pass Optimization (Peaks and Valleys):** It IS technically possible to solve this in $O(1)$ space and a single pass by tracking the slopes (increasing vs decreasing sequences). You count the height of an "up-slope" and a "down-slope" and calculate the required candies mathematically using triangle numbers (1+2+3+...). It is notoriously difficult to code without edge-case bugs and is usually not expected in interviews over the Two-Pass approach.
- **Trapping Rain Water (`two_pointers_01`):** Uses an almost identical "Left Max Array, Right Max Array" concept to calculate water volume, decoupled into two separate passes.

## Real-world applications

- **Salary/Bonus Normalization:** Distributing performance bonuses across a ranked department where employees are only aware of their immediate peers' salaries, ensuring fairness (higher rank = higher pay than peers) while minimizing corporate budget.

## Related algorithms in cOde(n)

- **[greedy_06 - Gas Station](greedy_06_gas-station.md)** — Another Greedy $O(N)$ sweep algorithm.
- **[two_pointers_01 - Trapping Rain Water](../two_pointers/two_pointers_01_trapping-rain-water.md)** — The pre-computation arrays in Trapping Rain Water utilize the exact same decoupled Left-to-Right / Right-to-Left logic.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
