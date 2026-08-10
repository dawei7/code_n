## General

The output consists of three consecutive groups: values less than `pivot`, values equal to it, and values greater than it. The relative order within the less-than and greater-than groups must be stable.

The exact solution constructs these groups independently while scanning the input once.

**Classify every value exactly once**

Three lists begin empty:

- `a` stores values less than the pivot;
- `b` stores values equal to the pivot;
- `c` stores values greater than the pivot.

For each `x` in `nums`, the `if`, `elif`, and `else` chain places it into exactly one list. Integer comparison is exhaustive: every value is less than, equal to, or greater than the pivot, and no value belongs to two categories.

**Why appending preserves relative order**

The loop visits `nums` from left to right. Suppose two less-than values occur at original indexes $i<j$. The first is appended to `a` before the second, and list append never changes earlier positions. They retain their relative order.

The same argument applies to greater-than values in `c`. Equal values are indistinguishable numerically, but `b` also preserves their encounter order.

This stability is the reason an in-place quicksort-style partition is unsuitable: swapping values toward opposite ends can reverse or scramble elements within a category.

**Concatenate groups in the required order**

The return expression `a + b + c` creates a list containing all of `a`, followed by all of `b`, followed by all of `c`.

Every less-than value therefore precedes every equal and greater value. Every pivot value lies between the outer groups. Every greater value appears last. Since each group is stable, all contract conditions hold simultaneously.

For `[9,12,5,10,14,3,10]` with pivot ten:

- `a` becomes `[9,5,3]`;
- `b` becomes `[10,10]`;
- `c` becomes `[12,14]`.

Concatenation yields `[9,5,3,10,10,12,14]`.

**Why every input occurrence appears once**

Each loop iteration performs one append, and there are $n$ iterations. The three list lengths sum to $n$. Concatenation therefore neither drops nor duplicates any occurrence.

The contract guarantees that `pivot` appears in `nums`, so `b` is non-empty. The algorithm would still behave sensibly without that guarantee by joining an empty middle list.

**Why the construction is correct**

Take any returned position. Its containing list proves its comparison category, and list concatenation proves its category’s global placement. For two original values in the same required stable category, encounter-order appends preserve their order. These facts cover ordering, stability, and multiplicity, so the returned list is a valid rearrangement.

Conversely, the required category order fixes the three-block structure. The method fills each block with exactly its input subsequence, so it constructs the natural stable partition directly.

**Maintain a simple loop invariant**

After any prefix of `nums` has been processed, `a`, `b`, and `c` are exactly the less-than, equal, and greater subsequences of that prefix in encounter order. Classifying the next value appends it to the one correct subsequence without disturbing the other two. When the prefix becomes the whole input, the invariant describes the complete three blocks used by the return expression.

## Complexity detail

Let $n$ be the length of `nums`. Classification visits each element once, costing $O(n)$ time. Concatenating three lists copies $n$ references into the returned list, adding another $O(n)$ pass. Total time remains $O(n)$.

Lists `a`, `b`, and `c` together store $n$ references. The concatenated result stores another $n$ references while the category lists still exist, so peak additional memory is $O(n)$. The exact code does not reuse one category list as the output.

The input list is never modified.

## Alternatives and edge cases

- **Fixed output with counted boundaries:** First count category sizes, then make a second stable pass writing into three known output regions. This is also $O(n)$ time and output space.
- **Two-direction stable fill:** Scan less-than values forward and greater-than values backward while filling opposite ends carefully. It can reduce temporary lists but is less direct.
- **Quicksort partition:** Standard swaps achieve category separation but do not preserve relative order.
- **Sort the array:** Sorting is $O(n\log n)$ and imposes value order within categories rather than merely preserving original order.
- **All values equal pivot:** `a` and `c` are empty, and the output equals the input.
- **No values less than pivot:** Concatenation begins with `b` and then `c`.
- **No values greater than pivot:** `c` is empty, so pivot values finish the result.
- **One element:** It must equal the pivot under the guarantee and is returned alone.
- **Duplicate non-pivot values:** Every occurrence is appended, and their original sequence is retained.
- **Negative values:** Comparisons work without sign-specific branches.
- **Pivot at the input’s beginning or end:** Original pivot position is irrelevant; all equal values move into the middle block.
- **Stable requirement applies separately:** A less-than value need not preserve order relative to a greater-than value because categories must be separated.
- **Input preservation:** Fresh lists satisfy the instruction without mutating `nums`.
- **Unique stable result:** Although equal pivot copies are indistinguishable, the less-than and greater-than subsequences have only one order that satisfies stability.
