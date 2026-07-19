# Faulty Sensor

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/faulty-sensor/) |
| Frontend ID | 1826 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two sensors were intended to record the same sequence. One sensor failed: at some position it omitted the correct reading, every later correct reading shifted one position left in that sensor's array, and an unrelated value was placed in its final position so both recorded arrays still have equal length. Before the omission, the recordings agree.

Given `sensor1` and `sensor2`, determine which sensor's sequence exhibits that shift. Return `1` when only sensor 1 can be faulty, `2` when only sensor 2 can be faulty, or `-1` when the evidence cannot distinguish the two explanations. The arbitrary final value may accidentally preserve ambiguity.

### Function Contract

**Inputs**

- `sensor1` and `sensor2`: equal-length integer arrays representing the two recordings.
- Their common length is at most 100, and recorded values are positive integers at most 100.
- The input is consistent with the stated single-fault process, although the faulty sensor may be impossible to identify uniquely.
- Let $n$ be the common length.

**Return value**

- Return `1` if only sensor 1's suffix is shifted, `2` if only sensor 2's suffix is shifted, or `-1` if both explanations remain possible.

### Examples

**Example 1**

- Input: `sensor1 = [2,3,4,5], sensor2 = [2,1,3,4]`
- Output: `1`

After the first mismatch, `sensor1`'s values `[3,4]` align with `sensor2` one position later.

**Example 2**

- Input: `sensor1 = [2,1,3,4], sensor2 = [2,3,4,5]`
- Output: `2`

This is the reversed directional case.

**Example 3**

- Input: `sensor1 = [2,2,2,2,2], sensor2 = [2,2,2,2,5]`
- Output: `-1`

The final arbitrary reading is the first mismatch, so neither shift direction is distinguishable.
