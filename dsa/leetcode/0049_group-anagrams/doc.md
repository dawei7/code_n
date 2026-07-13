# Group Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 49 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/group-anagrams/) |

## Problem Description
### Goal
You are given a list of strings containing lowercase English letters. Two strings are anagrams when one can be formed by rearranging all characters of the other, including the same multiplicity of every letter.

Partition the input occurrences into complete anagram groups and return those groups in any order. Every list entry must appear exactly once, including repeated identical strings, which remain repeated members of one group. Member order within a group may also vary. Empty strings are anagrams of one another and form their own group.

### Function Contract
**Inputs**

- `strs`: `List[str]` containing lowercase English letters

**Return value**

A `List[List[str]]` in which each inner list is one complete anagram group.

### Examples
**Example 1**

- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ]` in any ordering

**Example 2**

- Input: `strs = [""]`
- Output: `[[""]]`

**Example 3**

- Input: `strs = ["a", "a"]`
- Output: `[["a", "a"]]`

### Required Complexity

- **Time:** $O(C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Replace character order with a complete frequency signature**

For each word, count its 26 lowercase letters. Convert the fixed array of counts to an immutable tuple and use it as a hash-map key. The tuple must contain all 26 positions, including zero counts, so the letter associated with each count remains unambiguous.

Here `C` denotes the total number of characters across all input strings.

**Buckets preserve multiplicity as well as membership**

After processing the first `i` strings, each occurrence has been appended exactly once to the bucket matching its frequency tuple, and no bucket contains a string with a different tuple. Appending rather than storing a set is important: repeated identical input strings are distinct occurrences and must all remain in the output.

**Trace several equivalence classes**

`eat`, `tea`, and `ate` all produce counts with one `a`, one `e`, and one `t`, so they enter one bucket. `tan` and `nat` share another tuple, while `bat` creates a third.

**The frequency tuple is a complete anagram signature**

Rearranging a lowercase word changes only character order, never the count of any of the 26 letters. Thus anagrams necessarily have equal frequency tuples. Conversely, equal tuples contain the same multiset of letters, so one word can be rearranged into the other.

Tuple equality is therefore exactly the anagram relation, not merely a heuristic. Appending each word to the bucket for its tuple places all and only mutually anagrammatic words together.

#### Complexity detail

Counting visits each character once, and creating a fixed-size 26-entry key is constant work per string, for $O(C)$ time. The returned strings and grouping map require $O(C)$ storage; keys add $O(26n)$, which is linear in the number of strings.

#### Alternatives and edge cases

- **Sort every word:** gives a convenient canonical key but costs $O(k \log k)$ per length-`k` word.
- **Compare every pair:** repeatedly recounts or compares strings and can become quadratic in the number of words.
- **Prime products:** can represent counts mathematically, but fixed-width implementations risk overflow and arbitrary-precision products become unnecessarily large.
- Every empty string has the all-zero signature, so empty strings group together naturally.
- The 26-count key relies on the lowercase-English-letter contract. A larger or unrestricted alphabet may favor sorting or a sparse frequency representation.

</details>
