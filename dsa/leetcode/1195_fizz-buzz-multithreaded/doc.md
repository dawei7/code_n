# Fizz Buzz Multithreaded

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1195 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/fizz-buzz-multithreaded/) |

## Problem Description

### Goal

Four provided callbacks print `"fizz"`, `"buzz"`, `"fizzbuzz"`, or an integer. One shared `FizzBuzz` instance is passed to four different threads, which respectively call its `fizz`, `buzz`, `fizzbuzz`, and `number` methods.

Modify the class so those concurrent method calls collectively output the ordered, 1-indexed sequence from `1` through `n`. A position divisible by both 3 and 5 produces `"fizzbuzz"`; one divisible by 3 only produces `"fizz"`; one divisible by 5 only produces `"buzz"`; every other position produces its integer. Each token must appear exactly once and in sequence order.

### Function Contract

**Initialization and concurrent methods**

- `FizzBuzz(n)`: Initializes one shared object for a sequence length satisfying $1\le n\le50$.
- `fizz(printFizz)`: Called by thread A and invokes `printFizz()` for multiples of 3 but not 5.
- `buzz(printBuzz)`: Called by thread B and invokes `printBuzz()` for multiples of 5 but not 3.
- `fizzbuzz(printFizzBuzz)`: Called by thread C and invokes `printFizzBuzz()` for multiples of both 3 and 5.
- `number(printNumber)`: Called by thread D and invokes `printNumber(value)` for positions divisible by neither 3 nor 5.

**Return value**

- The four methods return no value; their synchronized callback side effects must form the required sequence without deadlock.

### Examples

**Example 1**

- Input: `n = 15`
- Output: `[1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]`

**Example 2**

- Input: `n = 5`
- Output: `[1,2,"fizz",4,"buzz"]`

**Example 3**

- Input: `n = 1`
- Output: `[1]`

Only the number thread emits a token for this boundary input.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Share one guarded position.** Store `current = 1` and protect it with a condition variable. Each worker owns a predicate describing exactly the positions for its callback. While the sequence is unfinished but the predicate is false, that worker waits and releases the condition lock so the responsible worker can proceed.

**Emit and transfer ownership atomically.** The worker whose predicate matches invokes its callback while holding the condition lock, increments `current`, and wakes every waiting worker. Keeping the callback and increment in one critical section prevents another thread from printing the next token first. The four predicates are mutually exclusive and collectively exhaustive, so exactly one worker can advance each position.

**Terminate every waiter.** After the final callback changes `current` to `n + 1`, it notifies all workers. Each awakened loop checks the bound before testing its predicate or printing, allowing all four methods to return even when their final owned positions occurred much earlier.

#### Complexity detail

Exactly one callback and one increment occur for each of the $n$ sequence positions, giving $O(n)$ total productive work. Condition waits do not busy-spin. The shared counter, condition variable, and fixed set of four worker states use $O(1)$ auxiliary space, excluding the platform's output collection.

#### Alternatives and edge cases

- **Four routing semaphores:** A number coordinator can release the semaphore for the appropriate callback and wait for completion; this is correct but needs more explicit handoff state.
- **Busy waiting:** Repeatedly reading an unguarded counter wastes CPU and risks data races or visibility errors.
- **Independent loops without synchronization:** Even correct per-thread divisibility tests cannot preserve global output order under arbitrary scheduling.
- **Predicate overlap:** The fizz and buzz predicates must exclude multiples of 15 so only `fizzbuzz` owns those positions.
- **Small `n`:** Some worker predicates may never match, but the final notification must still let those threads terminate.
- **Spurious wakeups:** Every wait is enclosed in a loop that rechecks both the bound and its predicate.
- **Callback ordering:** Invoking a callback outside the guarded handoff could let later output overtake it.
- **Completion:** Advancing past `n` and notifying all waiters prevents a thread from remaining blocked after the sequence ends.

</details>
