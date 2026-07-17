# Can You Eat Your Favorite Candy on Your Favorite Day?

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1744 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) |

## Problem Description

### Goal

`candiesCount[i]` is the available number of candies of type $i$. Starting on day `0`, you must eat at least one candy per day until none remain, and you must finish every candy of type $i-1$ before eating any of type $i$. You may cross from one type to the next during the same day.

Each query `[favoriteType, favoriteDay, dailyCap]` asks whether some valid eating schedule can include at least one candy of `favoriteType` on `favoriteDay`, while never eating more than `dailyCap` candies on any day. Return one boolean answer per query.

### Function Contract

**Inputs**

- `candiesCount`: positive counts for candy types in their mandatory eating order.
- `queries`: triples `[favoriteType, favoriteDay, dailyCap]`, with zero-indexed days and types.

Let $n$ be the number of candy types and $q$ the number of queries.

**Return value**

- Return a length-$q$ boolean list; each value states whether at least one schedule satisfying that query's cap can eat the requested type on the requested day.

### Examples

**Example 1**

- Input: `candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]`
- Output: `[true,false,true]`
- Explanation: Type `0` can still be in progress on day `2`; type `4` cannot be reached that early under cap `4`; type `2` can be delayed through day `13`.

**Example 2**

- Input: `candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]`
- Output: `[false,true,true,false,false]`
- Explanation: Each query has its own independent cap and therefore its own feasible range of cumulative consumption.

**Example 3**

- Input: `candiesCount = [2,2], queries = [[1,0,3]]`
- Output: `[true]`
- Explanation: On day `0`, eating both type-`0` candies followed by one type-`1` candy is valid.

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Map each type to cumulative candy positions**

Number all candies from one in mandatory eating order. A prefix sum gives the position immediately before each type and the last position belonging to it. If `before` candies have earlier types and `through` candies have types up to the favorite, then the favorite occupies positions `before + 1` through `through`.

**Bound consumption through the favorite day**

By the end of zero-indexed day `d`, at least `d + 1` candies have been eaten because every active day consumes at least one. Under cap `c`, at most `(d + 1) * c` candies can have been eaten. These bounds describe all relevant schedule flexibility.

**Test whether the two intervals overlap**

The favorite type can be eaten on day `d` precisely when the maximum possible cumulative consumption reaches beyond `before`, while the minimum mandatory consumption has not already passed `through`:

$$
\texttt{before} < (d+1)c
\quad\text{and}\quad
d+1 \le \texttt{through}.
$$

The first strict inequality ensures at least one favorite candy can be reached by that day. The second inclusive inequality allows the last favorite candy to be eaten exactly on that day. Together they are sufficient because daily amounts can be adjusted between one and the cap to hit any cumulative total between those bounds.

#### Complexity detail

Building all type prefix sums takes $O(n)$ time. Each of the $q$ queries uses two prefix values and constant arithmetic, so total time is $O(n+q)$. The prefix array stores $n+1$ cumulative counts and uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Sum earlier types per query:** Recomputing `before` from the raw counts takes $O(nq)$ time in the worst case.
- **Simulate days:** Favorite days and caps can reach $10^9$, so day-by-day simulation is neither necessary nor feasible.
- **Day zero:** The minimum cumulative amount is one, not zero.
- **Same-day type transition:** A day may finish one type and immediately begin the next, so reaching `before + 1` within the cap is enough.
- **Exact last candy:** `d + 1 == through` remains feasible because the favorite's last candy may be the mandatory candy for that day.
- **Too early:** If `(d + 1) * dailyCap <= before`, even the fastest schedule cannot reach the favorite type.
- **Too late:** If `d + 1 > through`, eating at least one per day forces the schedule past the favorite type.
- **Large products:** Use integer arithmetic wide enough for `(favoriteDay + 1) * dailyCap`.

</details>
