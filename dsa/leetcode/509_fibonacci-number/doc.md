# Fibonacci Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 509 |
| Difficulty | Easy |
| Topics | Math, Dynamic Programming, Recursion, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/fibonacci-number/) |

## Problem Description
### Goal
The Fibonacci sequence starts with $F(0) = 0$ and $F(1) = 1$. For every index $n > 1$, its value is defined by the recurrence $F(n) = F(n - 1) + F(n - 2)$.

Given an integer `n` from `0` through `30`, return `F(n)`. The index is zero-based, so input zero returns zero and input one returns one. Compute the numeric sequence value rather than returning the preceding pair, a generated list, or the number of additions performed.

### Function Contract
**Inputs**

- `n`: an integer index from `0` through `30`

**Return value**

- The integer `F(n)` defined by the Fibonacci recurrence

### Examples
**Example 1**

- Input: `n = 0`
- Output: `0`

**Example 2**

- Input: `n = 5`
- Output: `5`

**Example 3**

- Input: `n = 8`
- Output: `21`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep only the two values needed by the recurrence**

At the start of an iteration, let `previous = F(i)` and `current = F(i + 1)`. The simultaneous update `(previous, current) = (current, previous + current)` advances this relationship to the next index without storing the whole sequence.

**Advance exactly n times**

Initialize the pair as $(F(0), F(1)) = (0, 1)$. After `n` updates, the maintained relationship gives `previous = F(n)`, so return `previous`. This also handles $n = 0$: no update occurs and the initial zero is returned.

**Why simultaneous assignment matters**

The new second value must use both old values. Computing the pair together preserves them until their sum is formed; overwriting `previous` first in languages without simultaneous assignment requires a temporary variable.

#### Complexity detail

The loop performs one constant-time update for each of `n` indices, giving $O(n)$ time. Two running integers and the loop counter use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Memoized recursion:** evaluates each index once in $O(n)$ time but uses $O(n)$ cache and call-stack space.
- **Bottom-up array:** makes every intermediate value available later but uses $O(n)$ space unnecessarily.
- **Naive recursion:** mirrors the recurrence directly but repeats subproblems and takes exponential time.
- **Fast doubling or matrix exponentiation:** computes the value in $O(\log n)$ arithmetic steps and is useful for much larger indices, but is more machinery than these constraints require.
- **Zero:** returns the first base value without entering the loop.
- **One:** one update moves `previous` to the second base value.

</details>
