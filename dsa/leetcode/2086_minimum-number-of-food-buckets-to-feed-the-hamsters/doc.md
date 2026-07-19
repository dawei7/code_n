# Minimum Number of Food Buckets to Feed the Hamsters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2086 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/) |

## Problem Description

### Goal

A zero-indexed street is represented by `hamsters`. Each `"H"` marks a hamster, while each `"."` marks an empty position where a food bucket may be placed. A hamster at index $i$ is fed when a bucket occupies at least one adjacent position, $i-1$ or $i+1$; buckets cannot be placed on hamster positions.

Choose empty positions so that every hamster is fed, and return the minimum number of buckets used. One bucket between two hamsters may feed both of them. If no placement can feed every hamster, return `-1`.

### Function Contract

**Input**

- `hamsters`: a string of length $n$, where $1 \le n \le 10^5$ and every character is either `"H"` or `"."`.

**Return value**

Return the minimum number of buckets needed to feed all hamsters, or `-1` when a valid placement does not exist.

### Examples

**Example 1**

- Input: `hamsters = "H..H"`
- Output: `2`
- Explanation: Buckets at indices `1` and `2` feed the two endpoint hamsters.

**Example 2**

- Input: `hamsters = ".H.H."`
- Output: `1`
- Explanation: A bucket at index `2` is adjacent to both hamsters.

**Example 3**

- Input: `hamsters = ".HHH."`
- Output: `-1`
- Explanation: The middle hamster has no adjacent empty position.
