# Grumpy Bookstore Owner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1052 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [grumpy-bookstore-owner](https://leetcode.com/problems/grumpy-bookstore-owner/) |

## Problem Description & Examples
### Goal
For each minute, customers enter a bookstore and the owner is either grumpy or not. Non-grumpy minutes always satisfy customers. Choose one contiguous window of length `minutes` during which grumpiness is suppressed to maximize satisfied customers.

### Function Contract
**Inputs**

- `customers`: List[int]
- `grumpy`: List[int] where `1` means grumpy
- `minutes`: int length of the suppression window

**Return value**

int - maximum satisfied customers

### Examples
**Example 1**

- Input: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- Output: `16`

**Example 2**

- Input: `customers = [1], grumpy = [0], minutes = 1`
- Output: `1`

**Example 3**

- Input: `customers = [4, 10, 10], grumpy = [1, 1, 0], minutes = 2`
- Output: `24`

---

## Underlying Base Algorithm(s)
Sliding window over extra recoverable customers.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
