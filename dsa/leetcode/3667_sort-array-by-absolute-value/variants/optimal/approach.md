## General

The value domain contains only the 201 integers from $-100$ through $100$. Build a frequency array indexed by `value + 100`, preserving the multiplicity of every signed input value.

Emit all zeroes first. Then visit magnitudes $1$ through $100$ in ascending order. For each magnitude, append every copy of its negative value and every copy of its positive value. The order between those two same-magnitude buckets is arbitrary under the contract; choosing negative first makes the reference deterministic.

Every emitted occurrence comes from its exact signed-value count, so the output multiset equals the input multiset. Magnitude buckets are visited in increasing order, and both signs inside one bucket have the same absolute value. Consequently every adjacent output magnitude is non-decreasing, proving that the returned permutation is valid.

## Complexity detail

Let $n$ be the number of elements. Counting and emitting the $n$ occurrences takes $O(n)$ time. Traversing all 201 fixed-domain buckets adds $O(1)$ bounded work, so total time is $O(n)$.

The frequency array always has 201 entries, independent of $n$, and uses $O(1)$ auxiliary space under the stated value bounds. The returned array requires $O(n)$ output space.

The legal input length ends at $100$, and comparison sorting is implemented by optimized native code. Complete-domain timing cannot reliably distinguish it from bounded counting once harness and interpreter costs dominate. The package therefore uses a bounded-domain certificate that proves one count update per element, 201 bucket visits, and exactly one emission per output occurrence.

## Alternatives and edge cases

- **Comparison sort with key abs:** This is concise and contract-correct but takes $O(n\log n)$ comparison time in the general model.
- **Stable absolute-value sort:** Stability is allowed but not required; equal magnitudes may be reordered.
- **Zero:** Its magnitude is smallest and it must precede every nonzero value.
- **Opposite signs with equal magnitude:** Either sign may appear first.
- **Duplicate signed values:** Preserve every occurrence through its frequency count.
- **Minimum and maximum values:** Both $-100$ and $100$ belong to the same final magnitude bucket.
- **Single element:** It is already a valid absolute-value ordering.
- **Validation:** Correctness requires both the original multiset and non-decreasing magnitudes; checking only one condition is insufficient.
