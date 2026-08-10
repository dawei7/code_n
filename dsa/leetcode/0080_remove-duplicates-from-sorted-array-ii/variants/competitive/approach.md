## General

**Give the two pointers different responsibilities**

`i` scans original input positions from left to right. `last` is the index of the final value currently retained in the compacted prefix. Thus the meaningful output is always `A[:last + 1]`, and the next retained value will be written at `last + 1`.

For a nonempty input, the first value is already a valid retained value. Initialization sets `last = 0` and begins scanning at `i = 1`. The explicit empty-list guard returns zero outside or beyond the stated nonempty constraint.

Writes occur at or behind `i`, because the retained prefix cannot contain more elements than have been scanned. Therefore overwriting compacted positions never destroys a future unread input value.

**Let `same` describe the retained run length**

The Boolean `same` is false when the value at `A[last]` currently appears once at the end of the retained prefix. It is true when that value appears twice at the end. Since the array is sorted, no earlier separated occurrence of the current value needs to be considered; its entire run is consecutive.

Initially the first value has been retained once, so `same = False` is correct.

The compact condition accepts a scanned value when `A[last] != A[i] or not same`. These two parts cover the only legal cases:

- If the scanned value differs from the last retained value, it begins a new sorted run and its first copy must be kept.
- If it equals the last retained value but `same` is false, only one copy has been retained, so the second copy may be kept.
- If it equals and `same` is true, two copies are already retained, so the candidate is an excessive duplicate and is skipped.

**Update the Boolean before moving the write boundary**

Inside the acceptance branch, `same = A[last] == A[i]` is evaluated while `last` still refers to the previous final retained value.

For a different new value, the equality is false, correctly recording that the new run has one retained copy. For an equal accepted value, the equality is true, correctly recording that the current run now has two copies. Only then does the source increment `last` and write `A[i]` into the new output position.

If the candidate is skipped, none of `same`, `last`, or the retained prefix changes. The scan pointer still advances. More copies of the same run will continue to see equality plus `same == True` and will also be skipped until a different value begins a new run.

**Trace state across a run boundary**

For `[0, 0, 1, 1, 1, 1, 2, 3, 3]`, the second zero equals the last retained zero while `same` is false, so it is accepted and `same` becomes true. The first one differs, so it is accepted and resets `same` to false. The second one is accepted and sets `same` true; the third and fourth ones are skipped.

When two arrives, it differs from the last retained one and starts a new one-copy run. Both threes are then accepted. The meaningful prefix becomes `[0, 0, 1, 1, 2, 3, 3]`, and `last + 1` is seven.

**Why comparing with the retained prefix is correct**

The scan value is compared with `A[last]`, not with `A[i - 1]`. After excessive duplicates have been skipped, `A[i - 1]` may belong to input that was not retained. The question is whether the output already holds two copies, so the final retained value and `same` are the appropriate state.

Sorted order ensures that a different scan value truly starts a new run and that the algorithm will never encounter the old value again later.

**A loop invariant**

Before each iteration, `A[:last + 1]` is the correct at-most-two compaction of original input positions before `i`. It is non-decreasing. `same` is true exactly when the final retained value occurs twice at the end of that prefix.

A new value is copied and establishes a one-copy run. A second equal value is copied and establishes a two-copy run. A later equal value is skipped and leaves the already correct prefix unchanged. These are all cases allowed by sorted input, so each iteration preserves the invariant.

When `i` reaches the original length, the invariant describes the complete input. Returning `last + 1` gives the number of retained elements, and the custom judge reads exactly that correct prefix.

## Complexity detail

Let $n$ be the input length. The scan index increases once per loop iteration and never moves backward. Each element causes constant comparisons and at most one assignment, giving $O(n)$ time, matching the manifest.

The source stores two indices and one Boolean. It allocates no list, set, or count table, so auxiliary space is $O(1)$, also matching the manifest. Values beyond the returned prefix are deliberately left unspecified.

## Alternatives and edge cases

- **Value two positions back:** Keep a write length `k` and accept `x` when `k < 2` or `x != A[k - 2]`. It removes the explicit `same` flag.
- **Numeric run count:** Store an occurrence count instead of a Boolean. It generalizes more directly to “at most `r` copies” but carries more state than needed for two.
- **Physical deletion:** Popping extra values shifts later list elements and can make total time quadratic.
- **Empty list:** The defensive branch returns zero, although the official domain is nonempty.
- **One element:** Initialization already retains it, the loop is skipped, and one is returned.
- **Exactly two copies:** The second is accepted when `same` is false.
- **Long duplicate run:** Once `same` becomes true, every further equal scan value is skipped.
- **New value after skipped copies:** Inequality with the last retained value resets `same` to false and starts the new run correctly.
- **All distinct:** Every value starts a new run and the returned length is unchanged.
- **All equal:** At most the initial value and one additional value are retained.
- **Negative values:** Equality and ordering work identically for all allowed integers.
- **Unspecified tail:** Skipped original values may remain beyond `last`; the judge intentionally ignores them.
- **Sorted-order requirement:** The Boolean describes one consecutive run and would be insufficient for unsorted repeated values.
