## General

**Solve the suffix problem first**

From a current position `i`, every future decision depends only on positions to its right. Earlier positions and the path used to reach `i` do not affect which jumps are legal or what future costs will be paid.

This gives a backward dynamic-programming state:

`f[i]` is the minimum total cost of a valid path that starts at zero-based index `i` and reaches the final index, including the cost `coins[i]` itself.

If no such path exists, `f[i]` remains positive infinity.

The public path uses one-based indices, but the implementation stores and computes with Python's zero-based indices. Conversion happens only when a chosen index is appended to the answer.

**Handle a blocked destination immediately**

Every successful path must visit the final position. If `coins[-1] == -1`, that position is forbidden, so no path can succeed regardless of earlier costs or jump length. The exact solution immediately returns an empty list.

When the destination is valid, its state is the base case:

`f[n - 1] = coins[n - 1]`.

Starting at the destination requires no jump, but its visit cost still counts.

**Fill minimum suffix costs from right to left**

For each index `i` from `n - 2` down to zero:

- if `coins[i] == -1`, leave `f[i]` as infinity because the position cannot be visited;
- otherwise, examine every possible next index from `i + 1` through `min(n - 1, i + maxJump)`.

If the next position is `j`, a path pays `coins[i]` now and then follows an optimal suffix costing `f[j]`. Its candidate total is:

`coins[i] + f[j]`.

The strict update `if f[i] > f[j] + coins[i]` keeps the smallest candidate.

A blocked or unreachable `j` has `f[j] = inf`, so adding the finite current cost still gives infinity and cannot improve `f[i]`. The inner loop therefore does not need a separate blocked-position condition.

**Why backward order is necessary**

Every transition from `i` uses only larger indices `j`. By iterating downward, all those `f[j]` values have already been finalized when `f[i]` is computed. This makes each state a direct minimum over known answers rather than a guess that needs later revision.

**Detect an unreachable start**

After filling the table, `f[0] == inf` means no allowed sequence of jumps connects the starting position to the destination. In that case, the method returns an empty list.

The contract guarantees that the first position itself is not blocked, but it can still be stranded by blocked positions or a small `maxJump`.

**Reconstruct without a separate next-pointer array**

The most subtle part of the exact source is its reconstruction. It stores only minimum suffix costs, not the chosen next index.

Start with `s = f[0]`, the cost still represented by the path to reconstruct. Scan indices from left to right. Whenever `f[i] == s`:

1. choose index `i` and append `i + 1` to convert it to one-based form;
2. subtract `coins[i]` from `s`.

After choosing a current index `p`, the new `s` equals:

`f[p] - coins[p]`,

which is the minimum `f[j]` among legal next positions. Therefore, the next chosen index must be the earliest later index whose `f` value equals this remaining cost.

**Why the scan cannot jump too far**

The reconstruction does not explicitly test `i - p <= maxJump`, which may initially look unsafe. However, finite `f[p]` was produced from at least one legal next position `j` within that jump range, and that position has `f[j] == s`.

The scan proceeds in increasing index order. It must encounter some matching legal `j <= p + maxJump` before it could reach any index farther than the allowed range. If an even earlier matching index appears, it is also within the range and is a legal transition with the same minimum cost.

This argument repeats after each selected position, so every reconstructed jump respects `maxJump` even though the check is implicit in the DP equality.

**Why this produces the lexicographically smallest minimum-cost path**

All valid paths begin with one-based index one. Among minimum-cost continuations from a selected position, lexicographic order is decided first by the next chosen index. The left-to-right scan chooses the smallest possible next index whose suffix cost preserves the optimum.

Once that smallest next index is fixed, the same rule chooses the smallest optimal index after it. Repeating this greedy reconstruction yields the lexicographically smallest path among all paths with cost `f[0]`.

The strict inequality used while building `f` does not lose tie information because reconstruction consults every index with the required cost rather than relying on a stored transition.

**Walk through the first example**

For `coins = [1, 2, 4, -1, 2]` and `maxJump = 2`:

- the destination has `f[4] = 2`;
- index three is blocked;
- index two can jump to four, so `f[2] = 4 + 2 = 6`;
- index one can reach index two, giving `f[1] = 2 + 6 = 8`;
- index zero can choose index one for total nine or index two for total seven, so `f[0] = 7`.

Reconstruction begins with `s = 7`. Index zero matches, so append one and reduce `s` to six. Index two is the first later state with `f[2] = 6`, so append three and reduce `s` to two. Index four matches two, so append five. The result is `[1, 3, 5]`.

**Why the dynamic program is correct**

The destination state is correct because its only path is visiting itself. Assume every state to the right of `i` correctly stores its minimum suffix cost.

Any valid path from `i` must choose one legal next index `j` in the allowed forward range. After that jump, its cheapest possible continuation costs `f[j]` by the induction assumption, so the best path through `j` costs `coins[i] + f[j]`. Taking the minimum across every legal next index therefore gives exactly `f[i]`. Blocked or unreachable states contribute no finite candidate.

Backward induction proves every finite table value correct. The reconstruction selects only transitions achieving those values and chooses the smallest tied index, so it returns exactly the required path.

## Complexity detail

Let `N` be the number of positions and `B = maxJump`.

There are `N` DP states. Each state examines at most `B` later positions, giving `O(N * B)` time. Reconstruction scans the array once in `O(N)` time, which is dominated by the DP bound.

The `f` array stores one value per position, using `O(N)` space. The answer can contain up to `N` indices; as returned output, that is also `O(N)`. All other variables use constant space.

Infinity is used as an unreachable sentinel. Adding a finite cost to Python's floating-point infinity remains infinity, so comparisons behave as intended. All actual finite costs are integers and compare exactly against one another.

## Alternatives and edge cases

- **Store a `next` array:** During DP, record the chosen next index along with each minimum cost, preferring smaller indices on ties. Reconstruction then follows pointers. This is more explicit but requires another `O(N)` array.

- **Top-down memoization:** Recursively try each next jump and cache suffix costs. It has the same `O(NB)` time but adds call-stack overhead and requires careful tie-aware path reconstruction.

- **Shortest-path graph interpretation:** Treat positions as vertices and legal jumps as directed edges. A DAG shortest-path algorithm is equivalent to this backward DP; general-purpose Dijkstra is unnecessary because all edges move forward.

- **Segment tree or monotonic optimization:** Faster range-minimum structures may reduce transition lookup, but lexicographic reconstruction and constraints make the direct `O(NB)` method appropriate.

- **Destination blocked:** Return an empty list before allocating the DP array.

- **Start valid but unreachable:** `f[0]` remains infinity and the result is empty.

- **Single position:** The start is also the destination. Its finite state is selected and the returned path is `[1]`.

- **Blocked intermediate index:** Its state stays infinite, so it can neither improve a predecessor nor appear during reconstruction.

- **Equal-cost choices:** Scanning indices in ascending order chooses the smaller next index, which is exactly the first lexicographic difference.

- **Zero-cost positions:** Subtracting zero leaves `s` unchanged. The increasing scan can still choose successive zero-cost optimal states, and the DP guarantee keeps each jump legal.

- **Large `maxJump`:** The inner upper bound is clipped at `n`, preventing out-of-range access.

- **One-based output:** Internal index `i` must be appended as `i + 1`. Returning zero-based indices would violate the contract.

- **Cost includes endpoints:** Initializing the destination to its own cost and adding every current `coins[i]` ensures both start and destination are paid.

- **Negative one is not a cost:** It is a blocked marker. Such positions must remain unreachable rather than being treated as attractive negative-cost visits.
