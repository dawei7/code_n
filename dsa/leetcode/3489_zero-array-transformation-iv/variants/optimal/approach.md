## General

**Treat every array index as an independent subset-sum problem.** Query $q=[l,r,v]$ lets the algorithm independently choose any subset of indices in its range. For a fixed index $i$, that query contributes either:

- zero decrement if $i$ is not selected; or
- exactly $v$ if $i$ is selected and $l\le i\le r$.

Therefore, after a prefix of queries, `nums[i]` can become zero exactly when its target value can be formed as a subset sum of the `value` fields from applicable queries. Decisions for different indices do not conflict because one query may select any combination of indices in its range. Solving these subset sums independently is consequently both necessary and sufficient.

**Represent reachable sums as bits in one integer.** `possible[i]` is a bitset. Bit $s$ is one when total decrement $s$ is reachable for index $i$ from processed queries. Every index starts with integer one, whose only set bit is bit zero, because choosing no queries produces decrement zero.

When an applicable query has value $v$, shifting

`possible[index] << value`

moves every reachable sum $s$ to $s+v$, representing the choice to apply this query at that index. OR-ing the shifted and original bitsets retains both choices:

`possible[index] |= possible[index] << value`.

Because the update derives all new bits from the pre-update value within one expression, the same query value is used at most once. This is the standard zero-one subset-sum transition, not an unbounded coin transition.

**Discard sums above the target.** For target `nums[i]`, mask

`(1 << (target + 1)) - 1`

has bits zero through `target` set. AND-ing with it removes larger sums, which can never help reach the exact target later because all query values are positive. This keeps each bitset bounded to at most $1001$ meaningful bits.

After the update, expression

`(possible[index] >> nums[index]) & 1`

tests the target bit. Once it becomes one, the index is permanently satisfiable: later queries may simply omit that index. The source marks `satisfied[index]` and no longer updates its bitset.

**Track when all targets first become reachable.** `remaining` counts nonzero targets not yet satisfied. Targets initially equal to zero start satisfied because choosing no decrements already reaches them. If all targets are zero, the method returns $k=0$ before processing any query.

Queries are processed in their given sequence with one-based `query_index`. Each touches only indices from `left` through `right`. Whenever a target first becomes reachable, `remaining` decreases. The first query prefix after which `remaining == 0` is returned immediately.

This prefix is minimal because reachability can only gain bits as queries are added. Before the returned query, at least one index lacked a subset summing to its target, so no choices could make the entire array zero.

For `nums = [2,0,2]` and two initial full-range queries of value one, each target-two bitset evolves from bit set $\{0\}$ to $\{0,1\}$ and then $\{0,1,2\}$. The middle zero target was satisfied from the start. After the second query both target bits are present, so the method returns two.

**Independent subset witnesses can be combined globally.** Suppose every index has some subset of the first $k$ applicable queries summing to its target. For each query, select exactly the indices whose individual witnesses include that query. The operation explicitly permits any subset of indices in its range, so all these per-index choices can occur simultaneously. This proves that checking targets independently does not overlook a cross-index constraint.

**Why the algorithm is correct.** The bitset invariant follows by induction: before a query it contains exactly subset sums from earlier applicable queries; after OR with the shifted copy it contains exactly sums that omit or include the new value. Masking removes only sums that can never return to the smaller target. Thus the target bit is set exactly when that index can be zeroed. The combination argument turns all per-index witnesses into legal query selections. Finally, monotone sequential processing and the first all-satisfied return establish minimum prefix length.

## Complexity detail

Let $q$ be the number of queries and $n$ the array length. A query may cover all $n$ indices, so the source performs $O(nq)$ index updates in the worst case. Under the problem's bounded target of at most $1000$, each Python bitset occupies a constant number of machine words relative to $n$ and $q$, giving the manifest's constraint-aware $O(nq)$ time.

More explicitly, if $V=\max(\texttt{nums})$ and machine word size is $W$, each shift/OR/mask costs $O(V/W)$ word operations. The generalized bound is $O(nqV/W)$ time.

There are $n$ bitsets of at most $V+1$ bits, plus masks and Boolean flags. Constraint-aware auxiliary space is $O(n)$; the generalized bit-space bound is $O(nV/W)$ machine words. This explains what the manifest's $O(n)$ claim assumes.

## Alternatives and edge cases

- **Boolean DP array per index:** It implements the same subset sums but loops over up to $1000$ totals explicitly; Python integer bitsets perform those transitions in packed operations.
- **Greedily apply every query:** Overshooting a target is illegal, and choosing a query can prevent exact equality; subset-sum reachability is required.
- **Binary-search the prefix with a fresh feasibility test:** Feasibility is monotone, but rebuilding all subset DPs per test adds overhead; the source advances once and detects the first feasible prefix.
- **Treat indices as coupled:** Query subsets are arbitrary, so one index's choice does not consume the query for another.
- **Initial zero target:** Bit zero is already reachable, so that position is satisfied without queries.
- **Entire array initially zero:** The correct minimum is zero.
- **Query outside an index:** Its value is not shifted into that index's bitset.
- **Use one query value twice at an index:** The OR-with-one-shift transition prevents this; each query is a zero-one choice.
- **Reachable sum above target:** Positive future values cannot reduce it, so masking it away is safe.
- **Satisfied index:** Skipping later updates is safe because the earlier witness remains available.
- **No common feasible prefix:** If some target bit never appears after all queries, the method returns $-1$.
- **Bit-complexity accounting:** The simple manifest bounds rely on the fixed target limit; unbounded targets would not make big-integer operations constant.
