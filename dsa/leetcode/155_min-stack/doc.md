# Min Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Stack, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/min-stack/) |

## Problem Description
### Goal
Implement a stack of integers with the usual last-in, first-out behavior plus direct access to its current minimum. `push(val)` adds a value, `pop()` removes the most recently added remaining value, and `top()` returns that value without removing it.

`getMin()` must return the smallest value currently stored, including repeated minima that remain after only one copy is popped. Process the operation sequence in order and return one aligned result per call, using `None` for construction and mutating operations. All four methods must run in constant time; calls that inspect or remove a value are guaranteed to occur only when the stack is nonempty.

### Function Contract
**Inputs**

- `operations`: method names beginning with `MinStack`, followed by `push`, `pop`, `top`, and `getMin`
- `arguments`: one argument list per operation; only `push` receives an integer

**Return value**

A result list aligned with the operations: `None` for construction, push, and pop; the requested integer for top and getMin.

### Examples
**Example 1**

- Input: construct, `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`
- Output: `[null,null,null,null,-3,null,0,-2]`

**Example 2**

- Input: construct, `push(1)`, `getMin()`, `top()`
- Output: `[null,null,1,1]`

**Example 3**

- Input: push two equal minimum values and pop one
- Output: the remaining equal value is still the minimum

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Each stack entry snapshots the minimum for its complete prefix**

For every pushed value, store `(value, minimum_through_here)`. The first entry uses its own value as the minimum. Because stack pop always removes a suffix, the minimum snapshot beneath it immediately becomes correct again without recomputation.

**Push needs only the previous top snapshot**

When pushing $x$, read the current top minimum when present and store `min(x, current_min)`. All older values are already summarized by that single field. `top` returns the value field; `getMin` returns the minimum field.

**Duplicated minima are represented independently at every depth**

At every position, the stored minimum equals the minimum of values from the bottom through that entry. Equal minimum values create separate entries with the same snapshot, so popping one copy still exposes another correct minimum.

**Trace a minimum being popped**

After pushes `-2, 0, -3`, snapshots are `-2, -2, -3`. Popping `-3` exposes the entry `(0,-2)`, so the minimum returns to `-2` in constant time without scanning.

**Each entry carries the minimum of its entire prefix**

For every stored pair `(value, prefix_min)`, `prefix_min` is the smallest value from the bottom of the stack through that entry. A push preserves this property by recording the smaller of the new value and the previous top's minimum. A pop removes one complete prefix snapshot, so the newly exposed pair already contains the minimum of the shortened stack.

Consequently `top` reads the current value and `getMin` reads the current prefix minimum without any search.

#### Complexity detail

Each operation performs a fixed number of list and comparison operations, so all are $O(1)$. One pair is stored per stack value, giving $O(n)$ space.

#### Alternatives and edge cases

- **Compute the minimum on demand:** Evaluating `min(stack)` makes `getMin` take $O(n)$ time and violates the contract.
- **Separate minimum stack:** has the same asymptotic bounds and can store only new minima, but synchronized duplicate handling needs care.
- **Encode differences in one integer stack:** can reduce fields but is less transparent and risks fixed-width overflow in some languages.
- Repeated minima must survive until every copy is popped. Values may be negative.
- Valid operation sequences never call `pop`, `top`, or `getMin` on an empty stack; a broader API would need explicit error behavior.

</details>
