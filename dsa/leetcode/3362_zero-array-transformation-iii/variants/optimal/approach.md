## General

Each retained query can contribute one decrement independently at every index it covers. Therefore a retained set is feasible exactly when index $i$ is covered by at least `nums[i]` retained intervals. Maximizing removals is the same as selecting the fewest intervals that meet all these coverage requirements.

Sweep the indices from left to right after sorting queries by their left endpoint. Add every query that has started to a max-heap keyed by right endpoint. A difference array records when already selected queries expire, so `coverage` is the number of selected intervals still covering the current index.

If `coverage` is below the current requirement, select an available interval whose right endpoint is farthest away. This choice is safe by exchange: suppose another minimum retained set instead selects a currently available interval ending earlier. Replacing that interval with the farthest-ending one preserves coverage at the current index and cannot reduce coverage at any later index. Repeating this exchange justifies every greedy selection.

Each chosen interval raises current coverage by one and schedules a decrement immediately after its right endpoint. If the heap is empty, or even its largest endpoint is before the current index, no remaining interval can fill the deficit and the transformation is impossible. Otherwise the sweep finishes with the minimum number of selected queries, so subtracting that count from $q$ gives the maximum removable count.

## Complexity detail

Let $n$ be the length of `nums` and $q$ the number of queries. Sorting costs $O(q\log q)$. Every query enters the heap once and can leave it at most once, giving another $O(q\log q)$; the array sweep and difference updates take $O(n)$. Total time is $O(n+q\log q)$.

The sorted query list and heap use $O(q)$ space, while the expiration difference array uses $O(n)$, for $O(n+q)$ auxiliary space.

The benchmark defines `size` as $n=q$. Every query spans the full array, while requirements increase by one at each successive index. The heap method processes each query with logarithmic work. A correct greedy baseline that linearly scans all remaining queries to find the farthest endpoint for every new selection performs $\Theta(nq)$ work.

## Alternatives and edge cases

- **Linear scan for the best active query:** It implements the same correct greedy rule but costs $O(nq)$ in the benchmark's increasing-demand workload.
- **Select every query:** This proves feasibility when possible but does not maximize how many queries are removed.
- **Choose the earliest-ending interval:** It can consume a short query that helps only now and force an additional selection at a later index.
- **Binary search on the number removed:** Feasibility depends on which intervals remain, not only their count, so this does not avoid the selection problem.
- **Zero requirement:** No query needs to be selected at that index, although newly started queries still become candidates for later positions.
- **Expired queries:** An available heap entry ending before the current index cannot fill a deficit; if the maximum endpoint is expired, every heap entry is unusable.
- **Duplicate intervals:** They are distinct queries and may each contribute one unit of coverage.
- **Insufficient total coverage:** A deficit with no active candidate makes the answer `-1`, even if unused queries start later.

