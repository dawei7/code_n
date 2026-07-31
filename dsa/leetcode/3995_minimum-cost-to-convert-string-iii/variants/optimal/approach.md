## General

Every rule preserves length, and a position used by one application can never be used again. Consequently, the final transformation is a left-to-right partition into unchanged single positions and disjoint ranges handled by exactly one rule. No rule can create text that a later overlapping rule consumes.

Let `dp[i]` be the minimum cost of transforming the first `i` positions of `source` into the first `i` positions of `target`. Start with `dp[0] = 0`; every other state is initially unreachable.

At a reachable position `i`, there are two kinds of transition. If `source[i] == target[i]`, leave that position unused and carry the same cost to `dp[i + 1]`. For each rule, let its length be `length`. The rule can cover the next `length` positions only when the range fits, its replacement equals the corresponding target segment, and every non-wildcard pattern character equals the corresponding source character. A valid application updates `dp[i + length]` by its base cost plus the number of wildcards in its pattern.

These transitions enumerate every legal first choice after an already transformed prefix. Conversely, every transition is legal and consumes a range disjoint from the prefix. Induction over the prefix boundary therefore shows that each reachable state stores the minimum cost for exactly that prefix. The final state is the global minimum; if it remains unreachable, the requested transformation is impossible.

## Complexity detail

Let $n=\lvert\texttt{source}\rvert$, let $R=\lvert\texttt{rules}\rvert$, and let $L$ be the maximum rule length. At each of the $n$ prefix positions, checking every rule compares at most $L$ pattern and replacement characters, for $O(nRL)$ time. Counting wildcards while preparing the $R$ rules costs $O(RL)$ and is included in that bound.

The dynamic-programming array uses $O(n)$ space, and the prepared rule records use $O(R)$ additional space, for $O(n+R)$ auxiliary space. The input strings themselves are not copied as part of the asymptotic storage claim.

## Alternatives and edge cases

- **Shortest path on prefix indices:** Treat each unchanged character or rule application as a directed edge. A DAG shortest-path pass is equivalent to the presented dynamic program but adds graph terminology without reducing work.
- **Repeated relaxation:** Bellman-Ford-style passes over the prefix edges are correct, but reverse-order relaxation can require $O(n^2RL)$ time.
- **Recursive memoization:** A top-down search over prefix positions has the same $O(nRL)$ work but risks recursion depth near the maximum string length.
- **No chaining on one range:** Rules such as `"a" -> "b"` and `"b" -> "c"` cannot be applied successively to one position, because the first application permanently marks that position as used.
- **Unchanged characters:** A position may remain unused only when its source and target characters already match.
- **Wildcard charge:** Every `'*'` matches exactly one arbitrary source character and contributes one in addition to the rule's base cost.
- **Duplicate or dominated rules:** Testing all rules remains correct; the minimum transition naturally selects the cheapest applicable one.
- **Impossible target:** If no sequence of unchanged positions and valid disjoint rules reaches position $n$, return `-1`.
