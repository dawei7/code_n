# Check If a String Can Break Another String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) |

## Problem Description

### Goal

Two strings of equal length contain lowercase English letters. A permutation `x` can break a permutation `y` when `x[i]` is lexicographically greater than or equal to `y[i]` at every index.

Determine whether the characters of `s1` and `s2` can be rearranged so that a permutation of `s1` breaks a permutation of `s2`, or a permutation of `s2` breaks a permutation of `s1`. The direction only needs to work one way, but it must remain consistent across every paired position.

### Function Contract

**Inputs**

- `s1` and `s2`: lowercase English strings of the same length $n$, where $1 \le n \le 10^5$.

**Return value**

- `true` if some permutation of either string can break a permutation of the other; otherwise `false`.

### Examples

**Example 1**

- Input: `s1 = "abc", s2 = "xya"`
- Output: `true`

**Example 2**

- Input: `s1 = "abe", s2 = "acd"`
- Output: `false`

**Example 3**

- Input: `s1 = "leetcode", s2 = "interview"`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce permutations to ordered pairing.** If both multisets are sorted, pairing the smallest remaining character from each side is the decisive arrangement. Suppose one sorted string is componentwise at least the other. Those sorted permutations directly satisfy the breaking condition. Conversely, if a breaking pairing exists, the smallest character on the dominant side must be able to cover the smallest character on the other side; removing that pair and repeating yields the same sorted componentwise relation.

**Express sorted dominance with prefixes.** Count each of the 26 letters in both strings. While scanning letters from `a` through `z`, maintain

$$
B(c)=\#\{x\in s1:x\le c\}-\#\{y\in s2:y\le c\}.
$$

If `s1` can break `s2`, `s1` may never have more characters in a low-letter prefix, because those extra small characters could not all be paired above characters from `s2`. Thus every prefix balance must satisfy $B(c) \le 0$. In the opposite direction, every balance must satisfy $B(c) \ge 0$.

**Detect a direction change.** Record whether any prefix balance is positive and whether any is negative. Seeing only nonpositive balances means `s1` can break `s2`; seeing only nonnegative balances means `s2` can break `s1`. Zero balances are compatible with either direction. If both signs occur, neither string has consistent prefix dominance, so return `false` immediately.

**Why prefix dominance is sufficient.** Under one consistent sign, every low-letter prefix contains enough characters on the nondominant side to receive all characters from the corresponding prefix of the dominant side. Greedily pairing sorted characters therefore never forces a dominant character below its partner. The count condition reconstructs exactly the sorted-pairing criterion without materializing either permutation.

#### Complexity detail

Counting both length-$n$ strings takes $O(n)$ time, and examining the fixed 26-letter alphabet takes $O(1)$ additional time. Two arrays of 26 counts use $O(1)$ space because the alphabet size does not grow with $n$.

#### Alternatives and edge cases

- **Sort and compare:** Sorting both strings and checking the two possible componentwise directions is straightforward but takes $O(n\log n)$ time.
- **Try arbitrary matchings:** Searching permutations or pairings is unnecessary; sorted order already characterizes feasibility and combinatorial enumeration is intractable.
- **Anagrams:** Every prefix balance is zero, so either sorted string ties the other at every position and the result is `true`.
- **Single character:** The lexicographically larger character breaks the smaller one, and equal characters break each other.
- **Equal letters at some positions:** Breaking uses greater than or equal, so ties never invalidate a direction.
- **Balance changes sign:** One string has excess small characters at one threshold and the other does at another; no single breaking direction can satisfy all positions.

</details>
