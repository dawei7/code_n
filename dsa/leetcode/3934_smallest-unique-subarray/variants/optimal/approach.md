## General

**Group subarrays by where they end.** A suffix automaton compactly represents every distinct contiguous value sequence in `nums`. Each state represents an equivalence class of subarrays that occur ending at exactly the same set of positions. If a state is `v`, the lengths represented by that state form the complete interval

$$
\operatorname{maxlen}(\operatorname{link}(v))+1
\quad\text{through}\quad
\operatorname{maxlen}(v).
$$

Here `maxlen(v)` is the longest sequence represented by `v`, and `link(v)` is its suffix link. Because every sequence represented by one state has the same end-position set, they also have the same occurrence count.

**Build the automaton online.** Extend the automaton with each array value. A new ordinary state represents the newly completed prefix and begins with one terminal occurrence. Transitions are followed backward through suffix links until the new value is connected everywhere it is needed. When an existing transition would violate the required length relation, clone its target: the clone copies its transitions and suffix link, receives the shorter required `maxlen`, and redirects the affected transitions. A clone begins with zero terminal occurrences because it reorganizes existing sequences rather than adding a new array endpoint.

**Recover all occurrence counts.** Sort states by `maxlen` with a counting sort. Process them from longest to shortest and add each state's occurrence count to its suffix-link parent. Every endpoint represented by a state also belongs to every suffix represented by that parent, so this propagation produces the exact number of occurrences for every state.

A state with occurrence count one represents only unique sequences. Its shortest represented sequence has length `maxlen(link(v)) + 1`, so this is the best candidate contributed by that state. Conversely, every unique subarray belongs to some state with occurrence count one, and the state's shortest represented member is no longer than that subarray. Taking the minimum candidate over all unique states therefore returns exactly the minimum unique-subarray length.

## Complexity detail

A suffix automaton for an array of length $n$ has $O(n)$ states and transitions. Each extension performs amortized $O(1)$ transition and suffix-link work when transition maps use expected constant-time hashing. Counting states by `maxlen`, propagating occurrence counts, and scanning the states are all linear. The total expected time is $O(n)$ and the auxiliary space is $O(n)$.

The benchmark defines size as the all-equal array length $n$. The accepted automaton remains linear even though the answer is `n`. A direct dynamic program that computes the common-prefix length for every ordered pair of suffixes performs $\Theta(n^2)$ work on the same tiers.

## Alternatives and edge cases

- **Rolling hash plus binary search:** The source hints count fixed-length hashes and binary-search the first feasible length in $O(n\log n)$ expected time. A single hash can collide; multiple hashes reduce but do not mathematically eliminate that risk.
- **Suffix array plus adjacent LCP values:** A deterministic suffix array can derive each start position's longest match from neighboring suffixes, giving an $O(n\log n)$ construction with radix-sorted doubling and $O(n)$ additional LCP work.
- **Materialize every candidate tuple:** Exact tuple keys make frequency counting simple, but repeatedly building long tuples can require quadratic or worse total element processing.
- **Overlapping occurrences:** Equal subarrays at different starts are duplicates even when their intervals overlap. End-position counts retain all such occurrences.
- **All values equal:** Every proper subarray sequence repeats, so only the complete array is unique and the answer is `n`.
- **A unique singleton:** If any value occurs once, its automaton state has one occurrence and contributes length `1`, the smallest possible answer.
- **Clone states:** Clones must start with zero terminal occurrences. Giving them one would invent an endpoint and corrupt every propagated frequency.
