## General
**Represent values only by their remaining rank**

Start with an array of $n+1$ ones. At a stage with `m` possible ranks, `dp[j]` counts completions when the current first value has rank `j` among those values. After fixing the next relation, remove the current value; the next state has `m-1` ranks.

For `"I"`, a next value of rank `j` can follow precisely the smaller current ranks, so its count is a prefix sum through `dp[j]`. For `"D"`, it can follow larger current ranks, giving a suffix sum beginning at `dp[j + 1]`. Compute these cumulative sums in one pass, reduce modulo $P$, and replace `dp`. After all $n$ relations, one state remains and its count is the answer.

The initial ones correctly count the single completion after all relations have been assigned. Working backward through a relation, the prefix or suffix transition sums exactly the allowed current ranks for every next rank, with no invalid comparison included. Induction therefore makes every state equal to its number of valid completions. The final sole state counts all valid permutations.

## Complexity detail
The state lengths decrease from $n+1$ to one. Each prefix or suffix transition scans its current array once, so the total work is $O(n^2)$. Two rolling arrays hold at most $n+1$ values, using $O(n)$ space.

## Alternatives and edge cases
- **Recompute every range sum:** The same rank recurrence is correct, but summing each prefix or suffix separately takes $O(n^3)$ time.
- **Enumerate all permutations:** Direct checking takes factorial time and becomes infeasible almost immediately.
- **Two-dimensional dynamic programming:** Retaining every stage is correct but uses $O(n^2)$ space instead of rolling one row.
- **Single relation:** Both `"D"` and `"I"` admit exactly one of the two permutations.
- **All increasing:** Only `[0,1,\ldots,n]` is valid.
- **All decreasing:** Only `[n,n-1,\ldots,0]` is valid.
- **Alternating relations:** Prefix and suffix transitions alternate without changing the state definition.
- **Modulo reduction:** Apply $P$ during every cumulative sum so intermediate counts stay bounded.
