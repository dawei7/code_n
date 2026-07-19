## General
**Count each possible height:** Build a frequency array indexed from $1$ through $H$. This records the multiset of student heights without comparison sorting.

**Generate the expected order incrementally:** Iterate height values in increasing order. For each value, consume its recorded frequency and compare that value with the corresponding positions of the original `heights` array. Advance one shared position after every comparison.

**Count mismatching indices:** Increment the answer whenever the current original height differs from the generated expected height. Repeating every value according to its count produces exactly the unique non-decreasing sequence with the same multiset.

The frequency table preserves every input height and its multiplicity. Visiting its indices increasingly therefore generates the same `expected` array that sorting would produce. Since each generated value is compared at its exact position, the counter includes every and only index satisfying `heights[i] != expected[i]`.

## Complexity detail
Counting and comparing process $N$ array entries, while scanning the height domain costs $O(H)$. Total time is $O(N+H)$. The frequency array contains $H+1$ counters, using $O(H)$ space. Here $H=100$ is fixed, so these bounds are also linear time and constant auxiliary space with respect to $N$ alone.

## Alternatives and edge cases
- **Comparison sorting:** Compare `heights` with `sorted(heights)` in $O(N log N)$ time and $O(N)$ space for the copy.
- **Insertion sort:** Explicitly sort a copy and compare it, but descending input takes $O(N^2)$ time.
- **In-place sorting:** It can reduce the extra copy but destroys the current order needed for comparison unless that order is saved elsewhere.
- **Already non-decreasing:** Every position matches and the answer is zero.
- **All equal heights:** Sorting changes nothing.
- **Duplicate heights:** Frequencies preserve multiplicity, so equal students occupy the correct number of consecutive positions.
- **Single student:** The only height is already in its expected position.
- **Boundary heights:** Values `1` and `100` are ordinary frequency indices and need no special handling.
