# Minimum Cost to Cut a Stick

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1547 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) |

## Problem Description
### Goal
A wooden stick has length `n` and is marked at every position in `cuts`. Every marked position must eventually be cut. Performing a cut costs the current length of the particular stick segment being cut, not the length of the original stick.

You may perform the required cuts in any order. Earlier choices determine the segment containing each later mark and therefore change later costs. Return the minimum possible total cost after all requested cuts have been made.

### Function Contract
**Inputs**

- `n`: the original stick length, where $2 \le n \le 10^6$.
- `cuts`: $c$ distinct integer positions strictly inside the stick, where $1 \le c \le \min(n-1, 100)$ and $1 \le \texttt{cuts[i]} \le n-1$. The input order is arbitrary.

**Return value**

The minimum sum of segment lengths paid while performing every requested cut.

### Examples
**Example 1**

- Input: `n = 7, cuts = [1, 3, 4, 5]`
- Output: `16`
- Explanation: One optimal order is `3, 5, 1, 4`, with costs $7+4+3+2=16$.

**Example 2**

- Input: `n = 9, cuts = [5, 6, 1, 4, 2]`
- Output: `22`
- Explanation: Reordering the five required cuts avoids repeatedly paying for unnecessarily long pieces.

**Example 3**

- Input: `n = 5, cuts = [2, 4]`
- Output: `8`
- Explanation: Cutting at position two first costs five, then cutting the remaining length-three piece at position four costs three.

### Required Complexity

- **Time:** $O(c^3)$
- **Space:** $O(c^2)$

<details>
<summary>Approach</summary>

#### General

**Turn physical pieces into intervals between sorted marks**

Sort the cut positions and add the original endpoints zero and `n`. Any piece that can arise is then described by two boundary indices `left` and `right`. Its length is `points[right] - points[left]`, and the required cuts still inside it are exactly the marks at indices strictly between those boundaries.

**Define the cost of finishing one interval**

Let `cost[left][right]` be the minimum additional cost to perform every cut strictly between the two boundary marks. Adjacent boundaries contain no required cut, so their cost is zero.

For a wider interval, choose which interior mark is cut first. That first operation costs the full current interval length. It separates all remaining work into independent left and right pieces, giving the transition

$$
\textit{cost}[l][r]
=
\min_{l < m < r}
\left(
\textit{cost}[l][m]
+
\textit{cost}[m][r]
+
\textit{points}[r]
-
\textit{points}[l]
\right).
$$

**Fill smaller intervals before larger ones**

Process boundary widths from two upward, ensuring that both subinterval costs are already available for every candidate first cut. Every possible cutting order has some first cut; after it, the two sides never interact again. The transition tests every possible first cut and combines optimal solutions for both independent sides, so it includes an optimal order. Conversely, each transition describes a legal first cut followed by legal optimal suborders. Thus the minimum stored for the full interval is exactly the least achievable total cost.

#### Complexity detail

There are $O(c^2)$ boundary intervals after adding the two endpoints. Each interval tries at most $O(c)$ possible first cuts, so the dynamic program takes $O(c^3)$ time. Sorting costs $O(c \log c)$ and is dominated by the recurrence. The table contains $O(c^2)$ entries, which determines the auxiliary-space bound.

#### Alternatives and edge cases

- **Try every global cutting order:** evaluating all $c!$ permutations is correct but repeats the same subproblems exponentially many times.
- **Top-down memoization:** the same interval recurrence can be evaluated recursively and retains $O(c^3)$ time and $O(c^2)$ stored states, with additional recursion-stack overhead.
- **Greedy nearest or middle cut:** choosing a geometrically attractive next mark can be suboptimal because the future costs of both resulting pieces matter.
- Input cut positions must be sorted for boundary indices to represent physical intervals.
- A single required cut always costs `n`.
- Highly uneven gaps are handled by physical coordinate differences, not by the number of marks inside a segment.
- The endpoints are boundaries, not requested cuts, and add no operation of their own.
- Different optimal cut orders may have the same minimum total cost.

</details>
