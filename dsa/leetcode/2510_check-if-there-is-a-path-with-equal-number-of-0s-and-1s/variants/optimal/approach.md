## General

**Every valid path has the same number of cells**

From `(0,0)` to `(m-1,n-1)`, every path makes exactly `m-1` downward moves and `n-1` rightward moves. Including the starting cell, it visits

$$
L=m+n-1
$$

cells.

Equal numbers of zeroes and ones are possible only when $L$ is even. If $L$ is odd, the method immediately returns false.

For even $L$, a successful path must contain exactly

$$
s=\frac{L}{2}
$$

ones and exactly `s` zeroes.

The source initially stores `L` in `s`, checks parity, and then right-shifts `s` to divide it by two. After that point, `s` means the target count for each digit.

**Define the cached search state**

`dfs(i,j,k)` asks whether a valid completion exists starting at cell `(i,j)` when `k` ones have been seen before entering that cell.

The function first rejects coordinates outside the grid. It then adds `grid[i][j]` to `k`. Because cells are binary, this increments the count exactly when the current cell is one.

Every route reaching coordinate `(i,j)` has visited exactly `i+j+1` cells. Therefore, after including the current cell:

- ones seen are `k`;
- zeroes seen are `i+j+1-k`.

**Prune states that have already exceeded a target**

If `k>s`, too many ones have already been visited. Future moves can never remove them.

If `i+j+1-k>s`, too many zeroes have already been visited. That is equally irreversible.

The condition

`k > s or i+j+1-k > s`

rejects both cases immediately.

These checks do not attempt every possible future-feasibility bound; they are simple necessary conditions. Any state they reject is certainly impossible, and caching still makes the remaining search manageable.

**Accept only the correct destination count**

At `(m-1,n-1)`, the whole fixed-length path has been visited. Returning `k==s` verifies the target number of ones.

Because total path length is `2s`, having `s` ones automatically means the other `s` cells are zero. No separate zero test is needed at the destination.

**Explore the only two legal moves**

For a nonterminal state, the method returns:

`dfs(i+1,j,k) or dfs(i,j+1,k)`.

These are exactly the permitted down and right moves. Python's `or` short-circuits: as soon as one continuation succeeds, the other need not be explored.

If both fail, no valid path continues from this state.

**Why memoization is necessary**

Many different prefixes can arrive at the same coordinate with the same number of ones. From that point onward, their future possibilities are identical: only `i`, `j`, and `k` matter, not the precise route used earlier.

`@cache` stores the Boolean result for each state. The first visit explores it; later visits reuse the stored answer. This converts an exponential enumeration of paths into dynamic programming over a polynomial number of states.

The manifest describes rolling sets, but the exact Optimal implementation is top-down memoized DFS. Its state and space analysis must follow the cache.

**Why the recurrence is complete and sound**

Every path from a state begins with either a down move or a right move unless already at the destination. The recurrence examines both, so it cannot miss a legal path.

The running count exactly records ones along the visited prefix, the zero count follows from fixed prefix length, and pruning removes only prefixes that already exceed a required final count. A true terminal result therefore corresponds to a real equal-count path.

Conversely, any real equal-count path never exceeds `s` ones or zeroes on a prefix. Its sequence of moves remains available through the recurrence and reaches a terminal state with `k=s`, so the function returns true.

**Python closure timing**

The nested function is defined before local variables `m`, `n`, and `s` receive values, but it is called only after those assignments. Python closures look up these variables when the function executes, so the code is valid.

The maximum recursion depth is at most `m+n-1<=199`, comfortably below Python's usual recursion limit.

## Complexity detail

There are $mn$ cell coordinates and at most $O(m+n)$ relevant values of `k`. Each cached state does constant work aside from two cached calls, so worst-case time is

$$
O(mn(m+n)).
$$

The cache can store the same number of states, giving $O(mn(m+n))$ auxiliary space in the exact implementation. The recursion stack adds $O(m+n)$ and is dominated.

This differs from the manifest's rolling-DP space bound of $O(n(m+n))$ because no rolling table is used by the protected source.

## Alternatives and edge cases

- **Rolling sets per column:** Store reachable one-counts iteratively and reduce space to $O(n(m+n))$; this matches the manifest summary but not the exact code.
- **Odd path length:** Equal zero and one counts are impossible, so reject before searching.
- **Start and destination values:** Both are included in the counts.
- **Too many ones:** The state cannot recover and is safely pruned.
- **Too many zeroes:** Compute them as visited cells minus ones and prune symmetrically.
- **Same state by different routes:** Memoization merges their identical futures.
- **All-zero or all-one grid:** No equal-count path exists for positive even path length.
- **Strict move set:** Diagonal and upward moves are never considered.
- **Destination test:** Exactly `s` ones suffices because total length is fixed at `2s`.
- **Manifest mismatch:** The actual cache uses more space than a rolling implementation.
