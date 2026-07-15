# Groups of Special-Equivalent Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 893 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/groups-of-special-equivalent-strings/) |

## Problem Description
### Goal
All strings in `words` have the same length. In one move on a string, choose any two even indices and swap their characters, or choose any two odd indices and swap their characters. Any number of moves may be performed.

Two strings are special-equivalent when these moves can transform one into the other. The array is partitioned into maximal non-empty groups whose members are pairwise special-equivalent. Return the number of such groups.

### Function Contract
Let $N=\lvert\texttt{words}\rvert$ and let $L$ be the common word length.

**Inputs**

- `words`: $N$ lowercase English strings of length $L$, where $1 \leq N \leq 1000$ and $1 \leq L \leq 20$.

**Return value**

Return the number of distinct special-equivalence groups represented in `words`.

### Examples
**Example 1**

- Input: `words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]`
- Output: `3`

The groups are `{"abcd","cdab","cbad"}`, `{"xyzz","zzxy"}`, and `{"zzyx"}`.

**Example 2**

- Input: `words = ["abc","acb","bac","bca","cab","cba"]`
- Output: `3`

**Example 3**

- Input: `words = ["aa","aa","aa"]`
- Output: `1`

### Required Complexity
- **Time:** $O(NL)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Identify what the allowed swaps preserve**

An even-indexed character can move to any other even index but can never move to an odd index; the same holds independently for odd positions. Therefore every string preserves one multiset of even-index letters and another multiset of odd-index letters.

**Use the two multisets as a canonical signature**

Create 26 frequency slots for even indices and 26 for odd indices. Scan a word, incrementing the slot determined by its character and index parity, then convert all 52 counts to a tuple and insert it into a set. The number of distinct tuples is the answer.

Equal signatures are necessary because swaps do not change either parity multiset. They are also sufficient: arbitrary swaps can permute the even positions into any ordering of their multiset and can do the same independently for odd positions. Thus two words share a signature exactly when one is transformable into the other, and distinct signatures correspond exactly to the maximal special-equivalence groups.

#### Complexity detail

Each of the $N$ words contributes $L$ characters to one constant-size signature, so the running time is $O(NL)$. The set stores at most $N$ signatures; because the lowercase alphabet fixes each signature at 52 integers, the auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Sort the two parity slices:** Using `sorted(word[::2])` and `sorted(word[1::2])` is concise but costs $O(NL\log L)$ time.
- **Compare every pair of words:** Building equivalence groups by pairwise comparison can cost $O(N^2L\log L)$ time.
- **Generate reachable permutations:** Enumerating swap outcomes is unnecessary and grows factorially with the parity-class sizes.
- **One-character words:** Only the even-index frequency matters, so equal letters share a group and different letters do not.
- **Duplicate words:** Repeated identical strings add no new signature and therefore no new group.
- **Same overall letter multiset:** Two words can still be in different groups when letters occur in different index parities.
- **Odd word length:** The even-index class contains one more position than the odd-index class, which the separate counts handle automatically.

</details>
