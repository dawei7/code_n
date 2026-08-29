## General

**Try candidate submatrices in required answer order.** If board size is $M\times N$ and pattern size $R\times C$, a top-left corner must satisfy $0\le i\le M-R$ and $0\le j\le N-C$.

The outer loops enumerate rows first and columns second. This is exactly lexicographic coordinate order, so returning the first match automatically gives the lowest row, then lowest column.

If the pattern is larger than the board in either dimension, the corresponding range is empty and the method returns `[-1,-1]`.

**Validate literal digit cells directly.** `pattern[a][b].isdigit()` distinguishes a digit character. Its integer value must equal the corresponding board cell. One mismatch rejects the candidate immediately.

**Maintain a consistent letter-to-digit mapping.** Dictionary `d1` maps each encountered pattern letter to its board digit. On a repeated letter, a different board value rejects the candidate. This enforces that all occurrences of one letter receive the same digit.

**Maintain injectivity in the reverse direction.** Dictionary `d2` maps a used board digit back to its pattern letter. If another distinct letter tries to use that digit, the reverse mapping differs and the candidate fails.

Together `d1` and `d2` form a one-to-one mapping among pattern letters used in the candidate.

**A trace.** Pattern `["ab","bb"]` over board block `[[1,2],[2,2]]` sets `a -> 1` and `b -> 2`. Repeated b cells all see 2, and reverse mappings remain unique, so the block matches.

Pattern `["xx"]` over `[1,2]` first sets `x -> 1`, then the repeated x sees 2 and fails consistency.

**Why dictionaries reset for every placement.** A letter's chosen digit is local to a candidate submatrix. A later placement may map the same symbol differently. `check` creates fresh maps on each call, preventing state leakage.

**What `check` enforces for one candidate.** Literal cells are compared exactly. For letter cells, forward mapping enforces equal-symbol consistency and reverse mapping enforces distinct-letter uniqueness. Thus `check` returns true precisely when those implemented constraints hold for the candidate, and row-major early return selects the required first coordinate.

**Literal-digit distinctness defect.** The reference additionally says that for a letter $x$, every pattern cell not equal to $x$ must map to a different board digit. That includes literal digit cells. The exact source never inserts literal digits into `d2`, so it permits a letter to map to the same digit as a different literal symbol.

For example, pattern `"a1"` against board row `[1,1]` passes this code: `a` maps to 1 and the literal `1` matches. Under the stated “every different pattern cell must be different” rule, it should fail. This is a genuine correctness gap in the protected source.

## Complexity detail

There are at most $(M-R+1)(N-C+1)=O(MN)$ placements. Each successful/full check examines $RC$ cells, so worst-case time is $O(MNRC)$.

Maps hold at most 26 letters and 10 board digits. Under the fixed alphabets, auxiliary space per check is $O(1)$. The maps are discarded between placements. Inputs are not modified.

## Alternatives and edge cases

- **Include literals in reverse reservations:** Recording fixed digit symbols in the reverse mapping would enforce the full distinctness wording and repair the source defect.
- **Canonical encoding:** Convert each pattern and candidate block to equality-class signatures, while separately checking literals; this can make bijection rules explicit.
- **Repeated letter:** Every occurrence must see the same board digit.
- **Two different letters:** They must use different digits, enforced by `d2`.
- **Letter equals literal digit:** The exact source allows it, contradicting the reference's all-different-symbol wording.
- **All literal pattern:** Dictionaries remain empty and matching is direct equality.
- **Pattern larger than board:** No placement loop runs.
- **Multiple matches:** Row-major return chooses the required coordinate.
- **Early mismatch:** Validation stops without scanning the rest of that placement.
- **Fixed alphabet:** At most ten distinct letters can map simultaneously because board digits range only 0 through 9.
- **Literal conversion:** `int(pattern[a][b])` is safe because `isdigit()` was checked first and each pattern cell is one character.
- **Board zeros:** Zero is a normal candidate digit. Dictionary membership tests use keys rather than truthiness, so mapping to zero is handled correctly.
- **More than ten pattern letters:** No candidate can satisfy injectivity into ten digits, and `d2` eventually detects a collision among letter cells.
- **Fresh failure scope:** Returning false exits only the current `check`. The outer loops continue with the next coordinate and fresh mappings.
- **Row-major proof:** All columns of row $i$ are tested before row $i+1$, so an early return cannot skip a coordinate preferred by the tie-break.
- **Input preservation:** Neither matrix is edited; mappings are hypothetical and local.
- **Literal repetitions:** Two identical literal characters naturally require the same digit because both are compared directly with that literal value.
- **Dictionary update after checks:** The source verifies existing forward and reverse constraints before assigning, so a conflicting cell cannot overwrite evidence and hide the mismatch.
