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
