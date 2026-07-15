# Validate Stack Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 946 |
| Difficulty | Medium |
| Topics | Array, Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/validate-stack-sequences/) |

## Problem Description

### Goal

Two integer arrays, `pushed` and `popped`, contain the same distinct values. Starting with an empty stack, values must be pushed in exactly the order listed by `pushed`, while pop operations may be interleaved with those pushes.

Determine whether some legal sequence of stack pushes and pops could produce the values in exactly the order listed by `popped`. Return `true` when that pop order is possible and `false` otherwise; every pushed value must eventually account for one value in the proposed pop sequence.

### Function Contract

Let $n$ be the common length of `pushed` and `popped`.

**Inputs**

- `pushed`: a list of $n$ distinct integers with $1 \le n \le 1000$ and values from $0$ through $1000$.
- `popped`: a permutation of `pushed` describing the proposed pop order.

**Return value**

Return `true` if an initially empty stack can follow the prescribed push order and produce `popped`; otherwise return `false`.

### Examples

**Example 1**

- Input: `pushed = [1, 2, 3, 4, 5]`, `popped = [4, 5, 3, 2, 1]`
- Output: `true`

Push through `4`, pop it, push and pop `5`, then pop `3`, `2`, and `1`.

**Example 2**

- Input: `pushed = [1, 2, 3, 4, 5]`, `popped = [4, 3, 5, 1, 2]`
- Output: `false`

After `5` is popped, `2` remains above `1`, so `1` cannot be the next pop.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Simulate only the decisions that can help.** Keep an explicit stack and an index `next_pop` into `popped`. Process each value in `pushed` from left to right and append it to the stack. After every push, repeatedly pop while the stack is nonempty and `stack[-1] == popped[next_pop]`, advancing `next_pop` each time.

**Why immediate pops lose no valid sequence.** If the stack top equals the next required popped value, that value must leave before any later popped value. Delaying it and pushing more values would only place additional items above it, all of which would have to be removed first and would contradict the required order. Popping the match immediately is therefore forced in every valid execution. If the top does not match, no pop is legal for the proposed sequence, so the only possible progress is to consume another prescribed push.

Once all pushes have been processed, the sequence is valid exactly when `next_pop == n`. If an expected value remains unmatched, some different value blocks it on the stack, and no operations remain that could repair the order.

#### Complexity detail

Each of the $n$ values is pushed once and popped at most once, so the total simulation work is $O(n)$. The explicit stack can hold all $n$ values, giving $O(n)$ space.

#### Alternatives and edge cases

- **Reuse the input array as stack storage:** Maintain a write pointer into `pushed` and overwrite positions as the simulated stack. This preserves $O(n)$ time and reduces auxiliary space to $O(1)$, but mutates the input.
- **Backtrack over push/pop choices:** Explore both operations whenever they are legal. This can verify the sequence but repeats equivalent states and may take exponential time.
- **Remove the next pushed value from the front:** A direct simulation that repeatedly shifts a list is correct, but front removal can make the implementation $O(n^2)$.
- **One value:** The only permutation matches one push followed by one pop.
- **Immediate-pop order:** When `popped` equals `pushed`, each value can be popped as soon as it is pushed.
- **Reverse order:** Push every value first, then pop the entire stack; this is always valid.
- **Blocked earlier value:** Once a later-pushed value sits above the next required value and is not itself next in `popped`, the proposed sequence cannot be repaired by another pop.

</details>
