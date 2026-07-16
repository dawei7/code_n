# Kth Missing Positive Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1539 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/) |

## Problem Description
### Goal
You are given a strictly increasing array `arr` of positive integers and a positive integer `k`. Some positive integers may be absent before the first stored value, between consecutive entries, or after the final entry.

List every positive integer that does not occur in `arr` in increasing order. Using one-based rank, return the $k$th value in that missing sequence. Values already present in the array never count toward the rank, even when the answer lies beyond the array's largest element.

### Function Contract
**Inputs**

- `arr`: a strictly increasing array of positive integers, with length $n$ between $1$ and $1000$ and values at most $1000$.
- `k`: the one-based rank of the missing positive integer to find, where $1 \le k \le 1000$.

**Return value**

The $k$th positive integer absent from `arr`.

### Examples
**Example 1**

- Input: `arr = [2, 3, 4, 7, 11], k = 5`
- Output: `9`
- Explanation: The missing sequence starts `1, 5, 6, 8, 9`, so its fifth value is `9`.

**Example 2**

- Input: `arr = [1, 2, 3, 4], k = 2`
- Output: `6`
- Explanation: The first two missing positives are `5` and `6`.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count missing values before an array position**

If no positive integer were absent, index `i` would contain `i + 1`. Because the array is strictly increasing, the excess

`arr[i] - (i + 1)`

is exactly the number of positive integers missing before `arr[i]`. This count is nondecreasing as `i` moves right, which makes it a binary-search predicate.

**Find the first position that has skipped enough values**

Binary-search the half-open index range `[0, len(arr))` for the first position whose missing count is at least `k`. If `arr[middle] - middle - 1 < k`, the desired missing value lies to the right, so set `left = middle + 1`; otherwise keep `middle` in the search by setting `right = middle`.

When the search ends, `left` is the number of array elements that occur before the answer. Among the positive integers from `1` through the answer, exactly `k` are missing and exactly `left` are present. Therefore the answer is `left + k`.

This formula also covers both boundaries. If enough values are missing before the first array element, `left` is zero and the answer is `k`. If fewer than `k` values are missing by the final element, `left` becomes `n`, extending the result beyond the array as `n + k`.

**Why the boundary is unique**

For consecutive indices, the missing count changes by `arr[i + 1] - arr[i] - 1`, which is never negative. Thus every position before `left` has skipped fewer than `k` positives, while every position from `left` onward has skipped at least `k`. The count identity above then proves that `left + k` is present in neither side of the array and has exactly `k - 1` missing positives before it.

#### Complexity detail

Binary search examines $O(\log n)$ positions and uses only its two boundaries and a midpoint, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Linear gap scan:** subtract each gap from `k` until locating the target; it is straightforward but takes $O(n)$ time in the worst case.
- **Hash-set enumeration:** test positive integers one by one against a set, using $O(n)$ extra space and potentially scanning beyond the final array value.
- If `arr[0] > k`, the answer is `k` because the first `k` positive integers are all absent.
- When `arr` begins with a consecutive prefix from `1`, those entries contribute no missing values, and the binary search moves past them.
- The $k$th missing value may lie after `arr[-1]`; the half-open search naturally returns `n` in that case.
- Strict increase is essential to the missing-count monotonicity and rules out duplicate entries.

</details>
