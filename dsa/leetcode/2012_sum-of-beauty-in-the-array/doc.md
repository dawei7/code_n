# Sum of Beauty in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2012 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-beauty-in-the-array/) |

## Problem Description

### Goal

For every interior index $i$ of the zero-indexed array `nums`, assign a beauty
score using strict comparisons.

The score is $2$ when every earlier value is smaller than `nums[i]` and every
later value is larger. If that global condition fails but the immediate
neighbors satisfy `nums[i - 1] < nums[i] < nums[i + 1]`, the score is $1$.
Otherwise, it is $0$. Return the sum of the scores for indices $1$ through
$N-2$; the first and last elements never receive a score.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $3\le N\le10^5$ and
  $1\le\texttt{nums[i]}\le10^5$.

**Return value**

Return the sum of all interior beauty scores.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`
- Explanation: The only interior value is greater than everything before it
  and smaller than everything after it.

**Example 2**

- Input: `nums = [2, 4, 6, 4]`
- Output: `1`
- Explanation: `4` lies strictly between its neighbors but fails the global
  condition; `6` has beauty zero.

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `0`
- Explanation: The only interior value satisfies neither condition.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Make the global comparisons constant-time.** Build
`suffix_minimum[i]`, the minimum value from index `i` through the end. During a
left-to-right scan, maintain `prefix_maximum`, the maximum strictly before the
current index. The score-$2$ condition becomes
`prefix_maximum < nums[i] < suffix_minimum[i + 1]`.

**Apply the higher score before the fallback.** If the global condition holds,
add $2$. Otherwise test the two immediate neighbors and add $1$ only when
`nums[i - 1] < nums[i] < nums[i + 1]`. Update the prefix maximum after scoring
the current index so it still describes only earlier positions.

The stored extrema summarize all values on their respective sides. Therefore,
the first test is equivalent to both universal comparisons in the definition,
not merely a necessary approximation. When it fails, the second test exactly
matches the stated fallback. Every interior index receives its prescribed
exclusive score once, so their accumulated total is correct.

#### Complexity detail

Here $N$ is the length of `nums`. Constructing suffix minima and scanning the
interior indices each take $O(N)$ time. The suffix array uses $O(N)$ space,
while the prefix side needs one scalar.

#### Alternatives and edge cases

- **Rescan both sides per index:** Computing a fresh left maximum and right
  minimum for every position is correct but takes $O(N^2)$ time.
- **Prefix and suffix arrays:** Storing both extrema arrays is also linear in
  time and space, but the prefix maximum can be maintained incrementally.
- All comparisons are strict; an equal value anywhere on the relevant side
  prevents beauty $2$, and an equal neighbor prevents beauty $1$.
- An array of length three has exactly one scored index.
- A locally increasing triple can earn $1$ even when a distant earlier maximum
  or later minimum invalidates the global condition.

</details>
