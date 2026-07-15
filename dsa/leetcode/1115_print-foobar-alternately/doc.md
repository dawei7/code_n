# Print FooBar Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1115 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| LeetCode | [Open problem](https://leetcode.com/problems/print-foobar-alternately/) |

## Problem Description

### Goal

A shared `FooBar` instance stores a positive integer `n` and is passed to two asynchronous threads. One thread calls `foo(printFoo)`, whose callback emits `"foo"`; the other calls `bar(printBar)`, whose callback emits `"bar"`.

Coordinate the two methods so their callbacks alternate strictly, beginning with `printFoo()`. The combined output must be `"foobar"` repeated exactly `n` times, regardless of which thread starts first or how the operating system schedules them.

### Function Contract

**Inputs**

- `n`: the number of required `"foobar"` repetitions, with $1 \le n \le 1000$.
- `printFoo` and `printBar`: zero-argument callbacks executed by `foo` and `bar` on two threads sharing one `FooBar` instance.

**Return value**

- Both methods return `None`; their ordered callback side effects must concatenate to `"foobar"` repeated `n` times.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `"foobar"`

**Example 2**

- Input: `n = 2`
- Output: `"foobarfoobar"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Encode whose turn it is with two permits:** Initialize a `foo` semaphore with one permit and a `bar` semaphore with zero. The first `foo` iteration may proceed immediately, while an early `bar` thread blocks.

**Hand ownership to the other thread after every print:** On each of its $n$ iterations, `foo` acquires the `foo` permit, invokes `printFoo()`, and releases the `bar` permit. Symmetrically, `bar` acquires `bar`, invokes `printBar()`, and releases `foo` for the next round.

Initially only `foo` can print. Each print disables further progress by that same method until the other method prints and returns the permit, so neither `"foofoo"` nor `"barbar"` can occur. Every `foo` releases exactly one opportunity for `bar`, and every nonfinal `bar` releases the next opportunity for `foo`; with $n$ loop iterations in each method, the output is exactly $n$ ordered `"foobar"` pairs.

#### Complexity detail

Each thread performs $n$ callback calls and a constant number of semaphore operations per iteration, for $O(n)$ total work. The two semaphores and loop counters occupy $O(1)$ space. Blocking time depends on scheduling but does not add polling work.

#### Alternatives and edge cases

- **Condition variable with a turn flag:** It is correct when waits use guarded predicate loops, but requires more explicit lock and notification logic.
- **Two events:** Events can alternate if each phase carefully clears its own signal before setting the other; semaphores state the single-permit handoff more directly.
- **Busy waiting:** Polling a Boolean wastes CPU and lacks portable memory-order guarantees without synchronization.
- **One mutex only:** Mutual exclusion prevents simultaneous callbacks but does not by itself force alternation or make `foo` go first.
- **`n = 1`:** One permit handoff produces exactly one `"foobar"` pair.
- **Bar thread starts first:** It blocks on its zero-permit semaphore until `foo` emits the first token.
- **Spurious scheduling delays:** A delayed thread retains the only available permit, so the other thread cannot print out of turn.

</details>
