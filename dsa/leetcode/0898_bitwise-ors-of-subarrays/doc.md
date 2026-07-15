# Bitwise ORs of Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 898 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-ors-of-subarrays/) |

## Problem Description
### Goal
Given an integer array `arr`, consider every non-empty subarray and compute the bitwise OR of all integers in that subarray. A one-element subarray has the value of its sole element.

A subarray is a contiguous, non-empty sequence of array elements. Different subarrays may produce the same OR value; only the resulting value matters, not how many subarrays produce it.

Return the number of distinct values produced across all such subarrays.

### Function Contract
Let $n$ be the length of `arr`, let $M=\max(\texttt{arr})$, and define the relevant bit width as

$$
b =
\begin{cases}
1, & M=0,\\
1+\lfloor \log_2 M \rfloor, & M>0.
\end{cases}
$$

Under the input bounds, $b \leq 30$.

**Inputs**

- `arr`: an integer array with $1 \leq n \leq 5 \cdot 10^4$.
- Every element satisfies $0 \leq \texttt{arr}[i] \leq 10^9$.

**Return value**

Return the number of distinct bitwise-OR results among every non-empty contiguous subarray of `arr`.

### Examples
**Example 1**

- Input: `arr = [0]`
- Output: `1`

The only subarray produces `0`.

**Example 2**

- Input: `arr = [1,1,2]`
- Output: `3`

The subarrays produce only `1`, `2`, and `3` as distinct OR values.

**Example 3**

- Input: `arr = [1,2,4]`
- Output: `6`

The distinct results are `1`, `2`, `3`, `4`, `6`, and `7`.

### Required Complexity
- **Time:** $O(nb)$
- **Space:** $O(nb)$

<details>
<summary>Approach</summary>

#### General

**Keep only subarrays ending at the current position**

Let `ending` be the set of OR values for all subarrays ending at the previous index. When the next value `x` arrives, every subarray ending here is either the one-element subarray `[x]` or an earlier ending subarray extended by `x`. Therefore compute `next_ending = {x} | {value | x for value in ending}`.

Add every value in `next_ending` to a global `results` set, then replace `ending` with `next_ending`. The size of `results` after the final element is the answer.

**Why each ending set stays small**

Extending a subarray leftward can only turn zero bits into one bits in its OR; a bit never turns off. After duplicate OR values are merged, each strict change must add at least one of the $b$ relevant bits. Thus at most $b+1$ distinct OR states can occur for subarrays sharing one right endpoint.

For the first element, `ending` contains exactly its one-element subarray OR. Inductively, the transition includes the new one-element subarray and extends every subarray from the preceding endpoint, so it produces exactly all OR values ending at the current index. Unioning those sets over all endpoints therefore places every non-empty subarray result in `results`, and nothing else. Returning the set size gives precisely the number of distinct results.

#### Complexity detail

At each of $n$ indices, at most $b+1$ ending values are extended, giving $O(nb)$ time. The current endpoint set uses $O(b)$ space, while the global result set can contain $O(nb)$ distinct values, so total space is $O(nb)$.

#### Alternatives and edge cases

- **Enumerate every subarray incrementally:** Carrying a running OR for each left endpoint avoids recomputing a subarray from scratch, but still takes $O(n^2)$ time.
- **Recompute each subarray OR:** Three nested loops are straightforward but can require $O(n^3)$ time.
- **In-place compressed list:** The endpoint states can be stored in a deduplicated list instead of a set, preserving the same $O(nb)$ bound with more manual duplicate handling.
- **One element:** The only result is that element itself.
- **All zeros:** Every subarray OR is `0`, so the answer is one.
- **Repeated values:** Equal subarrays and overlapping subarrays may yield duplicate ORs; both endpoint and global sets must deduplicate them.
- **Zero inside a subarray:** OR with zero leaves the accumulated value unchanged, which the endpoint set naturally merges.
- **Maximum values:** Python integers safely represent the allowed values, and only the lowest $b \leq 30$ bits can participate.

</details>
