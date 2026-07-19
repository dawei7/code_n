# Maximum Number of Removable Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1898 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/) |

## Problem Description

### Goal

You receive strings `s` and `p`, where `p` is already a subsequence of `s`. You also receive `removable`, a list of distinct indices into the original string. For a chosen integer $k$, remove the characters at the first $k$ indices of this list. The indices always refer to their positions in the original `s`; deleting one character does not renumber the others.

Choose as many leading entries of `removable` as possible while ensuring that `p` remains a subsequence of the characters left in their original relative order. Return that maximum prefix length $k$, which may be zero or the entire length of `removable`.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$.
- `p`: a nonempty lowercase English string that is a subsequence of `s`.
- `removable`: an array of $r$ distinct zero-based indices of `s`, in removal order.
- The constraints satisfy $1 \le \lvert p \rvert \le n \le 10^5$ and $0 \le r < n$.

**Return value**

Return the greatest integer $k$ with $0 \le k \le r$ such that deleting the characters at `removable[0]` through `removable[k - 1]` leaves `p` as a subsequence.

### Examples

**Example 1**

- Input: `s = "abcacb", p = "ab", removable = [3, 1, 0]`
- Output: `2`
- Explanation: Removing original indices `3` and `1` leaves `"accb"`, which still contains `"ab"` as a subsequence. Removing index `0` as well destroys that subsequence.

**Example 2**

- Input: `s = "abcbddddd", p = "abcd", removable = [3, 2, 1, 4, 5, 6]`
- Output: `1`
- Explanation: After the first removal, `"abcddddd"` still contains `"abcd"`. The next removal makes that impossible.

**Example 3**

- Input: `s = "abcab", p = "abc", removable = [0, 1, 2, 3, 4]`
- Output: `0`
- Explanation: Removing original index `0` immediately eliminates every possible `"abc"` subsequence.

### Required Complexity

- **Time:** $O((n + r)\log(r + 1))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn removal order into a threshold.** Build an array `removal_time` aligned with `s`. If original index `i` is the $j$-th entry of `removable`, store $j$; for an index that is never removable, store $r$. Under a candidate prefix length $k$, the character at index `i` remains exactly when `removal_time[i] >= k`. This avoids constructing a new string or repeatedly shifting indices.

**Test one prefix with two pointers.** Scan `s` from left to right while tracking the next unmatched character of `p`. Ignore positions removed before $k$. Whenever a retained character equals the current character of `p`, advance the pattern pointer. The test succeeds if that pointer reaches the end of `p`. Because matches are taken in increasing original-index order, success is precisely the definition of `p` being a subsequence.

**Binary-search the last successful prefix.** If `p` survives $k$ removals, it also survives any smaller prefix because restoring characters cannot invalidate a subsequence. Conversely, once a prefix fails, every larger prefix fails. This monotone true-then-false predicate lets an upper-midpoint binary search retain the greatest successful $k$, including the boundary answers $0$ and $r$.

#### Complexity detail

Let $n = \lvert s \rvert$ and $r = \lvert\texttt{removable}\rvert$. Constructing `removal_time` costs $O(n + r)$ time and $O(n)$ space. Each subsequence test scans at most $n$ positions, and binary search performs $O(\log(r + 1))$ tests. The total time is $O((n + r)\log(r + 1))$, with $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Rebuild the retained string for every candidate:** This preserves correctness but performs extra allocation and may repeatedly copy $O(n)$ characters; a removal-time array supports the same test in place.
- **Try every prefix in increasing order:** Rechecking the subsequence after each removal can require $O(nr)$ time when `p` survives nearly every prefix.
- **Empty `removable`:** The only legal choice is $k = 0$, and the initial subsequence guarantee makes it valid.
- **All listed removals are harmless:** The answer can equal $r$ even though the constraints require $r < n$.
- **Original indices:** Entries in `removable` never shift after earlier deletions; treating them as indices into a shortened string changes the problem.
- **Repeated characters:** A greedy left-to-right subsequence match is necessary because retaining the right counts alone does not preserve relative order.

</details>
