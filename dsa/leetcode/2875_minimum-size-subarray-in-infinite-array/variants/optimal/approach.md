## General

**Separate complete copies from the circular remainder**

Let

$$
S = \sum_{x \in \texttt{nums}} x.
$$

Every block of $n$ consecutive positions in the infinite array contains one complete copy of `nums` and therefore has sum $S$. Write `target` as $qS + r$ with `q, r = divmod(target, S)`. Any solution must contribute $q$ complete copies and a circular subarray whose sum is $r$.

This decomposition is safe because every input value is positive. After removing as many complete blocks of $n$ positions as possible, a remaining segment shorter than $n$ has sum strictly less than $S$. It therefore cannot replace one full copy with a different remainder of $S+r$.

If $r=0$, exactly $q$ copies already form the target, so the answer is $qn$.

**Search one circular remainder with a positive sliding window**

For $r>0$, every circular subarray of one copy appears inside two consecutive virtual copies. Scan indices from $0$ through $2n-1$, obtaining each value as `nums[index % n]` so the infinite array is never materialized.

Maintain a left pointer and the sum of the current window. Add the new rightmost value, then remove values from the left while the sum exceeds $r$. Positivity makes the window sum monotonic under each pointer movement: extending increases it and shrinking decreases it. Whenever the sum equals $r$, record the window length.

Each circular candidate is considered while both pointers move only forward. If no window reaches $r$, the target is impossible. Otherwise, add the shortest remainder length to the $qn$ positions contributed by complete copies.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Summing the base array and scanning two virtual copies both take $O(n)$ time. Each pointer advances at most $2n$ positions, and the algorithm stores only numeric accumulators, so it uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size` with $n$ copies of `2` and target $2n-1$ at sizes 16, 64, and 256. The odd target cannot be formed, forcing the linear window to inspect the full doubled range. A correct baseline that starts a fresh circular scan at every position also returns $-1$ on every tier but exhibits quadratic scaling.

## Alternatives and edge cases

- **Prefix-sum hash table:** Prefix sums over two copies can find a matching difference in $O(n)$ time, but storing indices costs $O(n)$ auxiliary space.
- **Fresh scan from every start:** Enumerating circular windows independently is correct but takes $O(n^2)$ time in the worst case.
- **Materialize enough repetitions for `target`:** Building the infinite prefix directly can require up to $O(\texttt{target})$ elements and is unnecessary.
- **Zero remainder:** When `target` is divisible by $S$, the shortest answer is exactly $qn$; searching for an empty remainder must not incorrectly return $-1$.
- **Boundary crossing:** Searching two virtual copies is necessary because the shortest remainder can use a suffix followed by a prefix.
- **Impossible remainder:** Complete cycles do not help when no circular subarray sums to $r$.
- **Large target:** The result can be much larger than $n$, even though only two copies need to be searched.
