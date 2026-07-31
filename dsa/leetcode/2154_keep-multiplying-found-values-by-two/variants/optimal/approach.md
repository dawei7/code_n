## General

**Separate membership from the doubling process**

The process only asks whether each current value occurs at least once; it never
removes an occurrence. Store every array value in a hash set, then repeatedly
test the current value and double it while the membership test succeeds.

Every performed multiplication is required because its pre-doubling value is
present. The loop stops exactly at the first absent value, which is the
requested final value. Duplicates collapse harmlessly in the set because their
multiplicity cannot change either decision.

## Complexity detail

Let $n$ be the length of `nums`. Building the set takes $O(n)$ expected time
and $O(n)$ space. Positive doubling makes the current value strictly increase,
and the bounded input values limit the number of successful membership checks;
the total expected time is therefore $O(n)$.

## Alternatives and edge cases

- **Sort then search:** Sorting followed by binary searches takes
  $O(n\log n)$ time and may modify the input.
- **Insertion sort then scan:** This remains correct but takes $O(n^2)$ time
  on reverse-ordered arrays.
- **Repeated linear membership:** It avoids extra storage, but rescans the
  array for each value in the bounded doubling chain.
- If `original` is absent, return it without doubling.
- Duplicate occurrences do not cause repeated use of the same value.
- The returned value may exceed `1000`; only inputs carry that bound.
- A missing intermediate double stops the process even if later powers are
  present.
