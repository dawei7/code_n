## General

**Fix the middle index first.** A length-five subsequence with middle at index `index` must choose exactly two indices to its left and exactly two to its right. Let middle value be `m`.

There are

$$
\binom{L}{2}\binom{R}{2}
$$

total index choices, where $L=\texttt{index}$ and $R=n-\texttt{index}-1$. The source counts all of them and subtracts selections where `m` is not the unique mode.

**Maintain value frequencies on both sides.** `left[v]` counts occurrences strictly before the middle. `right[v]` counts occurrences strictly after it. Initially right contains the whole array; before evaluating one middle occurrence, the source removes that occurrence from right.

`left_middle` and `right_middle` are the available copies of `m` on each side after this removal.

**When is the middle automatically a unique mode?** The selected subsequence already contains the central `m`. If at least two of the four side choices also equal `m`, then its frequency is at least three. Among only five positions, no different value can also occur three times, so `m` is automatically unique mode.

Invalid selections therefore have either zero or exactly one additional copy of `m`.

**Subtract the zero-extra-middle case.** Choose both left positions from values other than `m` and both right positions likewise:

$$
\binom{L-L_m}{2}\binom{R-R_m}{2}.
$$

Then `m` occurs only once and cannot be the unique mode. This is the first `invalid` term.

**Handle exactly one extra middle from the left.** Choose one of `left_middle` copies of `m`. The other three chosen side values consist of one non-middle left value and two non-middle right values.

For `m`, total frequency is two. It fails to be unique precisely when some other value also appears at least twice among those three positions.

The parenthesized expression combines these bad patterns:

- `left_other * other_right_pairs` counts a matching pair chosen on the right, with any non-middle left choice;
- `right_other * other_cross` counts a matching value selected once on each side, plus another right choice;
- `other_left_right_squared` removes overlap introduced when these descriptions count the same all-matching configuration more than intended.

Multiplying by `left_middle` chooses which left occurrence supplies the second `m`.

**Handle exactly one extra middle from the right symmetrically.** Now one of `right_middle` copies is selected, leaving two non-middle left choices and one non-middle right choice. The formula uses left-side equal pairs, cross matches, and `other_left_squared_right` for the symmetric inclusion-exclusion correction.

**Understand the aggregate statistics.** Recomputing sums over every distinct value for every middle would be quadratic. The source maintains:

- `left_pairs = sum_v C(L_v,2)`;
- `right_pairs = sum_v C(R_v,2)`;
- `sum_left_right = sum_v L_v R_v`;
- `sum_left_right_squared = sum_v L_v R_v^2`;
- `sum_left_squared_right = sum_v L_v^2 R_v`.

Subtracting the contribution of `m` converts each global aggregate into its “other values only” version.

**Remove the current occurrence from right in constant time.** If old right count is $q$ and new count is $q-1$, then

$$
\binom q2-\binom{q-1}2=q-1.
$$

So `right_pairs -= right_middle`.

The other moment updates use exact algebraic differences: $L_mR_m$, $L_mR_m^2$, and $L_m^2R_m$ change only for the middle value. This avoids scanning counter keys.

**Add the current occurrence to left after counting.** Moving `m` from middle to the left for the next iteration raises its left count from $p$ to $p+1$. Pair count increases by $p$. Cross moment increases by $R_m$; the squared moments increase by $R_m^2$ and $(2p+1)R_m$ because

$$
(p+1)^2-p^2=2p+1.
$$

The update order preserves the invariant that counters always describe positions strictly around the next middle.

**Count valid selections for this middle.** `total-invalid` leaves exactly those choices where central `m` has strictly greater frequency than every other value. The source adds this contribution modulo $10^9+7$.

**Trace the all-equal case.** Every side choice equals `m`, so `left_other=right_other=0` and all invalid terms vanish. Each choice of middle with at least two positions on each side contributes all $\binom L2\binom R2$ selections. Across six equal elements, this totals six length-five index subsequences.

**Why the linear aggregation is complete.** Every length-five subsequence has one unique middle index. For that middle, it belongs to exactly one of zero, one, or at-least-two extra-middle cases. The formulas reject precisely the first case and tied-frequency selections in the second; the third is automatically valid. Frequency moments count all competing values collectively.

## Complexity detail

Building the right counter costs $O(n)$. Each middle iteration performs a constant number of counter accesses, arithmetic updates, and aggregate formulas, so total time is $O(n)$.

The left and right counters contain at most $O(n)$ distinct values. Other state is scalar, giving $O(n)$ space. Arithmetic uses Python integers, and the accumulated answer is reduced modulo the required constant.

## Alternatives and edge cases

- **Enumerate all five-index subsequences:** It costs $O(n^5)$ and is impossible at $n=1000$.
- **Enumerate competing values per middle:** It can become $O(n^2)$; maintained moments collapse those sums.
- **At least three middle copies:** The middle is automatically unique mode.
- **Exactly two middle copies:** Any other value appearing twice creates a tie and is invalid.
- **Only one middle copy:** It cannot be unique mode among five positions.
- **Not enough positions on one side:** Combination helper returns zero naturally for counts below two.
- **Negative and large values:** Counter keys handle them without coordinate compression.
- **Repeated equal values:** Distinct indices are counted through combination factors.
- **Middle removal timing:** The current occurrence must leave right before formulas are evaluated.
- **Left insertion timing:** It happens only after the current middle contribution is counted.
- **Modulo:** Subtraction may be negative before Python's final modulo normalizes it.
- **Moment exclusion:** Middle-value contributions are subtracted before counting competitors.
- **Generated source:** No local editorial exists; the explanation follows the exact inclusion-exclusion formulas.
- **Input preservation:** Only counters and scalar moments change.
