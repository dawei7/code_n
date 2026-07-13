# Fizz Buzz Multithreaded

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1195 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [fizz-buzz-multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/fizz-buzz-multithreaded/).

### Goal
Coordinate four threads so they print the standard Fizz Buzz sequence from `1` through `n` in order.

### Concurrency Contract
**Operations**

- `FizzBuzz(n)`: Initialize the sequence length.
- `fizz(printFizz)`: Called by the thread responsible for multiples of `3` but not `5`.
- `buzz(printBuzz)`: Called by the thread responsible for multiples of `5` but not `3`.
- `fizzbuzz(printFizzBuzz)`: Called by the thread responsible for multiples of both `3` and `5`.
- `number(printNumber)`: Called by the thread responsible for ordinary numbers.

**Return value**

The methods coordinate side effects through the provided print callbacks.

### Examples
**Example 1**

- Input: `n = 15`
- Output: `1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz`

**Example 2**

- Input: `n = 5`
- Output: `1,2,fizz,4,buzz`

**Example 3**

- Input: `n = 1`
- Output: `1`

---

## Solution
### Approach
Keep a shared current number protected by synchronization. Each worker waits until the current number matches its predicate, prints, increments the number, and wakes the other workers.

This can be implemented with a mutex plus condition variable, or with semaphores that route each number to the correct worker.

### Complexity Analysis
- **Time Complexity**: `O(n)` total printed steps, excluding blocked waiting time.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
