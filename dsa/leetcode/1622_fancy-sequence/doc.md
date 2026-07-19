# Fancy Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1622 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Design, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fancy-sequence/) |

## Problem Description
### Goal
Implement a mutable `Fancy` sequence that starts empty. `append(val)` places a new value at the end. `addAll(inc)` adds `inc` to every value already present, and `multAll(m)` multiplies every value already present by `m`. Operations performed before an append do not affect the newly appended value.

`getIndex(idx)` returns the current zero-based value at `idx`, reduced modulo $10^9+7$; it returns `-1` when `idx` is outside the sequence. At most $10^5$ total method calls are made, so operations that rewrite every stored value cannot meet the required scaling.

### Function Contract
**Inputs**

- `operations`: a source-native trace beginning with `Fancy`, followed by method names `append`, `addAll`, `multAll`, or `getIndex`.
- `arguments`: one argument list for each operation. Constructor arguments are empty; other values satisfy $1 \le \texttt{val},\texttt{inc},m \le 100$, and $0 \le \texttt{idx} \le 10^5$.
- Let $Q \le 10^5$ be the number of trace operations, $A$ the number of appended values, and $M=10^9+7$.

**Return value**

Return the trace result list: `null` for construction and mutating calls, the current residue for a valid `getIndex`, and `-1` for an out-of-range index.

### Examples
**Example 1**

- Input: `operations = ["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]`, `arguments = [[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]`
- Output: `[null,null,null,null,null,10,null,null,null,26,34,20]`

**Example 2**

- Input: `operations = ["Fancy","getIndex"]`, `arguments = [[],[0]]`
- Output: `[null,-1]`

**Example 3**

- Input: `operations = ["Fancy","addAll","append","getIndex"]`, `arguments = [[],[5],[2],[0]]`
- Output: `[null,null,null,2]`
