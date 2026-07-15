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

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Make every chosen slot as light as possible.** Sort the apple weights in ascending order. For any target count $c$, the $c$ lightest apples have no greater total weight than any other selection of $c$ apples. Consequently, if that lightest prefix does not fit, no selection of the same size can fit; if it does fit, it is a valid selection.

**Grow the feasible prefix greedily.** Traverse the sorted weights while maintaining the current total. Add the next apple when the new total is at most 5000. The first weight that would exceed capacity proves that the current prefix count is maximal by the lightest-prefix argument, so return it immediately. If no weight causes overflow, every apple fits and the answer is $n$.

#### Complexity detail

Sorting $n$ weights costs $O(n\log n)$ time, and the prefix scan costs $O(n)$, for an overall $O(n\log n)$ bound. Python's sorted copy may use $O(n)$ auxiliary space; the running total and count themselves require $O(1)$ space.

#### Alternatives and edge cases

- **Repeated minimum selection:** Finding and removing the lightest remaining apple on every step is correct but can take $O(n^2)$ time.
- **Counting by weight:** Because weights lie between 1 and 1000, a fixed frequency array can avoid comparison sorting and run in $O(n+1000)$ time, at the cost of a less general implementation.
- **All apples fit:** Exhausting the sorted list returns its full length.
- **Exact capacity:** A cumulative weight of exactly 5000 is valid; only a strictly larger sum stops selection.
- **Single apple:** Its weight is at most 1000, so it always fits.
- **Duplicate weights:** Equal-weight apples are interchangeable, and each occurrence still contributes one to the count.
- **Input order:** Heavy apples appearing first must not prevent lighter later apples from being selected.
- **Positive weights:** Since every weight is at least 1, adding another apple never decreases the cumulative weight.

</details>
