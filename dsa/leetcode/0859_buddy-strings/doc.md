# Buddy Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 859 |
| Difficulty | Easy |
| Topics | Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/buddy-strings/) |

## Problem Description
### Goal
Given two lowercase strings `s` and `goal`, decide whether exactly one swap within `s` can make it equal to `goal`. A swap chooses two distinct, zero-indexed positions `i` and `j` and exchanges `s[i]` with `s[j]`; for example, swapping positions `0` and `2` in `"abcd"` produces `"cbad"`.

The two chosen letters are allowed to be equal. Consequently, an already matching pair of strings is valid only when `s` contains a repeated letter whose two occurrences can be swapped without changing the string. Return whether a valid pair of swap positions exists.

### Function Contract
**Inputs**

- `s`: a lowercase English string.
- `goal`: another lowercase English string, where $1 \leq \lvert\texttt{s}\rvert, \lvert\texttt{goal}\rvert \leq 2\cdot 10^4$.

Let $n=\lvert\texttt{s}\rvert$.

**Return value**

Return `true` if swapping the letters at exactly two distinct positions in `s` can produce `goal`; otherwise, return `false`.

### Examples
**Example 1**

- Input: `s = "ab", goal = "ba"`
- Output: `true`

Swapping `s[0]` and `s[1]` produces `goal`.

**Example 2**

- Input: `s = "ab", goal = "ab"`
- Output: `false`

The only possible swap changes the string.

**Example 3**

- Input: `s = "aa", goal = "aa"`
- Output: `true`

The two equal letters can be swapped while leaving `s` unchanged.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate equality from actual mismatches**

Strings of different lengths cannot become equal through a swap. For equally long strings, scan paired characters once and record the indices where they differ. A single swap changes at most two positions, so more than two mismatches makes the transformation impossible. Exactly one mismatch is also impossible because exchanging two positions cannot repair just one changed position.

While scanning, track which of the 26 lowercase letters have appeared and whether any letter is duplicated. This information handles the case with no mismatches: because the operation must choose distinct indices, an unchanged result is possible exactly when two equal occurrences can be exchanged.

**Character crossings characterize two mismatches**

Suppose the only mismatching indices are `i` and `j`. Swapping them works precisely when `s[i] == goal[j]` and `s[j] == goal[i]`. These two crossed equalities are necessary because no other positions change, and they are sufficient because every position outside the pair already matches.

The scan therefore covers all possible cases: zero mismatches uses the duplicate flag, two mismatches uses the crossed comparison, and every other mismatch count returns `false`. No possible one-swap transformation is omitted.

#### Complexity detail

The paired scan examines $n$ positions once, so it takes $O(n)$ time. The mismatch list is capped at two indices, and the seen-letter table has exactly 26 entries because the alphabet is fixed. Auxiliary space is therefore $O(1)$.

#### Alternatives and edge cases

- **Try every pair of indices:** Performing each possible swap is correct, but there are $O(n^2)$ pairs and materializing each result can add another linear factor.
- **Sort both strings:** Equal sorted forms verify that the character multisets match, but they do not enforce that exactly one swap suffices and sorting costs $O(n\log n)$ time.
- **Frequency counting alone:** Matching counts is necessary but not sufficient; `"abcd"` and `"badc"` have the same counts yet require two swaps.
- **Different lengths:** A swap preserves length, so the answer is immediately `false`.
- **Already equal strings:** The answer is `true` only if some letter appears at least twice.
- **One-character strings:** Distinct swap indices do not exist, so the answer is `false`.
- **Exactly one mismatch:** A swap affects two positions and cannot repair only one.
- **More than two mismatches:** One exchange cannot change enough positions.

</details>
