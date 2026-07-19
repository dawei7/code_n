# Distant Barcodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1054 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/distant-barcodes/) |

## Problem Description

### Goal

A warehouse stores a row of barcode values, where `barcodes[i]` is the barcode at position `i`. Values may occur more than once.

Rearrange the entire array so that no two adjacent positions contain equal barcode values. Every input occurrence must appear exactly once in the result. Return any arrangement satisfying that condition; the input is guaranteed to admit at least one valid answer.

### Function Contract

**Inputs**

- `barcodes`: $N$ barcode values, where $1 \le N \le 10^4$ and $1 \le \texttt{barcodes[i]} \le 10^4$; let $U$ be the number of distinct values.

**Return value**

- Any permutation of all input values in which adjacent barcodes are always different.

### Examples

**Example 1**

- Input: `barcodes = [1,1,1,2,2,2]`
- Output: `[2,1,2,1,2,1]`
- Explanation: The counts are preserved and the two values alternate.

**Example 2**

- Input: `barcodes = [1,1,1,1,2,2,3,3]`
- Output: `[1,3,1,3,1,2,1,2]`
