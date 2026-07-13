# Partition Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 763 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-labels/) |

## Problem Description

### Goal

Given a string `s`, partition it into as many nonempty consecutive parts as possible so that each distinct letter appears in at most one part. Every character must belong to exactly one part, and the parts must preserve the string's original order.

Return a list containing the part lengths from left to right. A letter may occur several times inside its one assigned part, but no occurrence of that letter may appear in another part; maximizing the number of parts determines where valid cuts should be made.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase string.

**Return value**

- A list of positive partition lengths whose sum is `len(s)` and whose partitions do not share any letter.

### Examples

**Example 1**

- Input: `s = "ababcbacadefegdehijhklij"`
- Output: `[9,7,8]`
- Explanation: Each letter is confined to one of the three parts, and no valid partition can end earlier.

**Example 2**

- Input: `s = "eccbbbbdec"`
- Output: `[10]`
- Explanation: Occurrences link every position into one required partition.

**Example 3**

- Input: `s = "ynbi"`
- Output: `[1,1,1,1]`
- Explanation: Every character is unique, so every position can be its own part.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Precompute where every letter ends**

Record the final index of each character. While scanning a prospective partition, maintain `partition_end`, the farthest final occurrence of any character encountered in that partition. The partition cannot legally end before this boundary because doing so would place another occurrence of one of its letters in a later part.

**Close at the first reachable boundary**

At index `i`, extend `partition_end` with the current character's final index. When `i = partition_end`, every character seen since the current partition began has its last occurrence at or before `i`. Cutting there is therefore valid.

It is also optimal to cut immediately: every valid partition starting at the same position must include through `partition_end`, while extending past it would only merge a suffix that could remain separate. Thus each greedy cut is the earliest legal cut. Repeating this argument on the untouched suffix maximizes the total number of parts, and the recorded distances are exactly their lengths.

#### Complexity detail

The final-occurrence pass and greedy scan each take $O(n)$ time. Because the input alphabet is the fixed 26 lowercase letters, the last-position table uses $O(1)$ auxiliary space; the returned lengths are output space.

#### Alternatives and edge cases

- **Merge character intervals:** Treat each letter's first-to-last span as an interval and merge overlapping spans; this is also linear with a fixed alphabet but needs more bookkeeping.
- **Repeated suffix scans:** Searching for every encountered character's last occurrence without preprocessing is correct but can take $O(n^2)$ time.
- **Backtracking over cut positions:** It can test all valid partitions but explores unnecessary combinations because every earliest legal boundary is forced.
- **All characters unique:** Every partition has length one.
- **One repeated character:** Its occurrences force the entire string into one part.
- **Chain of overlapping spans:** Even characters that do not repeat can lie inside a partition extended by other letters.
- **Output accounting:** Partition lengths must be positive and sum to the full string length.

</details>
