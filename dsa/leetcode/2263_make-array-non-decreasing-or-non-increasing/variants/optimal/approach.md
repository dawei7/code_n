## General

**Solve one monotonic direction as L1 isotonic regression**

First minimize the cost of making the values non-decreasing. Process them from
left to right while a max-heap stores the fitted levels represented by the
current optimal prefix. When the next value is at least the largest heap value,
adding it creates no order violation.

If the largest represented level is greater than the new value, those two
levels are inverted. Lowering one copy of that largest level to the new value
is the cheapest exchange that repairs the newly introduced violation. Add
their difference to the cost and replace the heap maximum with another copy of
the new value. The new value is also pushed before this repair, so the heap
retains the correct number of prefix representatives.

This is the priority-queue form of the pool-adjacent-violators method for
absolute-error isotonic regression. At each prefix, the heap encodes median
choices for its merged monotonic blocks. A violation merges the affected
blocks, and replacing the excessive maximum performs exactly the necessary
L1 adjustment; unaffected smaller levels remain feasible and optimal.

**Reuse the same routine for non-increasing order**

Negating every value reverses comparisons without changing absolute
differences:
$\lvert -x-(-y)\rvert=\lvert x-y\rvert$. A non-increasing original target
becomes a non-decreasing target after negation. Run the same heap routine on
`nums` and on the negated values, then return the smaller cost.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each of two passes performs at most one heap
push and one replacement per value, costing $O(n\log n)$ total time. A heap
can hold $n$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Dynamic programming over target values:** Prefix minima over all legal values are exact, but cost $O(nV)$ time for value range $V$.
- **Change each inversion locally:** Pairwise fixes can conflict with later positions and do not guarantee a global minimum.
- **Sort the array:** Reordering elements is not an allowed operation; only values may change.
- **Already monotonic:** One direction has zero cost.
- **Equal neighbors:** They satisfy both non-decreasing and non-increasing relations.
- **Single element:** It is monotonic in both directions and costs zero.
- **Both directions tie:** Returning either common minimum is sufficient.
- **Large gaps:** Each unit of the absolute difference counts as one operation.
- **Negation:** It changes only the comparison direction, not the adjustment cost.
