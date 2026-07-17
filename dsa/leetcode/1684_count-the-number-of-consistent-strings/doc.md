# Count the Number of Consistent Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1684 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-consistent-strings/) |

## Problem Description
### Goal

The string `allowed` contains distinct lowercase English letters and defines which characters may appear in a consistent string. A word is consistent only if every one of its characters occurs in `allowed`; repeated uses of an allowed character remain valid, and a single character outside the set makes the whole word inconsistent.

Inspect each string in `words` independently and return how many of them are consistent. The answer counts array entries rather than distinct word values, so equal words at different positions each contribute when they satisfy the rule.

### Function Contract
**Inputs**

- `allowed`: a nonempty string of distinct lowercase English letters
- `words`: a nonempty list of nonempty lowercase English strings

Let

$$
S = \lvert \texttt{allowed} \rvert + \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

The number of entries in `words` whose every character belongs to `allowed`.

### Examples
**Example 1**

- Input: `allowed = "ab", words = ["ad", "bd", "aaab", "baa", "badab"]`
- Output: `2`

Only `"aaab"` and `"baa"` use no letter outside `"ab"`.

**Example 2**

- Input: `allowed = "abc", words = ["a", "b", "c", "ab", "ac", "bc", "abc"]`
- Output: `7`

Every word is consistent.

**Example 3**

- Input: `allowed = "cad", words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]`
- Output: `4`

The consistent entries are `"cc"`, `"acd"`, `"ac"`, and `"d"`.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Preprocess membership once**

Store the distinct letters of `allowed` in a constant-time membership representation. A set is direct; a 26-bit integer is an equally suitable fixed-alphabet representation. This avoids rescanning `allowed` for every character of every word.

**Reject a word at its first forbidden letter**

For each word, test its characters against the membership representation. Count the word if all tests succeed. If any test fails, the word cannot be consistent, so its remaining characters need not be examined.

Every counted word satisfies the definition because each of its characters passed the allowed-membership test. Every uncounted word has at least one character that failed that test and is therefore inconsistent. Processing array entries separately also preserves multiplicity when the same word appears more than once.

#### Complexity detail

Building the allowed representation and inspecting the word characters takes $O(S)$ total time. At most 26 lowercase letters are stored, so the auxiliary space is $O(26)=O(1)$. Early rejection may save work on particular words but does not change the worst-case bound.

#### Alternatives and edge cases

- **Scan `allowed` for each character:** this is correct but takes $O(A S)$ time when $A = \lvert \texttt{allowed} \rvert$, repeating membership work that preprocessing removes.
- **Bitmask membership:** map each lowercase letter to one of 26 bits; this has the same linear time and constant space as a set with smaller fixed storage.
- **Set difference per word:** checking whether `set(word) - set(allowed)` is empty is concise, but repeatedly allocates a set for each word.
- **Repeated letters:** a consistent word may use the same allowed letter any number of times.
- **Duplicate words:** identical entries are counted independently because the result is over the array, not over distinct strings.
- **One forbidden character:** one disallowed letter invalidates the entire word even if every other letter is allowed.

</details>
