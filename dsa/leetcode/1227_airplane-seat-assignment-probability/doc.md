# Airplane Seat Assignment Probability

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1227 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Brainteaser, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/airplane-seat-assignment-probability/) |

## Problem Description

### Goal

There are `n` passengers boarding an airplane with exactly `n` seats. Passenger $i$ is assigned seat $i$. The first passenger has lost their ticket and chooses one of the seats uniformly at random.

Each later passenger takes their own assigned seat when it is still available. If that seat is occupied, the passenger instead chooses uniformly at random from all remaining unoccupied seats.

Return the probability that passenger `n` ultimately sits in seat `n`.

### Function Contract

**Inputs**

- `n`: The number of passengers and seats, where $1\le n\le10^5$.

**Return value**

- The probability, as a floating-point value, that the last passenger occupies their assigned seat.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `1.0`

The only passenger necessarily chooses the only seat.

**Example 2**

- Input: `n = 2`
- Output: `0.5`

The first passenger chooses seat `1` or seat `2` with equal probability.

**Example 3**

- Input: `n = 3`
- Output: `0.5`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Handle the one-passenger base case.** When `n` is `1`, the first passenger is also the last and seat `1` is the only choice, so the probability is `1.0`.

**Condition on the first random seat.** For $n>1$, choosing seat `1` immediately guarantees that every later passenger finds their own seat, while choosing seat `n` immediately prevents the last passenger from doing so. If the first passenger chooses an intermediate seat $k$, passengers before $k$ sit normally and passenger $k$ becomes the next displaced passenger. The remaining uncertain process has the same structure on a smaller set containing the original first and last seats.

**Derive the invariant probability.** Assume every smaller nontrivial instance succeeds with probability $1/2$. Among the first passenger's $n$ equally likely choices, seat `1` contributes probability $1$, seat `n` contributes $0$, and each of the $n-2$ intermediate choices contributes $1/2$. Therefore

$$
P_n=\frac{1+(n-2)/2}{n}=\frac12.
$$

The base $P_2=1/2$ starts the induction, proving that every `n > 1` has the same answer.

#### Complexity detail

The result requires one comparison and returns one of two constants, so time and auxiliary space are both $O(1)$.

#### Alternatives and edge cases

- **Linear probability recurrence:** Computing all values from $P_1$ through $P_n$ reproduces the result but takes $O(n)$ time.
- **Monte Carlo simulation:** Random trials approximate the probability and introduce sampling error, while the exact value is available directly.
- **Explicit state distribution:** Tracking which passenger is displaced is correct but retains states whose aggregate probability collapses to the same symmetry.
- **One passenger:** This is the only case with probability `1.0`.
- **Every larger input:** The answer is exactly `0.5`, not merely an asymptotic limit.
- **Floating-point return:** Both representable outputs, `1.0` and `0.5`, are exact in binary floating point.

</details>
