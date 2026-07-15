# Fixed Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1064 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/fixed-point/) |

## Problem Description

### Goal

Given an array `arr` of distinct integers sorted in **ascending order**, find an index `i` whose stored value equals the index itself, so `arr[i] == i`. Such an index is called a fixed point.

Return the smallest index satisfying that equality. More than one fixed point may exist, so finding any match is insufficient when an earlier match is present. If the array contains no fixed point, return `-1`.

### Function Contract

**Inputs**

- `arr`: an ascending array of $N$ distinct integers, where $1 \le N < 10^4$ and each value lies between $-10^9$ and $10^9$.

**Return value**

- The smallest index `i` for which `arr[i] == i`, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `arr = [-10, -5, 0, 3, 7]`
- Output: `3`
- Explanation: `arr[3]` equals `3`.

**Example 2**

- Input: `arr = [0, 2, 5, 8, 17]`
- Output: `0`

**Example 3**

- Input: `arr = [-10, -5, 3, 4, 7, 9]`
- Output: `-1`

### Required Complexity

- **Time:** $O(\log N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Create a monotone comparison:** Compare each value with its index. Because `arr` contains distinct integers in ascending order, moving from one index to the next increases the array value by at least one. Therefore `arr[i] - i` never decreases.

**Search for the left boundary:** Binary-search for the first index where `arr[i] >= i`. If `arr[mid] < mid`, every earlier index also has `arr[index] < index`, so the search moves right. Otherwise, `mid` might be the first fixed point or lie after it, so retain it and move the right boundary left.

**Verify the candidate:** At the lower-bound index, equality may hold, in which case it is the smallest fixed point by construction. If the value is strictly greater than its index, monotonicity means all later differences are also positive, so no fixed point exists.

#### Complexity detail

Each comparison discards at least half of the remaining indices, requiring $O(\log N)$ time. The search stores only two boundaries and a midpoint, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Linear scan:** Check indices from left to right and return the first match. It is simple but takes $O(N)$ time when the match is late or absent.
- **Search for any equality:** A conventional binary search that returns immediately can miss a smaller fixed point; the lower-bound formulation preserves the minimum-index requirement.
- **First index fixed:** The lower-bound candidate is zero and is returned immediately after verification.
- **Several fixed points:** The first index where `arr[i] >= i` is the smallest equality.
- **No candidate below the array length:** If every value is below its index, the lower boundary moves past the array and the answer is `-1`.
- **Candidate strictly above its index:** Since later differences cannot decrease, equality is impossible afterward.
- **Negative values:** They participate normally and often force the lower-bound search toward later indices.

</details>
