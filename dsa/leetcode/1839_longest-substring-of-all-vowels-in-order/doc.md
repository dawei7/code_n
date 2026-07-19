# Longest Substring Of All Vowels in Order

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) |
| Frontend ID | 1839 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A string is beautiful when it contains each of the five vowels `a`, `e`, `i`, `o`, and `u` at least once, and its characters are in alphabetical order. Thus all `a` characters precede all `e` characters, which precede all `i`, `o`, and `u` characters in that order.

Given `word`, a string containing only those five lowercase vowels, return the length of its longest contiguous beautiful substring. Repeated copies within a vowel group are allowed. If no substring contains all five groups in the required order, return 0.

### Function Contract

**Inputs**

- `word`: a string of $n$ characters drawn only from `a`, `e`, `i`, `o`, and `u`, where $1 \le n \le 5\cdot10^5$.

**Return value**

- Return the greatest length of a contiguous substring whose characters are non-decreasing and include all five vowels.
- Return 0 when no such substring exists.

### Examples

**Example 1**

- Input: `word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"`
- Output: `13`

The longest beautiful substring is `"aaaaeiiiiouuu"`.

**Example 2**

- Input: `word = "aeeeiiiioooauuuaeiou"`
- Output: `5`

The descending transition from `o` to `a` resets the first run; the final `"aeiou"` is beautiful.

**Example 3**

- Input: `word = "a"`
- Output: `0`

Four required vowel groups are absent.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat each non-decreasing run as one candidate region**

Scan adjacent characters. A strict decrease such as `u` followed by `a` makes every substring crossing that boundary invalid, so reset the current run length to 1 and its distinct-group count to 1. Equal adjacent vowels extend the current group, while a strict increase extends the run and begins one new vowel group.

Because `word` contains only the five ordered vowels, a non-decreasing run can change character at most four times. Reaching five distinct groups means it started with `a` and encountered `e`, `i`, `o`, and `u` in order without skipping one.

**Measure a run only after all groups appear**

Track the current run length from its most recent decrease. Whenever its group count is five, the full current run is beautiful. Update the maximum on every later character as well, because additional `u` characters continue extending the same valid substring.

If a run skips a vowel, it cannot reach five groups: there are only five possible vowel values. If it decreases, resetting discards exactly the prefixes that no longer can participate in an ordered substring.

**Why the scan finds the longest substring**

Every beautiful substring lies entirely inside one maximal non-decreasing run. Within such a run, once all five groups have appeared, taking the substring from the run's beginning through the current position is at least as long as any beautiful suffix ending there and remains valid. The algorithm evaluates that maximal candidate at every endpoint, so the largest recorded length equals the longest beautiful substring.

#### Complexity detail

The scan examines each of the $n$ characters once and performs constant work, giving $O(n)$ time. The run length, group count, and best length use $O(1)$ space.

#### Alternatives and edge cases

- **Start a scan at every position:** Incrementally checking ordered vowel groups is correct but takes $O(n^2)$ time on a fully ordered word.
- **Split on every descending pair:** Processing the resulting non-decreasing runs separately is also linear, but the direct scan avoids constructing substrings.
- **Count vowels globally:** Global counts ignore contiguity and order, so they cannot identify a beautiful substring.
- **Exactly `"aeiou"`:** This is the shortest possible beautiful substring, of length 5.
- **Missing vowel:** A run with fewer than five distinct groups is not beautiful regardless of length.
- **Skipped vowel:** A transition such as `a` to `i` prevents that run from accumulating all five groups.
- **Repeated vowels:** Equal adjacent characters extend the run without increasing the group count.
- **Descending transition:** Reset at the later character; no valid ordered substring can cross the decrease.
- **Multiple valid runs:** Keep the maximum rather than returning the first.
- **Only one vowel value:** Return zero even for a very long word.

</details>
