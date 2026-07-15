# Array of Doubled Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 954 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [array-of-doubled-pairs](https://leetcode.com/problems/array-of-doubled-pairs/) |

## Problem Description

### Goal

Given an even-length integer array `arr`, decide whether its elements can be reordered into consecutive pairs in which the second value is exactly twice the first.

More precisely, after reordering, every index $i$ from 0 through $\lvert\texttt{arr}\rvert/2-1$ must satisfy `arr[2 * i + 1] = 2 * arr[2 * i]`. Each occurrence must be used exactly once, so duplicate values and zeroes must have sufficient matching multiplicity. Return whether such a reordering exists.

### Function Contract

Let $N$ be the length of `arr`.

**Inputs**

- `arr`: an even-length list of $N$ integers, where $2 \le N \le 3\cdot 10^4$ and `-100000 <= arr[i] <= 100000`.

**Return value**

Return `true` if all occurrences can be partitioned into pairs `(x, 2 * x)`; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [3,1,3,6]`
- Output: `false`

**Example 2**

- Input: `arr = [2,1,2,6]`
- Output: `false`

**Example 3**

- Input: `arr = [4,-2,2,-4]`
- Output: `true`
- Explanation: The occurrences can form `(-2,-4)` and `(2,4)`.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Count occurrences before choosing pairs.** Store the multiplicity of every value. Pairing decisions then consume counts without depending on the input order.

**Process smaller absolute values first.** Sort the distinct values by absolute value. For a nonzero value `x`, every remaining occurrence must use an occurrence of `2 * x`. Handling smaller magnitudes first is essential for negative numbers: ordinary numeric order would process `-4` before `-2`, even though `-4` should serve as the double in `(-2,-4)`. If fewer doubles remain than `x` occurrences, pairing is impossible; otherwise subtract that count from `2 * x`.

**Treat zero as its own double.** Since `2 * 0 == 0`, zero occurrences pair among themselves and their count must be even. No nonzero value can use zero as its double. After this special check, the same greedy consumption covers all other values.

When a value is processed, no later, larger-magnitude base can legitimately consume it as a double of a smaller unprocessed magnitude. Thus committing all its occurrences to their only possible doubles cannot invalidate a different valid pairing. If every count can be consumed, the recorded pair choices partition the whole array.

#### Complexity detail

Counting takes $O(N)$ time. Sorting at most $N$ distinct values costs $O(N\log N)$, and the greedy scan is linear in the number of distinct values. The frequency map and sorted keys use $O(N)$ space.

#### Alternatives and edge cases

- **Repeated unmatched-partner scan:** Process values by absolute magnitude but linearly search all unused occurrences for each required double. It is correct but costs $O(N^2)$ time.
- **Bounded frequency array:** The fixed numeric range permits an indexed count array, trading hash storage for space proportional to the value domain.
- **Ordinary numeric sorting:** Processing negative values from most negative upward is incorrect because a double may be consumed before its half.
- **Odd zero count:** Zero is its own double, so an unpaired zero makes the answer false.
- **Duplicate values:** Counts, not merely set membership, determine whether enough doubles exist.
- **Overflow:** The authored Python solution has unbounded integers; fixed-width implementations should ensure `2 * x` is represented safely.

</details>
