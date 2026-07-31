# Count the Number of Infection Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2954 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-infection-sequences/) |

## Problem Description
### Goal
There are `n` people standing at positions `0` through `n - 1` in a line.
The increasing array `sick` lists the positions already infected. At each
subsequent step, exactly one uninfected person who is adjacent to an infected
person becomes infected. The process continues until nobody remains healthy.

An infection sequence records, in order, the positions of the people infected
during this process; the initially infected positions are excluded. Count the
distinct valid infection sequences and return the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the total number of people in the line
- `sick`: the strictly increasing positions of the initially infected people

The contract guarantees $2\le\texttt{n}\le10^5$,
$1\le\lvert\texttt{sick}\rvert\le\texttt{n}-1$, and every stored position is
between `0` and `n - 1`.

**Return value**

The number of possible infection orders for the initially healthy people,
reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 5, sick = [0,4]`
- Output: `4`
- Explanation: Positions `1` and `3` are exposed first; four of the six permutations of `1,2,3` respect the spreading rule.

**Example 2**

- Input: `n = 4, sick = [1]`
- Output: `3`
- Explanation: The valid orders are `[0,2,3]`, `[2,0,3]`, and `[2,3,0]`.
