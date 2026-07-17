# Determine if Two Strings Are Close

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1657 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/) |

## Problem Description
### Goal
Two strings are close when either can be transformed into the other by repeating two operations. The first operation swaps any two positions, allowing arbitrary reordering. The second chooses two character values already present in the string and exchanges them everywhere: every occurrence of the first becomes the second, and every occurrence of the second becomes the first.

Given lowercase strings `word1` and `word2`, determine whether these operations can make them equal. A global character exchange cannot create a previously absent character and moves an entire occurrence count from one character label to another.

### Function Contract
**Inputs**

- `word1`: a lowercase English string of length between 1 and $10^5$.
- `word2`: another lowercase English string in the same length range.

Let $N=\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$.

**Return value**

Return `true` if the strings are close under any sequence of the two allowed operations; otherwise return `false`.

### Examples
**Example 1**

- Input: `word1 = "abc", word2 = "bca"`
- Output: `true`

Position swaps alone can reorder one string into the other.

**Example 2**

- Input: `word1 = "a", word2 = "aa"`
- Output: `false`

Neither operation changes string length.

**Example 3**

- Input: `word1 = "cabbba", word2 = "abbccc"`
- Output: `true`

The strings use the same characters and have the same multiset of occurrence counts, so global exchanges can reassign those counts to the required labels before reordering.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Identify what operations cannot change.** Arbitrary position swaps preserve every character count. A global exchange swaps the counts attached to two existing character labels. Therefore both operations preserve the set of characters that occur and the multiset of their positive frequencies. Different lengths, different character support, or different frequency multisets make transformation impossible.

**Count both fixed alphabets.** Build a frequency map for each word. Compare their key sets to verify that no character would need to be introduced or removed. Then sort the two collections of positive counts and compare them. Sorting at most 26 counts is constant work relative to the input length.

**Why the invariants are sufficient.** When support sets match and the frequency multisets match, pair each target character with a source character having its required count. Global exchanges can permute the count assignments among the existing labels to realize that pairing. Once every label has the target count, arbitrary position swaps can arrange the characters into `word2`. Thus the two comparisons exactly characterize closeness.

#### Complexity detail

Counting scans all $N$ characters once. Key and frequency comparisons involve at most 26 lowercase letters, so they add constant work. Total time is $O(N)$ and the fixed-size counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Fixed arrays:** Two arrays of 26 counts avoid hash maps and test positive positions plus sorted count arrays directly, with the same $O(N)$ time and $O(1)$ space.
- **Sort every character:** Full string sorting can derive frequency runs but costs $O(N\log N)$ and still needs separate support and run-length comparisons.
- **Compare only sorted frequencies:** This wrongly accepts strings such as `aabb` and `ccdd`, because global exchanges may use only characters already present.
- **Compare only character sets:** Matching support does not help when the occurrence-count multisets differ.
- Strings of different lengths are never close because both operations preserve length.
- Two permutations of the same multiset are close using only position swaps.
- A one-character string is close only to the same one-character string.
- Repeated global exchanges may permute frequencies arbitrarily among present characters, but cannot introduce a missing letter.
- Equal frequency values are interchangeable and require no special matching order.

</details>
