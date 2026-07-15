# K-Concatenation Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-concatenation-maximum-sum/) |

## Problem Description

### Goal

You are given an integer array `arr` and an integer `k`. Construct a modified array conceptually by repeating `arr` exactly `k` times in sequence. For example, repeating `[1,2]` three times produces `[1,2,1,2,1,2]`.

Find the maximum sum of a contiguous subarray in that modified array. The chosen subarray may have length zero, in which case its sum is zero, so the answer is never negative. Because the maximum sum may be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le10^5$ and $-10^4\le\texttt{arr[i]}\le10^4$.
- `k`: The number of consecutive copies, where $1\le k\le10^5$.

**Return value**

- The maximum contiguous-subarray sum over the conceptual $k$-copy array, allowing the empty subarray, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `arr = [1,2]`, `k = 3`
- Output: `9`

All six values in the conceptual array have positive sum.

**Example 2**

- Input: `arr = [1,-2,1]`, `k = 5`
- Output: `2`

**Example 3**

- Input: `arr = [-1,-2]`, `k = 7`
- Output: `0`

The empty subarray is better than every non-empty subarray.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce an enormous conceptual array to two copies.** Kadane's recurrence maintains the best nonnegative sum ending at the current position and the best sum seen. When `k == 1`, one pass over `arr` directly answers the problem. For `k >= 2`, any best subarray either stays within one copy or crosses at least one copy boundary. Scanning two consecutive copies captures every possible starting suffix, ending prefix, and one-copy internal choice.

**Decide whether complete middle copies help.** Let

$$
T = \sum_{x\in\texttt{arr}} x.
$$

If $T\le0$, inserting another complete copy cannot improve a crossing subarray, so the two-copy Kadane value is final. If $T>0$, a subarray spanning more than two copies benefits from including every one of the `k - 2` complete middle copies. Adding `(k - 2) * T` to the best two-copy value yields the optimum without constructing those copies.

**Delay the modulo operation.** Kadane comparisons and the sign of $T$ must use the true integer sums. Reduce only the final nonnegative optimum modulo $10^9+7$; applying modulo during the recurrence could change which candidate is larger and produce an incorrect maximum.

#### Complexity detail

Kadane's algorithm examines either one or two copies of the $n$-element input, and computing $T$ takes one additional pass, so the total time is $O(n)$ and does not depend on `k`. The running sum, best sum, total, and loop indices use $O(1)$ auxiliary space; the conceptual concatenation is never materialized.

#### Alternatives and edge cases

- **Materialize all copies:** Running Kadane on `arr * k` is straightforward but takes $O(nk)$ time and space, which is infeasible at the maximum constraints.
- **Prefix and suffix tables:** Computing the best suffix and prefix separately also derives the best boundary-crossing sum, but storing full tables wastes $O(n)$ space when running aggregates suffice.
- **One copy:** When `k == 1`, adding any cross-copy contribution would refer to elements that do not exist.
- **All negative values:** Resetting the running sum to zero implements the explicitly allowed empty subarray and returns zero.
- **Zero or negative total:** Additional complete copies cannot increase the optimum, although a profitable suffix-to-prefix segment may still cross one boundary.
- **Positive total:** Every complete middle copy increases a spanning candidate by exactly $T$.
- **Large arithmetic:** The unreduced optimum can exceed fixed-width 32-bit integers, so implementations in bounded-integer languages need a sufficiently wide type.
- **Modulo timing:** Only the returned value is reduced; intermediate values retain their true order and sign.

</details>
