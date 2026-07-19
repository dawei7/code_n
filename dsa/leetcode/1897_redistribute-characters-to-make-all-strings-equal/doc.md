# Redistribute Characters to Make All Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1897 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/) |

## Problem Description

### Goal

An operation chooses two different word indices, removes any one character from a nonempty source word, and inserts that character at any position in the destination word. The operation may be repeated any number of times, and the selected source and destination can change between operations.

Given an array of lowercase words, decide whether these moves can make every word exactly equal. Character order and the initial word lengths may change, but no character can be created, deleted, or changed into another letter.

### Function Contract

**Inputs**

- `words`: an array of $N$ nonempty lowercase English strings, where $1 \le N \le 100$ and every initial word has length from $1$ through $100$.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

Return `true` if character moves can make all $N$ strings identical; otherwise return `false`.

### Examples

**Example 1**

- Input: `words = ["abc","aabc","bc"]`
- Output: `true`
- Explanation: Moving one `a` from the second word to the third produces three copies of `"abc"`.

**Example 2**

- Input: `words = ["ab","a"]`
- Output: `false`

**Example 3**

- Input: `words = ["ab","ba"]`
- Output: `true`
- Explanation: The combined counts contain two copies of each letter, so each of two final words can receive one.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Every move preserves the combined number of occurrences of each letter. If all $N$ final words are identical, the global count of every character must therefore be divisible by $N$.

This condition is also sufficient. When every letter count is divisible by $N$, assign exactly one-$N$th of each letter's occurrences to every target word. The operation permits moving any character to any position, so characters can always be rearranged to realize those identical multisets and then ordered identically.

Count all letters across all words in one pass, and return whether every resulting count is divisible by `len(words)`.

#### Complexity detail

The scan visits each of the $S$ input characters once, so it takes $O(S)$ time. Only counts for the 26 lowercase English letters are needed. Because that alphabet size is fixed independently of the input, the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Compare total length only:** Divisibility of $S$ by $N$ is necessary but not sufficient; each individual letter count must divide evenly.
- **Simulate moves:** Constructing a sequence of character transfers is unnecessary because the divisibility test completely characterizes feasibility.
- **Sort all characters:** Sorting can expose counts, but it costs $O(S \log S)$ time instead of a linear scan.
- **One word:** With $N=1$, every count is divisible and no operation is needed.
- **Different initial lengths:** The operation may empty or lengthen words, so unequal starting lengths do not by themselves make the answer false.
- **Repeated characters:** Multiplicity is the essential information; the original positions of equal letters do not matter.

</details>
