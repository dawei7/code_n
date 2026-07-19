# How Many Apples Can You Put into the Basket

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1196 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) |

## Problem Description

### Goal

You have a collection of apples and one basket that can carry at most 5000 units of total weight. The integer array `weight` describes the apples individually, with `weight[i]` giving the weight of the $i$th apple.

Choose any subset of the apples whose combined weight does not exceed the basket's capacity. Return the maximum possible number of apples in such a subset; only the count matters, not which particular apples are chosen when several selections attain it.

### Function Contract

**Inputs**

- `weight`: A list of $n$ apple weights, where $1\le n\le1000$ and $1\le\texttt{weight[i]}\le1000$.

**Return value**

- The greatest number of apples whose combined weight is at most 5000.

### Examples

**Example 1**

- Input: `weight = [100,200,150,1000]`
- Output: `4`

All four apples weigh 1450 in total, within the basket capacity.

**Example 2**

- Input: `weight = [900,950,800,1000,700,800]`
- Output: `5`

All six exceed 5000, while a selection of five fits.

**Example 3**

- Input: `weight = [1000,1000,1000,1000,1000]`
- Output: `5`

The five weights exactly fill the basket.
