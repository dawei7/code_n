## General
**Deduplicate each array before counting**

Convert one input array at a time to a set. For each value in that set,
increment a map recording the number of distinct arrays in which the value has
appeared. This prevents duplicates such as two copies of `2` in `nums1` from
being mistaken for presence in two arrays.

**Select values with at least two appearances**

After all three sets have contributed, return every map key whose count is two
or three. Each key occurs only once in the map, so the output is automatically
distinct.

A value receives one increment for each and only each input array containing
it. Its final count is therefore exactly its number of source arrays, making
the threshold test equivalent to the problem condition. Iterating map keys
once also ensures no qualifying value is duplicated in the result.

## Complexity detail
Building the three sets and processing their members reads $S$ input elements,
so the expected time is $O(S)$. The per-array sets, appearance map, and result
store at most $O(S)$ distinct values in the general bound, using $O(S)$ space.
The stated value domain is even smaller, but the bound remains source-size
based.

## Alternatives and edge cases
- **Bit masks per value:** Associate one bit with each input array and OR that
  bit into a value's mask. A mask with at least two set bits qualifies and
  gives the same $O(S)$ bounds.
- **Repeated membership scans:** For every encountered value, search all three
  arrays directly. This remains correct but can take $O(S^2)$ time.
- Duplicates inside one array count as only one array appearance.
- A value present in all three arrays must still appear only once in output.
- If the three arrays are pairwise disjoint, the result is empty.
- Output order is unconstrained and must not affect correctness.
