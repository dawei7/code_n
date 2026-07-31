# Watering Plants II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [watering-plants-ii](https://leetcode.com/problems/watering-plants-ii/) |

## Problem Description

### Goal

Alice and Bob must water a row of $n$ plants labeled from $0$ through $n-1$. Alice starts at the left end and moves right, while Bob starts at the right end and moves left. They begin simultaneously, watering one plant per step regardless of its required amount. Each has a separate watering can that starts full with capacity `capacityA` or `capacityB`.

The assigned gardener must completely water the next plant if the current can holds enough water. Otherwise, that gardener instantly refills the can before watering it. If both gardeners reach the same remaining plant, the one with more water left handles it; Alice handles an exact tie. Given each plant's required amount, return the total number of refills used before all plants are watered.

### Function Contract

**Inputs**

- `plants`: A 0-indexed integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{plants[i]} \le 10^6$.
- `capacityA`: Alice's can capacity, where $\max(\texttt{plants}) \le \texttt{capacityA} \le 10^9$.
- `capacityB`: Bob's can capacity, where $\max(\texttt{plants}) \le \texttt{capacityB} \le 10^9$.

**Return value**

Return the number of times Alice and Bob refill their cans while watering all plants.

### Examples

**Example 1**

- Input: `plants = [2, 2, 3, 3], capacityA = 5, capacityB = 5`
- Output: `1`
- Explanation: Alice can water her first two plants without refilling. Bob has only two units left when he reaches the plant needing three, so he refills once.

**Example 2**

- Input: `plants = [2, 2, 3, 3], capacityA = 3, capacityB = 4`
- Output: `2`
- Explanation: After the outer plants, neither gardener has enough for the next assigned plant, so each refills once.

**Example 3**

- Input: `plants = [5], capacityA = 10, capacityB = 8`
- Output: `0`
- Explanation: Both reach the only plant; Alice has more water and can water it without refilling.
