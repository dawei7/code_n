# Two Furthest Houses With Different Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2078 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) |

## Problem Description

### Goal

There are $n$ evenly spaced houses in a line, numbered by zero-based index. The integer `colors[i]` identifies the paint color of house $i$.

Choose two houses with different colors and maximize their distance. For indices $i$ and $j$, that distance is $\lvert i-j\rvert$. At least two houses are guaranteed to have different colors, so a valid pair always exists.

### Function Contract

**Inputs**

- `colors`: an integer list of length $n$, where $2 \le n \le 100$ and $0 \le \texttt{colors[i]} \le 100$.

**Return value**

- Return the maximum value of $\lvert i-j\rvert$ over all pairs with `colors[i] != colors[j]`.

### Examples

**Example 1**

- Input: `colors = [1,1,1,6,1,1,1]`
- Output: `3`
- Explanation: The lone house of color 6 is three positions from either endpoint.

**Example 2**

- Input: `colors = [1,8,3,8,3]`
- Output: `4`
- Explanation: Houses 0 and 4 have different colors and span the entire street.

**Example 3**

- Input: `colors = [0,1]`
- Output: `1`
- Explanation: The only two houses have different colors and are one position apart.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only endpoint pairs can be necessary**

Consider any valid pair with indices $i<j$. If `colors[j]` differs from the first color, replacing $i$ by index 0 keeps the colors different and cannot shorten the distance. Similarly, if `colors[i]` differs from the last color, replacing $j$ by index $n-1$ cannot shorten it. If neither condition holds, then `colors[j]` equals the first color and `colors[i]` equals the last color; because the pair is valid, the two endpoint colors differ, and the endpoints themselves dominate it. Thus some optimal pair includes index 0 or index $n-1$.

**Evaluate both endpoint families**

Scan every index once. When its color differs from `colors[0]`, its distance from the first house is the index itself. When it differs from `colors[n - 1]`, its distance from the last house is `n - 1 - index`. Keep the largest value from both checks.

**The maximum is guaranteed to become positive**

The input contains at least two colors. If the endpoints differ, the scan records $n-1$, the greatest possible distance. If they match, at least one interior house differs from that shared endpoint color, and one of its two endpoint distances is recorded.

#### Complexity detail

The scan examines each of the $n$ houses once and performs constant work per house, for $O(n)$ time. It stores only the final index and current maximum, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Check every pair:** Exhaustive comparison is correct but takes $O(n^2)$ time and repeats unnecessary interior-pair work.
- **Two directed scans:** Search from the right for the last color differing from `colors[0]` and from the left for the first color differing from `colors[n - 1]`; this is equivalent and remains $O(n)$.
- **Different endpoint colors:** The answer is immediately $n-1$, although the uniform scan already discovers it.
- **Matching endpoint colors:** An interior outlier may achieve its larger distance to either end, so both endpoint families must be considered.
- **Repeated colors:** Only inequality matters; frequencies and numeric color magnitude do not.
- **Two houses:** The guarantee forces different colors, making the answer 1.

</details>
