## General

**The last face and its current streak contain all relevant history**

There are \(6^n\) unconstrained roll sequences, so enumerating them separately is infeasible. The restriction, however, depends only on consecutive equal rolls. Once the number of rolls already placed, the last face, and the length of its current run are known, earlier faces have no influence on which next roll is legal.

The memoized function `dfs(i, j, x)` uses exactly this state:

- `i` is the number of positions already filled;
- `j` is the most recently rolled face, from 1 through 6;
- `x` is how many times `j` currently appears consecutively at the end.

The initial call `dfs(0, 0, 0)` uses face zero as a sentinel meaning “there is no previous roll.” Zero is not a real die face, so every choice from one through six differs from it and begins a new streak of length one.

**The completed-sequence base case**

When `i >= n`, exactly \(n\) rolls have been chosen, so the function returns one. That one counts the single completed sequence represented by the choices on the recursive path. The function cannot normally reach `i > n` because every recursive call adds exactly one, but `>=` makes the termination condition robust.

**Trying each possible next face**

The loop `for k in range(1, 7)` considers all six values for the next roll.

If `k != j`, the face changes. Any previous consecutive run has ended, so the new suffix consists of one occurrence of `k`. The transition is `dfs(i + 1, k, 1)`. No limit test is needed before this transition because every `rollMax` entry is at least one.

If `k == j`, the existing run would grow from `x` to `x + 1`. This transition is legal only when `x < rollMax[j - 1]`. The list is zero-indexed while faces are numbered one through six, which is why face `j` uses entry `j - 1`. If the current run has already reached its maximum, the code simply adds no recursive result for this choice.

Every legal sequence from the current state has exactly one next face and therefore belongs to exactly one loop branch. Adding the recursive counts counts all legal completions without overlap.

**Why memoization eliminates repeated work**

Different roll prefixes can reach the same triple `(i, j, x)`. For example, many earlier patterns may lead to position ten with face four appearing twice at the end. Their future options are identical because the restriction remembers only that suffix run.

The `@cache` decorator stores the result for each state after its first evaluation. Later calls with the same arguments return the stored count rather than rebuilding the remaining search tree. This collapses exponential enumeration into a number of computations proportional to the number of distinct states.

**A small example**

Let `n = 2` and `rollMax = [1, 1, 2, 2, 2, 3]`. From the sentinel state, each of six first faces is allowed. After rolling face one, state `(1, 1, 1)` cannot choose one again because `x < rollMax[0]` is \(1<1\), which is false; it has five legal completions. Face two behaves the same way. After any of faces three through six, repeating is allowed and all six second faces are legal. The total is \(5+5+6+6+6+6=34\).

**Why the state recurrence is correct**

Take any state `(i, j, x)`. If \(i=n\), the chosen prefix is already one complete valid sequence, so returning one is correct. Otherwise, every valid completion begins with exactly one next face \(k\). When \(k\neq j\), its new streak is exactly one. When \(k=j\), it is legal exactly if increasing the current streak does not exceed that face’s limit. The two branches reproduce these conditions exactly and update all information needed by the next state.

Assuming recursive calls correctly count completions of states with one more placed roll, summing them counts every valid completion of the current state exactly once. Induction backward from \(i=n\) proves every cached result, including the initial answer.

**Modulo handling**

The count can be enormous. Each state returns `ans % (10**9 + 7)`. Because parent states only add child counts, replacing each child by its remainder preserves the final remainder. The base case returns one directly, which is already below the modulus.

**Exact implementation costs and limitations**

It is important not to confuse this top-down source with a rolling bottom-up implementation. `@cache` retains results for every reached value of `i`, not merely the current and next layer. Its space consumption therefore grows with \(n\).

The recursion depth also grows by one per roll and can reach \(n+1\). With \(n\) as large as 5000, a standard Python interpreter’s usual recursion limit may be too low unless the execution environment raises it. The accepted package source shows that this implementation worked in its verification environment, but a standalone environment must account for that stack requirement.

## Complexity detail

Define

\[
R=\sum_{v=1}^{6}\texttt{rollMax}[v-1].
\]

For each position `i`, face \(v\) has at most `rollMax[v - 1]` possible positive streak lengths. Thus there are \(O(nR)\) reachable memo states. Each state loops over six faces, which is a fixed constant, so time complexity is \(O(nR)\).

The cache stores \(O(nR)\) results, and the recursive call stack uses \(O(n)\) additional space. Since \(R\geq6\), the cache dominates asymptotically, giving \(O(nR)\) auxiliary space for this exact code. The manifest’s \(O(R)\) space claim would describe a bottom-up rolling-layer implementation, not this all-layers `@cache` implementation.

## Alternatives and edge cases

- **Bottom-up rolling DP:** Keep counts for the current roll length by face and streak, then build the next layer. It preserves \(O(nR)\) time while reducing auxiliary space to \(O(R)\) and avoids recursion-depth concerns.
- **Bottom-up DP with all layers:** This mirrors the memo states iteratively and avoids recursion, but still uses \(O(nR)\) space.
- **Inclusion-style recurrence by final face:** Track totals ending in each face and subtract sequences whose run would become too long. It can reduce constant factors but is easier to index incorrectly.
- **Unrestricted brute force:** Testing all \(6^n\) sequences ignores overlapping suffix states and is infeasible.
- **Every limit equals one:** The next face must always differ from the last. There are six choices initially and five thereafter, so the answer is \(6\cdot5^{n-1}\) modulo the required modulus.
- **A limit larger than the remaining rolls:** It never binds during that state. The same-face branch remains available until the sequence ends.
- **Initial sentinel:** Starting with `j = 0` prevents indexing `rollMax[-1]` because every real `k` differs from zero. Replacing the sentinel with a real face would incorrectly constrain the first roll.
- **One roll:** All six faces are legal, so the recursion produces six completed sequences.
- **Face-to-index conversion:** Face \(j\) maps to `rollMax[j - 1]`. Omitting the minus one would read the wrong limit and fail for face six.
- **Recursion limit:** Depth can reach 5001 calls for the maximum input. A portable Python implementation should prefer the iterative rolling form or deliberately configure a sufficient recursion limit.
- **Required decorator import:** The exact source assumes `cache` from `functools` is available. A standalone module must import it.
