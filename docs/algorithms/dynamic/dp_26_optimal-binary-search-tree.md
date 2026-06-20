# Optimal Binary Search Tree

| | |
|---|---|
| **ID** | `dp_26` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(n^3)$ |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Optimal binary search tree](https://en.wikipedia.org/wiki/Optimal_binary_search_tree) |

## Problem statement

Given a sorted array of `n` keys, and an array `freq` where `freq[i]` is the number of times key `i` is searched.
Construct a Binary Search Tree (BST) that minimizes the **total search cost**.
The search cost of a key is exactly its depth in the tree multiplied by its frequency.

**Input:** Two arrays of size `n`: sorted `keys` and their `freq`.
**Output:** An integer representing the minimum total search cost.

**Example:**
`keys = [10, 12, 20]`. `freq = [34, 8, 50]`.
If we make 10 the root: Cost = `34*1 + 8*2 + 50*3 = 200`.
If we make 20 the root: Cost = `50*1 + 12*2 + 34*3 = 176`.
If we make 12 the root: Cost = `8*1 + 34*2 + 50*2 = 176`.
*(Actually, making 20 the root and 10 the left child, 12 the right child of 10 gives: `50*1 + 34*2 + 8*3 = 142`)*.

## When to use it

- To build static dictionaries or search indexes where the query distribution is highly skewed and known in advance.

## Approach

This is another classic **Interval DP** problem, identical in structure to Matrix Chain Multiplication.

Any key `k` (between `i` and `j`) can be the root of the optimal BST for the sub-array `keys[i...j]`.
If we make `k` the root:
1. The keys from `i` to `k-1` will form the left subtree.
2. The keys from `k+1` to `j` will form the right subtree.

The cost of this sub-tree will be the optimal cost of the left subtree + optimal cost of the right subtree.
**Wait!** Because we just pushed both subtrees down by one level (by placing them under the new root `k`), the depth of every single node in both subtrees just increased by 1!
Therefore, the search cost of *every single node* in the sub-array `i...j` just increased by `1 * freq[node]`.
So, we must add the **sum of all frequencies** from `i` to `j` to account for this depth shift.

**DP State:**
`dp[i][j]` = min cost of optimal BST using keys from `i` to `j`.
`dp[i][j] = min( dp[i][k-1] + dp[k+1][j] ) + sum(freq[i...j])` for all i \le k \le j.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_26: Optimal Binary Search Tree.

opt[i][j] = min cost over BSTs containing keys[i..j].
Recurrence: try k in [i, j] as the root. Cost of putting
a subtree at depth+1 adds the total probability.
"""


def solve(keys, probs, n):
    if n == 0:
        return 0
    INF = float("inf")
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + probs[i]
    opt = [[0.0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = INF
            for k in range(i, j + 1):
                left = opt[i][k - 1] if k > i else 0
                right = opt[k + 1][j] if k < j else 0
                c = left + right + prefix[j + 1] - prefix[i]
                if c < best:
                    best = c
            opt[i][j] = best
    return opt[0][n - 1]
```

</details>

## Walk-through

`freq = [34, 8, 50]`. (keys don't matter, just frequencies). `n=3`.

**L=1:**
`dp[0][0] = 34`
`dp[1][1] = 8`
`dp[2][2] = 50`

**L=2:**
- `i=0, j=1`. `sum = 34+8 = 42`.
  - Root `k=0`: left=0, right=`dp[1][1]=8`. Total = `0 + 8 + 42 = 50`.
  - Root `k=1`: left=`dp[0][0]=34`, right=0. Total = `34 + 0 + 42 = 76`.
  - `dp[0][1] = 50`.
- `i=1, j=2`. `sum = 8+50 = 58`.
  - Root `k=1`: left=0, right=`50`. Total = `50 + 58 = 108`.
  - Root `k=2`: left=`8`, right=0. Total = `8 + 58 = 66`.
  - `dp[1][2] = 66`.

**L=3 (Final):**
- `i=0, j=2`. `sum = 34+8+50 = 92`.
  - Root `k=0`: left=0, right=`dp[1][2]=66`. Total = `66 + 92 = 158`.
  - Root `k=1`: left=`dp[0][0]=34`, right=`dp[2][2]=50`. Total = `34 + 50 + 92 = 176`.
  - Root `k=2`: left=`dp[0][1]=50`, right=0. Total = `50 + 92 = 142`.
  - Minimum is `142`.

Output: `142`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n^3)$ | $O(n^2)$ |
| **Average** | $O(n^3)$ | $O(n^2)$ |
| **Worst** | $O(n^3)$ | $O(n^2)$ |

Just like Matrix Chain Multiplication, the 3 nested loops (L, i, k) dictate a strict $O(n^3)$ time complexity.
Space is $O(n^2)$ for the DP table.

## Variants & optimizations

- **Knuth's Optimization $O(n^2)$:** Donald Knuth proved that the optimal root K(i, j) for the range `i...j` always lies between the optimal roots of the sub-ranges: K(i, j-1) \le K(i, j) \le K(i+1, j). By restricting the inner `k` loop to this narrow mathematical window, the time complexity mathematically collapses from $O(n^3)$ to $O(n^2)$!

## Real-world applications

- **Static Parsers:** Hardcoding dictionaries for spell-checkers or programming language keyword tokenizers where the frequency of words (e.g., "if", "while") in source code is statistically known.

## Related algorithms in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — The engine behind this Interval DP.
- **[greedy_01 - Huffman Coding](../greedy/greedy_01_huffman-coding.md)** — A related optimal tree problem, but Huffman trees are NOT binary search trees (keys are not sorted left-to-right), allowing a greedy $O(n log n)$ solution!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
