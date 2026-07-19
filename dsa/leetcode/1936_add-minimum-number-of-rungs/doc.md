# Add Minimum Number of Rungs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1936 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/add-minimum-number-of-rungs/) |

## Problem Description
### Goal
A ladder's existing rung heights are given by the strictly increasing integer
array `rungs`. You begin on the floor at height zero and want to reach the
highest existing rung. From the floor or a rung, you may climb to the next
higher rung only when the height difference is at most `dist`.

You may add rungs at positive integer heights that do not already contain a
rung. Insert as few new rungs as possible so that every successive climb from
height zero through the final existing rung respects the distance limit.
Return the minimum number inserted.

### Function Contract
**Inputs**

- `rungs`: a strictly increasing list of $N$ positive integer heights, where
  $1 \le N \le 10^5$ and every height is at most $10^9$.
- `dist`: the maximum permitted height difference in one climb, where
  $1 \le \texttt{dist} \le 10^9$.

**Return value**

- The minimum number of positive-integer rung heights that must be inserted to
  make the last existing rung reachable from height zero.

### Examples
**Example 1**

- Input: `rungs = [1, 3, 5, 10], dist = 2`
- Output: `2`

For example, adding rungs at heights `7` and `8` makes every climb at most two.

**Example 2**

- Input: `rungs = [3, 6, 8, 10], dist = 3`
- Output: `0`

**Example 3**

- Input: `rungs = [3, 4, 6, 7], dist = 2`
- Output: `1`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Handle each gap independently**

Include the floor as the previous reachable height, initially zero. For every
existing rung, let $G$ be its distance above the previous existing rung. New
rungs placed inside this gap cannot help another gap, so minimizing the total
is equivalent to minimizing each gap separately and summing the results.

**Count the required intermediate steps**

If $k$ new rungs are placed inside a gap, they divide it into $k+1$ climbs.
All climbs can be at most `dist` exactly when
$k+1 \ge \lceil G/\texttt{dist}\rceil$. The minimum is therefore

$$
k = \left\lceil \frac{G}{\texttt{dist}} \right\rceil - 1
  = \left\lfloor \frac{G-1}{\texttt{dist}} \right\rfloor.
$$

The second form is the integer calculation `(G - 1) // dist`. It correctly
returns zero when $G$ is at most `dist`, and it avoids adding an unnecessary
rung when $G$ is an exact multiple of `dist`. Sum this value while advancing
the previous height to each existing rung. Every gap receives the fewest
possible insertions, so their sum is globally minimal.

#### Complexity detail

The scan performs constant work for each of the $N$ existing rungs, giving
$O(N)$ time. It keeps only the previous height and running total, so the
auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Insert simulated rungs one at a time:** Repeatedly advance by `dist` until
  an existing rung is reachable. This is correct, but its time depends on the
  potentially enormous number of inserted rungs rather than only on $N$.
- **Use `G // dist`:** This overcounts by one whenever $G$ is exactly divisible
  by `dist`, because the existing endpoint already completes the final climb.
- The floor at height zero is the starting endpoint of the first gap and must
  not be omitted.
- A gap exactly equal to `dist` needs no new rung.
- A gap of `dist + 1` needs exactly one new rung.
- Existing heights are strictly increasing, so every processed gap is
  positive.
- Inserted heights must be positive integers, and the formula is achievable by
  spacing them no more than `dist` apart.

</details>
