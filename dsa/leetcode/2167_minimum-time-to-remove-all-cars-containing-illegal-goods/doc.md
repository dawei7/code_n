# Minimum Time to Remove All Cars Containing Illegal Goods

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2167 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) |

## Problem Description
### Goal

A binary string `s` describes a sequence of train cars in their current order.
A character `0` marks a car without illegal goods, while `1` marks a car that
contains illegal goods.

Any number of removal operations may be performed. Removing the car currently
at the left end costs one unit of time, and removing the car currently at the
right end also costs one unit. A car at any position may instead be removed
directly for two units. End removals can therefore discard legal cars on the
way to illegal ones, while a direct removal need not disturb either end.

Return the minimum total time needed to leave no car containing illegal goods.
The remaining sequence may contain legal cars or be empty; an empty sequence
already satisfies the requirement.

### Function Contract
**Inputs**

- `s`: a binary string of length $n$, where $1\le n\le 2\cdot 10^5$ and every
  character is either `0` or `1`.

The order of cars is fixed except for cars disappearing through removals.

**Return value**

Return the minimum integer cost of removing every car represented by `1`.

### Examples
**Example 1**

- Input: `s = "1100101"`
- Output: `5`

One optimal plan removes two cars from the left, one from the right, and the
remaining illegal car directly, for a total cost of $2+1+2=5$.

**Example 2**

- Input: `s = "0010"`
- Output: `2`

The only illegal car can be removed directly for two units, or the two-car
suffix can be removed from the right for the same cost.

**Example 3**

- Input: `s = "0000"`
- Output: `0`

No operation is required when every car is already legal.
