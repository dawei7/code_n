# Number of Steps to Reduce a Number to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1342 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) |

## Problem Description
### Goal
Starting from the non-negative integer `num`, repeatedly apply the operation required by its current parity. When the value is even and positive, divide it by 2. When it is odd, subtract 1.

Return the number of operations performed when the value first reaches zero. The rule is deterministic—there is no choice between the two operations—and an input already equal to zero requires no steps.

### Function Contract
**Inputs**

- `num`: an integer satisfying $0\le\texttt{num}\le10^6$.

**Return value**

The number of mandated divide-or-subtract steps needed to transform `num` into zero.

### Examples
**Example 1**

- Input: `num = 14`
- Output: `6`
- Explanation: The sequence is `14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0`.

**Example 2**

- Input: `num = 8`
- Output: `4`

**Example 3**

- Input: `num = 123`
- Output: `12`

### Required Complexity
- **Time:** $O(\log \texttt{num})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Simulate the unique legal transition**

Initialize a step counter to zero. While `num` is positive, inspect its least significant bit. An even number has a zero bit there and must be replaced by `num // 2`; an odd number has a one bit and must be replaced by `num - 1`. Increment the counter after each replacement.

Every iteration exactly follows the operation specified for the current value, so the produced sequence is the only legal sequence. Each transition makes the value smaller, and every odd step creates an even value unless it reaches zero, ensuring termination. The counter therefore equals the requested number of operations.

#### Complexity detail

Each division removes one binary digit, and each subtraction clears a low one bit before a division. The number of iterations is $O(\log \texttt{num})$ for positive input; zero takes constant time. The algorithm stores only the current integer and counter, using $O(1)$ space.

#### Alternatives and edge cases

- **Bit-count formula:** For positive `num`, the answer is its bit length minus one divisions plus one subtraction for every set bit; this also takes $O(\log \texttt{num})$ time.
- **Dynamic programming through every integer:** Computing the recurrence for all values from 0 through `num` is correct but takes $O(\texttt{num})$ time and space.
- **Zero:** Return 0 without entering the loop.
- **One:** One subtraction reaches zero.
- **Power of two:** Repeated division reaches 1, followed by one final subtraction.
- **Odd value:** Subtraction occurs before any subsequent division.

</details>
