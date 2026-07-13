# 2 Keys Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 650 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/2-keys-keyboard/) |

## Problem Description
### Goal
A notepad initially displays exactly one character `A`. In one operation, you may use `Copy All` to copy every character currently on the screen—partial copying is not allowed—or use `Paste` to append the text copied by the most recent copy operation.

Given `n`, return the minimum number of operations required to display exactly `n` copies of `A`. Extra copies are not allowed in the final state, and pasting before any useful copy cannot create new text. When `n` is `1`, the initial screen already meets the target and the answer is `0`.

### Function Contract
**Inputs**

- `n`: the positive target number of `A` characters

**Return value**

- The minimum number of copy and paste operations needed to display exactly `n` characters

### Examples
**Example 1**

- Input: `n = 3`
- Output: `3`

**Example 2**

- Input: `n = 1`
- Output: `0`

**Example 3**

- Input: `n = 12`
- Output: `7`

### Required Complexity

- **Time:** $O(\sqrt{N})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View every copy phase as multiplication**

Suppose the screen currently contains `x` characters. Copying them once and then pasting $q - 1$ times costs `q` operations and changes the screen length from `x` to $q \cdot x$. A complete valid strategy therefore expresses `n` as a product of phase multipliers, and its operation count is the sum of those multipliers.

**Why only prime multipliers are needed**

If a phase multiplier is composite, write it as $a \cdot b$ with both factors at least two. Replacing that one phase by an `a` phase followed by a `b` phase changes its cost from $a \cdot b$ to $a + b$, which is never larger. Repeating this split leaves only prime multipliers. Consequently, the minimum operation count is the sum of `n`'s prime factors, including repetitions.

For example, $12 = 2 \cdot 2 \cdot 3$, so three multiplication phases cost $2 + 2 + 3 = 7$. The corresponding actions double, double, and then triple the number of characters.

**Extract the factors by trial division**

Try divisors beginning at two. Whenever a divisor divides the remaining target, add it to the answer and divide it out; repeated division records repeated prime factors. Once the candidate exceeds the square root of the remaining value, any remainder greater than one must itself be prime and is added once.

This returns a realizable cost because each recorded factor defines one copy-and-paste phase. It is minimal because every strategy decomposes into multipliers and splitting every composite multiplier cannot increase its cost, leaving exactly the prime-factor sum computed by the algorithm.

#### Complexity detail

Trial division checks at most the integers through $\lfloor\sqrt{N}\rfloor$ in the prime worst case. Factor divisions only reduce the remaining value, so the total time is $O(\sqrt{N})$. The algorithm stores only the candidate factor, remaining target, and accumulated step count, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Dynamic programming over screen and clipboard states:** models the operations directly, but uses substantially more time and memory than the number-theoretic reduction.
- **One-dimensional divisor DP:** computes the cheapest cost for every length through `n`; it is correct but solves many intermediate targets that the requested answer does not need.
- **Recursive factor search:** can express the same prime-factor recurrence, but iteration avoids recursion and repeated subproblems.
- $n = 1$ needs no operation because the initial screen already matches the target.
- A prime target requires one copy followed by $n - 1$ pastes, for a total cost of `n`.
- Repeated prime factors must be counted separately; for example, $8 = 2 \cdot 2 \cdot 2$ costs `6`, not `2`.

</details>
