# Swap For Longest Repeated Character Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1156 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) |

## Problem Description

### Goal

You are given a string `text` consisting only of lowercase English characters. You may swap two characters at any two positions in the string, or leave the string unchanged.

After using at most one swap, consider every substring whose characters are all the same. Return the greatest possible length of such a repeated-character substring. A swap only relocates characters already present in `text`; it cannot create another copy of the character used by the chosen substring.

### Function Contract

**Inputs**

- `text`: A lowercase English string of length $n$, where $1 \le n \le 2 \cdot 10^4$.

**Return value**

- The maximum length of a one-character substring obtainable after at most one swap.

### Examples

**Example 1**

- Input: `text = "ababa"`
- Output: `3`

**Example 2**

- Input: `text = "aaabaaa"`
- Output: `6`

**Example 3**

- Input: `text = "aaaaa"`
- Output: `5`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the available copies.** First count each lowercase character in the entire string. Any repeated-character substring made from a character `c` is capped by that global count: a swap can move an outside `c` into place, but it cannot increase how many copies exist.

**Examine one gap between equal runs.** Starting at a maximal run of one character, find its right boundary `j`. Then skip exactly the character at `j` and measure the immediately following run of the original character. If that second run exists, swapping the one-character gap with another copy joins the two runs. If it does not, an outside copy can still extend the first run by one. Both situations are captured by `min(left_run + right_run + 1, total[character])`.

Every useful swap has one of those forms. If it extends a single run, that run is examined at its start. If it joins two runs, they must be separated by exactly one different character, because one swap cannot remove a wider gap; the scan examines that pair when it starts at the left run. Taking the maximum capped candidate therefore covers every achievable answer. Advancing to `j` processes each original run once.

#### Complexity detail

Counting characters takes $O(n)$ time. The run pointers only move to the right, and each position participates in a constant number of scans, so the second phase is also $O(n)$. The frequency table has at most 26 entries and all pointers are scalar, giving $O(1)$ auxiliary space for the fixed lowercase alphabet.

#### Alternatives and edge cases

- **Try every swap:** Testing all position pairs and rescanning the result takes at least quadratic time and repeats equivalent choices.
- **Sliding window for every character:** Keeping at most one non-target character in a window is correct and still $O(n)$ because the alphabet has fixed size 26, but it scans the string once per possible target.
- **Ignore the global frequency cap:** This can claim a run was extended even when every copy of its character already lies inside the candidate region.
- **Gap wider than one:** One swap cannot make two equal-character runs contiguous when two or more intervening characters remain.
- **All characters equal:** No swap is needed, and the answer is the full string length.
- **Single occurrence:** A character appearing once can never form a repeated block longer than one.

</details>
