# Get the Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1537 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-the-maximum-score/) |

## Problem Description
### Goal
You are given two strictly increasing arrays of distinct positive integers. A valid path begins at index zero of either array and moves from left to right. Whenever the current value occurs in both arrays, the path may continue in its present array or switch to the other one. A shared value is counted only once when a switch occurs.

The score of a path is the sum of its visited values. Find the maximum score among all valid paths and return it modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums1`: a strictly increasing array with length $n$.
- `nums2`: a strictly increasing array with length $m$.
- Both lengths are between $1$ and $10^5$, and every value is between $1$ and $10^7$.

**Return value**

The greatest valid-path score, reduced modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums1 = [2, 4, 5, 8, 10], nums2 = [4, 6, 8, 9]`
- Output: `30`
- Explanation: The path `[2, 4, 6, 8, 10]` has the largest score.

**Example 2**

- Input: `nums1 = [1, 3, 5, 7, 9], nums2 = [3, 5, 100]`
- Output: `109`
- Explanation: The best path is `[1, 3, 5, 100]`.

**Example 3**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [6, 7, 8, 9, 10]`
- Output: `40`
- Explanation: With no shared value, the entire second array is optimal.

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Shared values divide every path into independent segments**

Between two consecutive values that occur in both arrays, switching is impossible. A path must take the whole intervening segment from exactly one array. At the next shared value, both choices meet at the same state again, so only the larger accumulated score can matter to any continuation.

Scan the sorted arrays with one pointer per array while maintaining `score1` and `score2`, the best scores reaching the current positions along their respective arrays. When `nums1[i]` is smaller, only the first path can consume it; add it to `score1` and advance `i`. Handle a smaller `nums2[j]` symmetrically.

**Merge the two states at an intersection**

If the pointed values are equal, either incoming path may reach that shared value and may leave through either array. Set both scores to `max(score1, score2) + nums1[i]`, then advance both pointers. Adding the shared value once preserves the path rule even though it appears in both inputs.

After one array ends, no further intersection exists. Add each remaining suffix to its corresponding score and return the larger total modulo $10^9 + 7$. The modulo is postponed until the end so comparisons always use the true path totals.

**Why discarding the smaller prefix is safe**

At a shared value, the possible future values depend only on the chosen outgoing array, not on how that intersection was reached. Any continuation available after the smaller prefix is also available after the larger prefix. Replacing both states with the larger incoming score plus the shared value therefore cannot remove an optimal path. Repeating this argument at every intersection proves that the final larger state is the maximum valid score.

#### Complexity detail

Each pointer advances monotonically and visits its array once, so the running time is $O(n + m)$. Apart from the pointers and two score accumulators, the scan uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Hash shared values, then process segments:** can also obtain the right score, but storing intersections uses $O(\min(n,m))$ extra space instead of exploiting the sorted order directly.
- **Search for every value in the other array:** repeated linear membership checks can take $O(nm)$ time; repeated binary searches improve this to $O((n+m)\log\max(n,m))$ but remain unnecessary.
- If the arrays have no common values, the answer is simply the larger complete-array sum.
- If every value is shared, each value is still counted exactly once and both running scores remain equal.
- A path may benefit from switching at several intersections; choosing the better prefix independently at each shared value captures all such combinations.
- Compute with unrestricted or sufficiently wide integers, and apply the modulus only to the final maximum so modular wraparound cannot reverse a score comparison.

</details>
