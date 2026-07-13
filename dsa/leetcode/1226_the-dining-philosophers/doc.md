# The Dining Philosophers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1226 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [the-dining-philosophers](https://leetcode.com/problems/the-dining-philosophers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-dining-philosophers/).

### Goal
Implement a synchronization policy for the dining philosophers problem. Five philosophers repeatedly try to eat; each one needs both adjacent forks, and the implementation must avoid deadlock while invoking the provided callbacks in a valid order.

### Concurrency Contract
**Inputs**

- `philosopher: int` - Philosopher id from `0` to `4`.
- `pickLeftFork`, `pickRightFork`, `eat`, `putLeftFork`, `putRightFork`: callbacks that must be called when the philosopher performs the corresponding action.

**Return value**

No explicit return value. Correctness is determined by the callback sequence and thread safety.

### Examples
**Example 1**

- Input: `n = 1`
- Output: one valid callback trace where philosopher `0` picks both forks, eats, and puts both forks down.

**Example 2**

- Input: several philosophers call `wantsToEat` concurrently.
- Output: any valid interleaving with no philosopher eating before holding both forks.

**Example 3**

- Input: repeated calls from all five philosophers.
- Output: the system continues to make progress without circular waiting deadlock.

---

## Solution
### Approach
Use mutual exclusion around forks and prevent circular waiting. A common robust strategy is a semaphore that allows at most four philosophers to try to pick up forks at the same time, then each philosopher locks the two adjacent fork locks, performs the callbacks, releases the locks, and leaves the semaphore. Another valid strategy is asymmetric fork acquisition order for one philosopher.

### Complexity Analysis
- **Time Complexity**: `O(1)` work per call, excluding time spent waiting for locks.
- **Space Complexity**: `O(1)` because there are always five forks and a constant number of synchronization primitives.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
