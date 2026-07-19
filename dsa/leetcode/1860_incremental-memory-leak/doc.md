# Incremental Memory Leak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1860 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/incremental-memory-leak/) |

## Problem Description
### Goal
Two memory sticks initially have `memory1` and `memory2` available bits. A
faulty program requests an increasing allocation every second: at second $i$,
it needs exactly $i$ bits. The request is taken from the stick with more
available memory at that moment; when both sticks are equal, the first stick is
chosen.

The program crashes at the first second when neither stick contains enough
available bits for that second's request. Return the crash time together with
the unused memory remaining on the first and second sticks at that instant.

### Function Contract
**Inputs**

- `memory1`: the first stick's initial available memory, from $0$ through
  $2^{31}-1$ bits.
- `memory2`: the second stick's initial available memory over the same range.

Let $M = \texttt{memory1} + \texttt{memory2}$ denote the initial total memory.

**Return value**

An integer array `[crashTime, memory1Crash, memory2Crash]`, preserving the
first-stick/second-stick order of the two remaining-memory values.

### Examples
**Example 1**

- Input: `memory1 = 2, memory2 = 2`
- Output: `[3,1,0]`

The requests of one and two bits use the first and second sticks respectively;
neither can supply the three-bit request.

**Example 2**

- Input: `memory1 = 8, memory2 = 11`
- Output: `[6,0,4]`

**Example 3**

- Input: `memory1 = 0, memory2 = 0`
- Output: `[1,0,0]`
