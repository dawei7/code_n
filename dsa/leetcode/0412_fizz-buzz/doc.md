# Fizz Buzz

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 412 |
| Difficulty | Easy |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/fizz-buzz/) |

## Problem Description
### Goal
Given a positive integer `n`, process each integer from `1` through `n` in increasing order. Replace multiples of both `3` and `5` with `"FizzBuzz"`, other multiples of `3` with `"Fizz"`, and other multiples of `5` with `"Buzz"`.

For every remaining integer, use its ordinary decimal string. Return exactly `n` strings aligned with their source integers, so result index zero describes `1`. The combined divisibility case takes precedence over either single word; do not emit separate neighboring entries for `"Fizz"` and `"Buzz"` at the same number.

### Function Contract
**Inputs**

- `n`: the positive inclusive upper bound

**Return value**

- Return the `n` required strings in increasing integer order.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `["1","2","Fizz"]`

**Example 2**

- Input: `n = 5`
- Output: `["1","2","Fizz","4","Buzz"]`

**Example 3**

- Input: `n = 15`
- Output: `["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]`
