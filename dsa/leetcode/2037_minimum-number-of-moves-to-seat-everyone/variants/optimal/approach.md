## General

**The movement cost is absolute distance**

Moving a student from position `b` to seat position `a` requires one operation per unit of distance. The exact cost of that assignment is therefore `abs(a - b)`.

The task is to choose a one-to-one matching between all students and all seats that minimizes the sum of these distances. Seats at the same numerical position are still separate available seats, and students at the same position are still separate people.

**Sort both sides and match by rank**

The source sorts `seats` and `students` in ascending order. It then pairs the smallest student position with the smallest seat position, the second smallest with the second smallest, and so forth.

The final generator

`abs(a - b) for a, b in zip(seats, students)`

computes the movement cost of every rank-matched pair, and `sum` returns their total.

**Why crossed assignments can be uncrossed**

Consider two student positions `p <= q` and two seat positions `a <= b`. A crossed matching sends `p` to `b` and `q` to `a`. The ordered matching sends `p` to `a` and `q` to `b`.

On a line, the ordered cost satisfies

$$
\lvert p-a\rvert+\lvert q-b\rvert
\le
\lvert p-b\rvert+\lvert q-a\rvert.
$$

Intuitively, crossed travel contains overlapping distance traveled in opposite directions. Swapping the two destinations removes that crossing without increasing total movement.

This inequality holds regardless of the relative placement of the four coordinates. If both seats lie to one side, the totals may tie; if their intervals interleave, uncrossing strictly removes duplicated travel.

**Turn uncrossing into a global proof**

Take any optimal matching. If it contains two students in sorted order whose assigned seats are in reverse order, apply the uncrossing swap. The total cost does not increase, and the number of inversions in the seat assignment decreases.

Repeating this process eventually yields an optimal matching with no inversions. In an inversion-free one-to-one matching, the first sorted student must use the first sorted seat, the second student the second seat, and so on. That is exactly the matching produced by the source.

Therefore rank matching is not merely a plausible nearest-seat heuristic; it is guaranteed to attain a global minimum.

**Why independently choosing the nearest available seat can fail**

A local nearest-seat decision can take a seat that is much more valuable to a later student. For example, a middle student may have two nearby options while a far-right student badly needs the rightmost seat.

Sorting resolves all assignments together. It preserves left-to-right order and prevents one student's locally convenient choice from forcing another student to cross back across it.

**Trace the first example**

`seats = [3,1,5]` sorts to `[1,3,5]`. `students = [2,7,4]` sorts to `[2,4,7]`.

The paired costs are `abs(1-2)=1`, `abs(3-4)=1`, and `abs(5-7)=2`. Their sum is four.

The identities of the original student indices are irrelevant; every student has the same unit movement cost. The sorted positions fully determine an optimal assignment.

**Duplicate positions are handled naturally**

Suppose two seats both lie at position two. Sorting retains two entries with value two. They can be paired with two different students, fulfilling the “no two students in the same seat” condition because the list entries represent separate physical seats despite sharing a coordinate.

Likewise, two students may begin at the same position. They occupy separate positions in the sorted list and are matched to separate seat entries.

**Why `zip` covers every participant**

The contract guarantees equal lengths. After sorting, `zip(seats, students)` therefore produces exactly `n` pairs and truncates neither side. Every student is assigned once and every seat is used once.

The sum is zero for an already aligned pair and positive for movement in either direction. Absolute value makes leftward and rightward motion cost the same, matching the operation definition.

**Mutation of the inputs**

The source uses in-place `list.sort()` on both arrays. The returned number is correct, but callers observing these lists afterward will see ascending order rather than the original ordering.

This mutation is not a problem for the LeetCode method contract, but it is part of the exact implementation behavior and differs from an approach using `sorted(...)` copies.

## Complexity detail

Let $N$ be the common number of seats and students. Sorting each list takes $O(N\log N)$ time. Pairing and summing takes $O(N)$, so total time is $O(N\log N)$.

Python's in-place sort can use $O(N)$ temporary memory in the worst case, consistent with the manifest's $O(N)$ space bound. The generator consumed by `sum` is lazy and uses only constant additional iteration state beyond sorting.

## Alternatives and edge cases

- **Counting by coordinate:** Positions are bounded by one hundred, so frequency differences can compute the cost in $O(N+U)$ time with $U=100$.
- **Minimum-cost bipartite matching:** General but far more expensive; one-dimensional absolute distance has the uncrossing property.
- **Nearest free seat per student:** Can be suboptimal because early choices may force later crossings.
- **Already matched sorted positions:** Every absolute difference is zero.
- **Duplicate seats:** Equal coordinates still represent distinct seat entries and remain separately paired.
- **Duplicate students:** Each occurrence is assigned to one distinct seat.
- **One student and one seat:** The answer is their absolute distance.
- **Students entirely left of seats:** Ordered matching remains optimal and sums all rightward distances.
- **Students entirely right of seats:** The same proof handles all leftward moves.
- **Tied optimal assignments:** The method returns the minimum cost without needing to reconstruct a unique assignment.
- **Equal input lengths:** This guarantee makes `zip` cover all entries.
- **Input mutation:** Both arrays are sorted in place.
