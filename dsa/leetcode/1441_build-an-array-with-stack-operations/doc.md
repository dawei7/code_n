# Build an Array With Stack Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1441 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/build-an-array-with-stack-operations/) |

## Problem Description

### Goal

A stream supplies the integers from `1` through `n` in increasing order. Reading the next stream value and placing it on an initially empty stack is recorded as `"Push"`. Removing the stack's top value is recorded as `"Pop"`.

Return a sequence of those operation names that makes the final stack equal `target` from bottom to top. Every read value must first be pushed, unwanted values may then be popped, and reading must stop as soon as the target has been built. The target is strictly increasing, so its order is compatible with the stream.

### Function Contract

**Inputs**

- `target`: a strictly increasing integer array of length $t$, where $1 \le t \le 100$.
- `n`: the stream's upper value, where $1 \le n \le 100$ and `target[t - 1] <= n`.
- Let $L=\texttt{target[t-1]}$ be the final stream value that must be read.

**Return value**

- A list containing `"Push"` and `"Pop"` operations that builds `target` and stops immediately after reading $L$.

### Examples

**Example 1**

- Input: `target = [1,3], n = 3`
- Output: `["Push","Push","Pop","Push"]`

**Example 2**

- Input: `target = [1,2,3], n = 3`
- Output: `["Push","Push","Push"]`

**Example 3**

- Input: `target = [2,3,4], n = 4`
- Output: `["Push","Pop","Push","Push","Push"]`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Follow the stream rather than searching for operations.** Iterate `current` from `1` upward and keep an index `target_index` for the next desired value. Every current value is read exactly once, so append `"Push"` unconditionally.

**Keep or discard the pushed value.** If `current == target[target_index]`, retain it on the stack and advance `target_index`. Otherwise, the strictly increasing target can never need that smaller skipped value later, so append `"Pop"` immediately.

**Stop at the final desired value.** Once `target_index == len(target)`, the stack already equals the complete target. Stop without reading any larger values, even when `n` is greater than the target's final entry.

**Why the emitted sequence is valid.** Before each stream read, the retained stack equals the processed prefix of `target`. A matching value extends that prefix by one. A nonmatching value is pushed as required and immediately removed, restoring the same prefix. This invariant continues until every target value is retained, at which point the stack is exactly `target` and the stopping rule is satisfied.

#### Complexity detail

The algorithm reads exactly the values $1$ through $L$, performing constant work per value, for $O(L)$ time. It returns between $L$ and $2L-t$ operation strings, so the required output occupies $O(L)$ space; auxiliary state aside from the output is $O(1)$.

#### Alternatives and edge cases

- **List membership for every stream value:** Testing `current in target` repeatedly can take $O(Lt)$ time with an array target.
- **Build a target set:** This also gives linear expected time but uses $O(t)$ extra space and does not directly track when construction is complete.
- **Consecutive target values:** Each is kept with one `"Push"` and no intervening `"Pop"`.
- **Skipped values:** Each requires the adjacent pair `"Push","Pop"`.
- **Target begins above one:** Every earlier stream value must be pushed and popped.
- **n exceeds the final target:** Do not read the unused suffix of the stream.
- **Single target value:** Process only through that value and stop.

</details>
