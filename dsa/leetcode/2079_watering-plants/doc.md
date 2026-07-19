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
