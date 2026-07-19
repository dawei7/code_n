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
