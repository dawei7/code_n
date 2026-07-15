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

### Required Complexity

- **Time:** $O(m\log s)$
- **Space:** $O(v+s)$

<details>
<summary>Approach</summary>

#### General

**Separate the two ordering requirements.** Store each stack as a list inside an outer list. The outer list preserves stack indices and makes its final element the rightmost represented stack. A min-heap of non-full indices independently exposes the leftmost place where a push is allowed.

**Maintain the heap lazily.** Before a push, discard heap entries that now lie beyond the trimmed outer list or refer to a full stack. If no valid index remains, append a new empty stack and put its index into the heap. Push onto the heap's smallest-index stack, then remove that heap entry if the stack has reached `capacity`. A stack that changes from full to non-full during removal is inserted into the heap.

**Trim only the unused right boundary.** `popAtStack(index)` rejects an absent or empty stack; otherwise it removes that stack's top value and records newly available space when necessary. It then drops empty stacks only from the end of the outer list. Heap entries for those removed indices may remain temporarily, but the next push recognizes them as stale. `pop()` trims the same empty suffix and delegates to the current final stack, which is exactly the rightmost non-empty one.

The heap minimum therefore always yields the leftmost usable stack after stale entries are removed, and the trimmed list's last stack always yields the rightmost available value. These are precisely the two required choices.

#### Complexity detail

Each heap insertion or removal costs $O(\log s)$. Every stack trimmed from the right was previously created, so all trimming across $m$ operations costs $O(m)$ in total. Consequently the full operation sequence takes $O(m\log s)$ time. The stacks hold $v$ values, while the outer list and heap use $O(s)$ metadata, for $O(v+s)$ space.

#### Alternatives and edge cases

- **Scan stacks from the left on every push:** This is simple and correct, but a long run of full stacks makes one insertion $O(s)$ and the complete sequence quadratic.
- **Track only the rightmost stack:** That supports `pop()` but cannot find the leftmost hole created by `popAtStack` efficiently.
- **Capacity one:** Every push fills its stack immediately, and any successful removal empties one; the same heap and trimming rules still apply.
- **Hole in the middle:** Removing from a non-final stack must make its index available without renumbering any later stack.
- **Absent or empty index:** `popAtStack` returns `-1` and changes no state.
- **Empty suffix:** Several trailing empty stacks can be trimmed together, but empty stacks between non-empty ones must retain their indices.
- **Completely empty structure:** `pop()` returns `-1`, and the next push creates stack `0` again.

</details>
