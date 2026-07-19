# Dinner Plate Stacks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1172 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Stack, Design, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/dinner-plate-stacks/) |

## Problem Description

### Goal

Imagine an infinite row of stacks numbered from `0` toward the right. Every stack has the same maximum `capacity`. Design `DinnerPlates` so that inserting a value always uses the leftmost stack whose size is less than `capacity`, while an ordinary removal uses the rightmost non-empty stack.

The structure must also support removing the top value from one explicitly indexed stack. Both removal operations return `-1` when their requested source does not contain a value: `pop()` does so when every stack is empty, and `popAtStack(index)` does so when that indexed stack is empty or absent.

### Function Contract

**Inputs**

- `capacity`: The maximum number of values in every stack, with $1 \leq \texttt{capacity} \leq 2\times 10^4$.
- `operations`: A sequence of at most $2\times 10^5$ calls represented as `[method, arguments]` pairs. A pushed `val` satisfies $1 \leq \texttt{val} \leq 2\times 10^4$, and a requested `index` satisfies $0 \leq \texttt{index} \leq 10^5$.
- Let $m$ be the number of operations, $s$ the number of represented stacks, and $v$ the number of stored values.

**Operations**

- `push(val)`: Add `val` to the leftmost stack whose size is below `capacity`; create a new stack to the right when all existing stacks are full.
- `pop()`: Remove and return the top value of the rightmost non-empty stack, or return `-1` if no value exists.
- `popAtStack(index)`: Remove and return the top value of stack `index`, or return `-1` if that stack is empty or absent.

**Return value**

- One result per operation in input order. A `push` result is `None`; each removal result is the removed integer or `-1`.

### Examples

**Example 1**

- Input: `capacity = 2`, `operations = [["push",[1]],["push",[2]],["push",[3]],["push",[4]],["push",[5]],["popAtStack",[0]],["push",[20]],["push",[21]],["popAtStack",[0]],["popAtStack",[2]],["pop",[]],["pop",[]],["pop",[]],["pop",[]],["pop",[]]]`
- Output: `[null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]`

After the first five pushes the stacks are `[1,2]`, `[3,4]`, and `[5]`. Removing `2` opens space in stack `0`, so the next push places `20` there before a later push uses stack `2`.

**Example 2**

- Input: `capacity = 1`, `operations = [["pop",[]]]`
- Output: `[-1]`

**Example 3**

- Input: `capacity = 1`, `operations = [["push",[7]],["popAtStack",[3]],["pop",[]]]`
- Output: `[null,-1,7]`
