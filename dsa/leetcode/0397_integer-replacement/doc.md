# Integer Replacement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 397 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Greedy, Bit Manipulation, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-replacement/) |

## Problem Description
### Goal
Starting from a positive integer `n`, repeatedly apply one legal operation. If the current value is even, replace it with half its value. If it is odd, replace it with either one less or one greater.

Return the minimum number of operations needed to reach exactly `1`. Choices at odd values affect later divisibility, so always decrementing or always incrementing is not necessarily optimal. The starting value `1` needs zero operations. Handle the largest signed input safely, since temporarily incrementing an odd value can exceed its original fixed-width range even though the mathematical process remains valid.

### Function Contract
**Inputs**

- `n`: the positive starting integer

**Return value**

- Return the minimum number of allowed operations needed to reach `1`.

### Examples
**Example 1**

- Input: `n = 8`
- Output: `3`

**Example 2**

- Input: `n = 7`
- Output: `4`

**Example 3**

- Input: `n = 4`
- Output: `2`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Always halve an even value**

For even `n`, division by two is the only permitted move and removes one trailing binary zero. Count the operation and shift the value right.

**Choose the odd move by its trailing bits**

An odd value ending in binary `01` should be decremented: that produces an even value with at least one trailing zero. An odd value ending in `11` should normally be incremented because the carry turns the entire trailing run of ones into zeros, enabling several halvings.

**Handle three as the one exception**

Binary `11` would suggest incrementing `3` to `4`, taking two more moves to reach one. Decrementing to `2` also takes two moves, and the conventional rule chooses decrement; more importantly, treating it explicitly prevents arguments about maximizing trailing zeros from overlooking that the target is already nearby.

**Why the bit choice is globally optimal**

After either odd move, the result must be halved next. For endings `01`, decrementing yields a smaller quotient than incrementing without sacrificing trailing zeros. For endings `11` above three, incrementing clears at least two low one bits, while decrementing clears only the final one and leaves a value ending in `10`. The increment route reaches a strictly more divisible state no farther from the target, so the greedy choices preserve an optimal path.

#### Complexity detail

Every one or two operations remove at least one significant binary bit, so the loop performs $O(\log n)$ iterations. The current value and step count use $O(1)$ space.

#### Alternatives and edge cases

- **Memoized recurrence:** explores both choices for odd values and caches results, giving a concise correctness baseline with logarithmically many relevant states.
- **Dynamic programming through every value up to n:** is correct but takes $O(n)$ time and space.
- **Recompute all bits before every odd choice:** preserves the greedy decision but can take $O((\log n)^2)$ total bit inspections.
- **Breadth-first search over integers:** finds a shortest path but stores unnecessary neighboring states.
- Starting at `1` requires zero operations.
- Powers of two use only halving operations.
- The maximum signed 32-bit input may be incremented once, so fixed-width implementations need a wider working type.
- Long trailing runs of binary ones favor incrementing before halving.

</details>
