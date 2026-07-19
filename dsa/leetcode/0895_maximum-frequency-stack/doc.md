# Maximum Frequency Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 895 |
| Difficulty | Hard |
| Topics | Hash Table, Stack, Design, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-stack/) |

## Problem Description
### Goal
Design a stack-like data structure that accepts pushed integers and removes elements according to frequency rather than only by physical top position.

An empty `FreqStack` supports two operations. Calling `push(val)` places `val` onto the stack. Calling `pop()` removes and returns a value whose current occurrence count in the stack is greatest. If several values share that maximum frequency, remove the tied value closest to the stack's top, meaning the one pushed most recently among those candidates.

The input sequence always leaves at least one element available before every `pop()` call.

### Function Contract
Let $q$ be the total number of `push` and `pop` calls in one operation sequence.

**Operations**

- `FreqStack()`: construct an empty frequency stack.
- `push(val)`: add `val` to the top, where $0 \leq \texttt{val} \leq 10^9$.
- `pop()`: remove and return the most frequent current value, breaking frequency ties by proximity to the top.
- At most $2 \cdot 10^4$ operations are issued, and every `pop()` is valid.

**App-local input**

- `operations`: the calls after construction, encoded as `["push", val]` or `["pop"]`.

**Return value**

Return the result trace: `None` for each `push` and the removed integer for each `pop`.

### Examples
**Example 1**

- Input: `operations = [["push",5],["push",7],["push",5],["push",7],["push",4],["push",5],["pop"],["pop"],["pop"],["pop"]]`
- Output: `[null,null,null,null,null,null,5,7,5,4]`

The first `pop()` returns `5` because it occurs three times. The next call sees `5` and `7` tied at frequency two and returns `7`, whose latest remaining occurrence is closer to the top. After another `5` is removed, `4`, `5`, and `7` are tied, so the most recently pushed value `4` is returned.

**Example 2**

- Input: `operations = [["push",9],["pop"]]`
- Output: `[null,9]`

**Example 3**

- Input: `operations = [["push",2],["push",1],["push",2],["push",1],["pop"],["pop"]]`
- Output: `[null,null,null,null,1,2]`
