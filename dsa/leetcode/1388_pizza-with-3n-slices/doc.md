# Pizza With 3n Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1388 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/pizza-with-3n-slices/) |

## Problem Description

### Goal

A circular pizza is divided into $3n$ slices of possibly different sizes. In each round, Alice chooses any remaining slice. Bob then takes the next remaining slice counterclockwise from Alice's choice, and Charlie takes the next remaining slice clockwise. The process repeats until no slices remain.

Alice therefore receives exactly $n$ slices, and no two slices she originally chooses can be adjacent in the circle. Given the slice sizes in circular order, maximize the total size Alice can obtain.

### Function Contract

**Inputs**

- `slices`: a circular array of positive sizes with length $L$, where $L$ is divisible by $3$.
- Let $C = L / 3$ be the exact number of slices Alice receives.

**Return value**

- The maximum sum of exactly $C$ pairwise nonadjacent circular slices.

### Examples

**Example 1**

- Input: `slices = [1,2,3,4,5,6]`
- Output: `10`

**Example 2**

- Input: `slices = [8,9,8,6,1,1]`
- Output: `16`

**Example 3**

- Input: `slices = [4,1,2,5,8,3]`
- Output: `12`

### Required Complexity

- **Time:** $O(LC)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Break the circular conflict.** The first and last slices are adjacent, so they cannot both be chosen. Every valid selection therefore belongs to at least one of two linear cases: exclude the last slice, or exclude the first slice. Solve both and keep the larger sum.

**Track an exact selection count.** For one linear array, let the dynamic-programming state after a prefix record the best sum for each count from `0` through `C`. When processing a slice, either skip it and retain the previous-prefix value, or take it and add its size to the state from two prefixes earlier with one fewer selected slice.

Initialize count zero to sum zero and all impossible positive counts to negative infinity. This prevents a state from claiming more selections than its prefix can supply. Rolling the arrays for the previous one and two prefixes preserves every recurrence dependency.

The recurrence considers both possibilities for the final slice of every prefix, so it covers all nonadjacent exact-count selections. The two outer cases cover the circular boundary, establishing the global optimum.

#### Complexity detail

Each linear case processes $O(L)$ slices and updates $C$ counts, giving $O(LC)$ time. Three rolling count arrays use $O(C)$ space.

#### Alternatives and edge cases

- **Full table dynamic programming:** Store every prefix-and-count state. It has the same $O(LC)$ time but uses $O(LC)$ space.
- **Rescan prior endpoints:** For every chosen count and ending position, search all compatible previous endpoints. It is correct but takes $O(L^2C)$ time.
- **Greedy largest slice:** Taking the current largest value can block two moderately large neighbors whose combined contribution is better.
- **First and last conflict:** Solve two linear exclusions; never allow both circular endpoints.
- **Exactly `C` selections:** Do not maximize over smaller counts, even though all sizes are positive.
- **Three slices:** Alice chooses the single largest slice.
- **Equal sizes:** Any valid $C$ nonadjacent positions give the same total.

</details>
