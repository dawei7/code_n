## General

**Match the next piece from the current target position**

The order inside each piece is fixed, but the pieces themselves may be permuted. Therefore, when the unmatched suffix of `arr` begins at index `i`, any piece placed next must begin with `arr[i]`.

The source uses `i` as the first unmatched target index. Its inner search starts `k` at zero and scans `pieces` until it finds a piece whose first value equals `arr[i]`. If the scan reaches the end, no piece can begin this portion of the target, so it returns false.

The global distinctness guarantee makes the starting value decisive: flattened `pieces` contains no repeated integer, so at most one piece can have `arr[i]` as its first element. There is no need to branch over several candidate pieces.

**Consume matching values in that piece**

After locating `pieces[k]`, `j` starts at zero. While `j` is still inside the piece and `arr[i] == pieces[k][j]`, both indices advance.

This compares the piece's values in their given order. It never rearranges them. If the complete piece matches, `j` reaches its length and the outer loop resumes with `i` at the next unmatched position of `arr`.

For `arr = [91,4,64,78]` and pieces `[[78],[4,64],[91]]`, the searches find:

- `[91]` at `i=0`,
- `[4,64]` at `i=1`,
- `[78]` at `i=3`.

Every piece is consumed in order and `i` reaches the target length, so the method returns true.

For `arr = [49,18,16]` and piece `[16,18,49]`, no piece begins with 49, so it returns false immediately. Having the same values is insufficient when their required internal order differs.

**Why the distinctness and total-length guarantees help**

In an intended successful execution, every chosen piece is determined uniquely by its first value and must match completely. Because the total length of all pieces equals `len(arr)`, consuming enough complete, non-repeated pieces to cover all of `arr` also consumes all available piece values. No separate “used piece” set is necessary for a valid formation.

The distinct values in `arr` also mean the scan cannot encounter the same target starting value twice, so a piece cannot be selected twice along a successful match.

The intended invariant is: before an outer iteration, `arr[:i]` equals the concatenation of the fully consumed pieces selected so far. Finding and completely matching the unique next piece extends that invariant. When `i == len(arr)`, those pieces form the whole target.

**What the exact implementation does on a partial mismatch**

The source does not explicitly test whether `j` reached the end of the selected piece. If a comparison fails inside the piece, the inner loop stops and the outer loop simply searches for a piece beginning at the still-unmatched `arr[i]`.

Under the total-length and uniqueness constraints, such abandoned piece suffixes prevent a genuine successful complete formation: matched prefixes plus omitted values cannot cover all $n$ distinct target positions using only $n$ available piece entries. The process will normally later fail to find a starting piece.

However, relying on that indirect failure is less robust than returning false immediately when `j < len(pieces[k])`.

**Why the missing local bounds check is safe under the coupled constraints**

The comparison loop checks `j < len(pieces[k])` but does not separately check `i < len(arr)` before reading `arr[i]`. Locally, that looks risky: what if the chosen piece matches the entire remaining target and still has an extra entry?

The global constraints rule that situation out. Every selected piece begins with a distinct value from `arr`, and `arr` itself has distinct values, so the same piece cannot be selected twice. Before selecting the current piece, suppose `i` target entries have been matched. The previously selected distinct pieces have total length at least `i`, because each supplied at most its full length of matches. If the current piece were longer than the remaining `len(arr) - i` positions, then the total lengths of the previously selected pieces plus the current piece would exceed `len(arr)`. But all selected pieces are a subset of `pieces`, whose total length is exactly `len(arr)`. That is impossible.

The same counting argument shows that a run reaching the end of `arr` cannot have abandoned a suffix of an earlier selected piece. Any abandoned entries would make the full lengths of the distinct selected pieces exceed the number of matched target positions, while all piece lengths together equal that target length.

So the implementation is bounds-safe for conforming inputs, although an explicit `i < len(arr)` test and a direct full-piece check would make the local control flow easier to audit. The exact source should still be distinguished from the hash-map implementation summarized by the manifest.

## Complexity detail

Let $n=\lvert arr\rvert$ and $p=\lvert pieces\rvert$. Suppose $b$ piece boundaries are attempted. At each boundary, the source scans from the beginning of `pieces` and can inspect all $p$ first values. Across the run, this costs $O(bp)$.

The character-by-character piece matching advances `i` on successful comparisons, so at most $O(n)$ such matches occur. Total time is $O(bp+n)$, which is $O(n^2)$ in the worst case because both $b$ and $p$ can be $O(n)$.

This differs from the manifest's `O(n)` time, which would require a hash map from each piece's first value to the piece. The checked-in source performs a repeated linear search and is not linear in the worst case.

Only indices `i`, `j`, and `k` are stored, so actual auxiliary space is $O(1)$, tighter than the manifest's `O(n)` map-based space. The input arrays are not modified.

## Alternatives and edge cases

- **First-value hash map:** Build `{piece[0]: piece}` once, then find each next piece in expected $O(1)$ time. Comparing all piece entries gives $O(n)$ total time and $O(p)$ space, matching the manifest.
- **Sort pieces and binary search first values:** This gives $O(p\log p+n\log p)$ time and mutates or copies the piece order. It is slower than hashing but faster than repeated full scans.
- **Explicit full-piece validation:** After the inner loop, immediately return false unless `j == len(piece)`. Also check `i < len(arr)` before each target access. This makes failure behavior direct and bounds-safe.
- **No piece begins with the next target value:** The source returns false through `k == len(pieces)`.
- **A piece has the right values in the wrong order:** Matching stops because piece order cannot be changed, and formation is impossible.
- **Single-element pieces:** They can be concatenated in the unique order dictated by `arr`.
- **One piece contains the whole target:** It succeeds only when every value matches in order.
- **Distinctness:** It guarantees at most one candidate piece for a starting value and prevents valid reuse of a piece.
- **Equal total length:** A successful full target match necessarily accounts for every available piece entry; this is central to the no-used-set reasoning.
- **Exact-source complexity:** Calling this variant “Optimal” does not change the fact that it linearly rescans `pieces` at every boundary.
- **Defensive indexing:** The matching condition should normally include `i < len(arr)` even when global constraints make an overrun difficult or impossible on conforming data.
