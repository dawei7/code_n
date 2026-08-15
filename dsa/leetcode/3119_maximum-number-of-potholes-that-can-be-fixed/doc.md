# Maximum Number of Potholes That Can Be Fixed

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3119 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/) |

## Problem Description

### Goal

You are given a string `road` containing only `x` and `.`. Each `x` represents a pothole, while each `.` represents a smooth section of road. You also have an integer `budget` available for repairs.

One repair operation may fix $k$ consecutive potholes for a price of $k+1$. You may perform multiple operations, provided their total price does not exceed `budget`. Return the maximum number of potholes that can be fixed. Repaired positions must come from consecutive potholes within the same uninterrupted `x` block; an operation cannot cross a smooth section.

### Function Contract

**Inputs**

- `road`: A string of length $n$ containing only `x` and `.`.
- `budget`: The maximum total repair price.

The constraints are $1 \le n \le 10^5$ and $1 \le \texttt{budget} \le 10^5+1$. Let $r$ be the number of maximal consecutive `x` blocks.

**Return value**

Return the largest number of potholes repairable without spending more than `budget`.

### Examples

#### Example 1

- **Input:** `road = "..", budget = 5`
- **Output:** `0`
- **Explanation:** The road contains no potholes.

#### Example 2

- **Input:** `road = "..xxxxx", budget = 4`
- **Output:** `3`
- **Explanation:** Repairing three consecutive potholes costs `3 + 1 = 4`.

#### Example 3

- **Input:** `road = "x.x.xxx...x", budget = 14`
- **Output:** `6`
- **Explanation:** Repairing all four pothole blocks costs `(1 + 1) + (1 + 1) + (3 + 1) + (1 + 1) = 10`, which is within budget.
