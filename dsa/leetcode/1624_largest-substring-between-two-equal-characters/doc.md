# Largest Substring Between Two Equal Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1624 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-substring-between-two-equal-characters/) |

## Problem Description
### Goal
Given a string `s`, choose two occurrences of the same character and consider the contiguous substring strictly between them. The two matching endpoint characters are excluded from its length.

Return the greatest possible length of such an interior substring. If no character appears at least twice, no valid pair of endpoints exists, so return `-1`. An adjacent equal pair is valid and encloses an empty substring of length zero.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 300$.
- Every character of `s` is a lowercase English letter.

**Return value**

Return the maximum value of $j-i-1$ over indices $i<j$ for which `s[i] == s[j]`, or `-1` when no such pair exists.

### Examples
**Example 1**

- Input: `s = "aa"`
- Output: `0`

The equal characters are adjacent, so there is no character between them.

**Example 2**

- Input: `s = "abca"`
- Output: `2`

The two `a` characters enclose `"bc"`.

**Example 3**

- Input: `s = "cbzxy"`
- Output: `-1`

No character occurs twice.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce each character to its widest pair.** For a fixed character, any pair using an occurrence later than its first can only shorten the distance to a future matching endpoint. Therefore, once the first index of a character is known, every later occurrence should be compared with that same first index. The last occurrence automatically produces that character's widest span, though updating the answer at every repeat avoids needing a separate pass.

**Scan while preserving first indices.** Traverse `s` from left to right. When a character appears for the first time, store its index. On every repeat at index `j`, compute the number of enclosed characters as `j - first[character] - 1` and maximize the answer. Initialize the answer to `-1`; it remains unchanged exactly when the scan finds no repeated character.

For every character, the scan considers the pair from its earliest occurrence to each possible right endpoint, including its latest occurrence. That includes the widest pair for that character. Taking the maximum across all repeats therefore returns the widest valid interior substring across the whole string.

#### Complexity detail

The scan visits each of the $n$ characters once, so it takes $O(n)$ time. At most 26 first indices are stored because the alphabet is fixed to lowercase English letters; this is $O(1)$ auxiliary space with respect to $n$.

#### Alternatives and edge cases

- **First and last position arrays:** Record both extreme indices for each letter and compare them after the scan. This has the same $O(n)$ time and $O(1)$ space but stores information that the one-pass update does not need.
- **Enumerate every index pair:** Testing all $i<j$ is direct and correct, but it takes $O(n^2)$ time.
- **Repeated substring searches:** Searching for later copies of each character can be linear per starting position and therefore quadratic overall.
- A one-character string and a string of all distinct characters both return `-1`.
- Adjacent equal characters produce zero, which is distinct from the no-pair result.
- With three or more copies of one character, its first and last occurrences form its widest pair; intermediate copies must not replace the stored first index.

</details>
