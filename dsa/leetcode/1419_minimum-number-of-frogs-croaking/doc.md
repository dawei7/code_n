# Minimum Number of Frogs Croaking

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1419 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-number-of-frogs-croaking/) |

## Problem Description

### Goal

Each frog repeatedly produces the five-character sound `"croak"` in that exact order, emitting one character at a time. The input `croakOfFrogs` is the chronological interleaving of all characters heard from some number of frogs, so different frogs' sounds may overlap.

Determine the minimum number of frogs that could produce the complete recording. Every participating sound must form a full `"croak"`; if the sequence cannot be partitioned into ordered, complete frog sounds, return `-1`.

### Function Contract

**Inputs**

- `croakOfFrogs`: a string of length $n$, where $1 \le n \le 10^5$, containing characters from `"croak"`.

**Return value**

- The minimum number of simultaneously available frogs needed to produce the recording, or `-1` if the recording is invalid.

### Examples

**Example 1**

- Input: `croakOfFrogs = "croakcroak"`
- Output: `1`

**Example 2**

- Input: `croakOfFrogs = "crcoakroak"`
- Output: `2`

**Example 3**

- Input: `croakOfFrogs = "croakcrook"`
- Output: `-1`
