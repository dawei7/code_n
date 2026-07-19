## General
**Separate the dominant project**

Let $L$ be the largest milestone count, let $R$ be the sum of all other
counts, and let $T=L+R$ be the total. Milestones from the non-dominant projects
can occupy $R$ separator positions between milestones from the largest
project.

If $L\le R+1$, the other milestones provide enough separators to place every
largest-project milestone without adjacency. The remaining projects can be
interleaved among those positions, so all $T$ milestones are schedulable.

**Count the unavoidable dominant case**

If $L>R+1$, at most one largest-project milestone can appear before, between,
and after the $R$ other milestones. Thus at most $R+1$ dominant milestones
can be used, giving

$$
(R+1)+R=2R+1
$$

working weeks. Alternating a largest-project milestone with each other
milestone, starting and ending with the largest project, constructs a schedule
of exactly that length. The upper bound is therefore attainable.

Computing the total and largest count is sufficient; the identities and
internal order of all smaller projects do not affect this separator argument.

## Complexity detail
One pass computes the sum and maximum of the $N$ counts. The final comparison
and formula are constant-time operations, so total time is $O(N)$. Apart from
the input, only `total`, `largest`, and `rest` are stored, giving $O(1)$
auxiliary space.

## Alternatives and edge cases
- **Priority-queue simulation:** Repeatedly choose the two projects with the
  most milestones. It can construct a valid schedule but costs time
  proportional to the number of worked milestones, which may be enormous.
- **Sort project counts:** Sorting can identify the largest project but costs
  $O(N\log N)$ when a linear maximum scan is sufficient.
- With one project, only one week can be worked.
- Equality $L=R+1$ still permits every milestone by starting and ending with
  the largest project.
- Several projects tied for the largest count cannot create a dominant
  imbalance; all milestones are schedulable.
- Counts and their sum may exceed 32-bit integer range, so implementations in
  fixed-width languages need a 64-bit result.
- The answer is never zero because every project has at least one milestone.
