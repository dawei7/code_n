## General

Partition `nums` conceptually into maximal strictly increasing runs. During a left-to-right scan, `current_run` is the length of the run ending at the current element, and `previous_run` is the length of the immediately preceding completed run.

**A pair has only two possible shapes.** Both adjacent blocks may lie inside one increasing run of length $r$. Splitting that run into two consecutive equal blocks yields a candidate $\lfloor r/2 \rfloor$. Otherwise, an increasing-run break lies between the blocks. Because a break cannot occur inside either strictly increasing block, it must be their shared boundary; consecutive run lengths $p$ and $r$ then yield a candidate $\min(p,r)$.

For each new value, extend `current_run` when it exceeds its predecessor. At a decrease or equality, move the completed length into `previous_run` and reset `current_run` to one. The best candidate ending at or before this position is updated with both `current_run // 2` and `min(previous_run, current_run)`.

These candidates are exhaustive. Any two adjacent blocks either contain no maximal-run boundary, so their combined $2k$ elements belong to one run, or contain a boundary. A boundary inside a block would violate strict increase, while two boundaries cannot fit without violating at least one block; therefore the only remaining placement aligns their shared edge with one boundary. Taking the maximum candidate throughout the scan returns the globally largest `k`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Every array element is processed once with constant work, giving $O(n)$ time. The algorithm stores only two run lengths, the current answer, and an index, so it uses $O(1)$ auxiliary space.

The benchmark size is $n$. A strictly increasing array makes the optimal method scan all $n$ elements while the answer grows to $\lfloor n/2 \rfloor$. The calibrated slower method tries every possible `k` and rechecks the corresponding elements from the beginning, requiring $O(n^2)$ work on these tiers.

## Alternatives and edge cases

- **Binary search on `k`:** A linear feasibility scan inside binary search gives $O(n\log n)$ time and is valid, but direct run lengths reveal the optimum in one pass.
- **Prefix and suffix run arrays:** Increasing lengths ending and starting at each index support $O(n)$ evaluation, but consume $O(n)$ space.
- **Enumerate every length:** Checking candidates one length at a time repeats comparisons and can require $O(n^2)$ time.
- **One long run:** A run of length $r$ contributes $\lfloor r/2 \rfloor$, even without a decrease between the blocks.
- **Consecutive unequal runs:** Two neighboring runs contribute the smaller of their lengths because each block must fit wholly on its side of the boundary.
- **Equality at the shared boundary:** Strict increase applies inside each block only, so `[1, 2]` beside `[2, 3]` is valid.
- **Entirely descending or equal input:** Every singleton is strictly increasing, so the answer is at least one when $n\ge2$.
- **Negative and large values:** Only adjacent comparisons matter; value signs and magnitudes do not affect the state.
