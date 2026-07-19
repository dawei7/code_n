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
