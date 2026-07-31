## General

Every valid schedule is a full binary tree. An internal node represents a split and contributes `splitTime` to every leaf below it; a leaf represents the single strain eliminated by that cell. Activity in the left and right subtrees is parallel, so if those subtrees need times $a$ and $b$ after they receive their shared cell, their parent needs

$$
\max(a,b)+\texttt{splitTime}.
$$

This also gives a bottom-up view of the schedule. Start with one completion requirement for every strain. Joining two requirements as sibling subtrees replaces them by their maximum plus the split cost. The question becomes which two requirements to join at each step.

The two smallest requirements can be placed as deepest siblings in some optimal tree. Take any deepest sibling pair: swapping shorter work into those deepest positions cannot increase the schedule's maximum root-to-leaf time. Contracting that sibling pair produces the same problem on one fewer requirement, with the contracted subtree represented by its slower child's requirement plus `splitTime`. Repeating this exchange argument proves that combining the two current minima is safe at every step.

Maintain all current subtree requirements in a min-heap. Remove the two smallest values $a \le b$ and insert $b+\texttt{splitTime}$; the smaller value disappears because the siblings run concurrently and $b$ determines when their parent subtree completes. When one value remains, it is the minimum time required by the whole schedule.

## Complexity detail

Let $n=\lvert\texttt{timeReq}\rvert$. Heap construction takes $O(n)$ time. There are $n-1$ merges, each using a constant number of $O(\log n)$ heap operations, so total time is $O(n\log n)$.

The copied heap contains at most $n$ integers, giving $O(n)$ auxiliary space. The benchmark increases $n$ while retaining varied completion requirements. It distinguishes heap maintenance from a correct implementation that sorts the entire shrinking collection before every merge, which takes $O(n^2\log n)$ time in the direct form.

## Alternatives and edge cases

- **Sort once and use fixed adjacent pairs:** A newly formed subtree requirement may belong between unprocessed values, so static adjacent pairing does not preserve the greedy order.
- **Repeated full sorting:** Sorting the active requirements before every merge implements the same correct choice but repeats far more work than a heap.
- **Binary search on the answer:** A deadline can be checked by greedily accounting for the splits available before each strain must start, but this introduces a logarithmic search over the answer range and is less direct than constructing the optimal merge tree.
- **Explicit split-tree enumeration:** Trying every binary grouping and assignment is exponential; the deepest-sibling exchange removes the need to enumerate trees.
- **Input order:** Strains may be eliminated in any order, so only their durations matter; heap construction deliberately discards the input ordering.
- **Equal durations:** Duplicate heap entries are separate strains and are merged normally.
- **Two strains:** Exactly one merge is required, producing `max(timeReq) + splitTime`.
- **Dominant strain:** A very long strain is kept near the root while shorter work absorbs additional split levels.
- **Large values:** Repeated split costs can push the result beyond 32-bit signed range, so fixed-width implementations need 64-bit arithmetic.
