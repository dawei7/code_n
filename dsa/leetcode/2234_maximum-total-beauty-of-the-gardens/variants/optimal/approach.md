## General

**Cap and sort the useful flower counts**

Flowers beyond `target` do not improve either beauty term, so cap every count at `target` and sort the result. If a chosen number of gardens will be complete, completing the largest currently incomplete counts is cheapest. The remaining incomplete gardens therefore form a sorted prefix.

Build prefix sums so the cost to complete a suffix is available in constant time. Enumerate every feasible total number of complete gardens, beginning with those that were already complete.

**Maximize the incomplete prefix minimum**

After paying to complete the selected suffix, use the remaining budget only to raise the minimum of the incomplete prefix. For a candidate level $x<\texttt{target}$, find how many prefix values are below $x$. Prefix sums give the required cost as

$$
xj-\sum_{i=0}^{j-1}\texttt{flowers}[i],
$$

where $j$ is the first index whose value is at least $x$. This feasibility predicate is monotone, so binary-search the greatest affordable level below `target`.

Combine that level times `partial` with the chosen complete count times `full`. Every optimal final state has some number of complete gardens; replacing its completed set by the largest initial values cannot cost more, and equalizing only the values below its incomplete minimum is the cheapest way to realize that minimum. The enumeration therefore contains a choice at least as good as every feasible state, and the maximum recorded beauty is optimal.

## Complexity detail

Let $n=\lvert\texttt{flowers}\rvert$. Sorting and prefix construction take $O(n\log n)$ time. There are at most $n+1$ complete-count choices, and each performs an $O(\log\texttt{target})$ level search whose cost check uses binary search and prefix sums. The total bound is $O(n\log n+n\log\texttt{target})$.

The capped sorted values and prefix sums use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Distribute flowers one at a time:** Repeatedly updating a current minimum can depend on `newFlowers`, which may be $10^{10}$.
- **Complete every affordable garden greedily:** A high `partial` multiplier can make one incomplete garden more valuable than completing it.
- **Try every minimum by direct rescanning:** This repeats linear work for each complete-count choice and can become quadratic.
- **Already complete gardens:** Counts at or above `target` are capped and contribute `full` without consuming budget.
- **All gardens complete:** The incomplete contribution is exactly zero.
- **One incomplete garden:** Its value itself is the incomplete minimum and must stay below `target`.
- **Unused flowers:** The budget is an upper bound; spending the last flowers may convert the final incomplete garden and reduce total beauty.
- **Values above `target`:** Extra existing flowers cannot be moved and confer no extra beauty.
