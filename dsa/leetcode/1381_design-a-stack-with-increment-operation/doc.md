# Design a Stack With Increment Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/design-a-stack-with-increment-operation/) |

## Problem Description

### Goal

Design a stack with a fixed maximum capacity. It supports ordinary `push` and `pop` operations together with an operation that adds a value to the bottom part of the current stack.

A push adds a value only when the stack is not full; otherwise it changes nothing. A pop removes and returns the top value, or returns `-1` when the stack is empty. An `increment(k, val)` call adds `val` to each of the bottom `min(k, current size)` elements.

### Function Contract

**Inputs**

- `max_size`: the positive stack capacity supplied to the constructor.
- `operations`: at most $1000$ calls encoded as `[method, args]` pairs, where `method` is `push`, `pop`, or `increment`.

**Return value**

- A list containing each method result in call order. `push` and `increment` contribute `null`; `pop` contributes the removed value or `-1`.

### Examples

**Example 1**

- Input: `max_size = 2, operations = [["push",[1]],["push",[2]],["pop",[]]]`
- Output: `[null,null,2]`

**Example 2**

- Input: `max_size = 3, operations = [["push",[1]],["push",[2]],["increment",[2,5]],["pop",[]]]`
- Output: `[null,null,null,7]`

**Example 3**

- Input: `max_size = 1, operations = [["pop",[]]]`
- Output: `[-1]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(	exttt{maxSize})$

<details>
<summary>Approach</summary>

#### General

**Attach deferred work to stack depths.** Store the pushed values normally and keep a parallel `increments` array. Entry `i` represents an addition that applies to every value from the bottom through depth `i`.

For `increment(k, val)`, find the deepest affected index, `min(k, size) - 1`, and add `val` only to that increment marker. No stored value needs to be changed immediately.

When popping depth `i`, add its marker to the stored value. If a lower element remains, propagate the same marker to depth `i - 1`, because every deferred increment covering the popped element also covered all elements below it. This transfers each marker downward exactly when needed and ensures a later pop receives every increment that included its depth.

A push appends a zero marker, so increments issued before that push never affect the new value. A full-stack push is ignored, and an empty pop returns `-1`, preserving the bounded-stack contract.

#### Complexity detail

Each `push`, `pop`, and `increment` performs constant work, so every operation takes $O(1)$ time. The values and deferred markers contain at most `maxSize` entries, using $O(\texttt{maxSize})$ space.

#### Alternatives and edge cases

- **Update values eagerly:** Add `val` directly to the bottom `k` entries. It is simple and correct but takes $O(k)$ time per increment.
- **Difference array without pop propagation:** Range markers can encode increments, but they must be accumulated in the correct direction when values are removed.
- **Push at capacity:** Ignore the value without changing either internal array.
- **Pop when empty:** Return `-1` and leave deferred state empty.
- **Increment beyond current size:** Affect every stored element, not nonexistent capacity slots.
- **Increment an empty stack:** Do nothing; no marker should be retained for future pushes.
- **Overlapping increments:** Markers add together and propagate, so each popped value receives precisely the operations whose bottom ranges covered it.

</details>
