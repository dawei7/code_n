# Subarray Sums Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 974 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subarray-sums-divisible-by-k/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, count the non-empty subarrays whose sums are divisible by `k`.

A subarray is a contiguous part of the original array. Its elements must therefore occupy consecutive positions; choosing separated elements does not form a subarray.

For a range to qualify, its sum may be positive, negative, or zero, but it must equal an integer multiple of `k`. Count every distinct contiguous range that satisfies this condition, even when different ranges contain the same sequence of values or produce the same sum.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1 \le N \le 3\cdot10^4$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `k`: the positive divisor, where $2 \le K = \texttt{k} \le 10^4$.

Define the prefix sum through the first $i$ elements as

$$
P_i = \sum_{j=0}^{i-1}\texttt{nums[j]},
$$

with $P_0=0$.

**Return value**

- The number of non-empty contiguous subarrays whose element sum is divisible by $K$.

### Examples

**Example 1**

- Input: `nums = [4, 5, 0, -2, -3, 1], k = 5`
- Output: `7`
- Explanation: seven contiguous ranges have sums that are multiples of $5$, including the whole array, `[5]`, `[0]`, and `[-2, -3]`.

**Example 2**

- Input: `nums = [5], k = 9`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**Turn range sums into prefix differences:** The sum of the subarray from index `a` through `b - 1` is $P_b-P_a$. This difference is divisible by $K$ exactly when $P_a$ and $P_b$ have the same remainder modulo $K$.

**Count earlier matching remainders:** Keep a frequency table for remainders of prefixes already visited. The empty prefix contributes remainder zero before any array element is processed, so initialize its frequency to one. After adding each value to the running prefix, compute its normalized remainder. Every earlier prefix with that same remainder defines one valid non-empty subarray ending at the current position, so add the stored frequency to the answer and then increment it.

This counts every valid subarray once: its ending prefix discovers its unique starting prefix. It counts no invalid subarray because equal remainders imply their prefix difference is a multiple of $K$.

**Handle negative values without branching:** Python's `prefix % k` already produces a remainder from `0` through `k - 1`. In languages whose remainder operator can be negative, normalize with `((prefix % k) + k) % k` before indexing the frequency table.

#### Complexity detail

Each of the $N$ values performs constant-time arithmetic and one frequency lookup, for $O(N)$ time. The table has exactly $K$ counters, so it uses $O(K)$ space.

#### Alternatives and edge cases

- **Enumerate every subarray:** Extending a running sum from every starting index is correct but requires $O(N^2)$ time.
- **Store all prefix sums:** Testing every pair of prefixes restates the same quadratic search; grouping prefixes by remainder is the information-preserving compression.
- **Zero values:** A zero contributes the same remainder as the preceding prefix, correctly adding subarrays whose sum is zero.
- **Negative totals:** Remainders must be normalized consistently so mathematically equivalent residues share one counter.
- **Whole-array match:** Seeding remainder zero accounts for any prefix, including the entire array, whose sum is divisible by $K$.

</details>
