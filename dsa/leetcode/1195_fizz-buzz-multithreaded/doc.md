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
