# Implement Rand10() Using Rand7()

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 470 |
| Difficulty | Medium |
| Topics | Math, Rejection Sampling, Randomized, Probability and Statistics |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/) |

## Problem Description
### Goal
The provided `rand7()` API returns each integer from `1` through `7` independently with equal probability. Implement `rand10()` using only calls to that API and ordinary deterministic computation.

Each `rand10()` call must return an integer from `1` through `10`, with all ten outcomes exactly equally likely. Do not call another random API or use a language's built-in random API. Combine enough `rand7()` outcomes to create an equiprobable sample space, reject any excess states that would bias the mapping, and retry as needed. Successive calls must preserve the same uniform distribution; the app uses a deterministic stream only to verify control flow.

### Function Contract
**Inputs**

- `rand7_values`: the app's deterministic cyclic stream of values from 1 through 7, used in place of LeetCode's hidden random API
- `draws`: the number of `rand10` outputs to generate in the app trace

**Return value**

- The generated output list. The native artifact exposes `Solution.rand10()` with no arguments and calls LeetCode's provided `rand7()` directly.

### Examples
**Example 1**

- Input: `rand7_values = [1, 1], draws = 3`
- Output: `[1, 1, 1]`

**Example 2**

- Input: `rand7_values = [7, 7, 1, 2], draws = 2`
- Output: `[2, 2]`

**Example 3**

- Input: `rand7_values = [6, 5], draws = 1`
- Output: `[10]`
