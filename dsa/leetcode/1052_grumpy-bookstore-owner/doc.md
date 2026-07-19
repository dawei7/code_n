# Grumpy Bookstore Owner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1052 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/grumpy-bookstore-owner/) |

## Problem Description

### Goal

A bookstore is open for $N$ minutes. At the start of minute `i`, `customers[i]` customers enter, and all of them leave after that minute. The binary value `grumpy[i]` is `1` when the owner is grumpy during that minute and `0` otherwise. Customers are satisfied exactly when the owner is not grumpy while they visit.

The owner can use a secret technique once to remain not grumpy for exactly `minutes` consecutive minutes. Choose when to use that single interval and return the maximum total number of customers who can be satisfied during the day.

### Function Contract

**Inputs**

- `customers`: the $N$ customer counts, where $0 \le \texttt{customers[i]} \le 1000$.
- `grumpy`: a length-$N$ binary array describing the owner's current mood each minute.
- `minutes`: the technique duration $M$, where $1 \le M \le N \le 2\cdot10^4$.

**Return value**

- The maximum number of satisfied customers after applying the technique to at most one length-$M$ interval.

### Examples

**Example 1**

- Input: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- Output: `16`
- Explanation: Applying the technique during the final three minutes yields the maximum total.

**Example 2**

- Input: `customers = [1], grumpy = [0], minutes = 1`
- Output: `1`
