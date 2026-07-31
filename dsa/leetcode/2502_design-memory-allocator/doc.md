# Design Memory Allocator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2502 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-memory-allocator/) |

## Problem Description
### Goal
Design an allocator for a 0-indexed memory array containing `n` units. Every unit is initially free.

An allocation request supplies a positive `size` and an identifier `mID`. It must reserve the leftmost block of `size` consecutive free units, label every unit in that block with `mID`, and return the block's first index. If no sufficiently long free block exists, the allocator returns `-1` without changing memory. The same `mID` may own several separate blocks.

A free request supplies an `mID`, releases every unit carrying that identifier even when those units belong to different blocks, and returns the number of released units. Process the requested operations in order.

### Function Contract
**Inputs**

- `commands`: An operation sequence beginning with `Allocator`, followed by `allocate` and `freeMemory` calls.
- `inputs`: Arguments aligned with `commands`; `Allocator` receives `n`, `allocate` receives `size` and `mID`, and `freeMemory` receives `mID`.

The values `n`, `size`, and `mID` are between $1$ and $1000$ inclusive. Let $q$ be the number of method calls after construction; $q\le 1000$.

**Return value**

A list aligned with the operations. Construction contributes `null`; each allocation contributes its starting index or `-1`; each free contributes the number of released units.

### Examples
**Example 1**

- Input: `commands = ["Allocator","allocate","allocate","allocate","freeMemory","allocate","allocate","allocate","freeMemory","allocate","freeMemory"]`, `inputs = [[10],[1,1],[1,2],[1,3],[2],[3,4],[1,1],[1,1],[1],[10,2],[7]]`
- Output: `[null,0,1,2,1,3,1,6,3,-1,0]`
- Explanation: Reusing `mID = 1` creates several blocks; freeing it later releases all three owned units.

**Example 2**

- Input: `commands = ["Allocator","allocate","allocate","freeMemory","allocate"]`, `inputs = [[6],[2,1],[2,2],[1],[3,3]]`
- Output: `[null,0,2,2,-1]`
- Explanation: Three units are free in total after the free, but they are not one consecutive block.

**Example 3**

- Input: `commands = ["Allocator","freeMemory","allocate"]`, `inputs = [[3],[9],[1,9]]`
- Output: `[null,0,0]`
- Explanation: Freeing an absent identifier changes nothing, and the following allocation starts at index $0$.
