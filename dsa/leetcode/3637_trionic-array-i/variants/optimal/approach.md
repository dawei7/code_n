## General

Start at index 1 and consume the maximal strictly increasing prefix. Its final position would be $p$. If no increasing edge was consumed, or the scan already reached the end, the required first turn and later phases cannot exist.

From the first non-increasing edge, consume the maximal strictly decreasing phase. This phase must also contain at least one edge and must stop before the array ends so a final increasing phase remains.

Consume one final maximal strictly increasing phase. The array is trionic exactly when this phase is nonempty and reaches the final element. A plateau or an unexpected direction stops the relevant scan; because phases must cover the whole array contiguously, no later index can repair that mismatch.

The maximal scans uniquely determine any possible breakpoints: within a strictly increasing run, ending the first phase earlier would make the next required decreasing comparison fail, and analogous reasoning applies to the decreasing run. Thus accepting the three consecutive maximal runs is equivalent to the existence of valid $p$ and $q$.

## Complexity detail

Let $n$ be the array length. The index advances monotonically and examines every adjacent pair at most once, giving $O(n)$ time. Only the index and phase boundaries are stored, so auxiliary space is $O(1)$.

The benchmark uses $S=n$. The accepted scan is $O(S)$, while trying every pair of breakpoints and rechecking all three segments takes $O(S^3)$ time.

## Alternatives and edge cases

- **Enumerate p and q:** Directly verifies the definition but repeats segment comparisons for $O(n^3)$ work.
- **Track difference signs:** Compressing adjacent comparisons to `+/-` and requiring exactly three nonempty runs is an equivalent linear approach.
- **Plateau:** Any equal adjacent pair makes the array non-trionic because all three phases are strict.
- **Missing first phase:** An array beginning with a decrease fails immediately.
- **Missing middle phase:** A fully increasing array has no valid $q$.
- **Missing final phase:** A peak followed by a decrease through the last element is insufficient.
- **Extra turn:** The required pattern covers the whole array and permits exactly the two specified direction changes.
- **Length three:** The index inequalities leave no room for both interior breakpoints.
