# Count Integers in Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2276 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Design, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-integers-in-intervals/) |

## Problem Description
### Goal
Design a data structure that starts with no intervals and supports a persistent
sequence of interval additions and coverage-count queries.

Calling `add(left, right)` inserts the inclusive interval `[left, right]`.
That interval represents every integer $x$ satisfying
$\texttt{left}\le x\le\texttt{right}$. Added intervals remain present for all
later operations. They may overlap, touch, contain one another, or duplicate
previous additions; an integer covered by several intervals is still counted
only once.

Calling `count()` returns the number of distinct integers contained in at
least one interval added so far. Implement `CountIntervals` so all operations
in the trace share the same state.

### Function Contract
**Inputs**

- `operations`: a list beginning with `"CountIntervals"`, followed by `"add"`
  and `"count"` method names
- `arguments`: argument lists aligned with `operations`; construction and
  `count` receive `[]`, while `add` receives `[left, right]`

Every added endpoint satisfies
$1\le\texttt{left}\le\texttt{right}\le10^9$. At most $10^5$ calls to `add`
and `count` occur in total, and at least one call is `count`.

Let $Q$ be the number of method calls after construction and let
$U=10^9$ be the inclusive coordinate-domain size.

**Return value**

Return one result per operation. Construction and `add` return `null`;
`count` returns the current number of distinct covered integers.

### Examples
**Example 1**

- Input: `operations = ["CountIntervals","add","add","count","add","count"]`,
  `arguments = [[],[2,3],[7,10],[],[5,8],[]]`
- Output: `[null,null,null,6,null,8]`

After the first two additions, `{2,3,7,8,9,10}` is covered. Adding `[5,8]`
expands the union to eight integers.

**Example 2**

- Input: `operations = ["CountIntervals","add","add","count"]`,
  `arguments = [[],[1,5],[2,4],[]]`
- Output: `[null,null,null,5]`

The nested interval adds no new integer.

**Example 3**

- Input: `operations = ["CountIntervals","add","add","count"]`,
  `arguments = [[],[1,1],[1000000000,1000000000],[]]`
- Output: `[null,null,null,2]`
