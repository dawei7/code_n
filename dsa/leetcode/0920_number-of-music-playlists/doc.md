# Number of Music Playlists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 920 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Combinatorics |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-music-playlists/) |

## Problem Description
### Goal

A music player contains $n$ different songs. Build a playlist of exactly `goal` plays for a trip; the same song may appear more than once, but every one of the $n$ songs must be played at least once.

To limit repetition, a song may be played again only after at least $k$ other songs have been played since its previous occurrence. Count all distinct playlists satisfying both rules and return the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of different songs.
- `goal`: the required playlist length.
- `k`: the number of other songs that must separate two plays of the same song.
- The values satisfy $0 \le k<n\le \textit{goal}\le100$.

**Return value**

The number of length-`goal` playlists that use every song at least once and respect the replay separation, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 3, goal = 3, k = 1`
- Output: `6`
- Explanation: Every valid playlist is one of the $3!$ orders of the three songs.

**Example 2**

- Input: `n = 2, goal = 3, k = 0`
- Output: `6`
- Explanation: Immediate repetition is allowed, but both songs must appear.

**Example 3**

- Input: `n = 2, goal = 3, k = 1`
- Output: `2`
- Explanation: The only possibilities alternate the two songs.
