# Minimum Deletions to Make Character Frequencies Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1647 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) |

## Problem Description
### Goal
A string is good when no two distinct characters that remain in it have the same positive frequency. Given a lowercase English string `s`, delete as few characters as possible to make it good.

Deleting every occurrence of a character reduces its frequency to zero; zero-frequency characters are absent and do not conflict with one another. Return only the minimum number of deletions, not a resulting string.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.

**Return value**

Return the minimum number of character deletions needed so that all positive character frequencies are pairwise distinct.

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `0`

The frequencies 2 and 1 are already distinct.

**Example 2**

- Input: `s = "aaabbbcc"`
- Output: `2`

The frequencies 3, 3, and 2 can become 3, 2, and 1 with two deletions.

**Example 3**

- Input: `s = "ceabaacb"`
- Output: `2`

Deleting both copies of `c` leaves positive frequencies 4, 2, and 1.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the fixed alphabet.** Build the frequency of each lowercase letter. Maintain a set of positive frequencies already assigned to processed characters.

**Lower each conflicting frequency greedily.** For a character with current count $f$, repeatedly decrement $f$ while it is positive and already used. Each decrement represents deleting one occurrence. If the resulting value remains positive, reserve it in the set; if it reaches zero, the character disappears and zero is not reserved.

For any processed prefix of characters, assigning the largest available frequency not exceeding the original loses the fewest occurrences. If a conflicting character were reduced below an unused larger frequency, raising it to that frequency would preserve uniqueness and use fewer deletions. Therefore the greedy choice is optimal at each step, and the sum of decrements is globally minimal.

#### Complexity detail

Counting scans $n$ characters. There are only 26 frequencies, and every decrement contributes directly to the returned deletion count, which cannot exceed $n$, so total time is $O(n)$. The counter and used-frequency set contain at most 26 entries; because the alphabet size is fixed, auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sort frequencies descending:** Assign each count at most one less than the preceding retained count. This is also greedy and runs in $O(n)$ time because only 26 counts are sorted.
- **Sort every character:** Character sorting can derive run lengths but costs $O(n\log n)$ and is unnecessary.
- **Try all target frequencies:** Backtracking over possible distinct counts is exponential and repeats the greedy dominance decision.
- A one-character string is already good.
- Several singleton characters can retain frequency 1 for only one character; every other singleton must be deleted.
- Characters reduced to frequency zero do not conflict because they no longer occur.
- The order in which equal original frequencies are processed does not change the minimum total deletions.
- A string whose positive frequencies are already distinct requires zero deletions.

</details>
