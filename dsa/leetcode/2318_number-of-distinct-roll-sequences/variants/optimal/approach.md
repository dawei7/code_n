## General

**Keep exactly the history that constrains the next roll**

After at least two rolls, whether a new face is legal depends only on the final
two faces. It must be coprime with the immediately previous face and different
from both stored faces. Let `counts[previous][last]` be the number of valid
prefixes ending with that ordered pair.

Initialize every length-two pair of distinct, coprime faces with count one.
For each later position, try all six candidate faces for every populated state.
When a candidate satisfies both rules, move the state's count to
`next_counts[last][candidate]`. The special length-one answer is six.

Every valid prefix belongs to exactly one final-pair state. The transition
accepts precisely the faces that preserve adjacency coprimality and prevent a
repeat at distance one or two, so it neither loses a valid extension nor
creates an invalid one. Induction over the sequence length therefore makes the
sum of the final table equal to the required count.

## Complexity detail

There are 36 ordered final-pair states and at most six transitions from each.
Those are fixed constants, so processing `n` positions takes $O(n)$ time. Two
$7\times7$ tables use $O(1)$ auxiliary space. Counts are reduced modulo
$10^9+7$.

## Alternatives and edge cases

- **Exhaustive generation:** Building every valid sequence directly is useful as a small oracle but grows exponentially with `n`.
- **Top-down memoization:** Caching `(remaining, previous, last)` states gives the same $O(n)$ time but uses $O(n)$ memo and recursion space.
- **Matrix exponentiation:** The constant transition matrix can reduce the dependence to $O(\log n)$ at the cost of substantially more machinery.
- **One roll:** Neither restriction compares anything, so all six faces are valid.
- **Equal adjacent ones:** Although $\gcd(1,1)=1$, the distance rule still forbids equal neighboring faces.
- **Distance two:** A candidate must be compared with both stored faces, not only the immediately previous one.
