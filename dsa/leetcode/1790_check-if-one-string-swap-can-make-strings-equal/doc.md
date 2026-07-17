# Check if One String Swap Can Make Strings Equal

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) |
| Frontend ID | 1790 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given two lowercase strings `s1` and `s2` of equal length. One string swap chooses two indices in one string and exchanges the characters at those positions; the indices are allowed to be the same.

Determine whether the strings can be made equal by performing at most one swap on exactly one of them. Using no swap is allowed when the strings already match. Return `false` if no single exchange within either string can repair every differing position.

### Function Contract

**Inputs**

- `s1`: a lowercase English string of length $n$.
- `s2`: another lowercase English string with the same length, where $1 \le n \le 100$.

**Return value**

- Return `true` if zero or one swap within one string can make `s1` and `s2` equal; otherwise, return `false`.

### Examples

**Example 1**

- Input: `s1 = "bank", s2 = "kanb"`
- Output: `true`

Swapping the first and last characters of either string repairs the two mismatches.

**Example 2**

- Input: `s1 = "attack", s2 = "defend"`
- Output: `false`

One swap cannot repair all differing positions.

**Example 3**

- Input: `s1 = "kelb", s2 = "kelb"`
- Output: `true`

The strings already match, so no operation is required.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Record only positions that a swap must repair**

Scan the strings together and record the ordered character pair `(s1[i], s2[i])` whenever the characters differ. A swap changes at most two positions, so more than two mismatches makes the answer immediately `false`.

**Classify the possible mismatch counts**

Zero mismatches means the strings are already equal, which is valid because the operation count is at most one. Exactly one mismatch cannot work: swapping two positions preserves each string's character multiset and cannot change only one position. More than two mismatches also cannot work.

The only nontrivial case therefore has exactly two mismatches.

**Require the two character pairs to cross-match**

Suppose the mismatches are `(a, b)` and `(c, d)`. Swapping the two positions in `s1` repairs both precisely when `a = d` and `c = b`. Equivalently, the second ordered pair must be the reverse of the first.

If this cross-match holds, performing that swap produces equality. If it does not, neither swapping those positions nor any positions that already match can repair both mismatches. These cases exhaust every possible one-swap outcome.

#### Complexity detail

The scan compares at most $n$ character pairs, taking $O(n)$ time. At most two mismatch pairs are retained, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Try every swap:** Constructing and testing every index pair is correct but takes at least $O(n^2)$ candidate swaps and may copy strings repeatedly.
- **Sort both strings first:** Equal character multisets are necessary for a repair, but four or more misplaced characters can share a multiset and still require several swaps.
- **Frequency counting plus mismatch count:** This is correct, but the two ordered mismatch pairs already verify both multiplicity and placement.
- **Already equal:** Return `true` without requiring an actual swap; choosing the same index would also leave a string unchanged.
- **One mismatch:** A swap cannot alter only one position, so the result is `false`.
- **Repeated characters:** They do not change the cross-pair criterion.
- **Adjacent or distant indices:** Distance is irrelevant; any two indices in one string may be swapped.
- **Swap either string:** The cross-match condition is symmetric, so checking one direction is sufficient.

</details>
