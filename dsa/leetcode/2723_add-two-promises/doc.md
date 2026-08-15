# Add Two Promises

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2723 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/add-two-promises/) |

## Problem Description

### Goal

Receive two promises, `promise1` and `promise2`. Each promise is guaranteed to fulfill with a number. Return a new promise whose fulfilled value is the arithmetic sum of those two numbers.

The two input promises may settle at different times. The returned promise cannot produce the sum until both values are available, but the inputs already represent active asynchronous work and should be observed together rather than recreated. Rejection behavior does not need a separate rule because both inputs are guaranteed to fulfill.

### Function Contract

**Inputs**

- `promise1`: A promise that fulfills with a number.
- `promise2`: A second promise that fulfills with a number.

**Return value**

Return a promise that fulfills with the numeric sum of the two fulfillment values after both inputs have settled successfully.

### Examples

#### Example 1

- **Input:** `promise1` fulfills with $2$ after $20$ ms, and `promise2` fulfills with $5$ after $60$ ms.
- **Output:** `7`
- **Explanation:** Once both values are available, their sum is $2+5=7$.

#### Example 2

- **Input:** `promise1` fulfills with $10$ after $50$ ms, and `promise2` fulfills with $-12$ after $30$ ms.
- **Output:** `-2`
- **Explanation:** Negative fulfillment values participate in ordinary numeric addition.

#### Example 3

- **Input:** Both promises fulfill immediately with $0$.
- **Output:** `0`
- **Explanation:** The returned promise still settles asynchronously with the sum.
