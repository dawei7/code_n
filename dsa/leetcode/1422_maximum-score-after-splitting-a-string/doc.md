# Maximum Score After Splitting a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1422 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) |

## Problem Description

### Goal

Split the binary string `s` into two nonempty contiguous parts. The score of a split is the number of `0` characters in its left part plus the number of `1` characters in its right part.

Evaluate every legal boundary between adjacent characters and return the maximum score. Neither part may be empty, so the split must occur after the first character and before the last character.

### Function Contract

**Inputs**

- `s`: a binary string of length $n$, where $2 \le n \le 500$.

**Return value**

- The greatest possible value of left-side zeros plus right-side ones over all nonempty two-part splits.

### Examples

**Example 1**

- Input: `s = "011101"`
- Output: `5`

**Example 2**

- Input: `s = "00111"`
- Output: `5`

**Example 3**

- Input: `s = "1111"`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count right-side ones before splitting.** Initially, every `1` belongs to the unsplit right side. Store their total, along with a left-zero count starting at zero.

Move the split boundary from left to right, processing positions zero through `n - 2` so the final character always remains in the right part. When the crossed character is `0`, increment the left-zero count. When it is `1`, decrement the right-one count. Their sum is then the score of the boundary immediately after that character; retain the largest sum.

Each update transfers exactly the crossed character from right to left. Thus the two counters equal the score definition at every legal boundary, and every legal boundary is considered once. The maximum recorded value is therefore the optimal score.

#### Complexity detail

Counting the initial ones and scanning the $n-1$ legal boundary positions take $O(n)$ time. The two counters and maximum use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Count both substrings per split:** Slicing and recounting each side is direct but takes $O(n^2)$ time.
- **Prefix arrays:** Store zero prefixes and one suffixes. This also takes $O(n)$ time but uses $O(n)$ extra space unnecessarily.
- **Length two:** There is exactly one legal split.
- **All zeros:** The best boundary leaves one character on the right and scores $n-1$.
- **All ones:** The best boundary leaves one `1` on the right and also scores $n-1$.
- **Zero score:** The string `"10"` has a legal split whose two counted categories are both absent.
- **Nonempty parts:** Never evaluate a boundary after the last character.

</details>
