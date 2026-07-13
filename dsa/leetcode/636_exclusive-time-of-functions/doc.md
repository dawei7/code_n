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

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(n + D)$

<details>
<summary>Approach</summary>

#### General

**Keep the active call stack**

The most recently started unfinished call owns the CPU. Store active function identifiers in a stack so its top always identifies the function that should receive elapsed exclusive time.

**Track the first unassigned timestamp**

Let `previous` be the first time unit not yet credited. At a `start` event at time `t`, the old stack top owns the half-open interval `[previous, t)`, contributing `t - previous`; then push the new call and set `previous = t`.

**Handle inclusive end events separately**

At an `end` event at time `t`, the active call owns `[previous, t]`, which has `t - previous + 1` integer units. Credit and pop it, then set `previous = t + 1` so the resumed caller cannot also claim the ending time unit.

**Why every time unit is credited exactly once**

Before each log, all time units below `previous` have been assigned to whichever call was on top when they elapsed. Start processing assigns only the interval before the new call becomes active. End processing assigns through the ending call's inclusive final unit and advances beyond it. These disjoint intervals cover the execution timeline, while the stack always names their correct owner, so the accumulated totals are exact.

#### Complexity detail

Each of the `L` logs is parsed once, and each call identifier is pushed and popped once, giving $O(L)$ time. The result uses $O(n)$ space and the active stack uses $O(D)$ space for maximum nesting depth `D`.

#### Alternatives and edge cases

- **Simulate every timestamp:** increment the active function one unit at a time; it is correct but can depend on the numeric timestamp span rather than the number of logs.
- **Pair starts and ends before accounting:** explicit call-tree construction can recover the same totals, but requires extra nodes and a later traversal.
- **Subtract child durations from parent durations:** works with a call tree but is more stateful than assigning elapsed intervals directly.
- An end timestamp is inclusive, so a call starting and ending at the same timestamp contributes one unit.
- Recursive calls push the same identifier more than once and all contributions accumulate at that identifier.
- Sequential calls may resume or start at exactly the time unit after an inclusive end.
- Functions with no calls retain zero exclusive time.
- Nested calls may have identical boundary timestamps; log order and the stack determine which call is active.

</details>
