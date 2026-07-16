# Detect Pattern of Length M Repeated K or More Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1566 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/) |

## Problem Description
### Goal

Given an integer array `arr`, a pattern length `m`, and a repetition count `k`, determine whether some contiguous block of `m` values occurs at least `k` times consecutively in the array.

The repeated copies must be adjacent and identical element by element. The pattern may begin at any index, and values outside the repeated region do not matter. Return whether such a region exists.

### Function Contract
**Inputs**

- `arr`: An integer array of length $N$, where $2 \le N \le 100$ and $1 \le \texttt{arr[i]} \le 100$.
- `m`: The positive length of one pattern copy, where $1 \le m \le 100$.
- `k`: The number of consecutive copies required, where $2 \le k \le 100$.

**Return value**

Return `true` if there is an index at which the next $mk$ values consist of $k$ identical length-`m` blocks; otherwise return `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,4,4,4,4], m = 1, k = 3`
- Output: `true`

**Example 2**

- Input: `arr = [1,2,1,2,1,1,1,3], m = 2, k = 2`
- Output: `true`

**Example 3**

- Input: `arr = [1,2,1,2,1,3], m = 2, k = 3`
- Output: `false`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare values one pattern length apart**

Inside consecutive copies of the same length-`m` pattern, every value equals the value exactly `m` positions later. Conversely, if this offset equality holds for $m(k-1)$ consecutive indices, those comparisons connect the first copy to the second, the second to the third, and so on through $k$ adjacent copies. That run of equalities is therefore exactly the condition the problem asks for.

**Track one consecutive equality run**

Scan `index` from left to right while `index + m` remains in the array. If `arr[index] == arr[index + m]`, increase `equal_offset_run`; otherwise reset it to zero because a repeated region cannot cross that mismatch. Return `true` as soon as the run reaches `m * (k - 1)`.

The threshold contains `k - 1` boundaries between adjacent copies and `m` element comparisons across each boundary. Reaching it proves that one length-`m` block is followed immediately by at least `k - 1` identical blocks. If the scan ends below the threshold, every possible repeated region contains a mismatch, so the answer is `false`.

#### Complexity detail

The scan performs one comparison at each of at most $N-m$ offsets, giving $O(N)$ time.

Only the current equality-run length is stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Check every starting index directly:** compare all $mk$ values against the first pattern copy. This is straightforward but can take $O(Nmk)$ time.
- **Slice comparison:** compare `arr[start:start + m] * k` with the candidate repeated region. It is concise, but repeated allocation and comparison can require quadratic time and linear temporary space.
- **Rolling hash:** hash length-`m` windows and count equal adjacent hashes. It adds collision handling and is unnecessary for the small integer-array scan.
- **Pattern length one:** the task becomes finding `k` equal adjacent values; the same offset-run logic uses offset one.
- **Insufficient remaining length:** if $mk>N$, no starting index can contain the required copies, and the equality threshold cannot be reached.
- **Repetition after a mismatch:** resetting the counter allows a valid region later in the array to be found independently.
- **More than `k` copies:** reaching the threshold at the first `k` copies is sufficient; additional copies do not change the answer.
- **Overlapping similarities:** partial or overlapping matches do not qualify unless they form $k$ complete adjacent blocks of exactly `m` values.

</details>
