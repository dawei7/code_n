## General

**The whole suffix sets the largest possible next value.** Let $x$ be the MEX of the current unremoved suffix. No prefix of that suffix contains $x$, so no prefix can have MEX greater than $x$. A prefix has MEX exactly $x$ precisely when it contains every value from $0$ through $x-1$. The lexicographically optimal next entry must therefore be $x$.

**Keep the longest suffix after fixing that value.** Scan only through the first occurrence needed to complete the set $\{0,1,\ldots,x-1\}$. This is the shortest prefix whose MEX is $x$. Any longer choice would produce the same current result entry while discarding additional elements that could still contribute later entries. Retaining them cannot restrict a future partition, so the shortest qualifying prefix gives the lexicographically greatest continuation.

When $x=0$, the required lower-value set is empty, but an operation must still remove at least one element. Since the suffix contains no zero, every one-element prefix has MEX $0$. Removing exactly one element preserves the maximum number of later zero entries and is optimal.

**Maintain the changing suffix.** Count the remaining occurrences of every value from $0$ through $n$; values above $n$ cannot affect the MEX of at most $n$ elements. After consuming a positive-MEX segment, start at zero and find the first value whose remaining count is zero. Removing elements can only create new missing values, so the suffix MEX never increases.

Each chosen segment realizes the greatest possible next entry, and the shortest such segment retains the greatest possible continuation. Applying the same choice to every remaining suffix therefore constructs the lexicographically maximum complete result.

## Complexity detail

Every array element is consumed exactly once. A positive-MEX segment with value $x$ contains at least the $x$ distinct values $0$ through $x-1$. Recomputing the next MEX scans at most $x$ present counters, so that scan can be charged to the just-consumed segment. Across all segments, both the input scan and all MEX scans total $O(n)$ work. Expected-time set membership for the values seen in one segment keeps the complete running time at $O(n)$.

The remaining-frequency array, the result, and the per-segment seen set use $O(n)$ auxiliary space in the worst case.

The benchmark tiers contain 32, 128, and 512 copies of value one. Every suffix has MEX zero, so the required method removes one element in constant work per result entry. A correct alternative that rebuilds the value set of every remaining suffix takes $O(n^2)$ time and should fail only the scaling verdict.

## Alternatives and edge cases

- **Recompute every suffix MEX:** Building a new frequency set from the entire remainder before every cut is correct but quadratic when the MEX stays zero and each segment has length one.
- **Try all prefix endpoints:** Evaluating the MEX of every candidate prefix repeats work and is unnecessary because the complete suffix gives an upper bound and the shortest prefix attaining it is optimal.
- **Next-occurrence queues:** Storing positions for each value can locate the shortest qualifying endpoint, but suffix counts and a single forward scan provide the same linear bound with simpler state.
- **MEX zero:** No remaining element equals zero; emit one zero per remaining element by taking single-element prefixes.
- **Repeated required value:** Only its first appearance inside the current segment satisfies that value's requirement; duplicates are consumed but do not reduce the unseen count again.
- **Large array value:** Any value greater than $n$ is irrelevant to MEX computation, though it is still consumed as part of its selected segment.
- **Complete consecutive set:** If the suffix contains every value from $0$ through $x-1$, its next entry is $x$ even when those required values appear in an arbitrary order with duplicates between them.
- **Equal prefix of result arrays:** Shorter qualifying cuts retain more elements and can add later entries, which wins when the compared result prefixes otherwise remain equal.
