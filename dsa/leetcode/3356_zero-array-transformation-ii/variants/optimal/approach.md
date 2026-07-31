## General

A prefix of queries is sufficient exactly when, at every index, the sum of the covering query values is at least the corresponding target. Each covered index may choose its decrement independently, so extra capacity at one position cannot repair a deficit elsewhere, and excess capacity never causes harm.

**Force the minimum prefix from left to right.** Scan `nums` in index order while a difference array tracks the capacity supplied by queries already consumed. At index $i$, its prefix sum is the currently available capacity. If that amount is below `nums[i]`, the final answer must include another query: no shorter prefix can satisfy this already-reached index. Consume queries in sequence until the deficit is removed or the list ends.

When consuming `[left, right, value]`, a query ending before $i$ cannot help any current or future requirement and is skipped. Otherwise, only its still-relevant interval from $\max(left,i)$ through `right` is recorded. If that interval begins at $i$, add its value to the current capacity immediately because the prefix sum for $i$ has already been read.

After index $i$ has enough capacity, never revisit it. Later queries are unnecessary for that position, and independent per-index decrement choices allow their effect there to be zero. Every query is consumed at most once and every index is scanned once.

The algorithm consumes a new query only when the current index proves that all shorter prefixes fail. Conversely, when the scan finishes, every index has enough capacity from exactly the consumed prefix. Therefore the returned count is both feasible and minimal; exhausting the list during a deficit proves impossibility.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. Each index and each query is processed at most once, so time is $O(n+q)$. The difference array uses $O(n)$ auxiliary space.

The benchmark size is $m$, with $n=q=m$. All values require the entire list of complete-range unit queries. The optimal consumer performs linear work, while directly applying every query value at every covered index performs $m^2$ updates.

## Alternatives and edge cases

- **Binary search the prefix length:** Feasibility is monotonic, and a difference-array check gives a correct $O((n+q)\log q)$ solution, but it repeats nearly the same coverage work.
- **Apply every query directly:** Updating all covered elements can require $O(nq)$ time for wide ranges.
- **Initially zero array:** The empty prefix already succeeds, so the answer is zero.
- **Queries ending in the past:** Once their right endpoint is below the current index, they cannot help any remaining deficit but still count if the prefix has consumed them.
- **Queries starting in the future:** Record their future interval, then continue consuming because they do not increase capacity at the current index.
- **Independent amounts:** Capacity exceeding a target is safe because that index may choose a smaller decrement than the query's maximum.
- **Sentinel endpoint:** A difference array of length $n+1$ safely stores the closing event at `right + 1 = n`.
- **Insufficient complete list:** If capacity remains below a target after every query is consumed, no valid prefix exists and the answer is $-1$.
