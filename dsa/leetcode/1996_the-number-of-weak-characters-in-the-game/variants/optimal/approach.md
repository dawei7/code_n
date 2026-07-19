## General
**Turn the two-dimensional comparison into a sweep.** Sort characters by decreasing attack. Every character processed earlier then has attack at least as large as the current one, so a running maximum can summarize their defenses.

**Neutralize equal-attack characters.** Within one attack value, sort defense in increasing order. During the left-to-right sweep, lower defenses from that same group appear first and may raise the running maximum, but they cannot exceed a later defense in their group. Consequently, no equal-attack character is incorrectly declared weak. When the attack decreases, the stored maximum may come from a strictly larger attack, which is exactly what the definition requires.

**Compare against the strongest eligible defense.** Maintain `maximum_defense` over the processed prefix. If the current defense is smaller, an earlier character has both strictly larger attack and strictly larger defense, so count the current character. Otherwise, update the maximum. This is sufficient because only the largest eligible defense matters: if it cannot dominate the current defense, no smaller processed defense can.

## Complexity detail
Sorting $N$ pairs takes $O(N\log N)$ time, and the sweep takes $O(N)$ time. Python's sort may use $O(N)$ auxiliary space in the worst case; the scan itself uses $O(1)$ additional state.

## Alternatives and edge cases
- **Compare every pair:** Directly searching for a dominator for each character takes $O(N^2)$ time.
- **Bucket by attack:** Because statistics are bounded, suffix maxima over attack buckets can achieve $O(N+M)$ time for maximum statistic value $M$, at the cost of an $O(M)$ table.
- Characters with equal attack never dominate one another, even when their defenses differ.
- Characters with equal defense never dominate one another, even when their attacks differ.
- Duplicate pairs are separate characters but cannot dominate each other.
- A character needs only one dominator; several possible dominators do not increase its contribution beyond one.
