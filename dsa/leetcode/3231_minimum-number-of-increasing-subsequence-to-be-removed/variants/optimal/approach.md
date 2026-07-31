## General

**View the operations as a partition.** Every original element is removed exactly once, so the operations partition the original positions into strictly increasing subsequences. Conversely, any such partition can be removed one subsequence at a time; deleting other positions never changes the order inside a chosen subsequence. The task is therefore the minimum increasing-chain cover of the sequence.

**Use the opposing subsequence as the lower bound.** A non-increasing subsequence can contribute at most one element to any strictly increasing chain. Its length is consequently a lower bound on the number of operations. The sequence form of the chain-cover theorem guarantees a partition into exactly as many increasing chains as the longest non-increasing subsequence, so this lower bound is attainable.

It remains to compute that length efficiently. Negate every value conceptually: a non-increasing subsequence of `nums` becomes a non-decreasing subsequence of the negated values. Maintain the smallest possible tail for each attainable non-decreasing length. For each transformed value, `bisect_right` finds the first tail strictly greater than it; replace that tail, or append if no such tail exists.

Using the right insertion boundary is essential. Equal original values may appear together in a non-increasing subsequence, and after negation equal values must extend a non-decreasing subsequence rather than replace one another. The final number of tails is therefore the longest non-increasing length and the minimum operation count.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each element performs one binary search in a tails array of length at most $n$, for $O(n\log n)$ time. The tails array uses $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Quadratic subsequence dynamic programming:** Computing the best non-increasing length ending at every index is direct and correct but takes $O(n^2)$ time.
- **Greedily remove one visible increasing subsequence:** A locally long removal need not minimize the number of remaining chains.
- **Use longest decreasing subsequence:** Strict decrease is wrong when duplicate values exist; the obstruction is non-increasing.
- **Use `bisect_left` after negation:** It collapses equal values and undercounts the required operations.
- A strictly increasing input is removed in one operation.
- A non-increasing input requires one operation per element.
- Equal values cannot share a strictly increasing removal and therefore raise the answer.
- A one-element array always has answer one.
- Negation is conceptual and does not mutate the input.
