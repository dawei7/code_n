## General
**Identify what every reversal preserves**

Reversing a subarray moves existing elements but does not change the multiset
of values. Therefore equal value frequencies are necessary: if some value
occurs a different number of times in the two arrays, no sequence of operations
can repair the difference.

This condition must compare multiplicities, not just membership. For example,
`[1,1,2]` and `[1,2,2]` contain the same distinct values but cannot become
equal because their counts differ.

**Why multiset equality is also sufficient**

The operation is more powerful than it may first appear. Reversing a subarray
of length two swaps one adjacent pair. Adjacent swaps can realize any
permutation: repeatedly move the value needed at the next target position
leftward through neighboring swaps. When duplicates exist, treat equal copies
as interchangeable. If the frequency of every value agrees, this process can
place a matching copy at every position, so `arr` can reach `target`.

Hence reachability is equivalent exactly to multiset equality; there is no need
to construct an actual reversal sequence.

**Compare frequencies in the fixed value domain**

Allocate a balance array indexed from 1 through 1000. For each value in
`target`, increment its balance; for each value in `arr`, decrement it.
Track how many balance entries are nonzero as updates are applied. After both
scans, that number is zero exactly when every multiplicity matches, avoiding a
separate pass over even the fixed value domain.

The source contract fixes the value universe at 1000 possible integers.
Consequently the balance array has constant size independent of $n$. Scanning
its 1001 slots after processing the inputs is also constant work with respect
to the input length.

The necessity argument shows that a `false` result is unavoidable whenever a
balance remains nonzero. The adjacent-swap construction shows that all-zero
balances guarantee a valid sequence of permitted reversals. The frequency test
therefore returns the correct reachability result in both directions.

## Complexity detail
Both length-$n$ arrays are scanned once, taking $O(n)$ time. The balance
storage has exactly 1001 integer slots plus one nonzero-entry counter, so
auxiliary space is $O(1)$ relative to $n$.

## Alternatives and edge cases
- **Sort both arrays:** Comparing sorted copies is concise and correct, but
  takes $O(n\log n)$ time and $O(n)$ storage for non-mutating copies.
- **General frequency map:** A hash map gives expected $O(n)$ time and is useful
  for an unbounded value domain, but can use $O(n)$ entries; the fixed
  1-through-1000 domain permits a constant-size array.
- **Repeated search and removal:** Finding and deleting one matching value for
  each target position is correct but can take $O(n^2)$ time.
- **Already equal arrays:** Zero reversals are allowed, so return `true`.
- **Single element:** Equal values return `true`; unequal values return
  `false`.
- **Duplicate multiplicities:** Counts must match exactly, even when the sets
  of distinct values agree.
- **Arbitrary permutation:** It need not be obtainable with one reversal;
  multiple length-two reversals can implement any required permutation.
- **Boundary values:** Values 1 and 1000 are ordinary valid balance indices.
- **Input preservation:** Frequency counting does not mutate either array.
