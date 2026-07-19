## General
**Turn movements into matching distances**

Moving a student from position $a$ to a seat at position $b$ costs
$\lvert a-b\rvert$, regardless of the route taken. The task is therefore a
minimum-cost one-to-one matching between the two position multisets.

**Uncross any pair of assignments**

Suppose two students satisfy $a \le b$ and two seats satisfy $x \le y$. A
crossing assignment sends $a$ to $y$ and $b$ to $x$. On a number line,

$$
\lvert a-x\rvert+\lvert b-y\rvert
\le
\lvert a-y\rvert+\lvert b-x\rvert.
$$

Thus swapping a crossing pair to match left with left and right with right
never increases the cost. Repeating this exchange removes every crossing from
an optimal assignment.

**Pair the two sorted sequences**

Sort both arrays and match equal ranks. This assignment has no crossings, and
the exchange argument shows that some optimum must have exactly this order.
Summing `abs(seat - student)` over the paired sorted positions therefore gives
the minimum. Duplicate positions cause no issue because their separate
occurrences remain separate list entries.

## Complexity detail
Sorting both length-$N$ arrays takes $O(N\log N)$ time, and the paired distance
sum takes $O(N)$ time. The app-local implementation creates sorted copies,
which use $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Counting sort by position:** Because positions lie from $1$ through $100$,
  frequency arrays can match students and seats in $O(N+100)$ time and
  $O(100)$ space.
- **Repeated nearest-seat choice:** Assigning each student independently to its
  nearest remaining seat can make a locally attractive choice that forces a
  later student much farther away; it lacks the sorted exchange guarantee.
- Students and seats already sharing the same sorted positions contribute zero
  moves even if the input orders differ.
- Duplicate seats at one coordinate are distinct and may receive different
  students.
- Duplicate students may be sent to different seat positions.
- Each unit of absolute distance is one move, so movements add independently
  across the final matching.
