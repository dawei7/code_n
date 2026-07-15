# Jump Game V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1340 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-v/) |

## Problem Description
### Goal
Given an integer array `arr` and a maximum distance `d`, choose any index as a starting position. From index `i`, a jump may move left or right by between 1 and `d` positions without leaving the array.

A destination `j` is legal only when `arr[j] < arr[i]`. In addition, every position strictly between `i` and `j` must also have a value lower than `arr[i]`; the first value greater than or equal to the current value blocks that direction, including every position beyond it.

Return the maximum number of indices that can be visited in one valid sequence, counting its starting index.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1\le n\le1000$ and $1\le\texttt{arr[i]}\le10^5$.
- `d`: the inclusive maximum jump distance, where $1\le d\le n$.

**Return value**

The greatest number of positions in any valid strictly descending jump sequence started at an arbitrary index.

### Examples
**Example 1**

- Input: `arr = [6,4,14,6,8,13,9,7,10,6,12]`, `d = 2`
- Output: `4`

**Example 2**

- Input: `arr = [3,3,3,3,3]`, `d = 3`
- Output: `1`
- Explanation: Equal values are not lower destinations and immediately block further positions.

**Example 3**

- Input: `arr = [7,6,5,4,3,2,1]`, `d = 1`
- Output: `7`

### Required Complexity
- **Time:** $O(n\log n+nd)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use strict descent as a dependency order**

Let `best[i]` be the maximum number of positions visitable when starting at `i`, including `i`. Every legal next index has a strictly smaller value, so `best[i]` depends only on states at lower heights. Sort all indices by `arr[i]` ascending and evaluate them in that order. Equal-valued indices may appear in either order because no jump is permitted between them.

For each index, scan outward separately to the left and right for at most `d` positions. Stop a directional scan as soon as it leaves the array or reaches a value greater than or equal to the starting value. Every lower position encountered before that barrier is a legal destination, so use its already-computed state to update `best[i]` with `1 + best[j]`.

The scan enumerates exactly the legal outgoing jumps: it includes every lower destination within range until the first blocking value, and excludes that blocker and everything behind it. Because lower destinations were processed earlier, each transition extends an already-optimal suffix. Induction through ascending values establishes every state, and the largest state permits the best arbitrary start.

#### Complexity detail

Sorting $n$ indices takes $O(n\log n)$ time. Each index examines at most $d$ positions in each direction, taking $O(nd)$ additional time. The index order and dynamic-programming array use $O(n)$ space.

#### Alternatives and edge cases

- **Memoized depth-first search:** The same strict-descent graph supports cached recursion in $O(nd)$ time, but a legal long chain can approach or exceed Python's recursion depth.
- **Repeated relaxation:** Updating every jump across $n$ full passes eventually finds all path lengths but takes $O(n^2d)$ time.
- **Single position:** The starting index alone gives an answer of 1.
- **Equal values:** They cannot be destinations and block all positions farther in that direction.
- **Lower intermediate values:** They do not block a longer jump and remain possible destinations themselves.
- **Higher or equal barrier:** No position beyond it is reachable directly from the current index.
- **Arbitrary start:** Return the maximum state, not only the state for index 0.
- **Direction changes:** A sequence may alternate left and right as long as each individual jump satisfies the rules.

</details>
