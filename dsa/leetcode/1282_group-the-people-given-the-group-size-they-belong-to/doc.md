# Group the People Given the Group Size They Belong To

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1282 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |

## Problem Description
### Goal
There are $n$ people with unique identifiers from $0$ through $n-1$, partitioned into groups whose membership is not yet known. The array `groupSizes` describes the required group of every person: `groupSizes[i]` is exactly the number of people that must be in the same group as person `i`.

Construct a grouping that contains every person exactly once and makes the size of each person's group equal to that person's requested value. A valid grouping is guaranteed to exist. The ordering of groups and the ordering of people within them are unrestricted, so any valid answer may be returned.

### Function Contract
**Inputs**

- `groupSizes`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{groupSizes[i]} \le n$.

**Return value**

A list of groups. Every index from $0$ through $n-1$ must occur exactly once, and each returned group must contain exactly `groupSizes[i]` people for every member `i` of that group.

### Examples
**Example 1**

- Input: `groupSizes = [3,3,3,3,3,1,3]`
- Output: `[[5],[0,1,2],[3,4,6]]`
- Explanation: Person 5 forms the required singleton; the other six people form two groups of three.

**Example 2**

- Input: `groupSizes = [2,1,3,3,3,2]`
- Output: `[[1],[0,5],[2,3,4]]`

**Example 3**

- Input: `groupSizes = [1,1,1]`
- Output: `[[0],[1],[2]]`
- Explanation: Each request for size one must become a separate group.
