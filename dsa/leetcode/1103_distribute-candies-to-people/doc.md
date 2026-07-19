# Distribute Candies to People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1103 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/distribute-candies-to-people/) |

## Problem Description

### Goal

Distribute `candies` among a row of `num_people` people. Give 1 candy to the first person, 2 to the second, and continue increasing the gift by one until the last person receives `num_people` candies.

Then return to the start of the row: the first person is due `num_people + 1`, the second is due `num_people + 2`, and the pattern repeats. When the remaining candies are fewer than the next scheduled gift, give all of them to that person and stop. Return the final distribution, whose length is `num_people` and whose sum is the original number of candies.

### Function Contract

**Inputs**

- `candies`: the total supply $C$, where $1 \leq C \leq 10^9$.
- `num_people`: the number of people $P$, where $1 \leq P \leq 1000$.

Define $G$ as the greatest number of complete scheduled gifts:

$$
G = \left\lfloor \frac{\sqrt{8C+1}-1}{2} \right\rfloor.
$$

**Return value**

An array of length $P$ in which index $i$ contains the total candies received by person $i$.

### Examples

**Example 1**

- Input: `candies = 7, num_people = 4`
- Output: `[1, 2, 3, 1]`

The fourth scheduled gift is 4, but only one candy remains.

**Example 2**

- Input: `candies = 10, num_people = 3`
- Output: `[5, 2, 3]`

After gifts 1, 2, and 3, the first person receives the remaining 4 candies.
