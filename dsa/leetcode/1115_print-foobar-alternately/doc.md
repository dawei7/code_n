# Print FooBar Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1115 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [print-foobar-alternately](https://leetcode.com/problems/print-foobar-alternately/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/print-foobar-alternately/).

### Goal
Coordinate two threads so that one repeatedly prints `foo` and the other repeatedly prints `bar`, producing `foobar` exactly `n` times.

### Concurrency Contract
**Inputs**

- `n`: Number of `foobar` repetitions.
- `foo(printFoo)`: Method run by one thread; it must call `printFoo`.
- `bar(printBar)`: Method run by another thread; it must call `printBar`.

**Required output order**

The combined output must be `"foobar"` repeated `n` times.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `"foobar"`

**Example 2**

- Input: `n = 2`
- Output: `"foobarfoobar"`

**Example 3**

- Input: `n = 3`
- Output: `"foobarfoobarfoobar"`

---

## Solution
### Approach
Use two synchronization signals. Initially, the `foo` signal is open and the `bar` signal is closed. The `foo` method waits for the `foo` signal, prints, then opens the `bar` signal. The `bar` method waits for the `bar` signal, prints, then opens the `foo` signal for the next round.

Semaphores, condition variables, or equivalent language-specific primitives can express this alternating handoff.

### Complexity Analysis
- **Time Complexity**: `O(n)` print operations per method.
- **Space Complexity**: `O(1)` synchronization state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
