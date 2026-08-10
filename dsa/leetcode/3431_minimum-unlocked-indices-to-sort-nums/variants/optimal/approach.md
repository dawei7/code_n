## General

**Only two adjacent inversions are swappable.** Values are restricted to $1$, $2$, and $3$. A swap at boundary $i$ is allowed only when

$$
\texttt{nums}[i]-\texttt{nums}[i+1]=1.
$$

Therefore, the only value pairs that can swap are $(2,1)$ and $(3,2)$. A pair $(3,1)$ differs by two and can never swap directly.

Adjacent swaps change the relative order of two elements only when those two elements are swapped with each other. Since a $3$ and a $1$ can never swap, their relative order is invariant under every allowed operation. If any $3$ initially appears before any later $1$, sorted non-decreasing order is impossible even after unlocking every index.

The source detects exactly this obstruction with:

- `first3`: the first index containing $3$;
- `last1`: the last index containing $1$.

If `first3 < last1`, some $3$ precedes some $1$, so it returns `-1`.

**Identify all boundaries needed for \(2\)-before-\(1\) inversions.** If a $2$ occurs before a later $1$, those values must eventually swap through adjacent $(2,1)$ operations. Let `first2` be the first position containing $2$ and `last1` the last position containing $1$.

Every boundary

$$
\texttt{first2}\le i<\texttt{last1}
$$

must permit a swap. One way to see necessity is to follow the earliest $2$ and the latest $1$: their relative order must reverse, so movement between their positions must cross every intervening boundary. A locked boundary anywhere in that interval would permanently separate some required $1$ and $2$ movement.

If no $2$ occurs before a $1$, then `first2 >= last1` and this half-open interval is empty.

**Identify all boundaries needed for \(3\)-before-\(2\) inversions.** Symmetrically, let `first3` be the earliest $3$ and `last2` the latest $2$. Sorting all $2$s before all $3$s requires every boundary

$$
\texttt{first3}\le i<\texttt{last2}
$$

to be unlocked whenever that interval is non-empty.

These are the only two unlock intervals because, after ruling out a $3$ before a $1$, every possible inversion in a three-value array is either $2$ before $1$ or $3$ before $2$.

**Why unlocking the union is sufficient.** Consider ordinary bubble-sort behavior: whenever an adjacent inverted pair appears, swap it. Under the feasibility condition, the only adjacent inverted pairs that can arise are $(2,1)$ and $(3,2)$, exactly the pairs allowed by the difference rule.

Any adjacent $(2,1)$ at boundary $i$ satisfies `first2 <= i < last1`: a $2$ exists at or before $i$, and a $1$ exists at or after $i+1$. Thus its boundary belongs to the first interval. Any adjacent $(3,2)$ similarly belongs to the second interval. If the union of both intervals is unlocked, every bubble-sort inversion swap is allowed, and repeated swaps eventually produce sorted order.

Thus every boundary in the union is necessary, and unlocking all of them is sufficient. The minimum operation count is simply the number of those boundary indices that are currently locked.

**How the source obtains the four endpoints.** One pass initializes missing-first sentinels to $n$ and missing-last sentinels to $-1$. When it sees:

- a $1$, it updates `last1`;
- a $2$, it updates `first2` on the first occurrence and always updates `last2`;
- otherwise, the constraints mean the value is $3$, so it updates `first3`.

The sentinels make absent-value cases work without branches. If there is no $2$, for example, the first interval starts at $n$ and the second ends at $-1$, so both relevant comparisons are false.

The final generator scans `locked`. Python treats $1$ as true and $0$ as false. The expression

`st and (first2 <= i < last1 or first3 <= i < last2)`

contributes one exactly when boundary $i$ is currently locked and lies in at least one mandatory interval. The logical `or` counts an overlapping boundary only once, as required because unlocking one index enables both kinds of swaps there.

For the impossible third example, a $3$ at index $4$ precedes a $1$ at index $6$. Since those two elements can never cross, all-zero `locked` still cannot make the array sortable, and `-1` is correct.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The first scan visits every value once, and the final sum visits every lock once. Total time is $O(n)$.

Only four endpoint indices, the length, and generator loop state are stored. The generator is lazy and does not construct an interval array, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Simulate swaps after every unlock choice:** Exploring subsets of locked boundaries is exponential and unnecessary once mandatory intervals are characterized.
- **Unlock every inversion position in the original array only:** Swaps create new adjacent inversions at different boundaries. Entire movement intervals, not just initially inverted adjacencies, must be available.
- **Standard unrestricted inversion count:** This problem does not allow arbitrary adjacent swaps. A $3$ and $1$ can never cross, which creates the explicit impossibility test.
- **Already sorted input:** Both mandatory intervals are empty, so the answer is zero regardless of unrelated locked positions.
- **No value \(2\):** A $3$ before a $1$ is impossible; otherwise the array already has all $1$s before all $3$s and no unlock is needed.
- **Only values \(1\) and \(2\):** Feasibility is automatic, and only `[first2,last1)` matters.
- **Only values \(2\) and \(3\):** Only `[first3,last2)` matters.
- **Overlapping intervals:** A locked boundary in both is counted once because one unlock operation changes that single `locked[i]` to zero.
- **Boundary versus element index:** `locked[i]` controls the swap between positions $i$ and $i+1$. Half-open endpoint intervals correctly enumerate those boundaries.
- **Sentinel values:** `n` for a missing first occurrence and `-1` for a missing last occurrence make all empty intervals fail their chained comparisons naturally.
