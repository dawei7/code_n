## General
**Retain both the final face and its run length.** A partial sequence's legal next rolls depend only on which face appears last and how many consecutive times it currently appears. Store a count for every permitted `(face, run_length)` state. At length one, each face has one sequence with run length one.

**Separate face changes from run extensions.** For each new roll position, first total the states ending in every face and the total across all faces. A new run of face `f` with length one can follow any sequence not ending in `f`, so its count is the all-face total minus face `f`'s total. Existing runs of `f` shift from length `r` to `r + 1` only while `r` is below `roll_max[f]`.

**Why the transitions form a partition.** Every valid longer sequence either changes face on its final roll, uniquely placing it in a new length-one state, or repeats its final face, uniquely extending the previous run by one. The limit check rejects exactly the forbidden extensions. Conversely, every constructed state respects its face's bound and inherits validity from its prefix. Induction over sequence length therefore makes the final sum count every valid sequence exactly once.

## Complexity detail
Each roll position totals and advances the $R$ states once, giving $O(nR)$ time. Only the current and next collections of $R$ states are retained, so auxiliary space is $O(R)$. All additions and subtractions are reduced modulo $M$.

## Alternatives and edge cases
- **Enumerate complete roll sequences:** Recursive generation is direct but explores exponentially many valid prefixes.
- **Recompute every prefix length independently:** It produces correct counts but repeats all earlier transitions and takes $O(n^2R)$ time.
- **Three-dimensional table by length, face, and run:** This mirrors the recurrence but stores $O(nR)$ values when only the preceding length is needed.
- **One roll:** Every face is legal regardless of its positive limit, so the answer is `6`.
- **All limits equal one:** Adjacent rolls must differ, yielding $6\cdot5^{n-1}$ sequences before modular reduction.
- **Large limits:** When every limit is at least `n`, all $6^n$ sequences are valid.
- **Simultaneous layer update:** New states must not feed other transitions at the same sequence length.
