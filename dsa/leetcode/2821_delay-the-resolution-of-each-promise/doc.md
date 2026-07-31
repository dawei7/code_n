# Delay the Resolution of Each Promise

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2821 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/delay-the-resolution-of-each-promise/) |

## Problem Description

### Goal

You receive an array named `functions`. Each element is a function that returns a promise. You also receive a nonnegative duration `ms`, measured in milliseconds.

Create a new array of functions in the same order. Calling one of the new functions must call its corresponding original function, wait for that source promise to settle, and then postpone the same outcome for another `ms` milliseconds. A fulfilled source promise must eventually fulfill with its original value; a rejected source promise must eventually reject with its original reason.

Constructing the array must not eagerly call the source functions. Each returned function represents an independent delayed invocation.

### Function Contract

**Inputs**

- `functions`: An array of functions. Every function returns a promise; the array length is between $1$ and $10$.
- `ms`: The additional settlement delay in milliseconds, where $10 le 	exttt{ms} le 500$.

Let $n$ be `functions.length`.

**Return value**

Return an array of $n$ functions in the original order. When returned function $i$ is invoked, it starts `functions[i]()` and returns a promise that reproduces its fulfillment value or rejection reason after an additional `ms` milliseconds.

### Examples

**Example 1**

A single source function fulfills after $30$ milliseconds. With `ms = 50`, its delayed wrapper fulfills after about $80$ milliseconds.

**Example 2**

Two source functions fulfill after $50$ and $80$ milliseconds. With `ms = 70`, their wrappers fulfill after about $120$ and $150$ milliseconds respectively. Their positions in the returned array stay unchanged.

**Example 3**

Two source functions reject after $20$ and $100$ milliseconds. With `ms = 30`, the corresponding wrappers reject after about $50$ and $130$ milliseconds, preserving each original rejection reason.
