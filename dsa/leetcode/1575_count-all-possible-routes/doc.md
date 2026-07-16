# Count All Possible Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1575 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/count-all-possible-routes/) |

## Problem Description
### Goal

There are $N$ cities on a number line. City `i` is located at coordinate `locations[i]`, and every coordinate is distinct. A journey begins at the city indexed by `start` with a fixed amount of `fuel`, and its destination is the city indexed by `finish`.

From the current city `i`, a route may move to any different city `j`. That move consumes exactly $\lvert\texttt{locations[i]}-\texttt{locations[j]}\rvert$ units of fuel. Fuel may never become negative, cities may be visited repeatedly, and a route may continue traveling after visiting `finish`.

Count every route that is at `finish` after zero or more moves without spending more than the available fuel. Stopping at different visits produces different valid routes; in particular, the empty route counts when `start == finish`. Return the total modulo $1{,}000{,}000{,}007$.

### Function Contract
**Inputs**

- `locations`: An array of $N$ distinct integer coordinates, where $2 \le N \le 100$ and $1 \le \texttt{locations[i]} \le 10^9$.
- `start`: The zero-based index of the starting city, where $0 \le \texttt{start} < N$.
- `finish`: The zero-based index of the destination city, where $0 \le \texttt{finish} < N$.
- `fuel`: The initial fuel amount, where $1 \le \texttt{fuel} \le 200$.

**Return value**

Return the number of valid routes from `start` to `finish`, modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `locations = [2, 3, 6, 8, 4], start = 1, finish = 3, fuel = 5`
- Output: `4`

**Example 2**

- Input: `locations = [4, 3, 1], start = 1, finish = 0, fuel = 6`
- Output: `5`

**Example 3**

- Input: `locations = [5, 2, 1], start = 0, finish = 2, fuel = 3`
- Output: `0`

### Required Complexity

- **Time:** $O(N^2F)$
- **Space:** $O(NF)$

<details>
<summary>Approach</summary>

#### General

**Make remaining fuel part of the state**

The same city can be revisited with different amounts of fuel, and those situations permit different future moves. Define `count_from(city, remaining)` as the number of valid routes that begin in that state and eventually choose to stop at `finish`.

A state contributes one route immediately when `city == finish`: stop without making another move. This does not end the recurrence, because routes that leave `finish` and return later must also be counted.

**Spend fuel on every possible next city**

For each `next_city != city`, compute the move cost as the absolute coordinate difference. Distinct coordinates guarantee that this cost is positive. If it does not exceed `remaining`, add the routes from `count_from(next_city, remaining - cost)`.

Every recursive transition strictly decreases the remaining fuel, so the state graph is acyclic even though routes may revisit cities. Memoizing by `(city, remaining)` evaluates each reachable state once and applies the modulus to keep counts bounded.

Every valid route has a unique first move, unless it stops immediately at `finish`. The recurrence partitions routes into exactly those disjoint choices. Conversely, every allowed transition preserves nonnegative fuel and every counted stopping state is at `finish`, so no invalid route is included.

#### Complexity detail

There are at most $N(F+1)$ city-and-fuel states. Each state considers $N-1$ possible next cities, giving $O(N^2F)$ time.

The memo table stores at most $O(NF)$ results. The recursion depth is at most $F$ because every move costs at least one unit, so its stack does not exceed the same asymptotic space bound.

#### Alternatives and edge cases

- **Bottom-up dynamic programming:** evaluate remaining fuel from zero through $F$ and fill the same recurrence iteratively. It has the same $O(N^2F)$ time and $O(NF)$ space bounds.
- **Recursion without memoization:** enumerate route prefixes directly. It is correct but repeatedly solves identical states and can take exponential time.
- **Sort cities and restrict moves:** a route may jump between any pair of cities, so sorting alone does not remove the need to consider both directions and all affordable destinations.
- **Start equals finish:** count the zero-move route immediately, plus every affordable route that leaves and later returns.
- **Reach finish multiple times:** each visit offers a distinct stopping point, while continuing after a visit may create further valid routes.
- **Insufficient fuel:** if no sequence can reach `finish`, the answer is zero.
- **Exact fuel use:** ending with zero remaining fuel is valid.
- **Distinct coordinates:** every move has positive cost, which prevents zero-cost cycles and makes the fuel-state recurrence well founded.
- **Modulo arithmetic:** reduce accumulated counts modulo $1{,}000{,}000{,}007$ at each state.

</details>
