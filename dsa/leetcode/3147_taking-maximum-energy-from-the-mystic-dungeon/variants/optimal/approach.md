## General

Every jump preserves the index modulo `k`. The array therefore splits into `k` independent chains. Within one chain, starting at a position means taking the entire suffix of that chain; stopping before its final position is not allowed.

**Build every forced path from its successor**

Scan indices from right to left. For residue $r$, let `suffix[r]` hold the total obtained from the most recently processed index having residue $r$. That index is exactly `i + k` when processing an earlier index `i`, if such a successor exists. The total for the path starting at `i` is therefore

$$
\texttt{energy[i]} + \texttt{suffix[i \bmod k]}.
$$

Store this new total back in the same residue slot and compare it with the global maximum. Before the final member of a chain is processed, its slot is zero, correctly representing the absence of a successor rather than permission to stop early.

By backward induction along each residue chain, every stored value equals the sum of exactly the indices that a start at that position must visit. Every possible starting index is processed once, so the greatest recorded total is precisely the requested optimum.

## Complexity detail

Let $n$ be the length of `energy`. The scan performs constant work for each of the $n$ indices, giving $O(n)$ time.

The residue totals occupy an array of length `k`, so the auxiliary space is $O(k)$. Since $k < n$, this is also $O(n)$ in the worst case.

## Alternatives and edge cases

- **Full dynamic-programming array:** Storing the forced-path total for every index also gives $O(n)$ time, but uses $O(n)$ space even when `k` is small.
- **Modify `energy` in place:** Adding `energy[i + k]` into `energy[i]` during a backward scan gives $O(1)$ auxiliary space, but unexpectedly destroys the caller's input.
- **Recompute every starting path:** Summing `energy[i]`, `energy[i + k]`, and so on independently for each start is correct but can take $O(n^2)$ time when `k = 1`; it is the principal slower benchmark comparison.
- Negative totals must remain eligible. Initializing the answer to zero would incorrectly claim that an empty path may be chosen.
- The final `k` positions have no successor, so each of them forms a valid one-magician path.
- A large positive value cannot justify stopping early; every later value in the same residue chain remains mandatory.
