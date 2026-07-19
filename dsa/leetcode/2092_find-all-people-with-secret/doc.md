# Find All People With Secret

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2092 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-all-people-with-secret/) |

## Problem Description

### Goal

There are $n$ people numbered from `0` through `n - 1`. Each meeting `[x, y, time]` connects people `x` and `y` at that time, and a person may participate in several simultaneous meetings. Person `0` knows a secret and shares it with `firstPerson` at time `0`.

Whenever a meeting occurs, either participant who already knows the secret shares it with the other. Sharing is instantaneous: someone may learn the secret in one meeting and pass it through another meeting at the same time. Process all meetings according to time and return every person who eventually knows the secret, in any order.

### Function Contract

**Inputs**

- `n`: the number of people, where $2 \le n \le 10^5$.
- `meetings`: $M$ triples `[x, y, time]`, where $1 \le M \le 10^5$.
- Each meeting joins two different valid people at a time from $1$ through $10^5$.
- `firstPerson`: a person from `1` through `n - 1` who learns the secret at time `0`.

**Return value**

Return all people who know the secret after every meeting. The order of the returned identifiers does not matter.

### Examples

**Example 1**

- Input: `n = 6`, `meetings = [[1,2,5],[2,3,8],[1,5,10]]`, `firstPerson = 1`
- Output: `[0,1,2,3,5]`
- Explanation: Knowledge passes from `1` to `2`, later to `3`, and from `1` to `5`.

**Example 2**

- Input: `n = 4`, `meetings = [[3,1,3],[1,2,2],[0,3,3]]`, `firstPerson = 3`
- Output: `[0,1,3]`
- Explanation: The time-`2` meeting cannot transmit retroactively. At time `3`, people `0`, `3`, and `1` are connected.

**Example 3**

- Input: `n = 5`, `meetings = [[3,4,2],[1,2,1],[2,3,1]]`, `firstPerson = 1`
- Output: `[0,1,2,3,4]`
- Explanation: At time `1`, person `2` learns and immediately passes the secret to `3`.
