# Exclusive Time of Functions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 636 |
| Difficulty | Medium |
| Topics | Array, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/exclusive-time-of-functions/) |

## Problem Description
### Goal
A single-threaded CPU runs calls to `n` functions identified from `0` through $n - 1$. Chronological logs record when a call starts at the beginning of an integer timestamp and when it ends at the end of an integer timestamp; nested calls pause the function below them on the call stack.

Return the exclusive execution time of every function identifier. Count only time units during which that function's call is at the top of the stack, excluding time spent in nested calls, and combine time from all calls of the same identifier, including recursive invocations. End timestamps are inclusive.

### Function Contract
**Inputs**

- `n`: the number of function identifiers, numbered from `0` through $n - 1$
- `logs`: chronologically ordered records formatted as `id:start:timestamp` or `id:end:timestamp`
- A start timestamp is the first time unit of a call; an end timestamp is the final inclusive time unit of that call

**Return value**

- A length-`n` list where index `id` contains that function's total exclusive execution time across all calls, including recursive calls with the same identifier

### Examples
**Example 1**

- Input: `n = 2`, `logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`
- Output: `[3,4]`

**Example 2**

- Input: `n = 1`, `logs = ["0:start:0","0:end:0"]`
- Output: `[1]`

**Example 3**

- Input: one function recursively starts at time `2` inside its call from time `0` through `6`
- Output: `[7]`
