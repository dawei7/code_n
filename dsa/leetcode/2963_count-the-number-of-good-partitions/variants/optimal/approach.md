## General

All occurrences of one value must remain in the same partition piece; a cut
between its first and last occurrence would place that value in two pieces.
Consequently, each value defines an interval that cannot be cut internally,
and overlapping intervals must merge into one indivisible component.

Record every value's last index. During a left-to-right scan, `rightmost` is the
furthest last occurrence required by any value seen in the current component.
When the scan index reaches `rightmost`, no value in this component appears
later, so the boundary after it is safe and one component ends. If a later last
occurrence is encountered first, the component extends to cover it.

Suppose the scan finds $C$ components. Every internal component boundary may
independently be cut or left joined: cuts never split a value interval, and any
good partition can cut only at these boundaries. There are $C-1$ such choices,
so the answer is $2^{C-1}$ modulo $10^9+7$.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Building the last-occurrence map and
scanning the array take $O(N)$ expected time under standard hash-map behavior.
The map stores at most $N$ values, using $O(N)$ space.

## Alternatives and edge cases

- **Test every cut with prefix and suffix sets:** Rebuilding both value sets at every boundary identifies the same safe cuts but takes $O(N^2)$ time.
- **Explicit interval sorting:** Constructing and sorting first-to-last intervals is correct in $O(N\log N)$ time, but array order already permits linear merging.
- **All values distinct:** Every adjacent boundary is safe, producing $2^{N-1}$ good partitions.
- **One spanning value:** If some occurrence interval covers the whole array, all overlapping intervals merge and only the uncut partition remains.
- **Crossing intervals:** Intervals such as the occurrences in `[1,2,1,2]` merge into one component even though neither contains the other.
- **Single element:** There is one component and therefore one good partition.
- **Modulo:** Apply modulo $10^9+7$ to the power because the number of choices grows exponentially.
