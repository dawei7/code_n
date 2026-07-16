# Running Sum of 1d Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1480 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) |

## Problem Description
### Goal

For an integer array `nums`, construct its running sum. At every index `i`, the returned value must equal the sum of the input elements from index `0` through `i`, inclusive.

Preserve the input order and return one prefix total for every input position. Negative values may reduce a later total, zeros leave it unchanged, and no sorting or omission is permitted.

### Function Contract
**Inputs**

Let $N$ be the length of `nums`.

- `nums`: an integer array with $1 \le N \le 1000$.
- Every value satisfies $-10^6 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return an array `runningSum` of length $N$ satisfying

$$
\texttt{runningSum[i]}=\sum_{j=0}^{i}\texttt{nums[j]}
$$

for every index $0 \le i < N$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[1,3,6,10]`
- Explanation: The prefixes contain one, two, three, and four input values respectively.

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `[1,2,3,4,5]`

**Example 3**

- Input: `nums = [3,1,2,10,1]`
- Output: `[3,4,6,16,17]`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Reusing the previous prefix**

The prefix ending at index `i` differs from the prefix ending at `i - 1` by exactly `nums[i]`. Maintain `total`, initially zero. For each value from left to right, perform `total += value` and append the new total.

This avoids re-reading values already included in earlier prefixes. The first update produces `nums[0]`; each later update extends the preceding prefix by one new element.

**Why every appended value is correct**

Before processing the first value, `total = 0` is the sum of the empty prefix. Assume that before index `i`, `total` equals the sum through `i - 1`. Adding `nums[i]` makes it the sum through `i`, which is immediately appended. Induction proves every output position satisfies the contract.

**Keeping input and output ownership separate**

Build a new result array so the app-local reference does not mutate its caller's `nums`. An in-place variant can overwrite each position with `nums[i] += nums[i - 1]`, but mutation is not needed to meet the requested bounds.

#### Complexity detail

The scan performs one addition and one append per input element, for $O(N)$ time. The returned array stores $N$ totals and therefore uses $O(N)$ space. Apart from the required output, only the scalar accumulator is stored.

#### Alternatives and edge cases

- **Re-sum each prefix:** Computing `sum(nums[:i + 1])` for every index is correct but reads earlier values repeatedly and takes $O(N^2)$ time.
- **In-place accumulation:** Overwrite each element from index one onward with the previous accumulated value plus itself. This uses $O(1)$ auxiliary space but mutates the input.
- **Prefix library primitive:** Standard scan or accumulate utilities express the same recurrence concisely, with the same bounds.
- **One element:** Its running sum is the element itself.
- **Negative values:** Totals need not be increasing.
- **Zeros:** A zero repeats the preceding total.
- **Large magnitudes:** Prefix totals can exceed the individual-value bound, so fixed-width languages should use a sufficiently wide integer type.
- **Input order:** Sorting would change every prefix and is never valid.

</details>
