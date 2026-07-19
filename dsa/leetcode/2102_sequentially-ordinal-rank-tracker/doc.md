# Sequentially Ordinal Rank Tracker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2102 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Design, Heap (Priority Queue), Data Stream, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/) |

## Problem Description

### Goal

Maintain a growing collection of scenic locations. Each location has a unique lowercase `name` and an attractiveness `score`. A higher score ranks better; when scores are equal, the lexicographically smaller name ranks better.

The tracker starts empty and supports adding locations one at a time. On the $i$th call to `get`, return the $i$th best location among every location added so far. New additions may change the ranking before later queries. The operation sequence always contains at least as many additions as queries at every prefix.

### Function Contract

Let $m$ be the number of locations added so far.

**Operations**

- `SORTracker()`: initialize an empty tracker.
- `add(name, score)`: add a location whose unique name has length from $1$ through $10$ and whose score satisfies $1 \le \texttt{score} \le 10^5$.
- `get()`: on its $i$th invocation, return the name of the location currently ranked $i$th.

At most $4 \cdot 10^4$ total calls to `add` and `get` are made.

**Return value**

Construction and `add` return no value. Each `get` returns the requested location name.

### Examples

**Example 1**

- Operations: `["SORTracker","add","add","get","add","get","add","get","add","get","add","get","get"]`
- Arguments: `[[],["bradford",2],["branford",3],[],["alps",2],[],["orland",2],[],["orlando",3],[],["alpine",2],[],[]]`
- Output: `[null,null,null,"branford",null,"alps",null,"bradford",null,"bradford",null,"bradford","orland"]`

**Example 2**

- Operations: `["SORTracker","add","get","add","get"]`
- Arguments: `[[],["zoo",5],[],["alpha",5],[]]`
- Output: `[null,null,"zoo",null,"zoo"]`
- Explanation: After the second addition, `"alpha"` ranks first, so the second query returns the second-ranked `"zoo"`.
