## General
**Split the four choices into two independent halves**

For a quadruple to total zero, the sum chosen from the first two arrays must be the negation of the sum chosen from the last two. Enumerating pairs on each side reduces four nested choices to two quadratic stages.

**Store multiplicity, not only membership**

Build a frequency map for every sum $a + b$. Equal values at different indices represent different pairs, so each occurrence increments the map rather than being collapsed into a set. For every $c + d$, add the stored frequency of $-(c + d)$ to the answer.

**Why every tuple is counted exactly once**

Each index quadruple has one unique first-half pair and one unique second-half pair. It contributes once when the second pair queries the complementary sum, while the map frequency accounts for every first pair producing that value. Noncomplementary pairs contribute zero, so the accumulated count is exactly the desired set of tuples.

## Complexity detail
Each half contains $n^{2}$ index pairs. Building the frequency table and querying all second-half pairs therefore take $O(n^2)$ expected time with a hash table. At most $n^{2}$ distinct sums are stored, giving $O(n^2)$ space.

## Alternatives and edge cases
- **Store both pair-sum lists and sort:** complementary values can be counted with two pointers in $O(n^2 \log n)$ time and $O(n^2)$ space.
- **Three loops plus a frequency table for the fourth array:** is correct but costs $O(n^3)$ time.
- **Four direct loops:** checks every quadruple in $O(n^4)$ time.
- **Duplicate values:** multiply the number of index choices; never deduplicate an input array or pair sum.
- **No complement:** a missing hash key contributes zero.
- **All zeros:** every one of the `n⁴` index quadruples is valid, so the result may be much larger than $n^{2}$.
- **Negative values:** complement lookup handles signs without a special case.
