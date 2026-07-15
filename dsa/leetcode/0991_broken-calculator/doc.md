# Broken Calculator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 991 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/broken-calculator/) |

## Problem Description

### Goal

A broken calculator initially displays the positive integer `startValue`. It supports only two operations: multiply the displayed number by $2$, or subtract $1$ from it. No other arithmetic keys are available, and each press applies its operation to the value currently shown.

Given `startValue` and another positive integer `target`, return the minimum number of allowed operations required to make the calculator display `target`.

### Function Contract

**Inputs**

- `startValue`: the calculator's initial integer, where $1\le\texttt{startValue}\le10^9$.
- `target`: the desired displayed integer, where $1\le\texttt{target}\le10^9$.

Let $T=\texttt{target}$.

**Return value**

- The minimum number of multiply-by-two and subtract-one operations needed to reach `target`.

### Examples

**Example 1**

- Input: `startValue = 2, target = 3`
- Output: `2`
- Explanation: Double to $4$, then subtract one to reach $3$.

**Example 2**

- Input: `startValue = 5, target = 8`
- Output: `2`
- Explanation: Subtract one to get $4$, then double to get $8$.

**Example 3**

- Input: `startValue = 3, target = 10`
- Output: `3`
- Explanation: The sequence $3\to6\to5\to10$ uses three operations.

### Required Complexity

- **Time:** $O(\log T)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reverse the operations:** Searching forward offers two choices at every step and can explore many unnecessary values. Starting from `target` makes the inverse move forced. An even value could have resulted from doubling, so halve it. An odd value greater than `startValue` cannot be the result of doubling; increment it first, which reverses a preceding subtract-one operation.

**Greedily remove the largest possible scale:** While the current reversed value exceeds `startValue`, perform the forced parity move and count it. Halving an even value is always preferable to incrementing or simulating extra forward decrements because any forward path that reaches that even value without a final doubling must spend at least as many operations adjusting a larger predecessor. For an odd value, incrementing is the only way to make a later inverse halving possible.

Once the reversed value is at most `startValue`, no inverse halving is useful: the forward calculator must subtract exactly `startValue - current` times. Adding that difference to the reversed-operation count completes an optimal path.

#### Complexity detail

Every one or two reversed iterations reduce the current value by roughly half. The loop therefore performs $O(\log T)$ operations and uses only counters plus the current value, for $O(1)$ space.

#### Alternatives and edge cases

- **Forward breadth-first search:** BFS finds the minimum path, but the reachable numeric state space grows with `target` and can require $O(T)$ time and space.
- **Forward greedy doubling:** Always doubling while below the target can overshoot in a way that requires more decrements than subtracting before an earlier doubling.
- **Target not above the start:** When `target <= startValue`, only subtraction can reduce the display, so the answer is their difference.
- **Odd reversed value:** Increment before halving; integer division directly would reverse no legal forward operation.
- **Equal values:** No operation is needed when `startValue == target`.

</details>
