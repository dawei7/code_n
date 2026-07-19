# Watering Plants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2079 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/watering-plants/) |

## Problem Description

### Goal

Plants numbered from $0$ through $n-1$ stand at matching coordinates along a line, while a river is located at coordinate $-1$. Begin at the river with a watering can filled to `capacity`, walk from left to right, and water every plant completely in index order.

After watering a plant, return to the river and refill only when the remaining water is insufficient for the next plant. Early refills are forbidden. Moving one coordinate in either direction costs one step. Determine the total steps needed to finish all plants.

### Function Contract

**Inputs**

- `plants`: a list of $n$ positive water requirements, where $1 \le n \le 1000$ and $1 \le \texttt{plants[i]} \le 10^6$.
- `capacity`: the full can capacity, where $\max(\texttt{plants}) \le \texttt{capacity} \le 10^9$.

**Return value**

- Return the total number of unit-coordinate steps walked until every plant has been watered.

### Examples

**Example 1**

- Input: `plants = [2,2,3,3], capacity = 5`
- Output: `14`
- Explanation: Refills are needed before plants 2 and 3, adding their return trips to the ordinary left-to-right steps.

**Example 2**

- Input: `plants = [1,1,1,4,2,3], capacity = 4`
- Output: `30`
- Explanation: The gardener refills after plant 2 and again before plants 4 and 5.

**Example 3**

- Input: `plants = [7,7,7,7,7,7,7], capacity = 8`
- Output: `49`
- Explanation: Every plant after the first requires a river trip, so the total equals $1+3+5+\cdots+13=49$.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the unavoidable forward progress**

Without refills, reaching each next plant costs one step: river to plant 0, then plant 0 to plant 1, and so on. Add this one step while processing every plant, giving a baseline of $n$ steps.

**Charge only the detour before a dry plant**

Before plant `index`, the gardener is at plant `index - 1`. If the remaining water is too small for the current requirement, returning from coordinate `index - 1` to the river costs `index` steps. Walking from the river to plant `index` costs `index + 1` steps, whereas the baseline already counted the one direct step. The refill therefore contributes exactly `2 * index` additional steps. Reset the remaining water to `capacity`, then water the plant.

**Mirror the mandated refill timing**

Checking capacity immediately before each plant is equivalent to checking the next requirement immediately after the preceding plant. Use strict insufficiency: when the remaining amount equals the next requirement, the plant can be watered completely and no refill is permitted. Since every requirement is at most `capacity`, one refill is always enough.

#### Complexity detail

The simulation visits each of the $n$ plant requirements once and performs constant work per plant, for $O(n)$ time. The remaining-water and step counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Simulate every walked coordinate:** Moving a position variable one step at a time is correct, but repeated river trips can make the running time proportional to the answer, which is $O(n^2)$.
- **Prefix-sum refill groups:** Partitioning plants into maximal consecutive groups that fit in one can also works, but it encodes the same greedy simulation with more bookkeeping.
- **Exact remaining water:** Equality is sufficient; refill only when `water < plants[index]`.
- **No refill needed:** The result is simply $n$ when all requirements fit into the initial can cumulatively.
- **Single plant:** Starting at the river and moving to coordinate 0 costs exactly one step.
- **Refill before the final plant:** The return trip still includes walking back out to that plant; the process does not end at the river.

</details>
