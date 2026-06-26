# Tiling Problem (2 x N Board)

| | |
|---|---|
| **ID** | `dc_12` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Tiling Problem](https://www.geeksforgeeks.org/tiling-problem/) |

## Problem statement

Given a `2 x N` board and tiles of dimension `2 x 1`, count the number of ways to tile the given board using these tiles.
A tile can either be placed horizontally (taking `1 x 2` space) or vertically (taking `2 x 1` space).
Since the answer can be huge, return it modulo 10^9 + 7.

**Input:** An integer `N` representing the width of the board.
**Output:** An integer representing the number of ways to tile it.

## When to use it

- To recognize when a spatial Divide and Conquer geometry problem mathematically collapses into a basic Fibonacci sequence.
- The most famous "trick" introductory Dynamic Programming / Recursion problem.

## Approach

**1. The Divide and Conquer Decision:**
Imagine you are filling the board from left to right. You are currently looking at the leftmost empty column. You have exactly two choices for how to place the first tile:
- **Choice A (Vertical):** You place one tile vertically. It perfectly fills the entire first column. You are now left with a perfectly rectangular empty board of size `2 x (N - 1)`.
- **Choice B (Horizontal):** You place one tile horizontally in the top-left corner. But wait! The space directly below it in the bottom-left corner is now empty and can ONLY be filled by another horizontal tile! Placing one horizontal tile forces you to place a second one directly below it. This `2 x 2` block is now filled. You are now left with a perfectly rectangular empty board of size `2 x (N - 2)`.

**2. The Recurrence Relation:**
Let f(N) be the number of ways to tile a `2 x N` board.
From the choices above, we can mathematically define it:
f(N) = f(N - 1) + f(N - 2)

Wait... that's the **Fibonacci Sequence**!

**3. Base Cases:**
- f(0) = 1: There is exactly 1 way to tile an empty board (do nothing).
- f(1) = 1: A `2 x 1` board can only be tiled with 1 vertical tile.
- f(2) = 2: A `2 x 2` board can be 2 vertical tiles, or 2 horizontal tiles.

**4. Execution:**
We don't need to actually write a recursive Divide and Conquer function (which would take $O(2^N)$ time or require $O(N)$ memoization space). We can just compute the N-th Fibonacci number iteratively using two variables in strictly $O(1)$ space!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_12: Tiling Problem (2 x N board).

Given a 2 x n board and tiles of size 2 x 1, count
"""


def solve(n):
    """Count the tilings of a 2 x n board with 2 x 1 dominoes.

    T(n) = T(n-1) + T(n-2), T(0) = 1, T(1) = 1 (Fibonacci).
    """
    if n <= 1:
        return 1
    a, b = 1, 1   # T(0), T(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

</details>

## Walk-through

`n = 4`. `MOD = 10^9 + 7`.
Initial: `prev2 = 1`, `prev1 = 1`.

1. **i = 2:**
   - `current = (1 + 1) % MOD = 2`.
   - `prev2 = 1`, `prev1 = 2`.
2. **i = 3:**
   - `current = (2 + 1) % MOD = 3`.
   - `prev2 = 2`, `prev1 = 3`.
3. **i = 4:**
   - `current = (3 + 2) % MOD = 5`.
   - `prev2 = 3`, `prev1 = 5`.

Result is `5`. ✓
*(The 5 ways: VVVV, VVHH, HHVV, VHHV, HHHH).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The `for` loop runs N - 1 times, doing simple integer addition. Time complexity is strictly $O(N)$.
Only three integer variables are maintained. Space complexity is strictly $O(1)$.

## Variants & optimizations

- **Matrix Exponentiation ($O(\log N)$):** If N is massive (e.g., 10^{18}), the $O(N)$ loop will trigger a TLE! You can write the Fibonacci sequence as a matrix multiplication: \begin{bmatrix} f(N) \\ f(N-1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{N-1} x \begin{bmatrix} f(1) \\ f(0) \end{bmatrix}. You can then apply Fast Exponentiation (`dc_01`) to the matrix to solve it in exactly $O(\log N)$ time!
- **Domino and Tromino Tiling (LeetCode 790):** What if you can use `2x1` dominoes AND L-shaped trominoes? The state branches drastically because an L-tromino leaves an irregular edge that needs to be filled! The recurrence relation becomes f(N) = 2 x f(N-1) + f(N-3).

## Real-world applications

- **Statistical Mechanics:** Analyzing the thermodynamic properties of diatomic molecules (dimers) absorbing onto a 2D crystalline lattice surface (known mathematically as the "Dimer Covering Problem").

## Related algorithms in cOde(n)

- **[dp_01 - Climbing Stairs](../dynamic/dp_01_climbing-stairs.md)** — The literal exact same Fibonacci recurrence relation, just framed as taking 1 or 2 steps on a staircase instead of placing tiles.
- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — Required for the $O(\log N)$ matrix exponentiation optimization.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
