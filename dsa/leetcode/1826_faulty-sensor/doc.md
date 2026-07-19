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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Ignore the shared prefix**

Advance to the first index where the sensors differ. The failure cannot be identified before this point because both arrays record the same values there. If no mismatch exists, either sensor could explain the data, so return `-1`.

**Test both possible one-position shifts**

If sensor 1 is faulty, each `sensor1[i]` from the first mismatch through the penultimate position must equal `sensor2[i + 1]`. Test this alignment across the suffix. Symmetrically, sensor 2 is a valid explanation when `sensor2[i] == sensor1[i + 1]` throughout that range. The final value of the purported faulty sensor is deliberately ignored because it is arbitrary.

**Resolve only a unique explanation**

Return a sensor number only when its alignment succeeds and the other alignment fails. If both succeed, the repeated values make either sensor consistent with the fault. If the first mismatch is only at the last position, the tested suffix is empty and both hypotheses likewise remain possible.

#### Complexity detail

The shared-prefix scan and the two simultaneous suffix checks each inspect at most $n$ positions, so time is $O(n)$. Boolean hypothesis flags and indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every failure position:** Reconstructing and comparing both shifted arrays for every candidate position is correct but can take $O(n^2)$ time.
- **Slice comparison:** Comparing `sensor1[i:-1]` with `sensor2[i+1:]` is concise and linear, but allocates $O(n)$ temporary space.
- **Identical arrays:** Return `-1`; the arbitrary replacement can preserve all observed values.
- **Mismatch only at the last index:** No shifted pair remains to test, so the result is ambiguous.
- **Repeated readings:** They can allow both directional alignments and require `-1`.
- **Failure at the first position:** The shared prefix is empty, but the same suffix checks apply.
- **Arbitrary last reading:** Never use the purported faulty sensor's final entry as alignment evidence.

</details>
