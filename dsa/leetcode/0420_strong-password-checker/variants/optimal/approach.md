## General
**Measure missing character classes and repeat repairs**

Count how many of lowercase, uppercase, and digit are absent. Also scan maximal equal-character runs. A run of length `L` needs $\lfloor L/3 \rfloor$ replacements when length is already valid, because one changed character can break one block of three.

**Handle passwords shorter than six**

At least $6 - n$ insertions are mandatory. Insertions can simultaneously add missing character classes and split repeated runs, so the optimum is `max(6 - n, missing_types)`; the short-length bound guarantees these edits can cover remaining repeat defects.

**Handle lengths from six through twenty**

No length edit is required. Replacements can both supply a missing type and break a repeat, so the required count is `max(missing_types, replacements)`.

**Spend mandatory deletions where they save replacements**

For $n > 20$, exactly $n - 20$ deletions are unavoidable. Deleting one character reduces $\lfloor L/3 \rfloor$ first for runs with $L \bmod 3 = 0$; after those, two deletions save one replacement for remainder-one runs. Every further replacement reduction costs three deletions. Apply deletions in that marginal-cost order.

**Combine deletion and remaining repair costs**

After optimizing runs, missing classes may still dominate the replacement count, and one replacement can satisfy both needs. The final answer is mandatory deletions plus `max(missing_types, remaining_replacements)`.

**Why the greedy deletion order is optimal**

Every deletion is mandatory regardless of location. A deletion costing one, then two, then three characters per saved replacement provides decreasing benefit. Exchanging a deletion spent on a higher-cost run with one available at lower cost cannot worsen length or class constraints and can only reduce repairs, so choosing marginal costs in order is optimal.

## Complexity detail
One scan identifies character classes and repeat lengths. The three deletion-allocation phases use only counts grouped by remainder, so total time is $O(n)$. A fixed set of counters uses $O(1)$ space.

## Alternatives and edge cases
- **Priority queue of repeat runs:** can repeatedly choose the best deletion target in $O(n \log n)$ time.
- **Rescan every run before each useful deletion batch:** remains correct but can take $O(n^2)$ time.
- **Breadth-first search over edited strings:** gives exact answers only for tiny inputs and has an explosive state space.
- Insertions and replacements can satisfy a missing type while breaking a repeat.
- A password exactly 20 characters long needs no deletion.
- Very long repeated runs may consume all three deletion-cost phases.
- Deleting characters must not be counted as replacing missing character classes.
