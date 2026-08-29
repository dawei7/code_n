## General

**Search for the smallest feasible cap on identical runs.** Candidate `m` means every maximal run in the final binary string must have length at most `m`. Helper `check(m)` computes the minimum flips needed and compares it with `numOps`.

If a cap is feasible, every larger cap is feasible. This false-then-true monotonicity supports a lower-bound binary search rather than testing all $n$ answers.

**Maximum run one means a completely alternating string.** There are only two legal binary targets:

`010101...` and `101010...`.

Against pattern `"01"[i & 1]`, the source counts positions already matching. Flipping those matching positions creates the opposite pattern, while flipping the nonmatching positions creates the first pattern. Therefore costs are `cnt` and `n-cnt`, and their minimum is exact.

This slightly counterintuitive match count is correct even though most implementations count mismatches.

**For caps above one, process maximal original runs.** Let one run have length `k`. To prevent any unchanged block from exceeding `m`, one strategically flipped character can separate each group of `m+1` original equal characters. Required count is

`k // (m + 1)`.

Run contributions add because the $m>1$ construction can place separators within each run without needing the globally rigid alternation required at cap one.

**Discover runs without storing them.** Counter `k` grows as the scan advances. A boundary occurs at the string end or when current and next characters differ. The method adds this run's quotient to total `cnt` and resets the counter.

It may continue scanning even after `cnt > numOps`; an early exit could improve constants but is not present in the exact source.

**Trace `s="000001"`.** Original run lengths are five and one. For `m=2`, cost is `5//3 + 1//3 = 1`, so one flip suffices. For `m=1`, the alternating-pattern comparison requires more than one flip, making answer two.

**Trace an exact multiple.** A run of length six under cap two costs two because two separators are needed. A run of length five costs one. The floor quotient by `m+1` captures both boundary cases.

**Binary search through `bisect_left`.** `range(n)` acts as a virtual array of candidates; `lo=1` excludes meaningless cap zero. Key function returns feasibility Boolean. Python orders false before true, so the insertion position of true is the first feasible cap.

If no value from one to `n-1` succeeds, the insertion position is `n`. Cap `n` always works without flips, so returning an index not physically present in `range(n)` is deliberate.

**Why binary-search monotonicity is secure.** A string whose longest run is at most `m` also has longest run at most `m+1`. The same flip set witnesses feasibility, independent of how `check` computes its minimum.

**Why the result is exact.** `check` gives exact flip costs for cap one and for every larger cap via run splitting. Binary search rejects all smaller caps and returns the first within the budget.

**Run costs depend only on lengths, not on whether the run is zeros or ones.** Flipping a separator changes it to the opposite bit in either case. The scan therefore needs only counter `k` and boundary comparisons; it never stores the run character.

**The feasibility key is sorted even though costs are recomputed.** As `m` grows, each quotient `k//(m+1)` cannot increase, and cap-one feasibility joins the same semantic monotonic property. Thus calls may occur in binary-search order rather than increasing order without affecting correctness.

**Why the always-feasible bound is `n`.** No string has an identical run longer than its total length. Performing zero flips witnesses cap `n` for every input and budget. This guarantees the lower-bound search has a conceptual true sentinel.

**Version-II scaling.** With `n<=10^5`, quadratic limit enumeration would be too slow. The $O(n\log n)$ design is necessary. The executable source is identical to version I; only the constraint makes its efficiency more consequential.

**Space differs from the manifest.** No run array, prefix structure, or transformed string is allocated. The source uses scalars, a two-character pattern, and a lazy `range`, so auxiliary space is $O(1)$ rather than $O(n)$.

## Complexity detail

One `check` scans all $n$ characters in $O(n)$ time. Binary search makes $O(\log n)$ probes, for $O(n\log n)$ total time.

Auxiliary space is $O(1)$. Python's range object does not materialize $n$ integers, and generator expressions are consumed lazily.

## Alternatives and edge cases

- **Linear scan over all caps:** It can cost $O(n^2)$ and fails version-II scale.
- **Precompute run lengths:** It reduces repeated boundary detection but uses $O(n)$ space; the exact source rescans.
- **Already alternating:** Answer is one with zero flips.
- **Single-character string:** Binary search returns one through insertion position behavior.
- **All equal, zero operations:** Answer is the full length.
- **Cap one:** Must compare both alternating patterns.
- **Run length below cap:** It contributes zero flips.
- **Run length `m+1`:** It contributes exactly one.
- **Run bit value:** Zero-runs and one-runs use the same quotient.
- **Conceptual true sentinel:** Cap `n` always succeeds without an actual key call.
- **Budget is “at most”:** Unused flips are harmless.
- **Odd/even pattern start:** Taking minimum covers both.
- **No early feasibility cutoff:** Exact code completes each scan.
- **Virtual upper bound:** Returned `n` need not be inside `range(n)`.
- **Modern Python dependency:** `bisect_left` needs `key` support.
- **Input preservation:** `s` remains unchanged.
