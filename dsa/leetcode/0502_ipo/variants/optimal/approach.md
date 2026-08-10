## General

At any moment, a project is either affordable—its required capital is at most current capital `w`—or still locked. Among affordable projects, choosing the one with greatest profit is always safe because profits are nonnegative and completing a project only increases capital.

The solution maintains two priority queues with different purposes:

- `h1` is a min-heap of `(required_capital, profit)` pairs, so its root is the locked-or-unprocessed project with smallest capital requirement;
- `h2` is a max-heap of profits for every project that has become affordable but has not been selected.

Python's heap implementation is a min-heap, so `h2` stores each profit negated. The most profitable value then has the most negative stored value and appears at the root.

**Initialize every project exactly once.** `zip(capital, profits)` pairs the requirement and profit at the same project index. The list comprehension creates one tuple per project, and `heapify(h1)` arranges them by required capital. Tuple comparison uses capital first, which is precisely what unlocking needs. If requirements tie, profit breaks the heap order, but all tied affordable projects will be transferred before selection, so that secondary order does not affect correctness.

**Unlock everything current capital can afford.** At each of at most `k` rounds, the inner loop examines `h1[0][0]`. While the smallest remaining requirement is at most `w`, that project is removed from `h1` and its negated profit is pushed into `h2`.

Once the smallest remaining requirement exceeds `w`, every other project still in `h1` also exceeds `w` because `h1` is ordered by requirement. The transfer loop has therefore moved exactly all currently affordable projects.

A transferred project stays in `h2` until selected. Capital never decreases, so an affordable project can never become locked again. This monotonicity lets the algorithm process each project's affordability only once.

**Choose the greatest available profit.** If `h2` is nonempty, `heappop(h2)` returns the most negative stored value, corresponding to the largest real profit. The update `w -= heappop(h2)` subtracts a negative number and therefore adds that profit to capital.

The chosen project is removed from the heap, ensuring every project is distinct and can be completed at most once. `k -= 1` consumes one allowed project slot.

If `h2` is empty after unlocking, no project can currently be started. Every project remaining in `h1` requires more capital, and without completing a project capital cannot rise. Continuing is impossible, so breaking early is correct.

**Why the greedy choice is optimal.** Consider any round with current capital `w` and affordable set `A`. Suppose an optimal plan chooses project `q` with profit smaller than maximum affordable profit `p`. Replace `q` with the project earning `p`. Immediately afterward, the replacement plan has at least as much capital as the original plan.

Any project affordable after choosing `q` is also affordable with this greater-or-equal capital. The replacement has used one different project, but it can follow the original future choices whenever they remain unused; if the original later intended to choose `p`, it may choose `q` at that point or omit it, never ending with less capital. Thus there exists an optimal plan whose first choice is the maximum affordable profit. Repeating this exchange argument at every round proves the greedy sequence is optimal.

The “at most `k`” wording is compatible with taking an available zero-profit project. It does not reduce capital. It also cannot unlock anything by itself, so using or skipping it yields the same final capital unless another profitable project is already available, in which case the max-heap chooses that one first. Negative profits would invalidate the always-choose argument, but the constraints guarantee profits are nonnegative.

For `k = 2`, `w = 0`, requirements `[0, 1, 1]`, and profits `[1, 2, 3]`, only profit one transfers initially. Selecting it raises capital to one. Both remaining projects then transfer, and the max-heap selects profit three, producing final capital four.

## Complexity detail

Let $n$ be the number of projects. Building the tuple list is $O(n)$ and `heapify` is $O(n)$. Each project moves from `h1` to `h2` at most once, involving one pop and one push, each $O(\log n)$. At most `min(k,n)` projects are selected from `h2`. A direct bound is $O(n\log n + k\log n)$, as in the manifest; because no more than $n$ projects can actually be selected, it also simplifies to $O(n\log n)$.

The two heaps together contain at most $n$ project entries at any time, so auxiliary space is $O(n)$. The inputs themselves are not modified.

## Alternatives and edge cases

- **Sort by capital plus one max-heap:** Sort project pairs once and advance a pointer as capital grows. It has the same asymptotic bound and is the editorial's common presentation.
- **Scan every project each round:** Finding all affordable projects and the largest profit repeatedly costs $O(kn)$ time.
- **One heap ordered only by profit:** It cannot efficiently distinguish unaffordable projects; the capital-ordered heap handles unlocking first.
- **No affordable project initially or later:** An empty `h2` means capital cannot increase, so the loop must stop.
- **`k` larger than project count:** Projects are removed when selected, and the loop eventually stops when both heaps offer nothing.
- **Equal capital requirements:** All projects at or below `w` transfer before selection, so the largest profit among them wins.
- **Zero-profit projects:** Choosing one cannot lower capital. It may consume a slot without benefit, but final capital is unchanged and the max-heap postpones it behind positive profits.
- **Duplicate profits or requirements:** Heap entries represent distinct project occurrences even when numeric fields match, and each tuple is popped only once.
- **Negated max-heap arithmetic:** `w -= negative_profit` adds the original positive profit; using `w += heappop(h2)` would incorrectly reduce capital.
