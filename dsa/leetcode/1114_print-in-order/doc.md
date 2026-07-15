# Print in Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1114 |
| Difficulty | Easy |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/print-in-order/) |

## Problem Description

### Goal

One shared `Foo` instance is passed to three different threads. One thread calls `first(printFirst)`, another calls `second(printSecond)`, and the third calls `third(printThird)`. Each callback emits its corresponding word, but operating-system scheduling may start or pause the threads in any order.

Modify `Foo` so that `printSecond()` cannot run until `printFirst()` has completed, and `printThird()` cannot run until `printSecond()` has completed. The observed output must always be `"firstsecondthird"`. The input permutation describes which calls are launched, but it does not guarantee their actual scheduling order.

### Function Contract

**Inputs**

- `printFirst`, `printSecond`, and `printThird`: zero-argument callbacks invoked by `first`, `second`, and `third` on three separate threads sharing one `Foo` instance.
- The judge invokes each method exactly once; the displayed `nums` value is a permutation of `[1,2,3]`.

**Return value**

- The methods return `None`; correctness is the happens-before order of callback side effects, which must produce `"firstsecondthird"` for every schedule.

### Examples

**Example 1**

- Input: `nums = [1,2,3]`
- Output: `"firstsecondthird"`

**Example 2**

- Input: `nums = [1,3,2]`
- Output: `"firstsecondthird"`

Even if the third-method thread starts before the second-method thread, it must wait for both earlier phases.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Create one gate for each dependency:** Initialize two unset synchronization events. The first event means that `first` has finished; the second means that `second` has finished.

**Publish completion only after the callback:** `first` executes `printFirst()` and then sets the first event. `second` waits for that event, executes `printSecond()`, and then sets the second event. `third` waits for the second event before executing `printThird()`.

The first gate establishes that every execution of the second callback happens after the first callback returns. The second gate similarly places the third callback after the second. Transitivity gives the required total order. A thread arriving early blocks without consuming the signal; once its prerequisite event is set, it proceeds, so all six launch permutations are handled without busy waiting.

#### Complexity detail

There are exactly three method calls and two fixed synchronization objects. Each method performs a constant number of callback, wait, and signal operations, so contract-level work and storage are both $O(1)$. Waiting duration depends on scheduling but does not add computational iterations.

#### Alternatives and edge cases

- **Semaphores:** Two zero-initialized semaphores can encode the same one-way dependencies, with `release` after each completed phase.
- **Condition variable plus phase counter:** It generalizes to more phases but needs a lock, guarded predicate loops, and notifications for this three-step task.
- **Busy-wait flags:** Polling shared booleans wastes CPU and can be incorrect without proper memory-visibility guarantees.
- **Sleeping for guessed delays:** Timing does not establish a happens-before relation and fails under different schedules or machine loads.
- **Third arrives first:** It blocks on the second gate, which cannot open before the first gate has enabled `second`.
- **Callback completion:** Each event is signaled after, not before, its callback so side effects themselves are ordered.
- **Single shared instance:** The gates belong to the `Foo` instance used by all three threads; separate per-method state would not synchronize them.

</details>
