# The Power Sum

| | |
|---|---|
| **ID** | `recursion_01` |
| **Category** | recursion |
| **Complexity (required)** | $O(2^{N^{1/N}})$ Time, $O(N^{1/N})$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **HackerRank Equivalent** | [The Power Sum](https://www.hackerrank.com/challenges/the-power-sum/problem) |

## Problem statement

Find the number of ways that a given integer X can be expressed as the sum of the N-th powers of **unique**, natural numbers.

For example, if X=13 and N=2.
We need to find the number of ways to express 13 as the sum of unique squares.
2^2 + 3^2 = 4 + 9 = 13.
There is exactly 1 way. Return 1.

If X=100 and N=2:
10^2 = 100
6^2 + 8^2 = 36 + 64 = 100
1^2 + 3^2 + 4^2 + 5^2 + 7^2 = 1+9+16+25+49 = 100
Return 3.

**Input:** Two integers X and N.
**Output:** An integer representing the number of combinations.

## When to use it

- To learn the most fundamental concept in all of recursion: **"Take it or Leave it" (Pick / Not Pick)**.
- This is the recursive backbone that powers the 0/1 Knapsack Problem and all Subset generation algorithms.

## Approach

**1. The Recursive Choices:**
We are given a target number X, and a power N.
We start testing base numbers starting from num = 1.
For the current num, we have exactly two choices:
- **Choice 1 (Take it):** We include num^N in our sum. This means our new remaining target is X - num^N. Since we must use unique numbers, we move on to the next available number: num + 1.
- **Choice 2 (Leave it):** We do NOT include num^N in our sum. Our target remains exactly X, but we move on to the next available number: num + 1.

The total number of valid ways is simply: `Take it + Leave it`.

**2. The Base Cases:**
Every recursive function must know when to stop!
- **Success:** If our target X becomes exactly `0`, it means our choices perfectly summed up to the original target! We return `1` (representing 1 valid combination found).
- **Failure 1:** If our target X becomes `< 0`, it means we overshot the target! Our choices summed to a number too large. Return `0`.
- **Failure 2:** If the number we are currently testing, num^N, is strictly greater than the remaining target X, then it's impossible to use this number (or any number larger than it). Return `0`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for recursion_01: Power Sum.

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. O(log n) time.
"""


def solve(x, n):
    if n == 0:
        return 1
    half = solve(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half
```

</details>

## Walk-through

X=13, N=2.
Start: `recurse(13, 1)`.

1. **`recurse(13, 1)`**: `val = 1^2 = 1`.
   - Take: `recurse(13 - 1, 2) => recurse(12, 2)`
   - Leave: `recurse(13, 2)`
2. **Explore `recurse(12, 2)`**: `val = 2^2 = 4`.
   - Take: `recurse(12 - 4, 3) => recurse(8, 3)`
   - Leave: `recurse(12, 3)`
3. **Explore `recurse(8, 3)`**: `val = 3^2 = 9`.
   - `val > target` (9 > 8).
   - Base Case Hit: Return `0`.
4. **Explore `recurse(12, 3)` (The Leave branch from step 2)**: `val = 3^2 = 9`.
   - Take: `recurse(12 - 9, 4) => recurse(3, 4)`
   - Leave: `recurse(12, 4)`
5. **Explore `recurse(3, 4)`**: `val = 4^2 = 16`.
   - `val > target` (16 > 3).
   - Base Case Hit: Return `0`.
6. **Let's jump back to the Leave branch from Step 1! `recurse(13, 2)`**:
   - `val = 2^2 = 4`.
   - Take: `recurse(13 - 4, 3) => recurse(9, 3)`
   - Leave: `recurse(13, 3)`
7. **Explore `recurse(9, 3)`**: `val = 3^2 = 9`.
   - Take: `recurse(9 - 9, 4) => recurse(0, 4)`
8. **Explore `recurse(0, 4)`**:
   - `target == 0`.
   - Base Case Hit: Return `1`! (We found 2^2 + 3^2).

After all recursive branches collapse and sum together, the final return value to the user is `1`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(2^{X^{1/N}})$ | $O(X^{1/N})$ |
| **Worst** | $O(2^{X^{1/N}})$ | $O(X^{1/N})$ |

At every step, the recursion splits into 2 branches (Take / Leave). This creates a Binary Tree structure.
The maximum depth of this tree is the largest number whose N-th power is \le X. This is mathematically bounded by \lfloor X^{1/N} \rfloor.
Because a binary tree of depth D has 2^D nodes, the time complexity is $O(2^{X^{1/N}})$.
The space complexity is the maximum depth of the Call Stack during recursion, which is exactly the depth of the tree: $O(X^{1/N})$.

*(Note: For X=100, N=2, the maximum depth is \sqrt{100} = 10. The tree has 2^{10} = 1024 nodes. For modern computers, this executes instantly in micro-seconds).*

## Variants & optimizations

- **Coin Change II (`dp_04`):** If the problem allowed REUSING the same numbers (e.g. 2^2 + 2^2 + \dots), the "Take it" branch would simply NOT increment `current_num`. It would call `recurse(target - val, current_num)`.
- **Dynamic Programming / Memoization:** The recursive parameters are `(target, current_num)`. You can cache the results of these tuples in a 2D array or Hash Map to drastically reduce the time complexity by pruning overlapping subproblems!

## Real-world applications

- **Subset Sum Algorithms:** Used in financial auditing to find a specific combination of transactions (out of thousands) that perfectly sum up to a specific missing accounting anomaly value.

## Related algorithms in cOde(n)

- **[backtracking_01 - Subsets](../backtracking/backtracking_01_subsets.md)** — The direct translation of the "Take it / Leave it" recursion tree used to literally print out combinations.
- **[dp_06 - 0/1 Knapsack](../dynamic/dp_06_0-1-knapsack.md)** — The heavily optimized Dynamic Programming version of "Take it / Leave it".

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
