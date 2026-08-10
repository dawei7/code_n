## General

Each item type has its own limit: among the arrivals that are kept in any window of at most the most recent $w$ days, one type may occur no more than $m$ times. Arrivals of different types do not compete for a shared capacity. That allows the algorithm to process days from left to right while maintaining the current kept count for each type.

The implementation uses three pieces of state:

- `cnt[x]` is the number of **kept** arrivals of type `x` that are still inside the relevant window before the current decision;
- `marked[i]` is $1$ if the arrival at index `i` was kept and $0$ if it was discarded; and
- `ans` is the number of discarded arrivals so far.

The indices in the code are zero-based even though the statement numbers days from one. At array index `i`, the statement's day is $i+1$. This shift does not change the window length or any decision.

**The exact window represented by the counter**

Before deciding whether to keep `arrivals[i]`, the only earlier indices that can constrain it are

$$
\max(0, i-w+1),\ldots,i-1.
$$

Once the current arrival is included, those indices plus `i` form the length-$w$ window ending today. Any earlier arrival lies more than $w-1$ days behind the current one and cannot coexist with it in a $w$-day window.

At the start of an iteration, the counter still includes the previous iteration's active kept arrivals. If `i >= w`, index `i-w` has just become too old. The solution removes exactly its contribution:

`cnt[arrivals[i - w]] -= marked[i - w]`

The subtraction is either one or zero. If that old arrival was kept, `marked[i - w]` is $1$, and its type's count must decrease. If it was discarded, it was never added to `cnt`, so subtracting zero correctly leaves the count unchanged.

This is why `marked` is necessary in this implementation. Merely knowing the old arrival's type is not enough: discarded arrivals exist in `arrivals` but must never be counted as inventory that was retained.

After the expiration step, `cnt[x]` for the current type `x` counts precisely the kept copies of `x` among the preceding $w-1$ possible positions. No stale copy remains, and no discarded copy is included.

**The keep-or-discard decision**

There are only two cases.

If `cnt[x] >= m`, the active window already contains $m$ kept copies of type `x`. Keeping today's copy would raise that number to at least $m+1$, immediately violating the rule in the window ending at `i`. The current arrival therefore must be discarded. The implementation increments `ans` but leaves `marked[i]` at its initial value zero and does not increment the counter.

If `cnt[x] < m`, adding the current arrival keeps the number of copies at most $m$. The solution records

`marked[i] = 1`

and increments `cnt[x]`. The arrival is now represented in the counter until index `i+w`, when it will expire before that later day's decision.

For example, with `arrivals = [1, 2, 3, 3, 3, 4]`, `w = 3`, and `m = 2`, the first two occurrences of type $3$ are kept. At the third occurrence, the counter still contains two retained threes from the preceding two indices. The new three must be discarded. On the next day, the earliest retained three expires before type $4$ is processed, though this does not affect the count of type $4$.

**Why keeping every feasible arrival is globally optimal**

It may initially seem useful to discard a feasible arrival now so that a later arrival of the same type can be kept. That exchange cannot reduce the total number of discards.

Focus on one item type, since decisions for other types do not affect its limit. Suppose the current copy can be kept. Keeping an earlier copy is never worse than reserving its place for a later copy: the earlier copy leaves every future sliding window no later than the later copy would. Thus, if a hypothetical optimal plan discards today's feasible copy but keeps some later copy whose capacity it wanted to reserve, swapping those choices—keep today and discard that later copy—does not reduce the number kept and cannot create a later violation. The replacement item expires earlier.

Now consider a day on which the algorithm discards type `x`. There are already $m$ kept copies of `x` in the preceding $w-1$ indices. Together with today's copy, these are $m+1$ occurrences lying inside one window of length at most $w$. Every valid plan must discard at least one of those $m+1$ occurrences. The greedy history has already kept the earlier $m$ copies, and discarding the newest one loses exactly one item—the unavoidable minimum for this conflict.

These two observations establish the left-to-right choice: accepting a feasible arrival never harms the best attainable retained count, while rejecting an infeasible arrival is mandatory for the current window. Applying this reasoning on every day maximizes the number kept and therefore minimizes the number discarded.

**Why all windows are covered**

Every relevant window has a right endpoint. When the algorithm processes that endpoint, the counter contains exactly the kept arrivals in the earlier part of its window, and the decision ensures the current type does not exceed $m$. Counts for types other than the arriving type do not increase on that day, so they remain valid as well. Expiration only decreases counts. Hence, after each iteration, the window ending at that day is valid, and processing all endpoints covers every window required by the statement.

## Complexity detail

Let $n$ be the length of `arrivals`.

The loop visits each array position once. At each position it performs a constant number of counter lookups or updates, one possible expiration, and one keep-or-discard decision. Python's `Counter` is hash-table based, so these operations take expected $O(1)$ time. The total expected running time is therefore $O(n)$.

Another useful accounting is that every kept arrival is added to the counter once and removed at most once. Discarded arrivals are represented by zero in `marked` and never contribute to a count. No item is repeatedly rescanned as the window moves.

The `marked` array contains $n$ integers, requiring $O(n)$ space. The counter has at most one key for every distinct item type encountered, which is at most $n$, so it also uses $O(n)$ space in the worst case. All remaining scalar variables use $O(1)$ space. Thus, the auxiliary space complexity is $O(n)$.

The manifest describes a deque of retained days per type, but the exact Optimal source uses a `Counter` plus the `marked` array instead. Both designs achieve the same asymptotic bounds; this document follows the actual source and its expiration-by-index data flow.

## Alternatives and edge cases

- **Deque per item type:** Store the retained indices of each type in a deque, remove indices older than the current window, and reject when that deque already has $m$ entries. This is also $O(n)$ time and $O(n)$ space, but it is not the data structure used by the exact Optimal source.
- **Recounting every window:** Scanning the last $w-1$ positions for each arrival can cost $O(nw)$ time, which becomes quadratic when $w$ is proportional to $n$.
- **Counting all arrivals instead of kept arrivals:** A discarded item must not consume future capacity. Failing to distinguish it would cause unnecessary later discards; `marked` prevents that error.
- **Expiring after the decision:** Index `i-w` is outside the window ending at `i` and must be removed before checking today's item. Removing it afterward can incorrectly discard a valid arrival.
- **`w = 1`:** The previous window is empty before every decision. Because `m >= 1`, every arrival can be kept.
- **`m = w`:** Any $w$-day window contains at most $w$ total days, so one type cannot occur more than $w$ times. The algorithm consequently performs no discards.
- **All arrivals have one type:** The method keeps up to $m$ sufficiently recent copies, discards additional copies while those remain active, and begins keeping again as old retained copies expire.
- **Many different types:** Each type has an independent counter. A busy window can contain many items overall; only the per-type multiplicity is restricted.
- **Discarded position leaving the window:** Its marker is zero, so expiration subtracts zero. This is intentional and avoids corrupting the retained count.
- **Short prefix windows:** During the first $w-1$ days there is no index to expire. The counter naturally represents the entire available prefix, exactly matching `max(1, i-w+1)` in the one-indexed statement.
