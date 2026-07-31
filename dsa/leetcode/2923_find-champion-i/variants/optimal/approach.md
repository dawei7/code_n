## General

**Eliminate a weaker candidate with one comparison.** Start with team 0 as the
best team seen so far. When the next team is considered, compare it directly
with the current candidate. If `grid[team][candidate] == 1`, the new team is
stronger and replaces the candidate. Otherwise the current candidate is
stronger and remains.

After processing indices through $t$, the candidate is the strongest among
those $t+1$ teams. This holds initially for one team. For the induction step,
the complete pairwise relation determines which of the previous strongest and
the new team is stronger, and transitivity ensures that winner is also
stronger than every earlier team. The invariant therefore holds through the
last index, where the candidate is strongest among all teams. No team is
stronger than it, so it is exactly the champion.

## Complexity detail

Let $n=\lvert\texttt{grid}\rvert$. The scan performs one matrix lookup for
each team after the first, taking $O(n)$ time. It stores only one candidate
index, so the auxiliary space is $O(1)$. The already supplied $n\times n$
input matrix is not auxiliary storage.

## Alternatives and edge cases

- **Scan every row:** Finding the row with $n-1$ wins is correct under the complete ordering but inspects $O(n^2)$ entries.
- **Count incoming losses:** Summing each column and selecting the zero-loss team also takes $O(n^2)$ time and $O(n)$ space if counts are stored.
- **Sort teams by comparisons:** A comparison sort needs $O(n\log n)$ lookups, while elimination needs only $n-1$.
- **Champion at the final index:** The last comparison can replace every prior candidate, so the scan must include all teams.
- **Non-numeric strength order:** Team labels do not imply strength; only matrix comparisons may guide elimination.
- **Cyclic tournament:** The contract excludes cycles through transitivity. Without that guarantee, elimination alone might require a final verification pass.

