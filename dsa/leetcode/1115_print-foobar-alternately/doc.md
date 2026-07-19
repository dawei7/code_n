# Print FooBar Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1115 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/print-foobar-alternately/) |

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
