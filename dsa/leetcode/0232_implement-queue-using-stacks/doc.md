# Implement Queue using Stacks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Design, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) |

## Problem Description
### Goal
Implement a first-in, first-out queue while using only stack-style storage operations. `push(x)` adds an integer at the back, `pop()` removes and returns the oldest remaining value at the front, and `peek()` returns that front value without removing it.

`empty()` reports whether the queue currently contains no values. Process all commands against one persistent queue state and return aligned operation results, using `null` for pushes. Calls that inspect or remove a front value occur only when the queue is nonempty. Internally, use only ordinary stack actions such as pushing, popping, top inspection, size, and emptiness rather than substituting a native queue.

### Function Contract
**Inputs**

- `operations`: method names chosen from `push`, `pop`, `peek`, and `empty`
- `values`: the corresponding pushed integer, or `null` for an operation with no argument

**Return value**

The result of every operation in order: `null` for `push`, the affected value for `pop` or `peek`, and a boolean for `empty`.

### Examples
**Example 1**

- Input: `operations = ["push","push","peek","pop","empty"], values = [1,2,null,null,null]`
- Output: `[null,null,1,1,false]`

**Example 2**

- Input: `operations = ["empty","push","pop","empty"], values = [null,7,null,null]`
- Output: `[true,null,7,true]`

**Example 3**

- Input: `operations = ["push","peek","peek"], values = [4,null,null]`
- Output: `[null,4,4]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Give each stack one direction**

Push new values onto an input stack. Read queue-front values from an output stack. When the output stack is empty and a front value is needed, move every input value to the output stack, reversing their order.

**The two stacks form one logical queue**

From queue front to back, the logical contents are the output stack from top to bottom followed by the input stack from bottom to top. A transfer preserves that order while making the oldest available item the output top.

**Move values only when the output side is empty**

Do not move values while the output stack still contains older items. Consequently, each enqueued value moves from input to output at most once and is popped once.

New items remain behind all items already in the output stack. When a transfer is required, reversing the input stack places its earliest pushed value on top. Thus `peek` and `pop` always select the globally earliest unremoved item, exactly matching FIFO behavior.

#### Complexity detail

Each value participates in a constant number of stack operations over its lifetime, so operations are $O(1)$ amortized; an individual transfer can take $O(n)$. Stored queue values occupy $O(n)$ space.

#### Alternatives and edge cases

- **Transfer on every push:** preserves FIFO order but costs $O(n)$ per insertion.
- **One dynamic-array stack with front deletion:** violates the intended stack-operation model and front deletion is linear.
- `empty` is true only when both stacks are empty; valid `pop` and `peek` calls occur only on non-empty queues.

</details>
