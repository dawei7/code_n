## General

Only the first and last letters of a word participate in the corner conditions. Sort the words first, then build one index by first letter and another by the pair `(first letter, last letter)`. The lists inside both indexes inherit sorted order.

Choose `top` in sorted order. A possible `left` must come from the first-letter bucket for `top[0]`, and a possible `right` must come from the bucket for `top[3]`. After choosing three distinct words, both required boundary letters of `bottom` are known: it must start with `left[3]` and end with `right[3]`. The corner-pair index therefore supplies exactly the bottom candidates worth checking. Discard any candidate already used in one of the other three roles.

Every emitted array satisfies the first two corner equalities by the first-letter bucket choices and the remaining two by the corner-pair lookup. The explicit distinctness checks ensure that its four sides use different words. Conversely, any valid square selects a `left`, `right`, and `bottom` from exactly those same buckets for its `top`, so the enumeration reaches and emits it.

The nested iteration order is `top`, then `left`, then `right`, then `bottom`, and each candidate list is sorted. That is precisely lexicographic tuple order, so the result needs no separate final sort.

## Complexity detail

Let $W$ be the number of input words and $A$ the number of returned squares. Sorting costs $O(W\log W)$. At most $O(W^3)$ distinct `(top, left, right)` candidates are examined. For each triple, at most three incompatible bottom words are rejected because they duplicate an existing role; every other visited bottom candidate contributes one result. The total time is therefore $O(W^3 + A)$, which subsumes sorting. The indexes use $O(W)$ auxiliary space, and the returned arrays occupy $O(A)$ space, for $O(W + A)$ total.

## Alternatives and edge cases

- **Enumerate all four-word permutations:** Testing every ordered group directly is simple and correct, but it takes $O(W^4)$ time even when almost no corner combinations can succeed.
- **Search the whole array for `bottom`:** Once its first and last letters are known, scanning every word repeats avoidable work; the corner-pair index narrows the search immediately.
- **Reuse a matching word:** A word whose endpoints fit more than one side still cannot occupy two roles in one square; all four selections must be distinct.
- **Unsorted traversal:** Finding the correct collection is insufficient because the contract also fixes lexicographic output order. Sorting the words before enumeration makes that ordering deterministic.
- **No compatible corner bucket:** If a required first-letter or corner-pair bucket is empty, that partial choice produces no square and is skipped naturally.
