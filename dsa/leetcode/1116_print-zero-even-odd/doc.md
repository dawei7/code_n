# Print Zero Even Odd

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1116 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| LeetCode | [Open problem](https://leetcode.com/problems/print-zero-even-odd/) |

## Problem Description

### Goal

The callback `printNumber(x)` writes the integer `x`. One shared `ZeroEvenOdd` instance stores a positive integer `n` and is passed to three asynchronous threads. One thread calls `zero(printNumber)` and may print only zeroes, one calls `even(printNumber)` and may print only even values, and one calls `odd(printNumber)` and may print only odd values.

Coordinate the three methods so the combined callback sequence alternates a zero with each integer from `1` through `n`: `0, 1, 0, 2, 0, 3, ...`. The sequence contains exactly $2n$ callback invocations and must remain correct regardless of thread start order or operating-system scheduling.

### Function Contract

**Inputs**

- `n`: the greatest positive integer to print, with $1 \le n \le 1000$.
- `printNumber`: a callback accepting one integer; the three methods run on separate threads sharing the same `ZeroEvenOdd` object.

**Return value**

- The methods return `None`; their combined side effects must be `0,1,0,2,...,0,n` in exactly that order.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `"0102"`

**Example 2**

- Input: `n = 5`
- Output: `"0102030405"`

The display concatenates callback values without separators; values are still passed to the callback as integers.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Give zero the initial permit:** Create three semaphores. `zero_turn` starts with one permit, while `odd_turn` and `even_turn` start with zero. This makes an early odd or even thread block until the first zero has been printed.

**Let zero choose the next numeric thread:** For each integer `value` from `1` through `n`, `zero` acquires `zero_turn`, calls `printNumber(0)`, and releases `odd_turn` when `value` is odd or `even_turn` when it is even. The loop index therefore identifies exactly which number must follow that zero.

**Return control after printing one number:** The odd method visits `1,3,5,...`; before each callback it acquires `odd_turn`, then releases `zero_turn`. The even method does the same for `2,4,6,...` using `even_turn`. At any point only the semaphore for the unique next callback is available. Every numeric callback returns the permit to zero, and every zero hands it to the correct parity thread, so induction over `value = 1..n` proves the entire sequence and termination.

#### Complexity detail

Exactly $n$ zero callbacks and $n$ numeric callbacks occur. Each performs a constant number of semaphore operations, so total work is $O(n)$. Three semaphores and fixed loop state use $O(1)$ space. Scheduling delays affect elapsed time but do not introduce polling work.

#### Alternatives and edge cases

- **Condition variable and phase state:** A shared next-value/turn predicate can coordinate all three methods, but every wait needs a guarded loop and notifications.
- **One zero semaphore plus a numeric semaphore:** The numeric side would still need safe routing between the odd and even threads, making separate parity gates clearer.
- **Busy-wait flags:** Polling wastes CPU and does not provide portable memory visibility without synchronization primitives.
- **Sleeping to influence order:** Delays cannot guarantee a happens-before relationship and fail under different schedules.
- **`n = 1`:** Zero releases only the odd gate, producing `"01"`; the even thread performs zero iterations.
- **Even terminal value:** The final zero releases `even_turn`, and the even callback completes without requiring another useful round.
- **A numeric thread starts first:** Its zero-initialized semaphore blocks it until zero selects that parity.

</details>
