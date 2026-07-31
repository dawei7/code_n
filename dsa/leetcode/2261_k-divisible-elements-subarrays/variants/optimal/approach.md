## General

**Represent sequences as trie paths**

Use a trie whose edges are integer values. Starting from its root, a path
`a, b, c` represents exactly the sequence `[a, b, c]`. Equal subarrays follow
the same path regardless of their original indices, while a different length
or first differing value leads to a different trie node. Each non-root node
therefore corresponds one-to-one with a distinct nonempty sequence.

**Extend every valid start only as far as allowed**

For each left endpoint, return to the trie root and extend the right endpoint
one value at a time. Maintain how many included values are divisible by `p`.
As soon as that count exceeds `k`, stop this start: every longer extension
retains those divisible elements and is also invalid.

For each still-valid extension, follow the edge labeled by the new value. If
that child does not yet exist, create it and increment the answer. Existing
children represent sequences already produced by an earlier subarray, so they
do not increment the distinct count.

Every eligible subarray is visited by its own endpoints and mapped to its exact
value path. A node is counted only on its first creation, so duplicates are
merged and distinct sequences are counted once. Invalid extensions and all
their supersets are excluded by the monotone divisibility cutoff. The final
node count is therefore precisely the requested answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. There are $O(n^2)$ start-end extensions,
and each performs expected $O(1)$ dictionary work, giving $O(n^2)$ expected
time. At most one trie node is created per distinct subarray, so the trie uses
$O(n^2)$ space.

## Alternatives and edge cases

- **Materialize every subarray tuple:** A set gives exact distinctness, but repeatedly constructing length-$O(n)$ tuples raises worst-case time to $O(n^3)$.
- **Single rolling hash:** It supports $O(n^2)$ enumeration with compact keys but admits collisions unless strengthened or verified.
- **Double rolling hash:** Collision probability becomes negligible, yet a trie remains exact without probabilistic assumptions.
- **All occurrences identical:** Different lengths remain distinct while equal lengths merge.
- **Repeated sequence at different indices:** Count it only once.
- **Exactly `k` divisible values:** The subarray remains eligible.
- **First excess divisible value:** Stop extending that left endpoint immediately.
- **No divisible values:** Every subarray satisfies the limit, though duplicates still merge.
- **`p = 1`:** Every element is divisible, so valid lengths are capped by `k`.
