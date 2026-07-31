# Frequency Tracker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2671 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/frequency-tracker/) |

## Problem Description

### Goal

Design a `FrequencyTracker` that begins empty and maintains a multiset of integers. It must support adding one occurrence of a number, deleting one occurrence when that number is present, and leaving the state unchanged when deletion targets an absent number.

It must also answer whether at least one stored number currently occurs exactly a requested positive number of times. The query concerns the frequency of some value, not how many total elements are stored.

### Function Contract

**Inputs**

- `operations`: A sequence containing `FrequencyTracker`, `add`, `deleteOne`, and `hasFrequency` operations.
- `arguments`: The corresponding argument list for every operation. Numbers and queried frequencies are between $1$ and $10^5$, and the complete sequence contains at most $2 \cdot 10^5$ method calls.

The first operation constructs an empty tracker. Each `add` or `deleteOne` receives one number; each `hasFrequency` receives one positive frequency.

**Return value**

- Return one result per operation: `null` for construction and mutations, and a Boolean for each `hasFrequency` query.

### Examples

**Example 1**

- Input: `operations = ["FrequencyTracker","add","add","hasFrequency"]`, `arguments = [[],[3],[3],[2]]`
- Output: `[null,null,null,true]`
- Explanation: After adding `3` twice, some number has frequency two.

**Example 2**

- Input: `operations = ["FrequencyTracker","add","deleteOne","hasFrequency"]`, `arguments = [[],[1],[1],[1]]`
- Output: `[null,null,null,false]`
- Explanation: Deleting the only occurrence of `1` leaves the tracker empty.

**Example 3**

- Input: `operations = ["FrequencyTracker","hasFrequency","add","hasFrequency"]`, `arguments = [[],[2],[3],[1]]`
- Output: `[null,false,null,true]`
- Explanation: No frequency exists initially; after adding `3`, frequency one exists.
