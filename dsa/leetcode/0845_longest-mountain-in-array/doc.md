# Longest Mountain in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 845 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Dynamic Programming, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-mountain-in-array/) |

## Problem Description
### Goal
An array is a mountain when it has at least three elements and contains an interior peak. Every element before that peak must be strictly increasing toward it, and every element after the peak must be strictly decreasing away from it. Consequently, neither side may be empty, and equal adjacent values cannot occur inside a mountain.

Given an integer array `arr`, find the maximum length among all contiguous subarrays that satisfy this mountain definition. Return `0` when no mountain subarray exists.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \leq n \leq 10^4$ and $0 \leq \texttt{arr[i]} \leq 10^4$.

**Return value**

Return the length of the longest subarray that is strictly increasing to one interior peak and then strictly decreasing. Return `0` if no such subarray exists.

### Examples
**Example 1**

- Input: `arr = [2,1,4,7,3,2,5]`
- Output: `5`

The subarray `[1,4,7,3,2]` is the longest mountain.

**Example 2**

- Input: `arr = [2,2,2]`
- Output: `0`

Equal adjacent values cannot form either strict side of a mountain.

**Example 3**

- Input: `arr = [0,1,0]`
- Output: `3`

The entire array rises to `1` and then falls.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent a mountain by its rising and falling edges**

Scan adjacent pairs from left to right. Let `up` count consecutive strictly increasing edges in the current candidate and `down` count the strictly decreasing edges that follow them. A valid mountain exists exactly when both counts are positive, and its length is then `up + down + 1` because a run of edges has one more vertex than edges.

**Reset only when the current shape can no longer continue**

An equal pair cannot belong to a strict mountain, so it clears both counters. A new ascent after a descent also starts a new candidate: the earlier candidate has already finished, while the current lower endpoint can be the first element of another rising side. Otherwise, an ascent increments `up`, and a descent increments `down`.

After each pair, update the answer only when `up > 0` and `down > 0`. At that moment the tracked segment has a nonempty strict rise followed by a nonempty strict fall, so it is a mountain. Conversely, every mountain's increasing edges are accumulated before its peak and its decreasing edges afterward; neither reset condition occurs inside it. The scan therefore measures every possible mountain and retains the longest.

#### Complexity detail

The scan examines each of the $n-1$ adjacent pairs once, so it takes $O(n)$ time. The two edge counts and the best length require $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Expand from every possible start:** Walking to the end of the increasing run and then the decreasing run for every start is correct, but repeated traversal can take $O(n^2)$ time.
- **Prefix and suffix lengths:** Arrays of increasing-run and decreasing-run lengths make each peak easy to evaluate in $O(n)$ time, but require $O(n)$ auxiliary space.
- **Entirely monotonic input:** A strictly increasing or strictly decreasing array has no interior peak with both required sides, so the answer is `0`.
- **Plateaus:** Any equal adjacent values split candidates because both sides must be strict.
- **Adjacent mountains:** The falling endpoint of one mountain can also begin the rise of the next, which is why a new ascent resets at its left endpoint rather than skipping it.
- **Short arrays:** Fewer than three elements can never contain a mountain.
- **Multiple peaks:** Each ascent after a descent begins a fresh candidate, and the maximum is preserved across all completed mountains.

</details>
