## General

**Process original values in sorted order.** An element with original value $x$ can contribute either $x$ or $x+1$. Sorting ensures that when $x$ is processed, every element that could precede either choice in an increasing consecutive sequence has already been considered.

Let `longest[v]` be the maximum length of a consecutive selected sequence whose final modified value is $v$, using only processed elements. For the next original value $x$, there are exactly two transitions:

- increment $x$ to $x+1$, extending the best existing sequence that ends at $x$;
- leave $x$ unchanged, extending the best existing sequence that ends at $x-1$.

Therefore the two new lengths are `longest[x] + 1` and `longest[x - 1] + 1`. Compute both before changing the map so the same array element cannot be used twice. Then store them as the best chains ending at $x+1$ and $x$.

**Why the assignments preserve the best chains.** Before processing $x$, no larger original value has been seen. A state ending at $x+1$ can only have come from an earlier copy of $x$ that was incremented; the new incremented state extends the current best chain ending at $x$ and cannot be worse. Likewise, repeated copies of $x$ all see the same already-final state ending at $x-1$, so assigning the unchanged transition does not discard a better alternative.

Inductively, after every processed element, each stored state is the best achievable consecutive sequence for its endpoint. Every legal selected sequence has some final endpoint, so the largest state created during the scan is the required maximum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting takes $O(n\log n)$ time, and the dynamic-programming scan performs expected $O(1)$ hash-map work per element. The total expected time is $O(n\log n)$, and at most $O(n)$ endpoint states use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic predecessor scan:** Dynamic programming can compare both modified choices of every element with every earlier element, but that takes $O(n^2)$ time.
- **Frequency-only greedy:** Consuming duplicates locally without tracking both possible endpoints can spend a value needed to bridge a later gap and miss the optimum.
- **Longest consecutive values without modification:** Ignoring the optional increment loses valid chains formed by moving one copy of a duplicated value upward.
- **One element:** The required selection is nonempty, so a single input value always gives answer `1`.
- **Duplicate values:** At most two equal originals can appear in one selected run—one unchanged and one incremented—and the update order prevents using one copy for both roles.
- **Values separated by two:** An increment may bridge such a gap, but values separated by at least three cannot become adjacent to each other.
- **Upper value boundary:** A value of $10^6$ may legally become $10^6+1$; the modified value is not constrained back to the original input range.
