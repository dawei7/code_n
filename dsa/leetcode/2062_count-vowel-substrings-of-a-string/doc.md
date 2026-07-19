# Count Vowel Substrings of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2062 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) |

## Problem Description

### Goal

A substring is a nonempty contiguous sequence of characters. Call a substring a vowel substring when every one of its characters is a vowel—`a`, `e`, `i`, `o`, or `u`—and all five different vowels occur at least once.

Given a lowercase English string `word`, return the number of its vowel substrings. Count different index ranges separately even when they contain the same text.

### Function Contract

**Inputs**

- `word`: a lowercase English string of length $n$, where $1 \le n \le 100$.

**Return value**

- Return the number of nonempty contiguous substrings that contain only vowels and include all five vowels.

### Examples

**Example 1**

- Input: `word = "aeiouu"`
- Output: `2`
- Explanation: The ranges spelling `"aeiou"` and `"aeiouu"` both satisfy the two conditions.

**Example 2**

- Input: `word = "unicornarihan"`
- Output: `0`
- Explanation: No all-vowel range contains all five distinct vowels.

**Example 3**

- Input: `word = "cuaieuouac"`
- Output: `7`
- Explanation: Seven contiguous ranges stay within the central vowel run and contain every vowel.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A consonant fixes the earliest legal boundary**

Scan `word` from left to right. Remember the index of the most recent consonant. Any all-vowel substring ending at the current position must start after that index, so a consonant discards every earlier candidate start at once.

**The least recent vowel controls completeness**

For each of the five vowels, store its latest index. At a vowel position, let $p$ be the minimum of those five indices. When $p$ lies after the latest consonant, every start from one position after that consonant through $p$ produces an all-vowel substring containing all five vowels. There are exactly `p - last_consonant` such starts, so add that quantity to the answer.

Every valid substring is counted at its right endpoint. Its start must be after the latest consonant, and it cannot pass the least recent last occurrence among the five required vowels. Conversely, every start in that interval includes each vowel and no consonant. The scan therefore counts every valid index range exactly once.

#### Complexity detail

The scan processes each of the $n$ characters once. Taking the minimum of five stored indices is constant work, so the total time is $O(n)$. The latest positions of five vowels and a few counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every start position:** Extending each all-vowel range and tracking its vowels is straightforward, but it can require $O(n^2)$ time.
- **Two at-most counts:** Within each vowel-only segment, subtract substrings containing at most four distinct vowels from those containing at most five; this is also linear but uses more sliding-window bookkeeping.
- A consonant resets the allowable start range even if all five vowels appeared earlier.
- Repeated copies of a vowel create additional valid starts or endings and must count as separate index ranges.
- Strings shorter than five characters, and strings missing any one vowel, contribute zero.

</details>
