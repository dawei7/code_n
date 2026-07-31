## General

An operation applied toward equality reduces one absolute pairwise difference
by one. The two separate budgets can therefore be pooled into
`operations = k1 + k2`: either array can supply the same one-unit reduction.
If the budget is at least the sum of all differences, every difference can
become zero.

**Why the largest difference must be reduced first**

Reducing a positive difference $d$ by one lowers its squared contribution by
$d^2-(d-1)^2=2d-1$. This benefit is larger for a larger $d$. Thus, whenever a
smaller difference is reduced while a larger one remains, exchanging that
operation to the larger difference cannot worsen the result.

**Move whole frequency levels**

Count how many differences occur at each occupied height, then sort those
distinct heights downward. Accumulate how many entries have been leveled
together. Moving that entire group from one occupied height to the next costs
the height gap multiplied by the group size.

If the remaining budget cannot reach the next occupied height, divide it by
the group size. Every grouped difference drops by the quotient, and the
remainder lets that many entries drop once more. Lower groups remain
unchanged, so their squared contributions can be added directly.

This realizes the greedy exchange rule one height layer at a time without
performing billions of individual operations. Once the budget ends, every
unperformed reduction has no larger available marginal benefit than those
already chosen, so summing `count * difference * difference` over the final
buckets is minimal.

## Complexity detail

Computing and grouping the $n$ differences takes $O(n)$ expected time.
Sorting at most $n$ occupied levels costs $O(n\log n)$ time and dominates the
linear scans. The differences, frequency map, and level list use $O(n)$ space.

## Alternatives and edge cases

- **Max-heap per operation:** Repeatedly decrementing the largest difference
  is correct but costs $O((k1+k2)\log n)$ and is infeasible for billion-sized
  budgets.
- **Dense frequency array:** Scanning every height from $D$ to zero gives
  $O(n+D)$ time and $O(D)$ space, but it wastes work when occupied levels are
  sparse.
- **Budget exceeds total difference:** Stop at all zeros; using extra
  operations is optional and cannot improve the result.
- **Tied maxima:** Reducing any members of the same frequency bucket has the
  same effect; a partial bucket move is sufficient.
- **Negative modified values:** Only absolute pairwise differences matter, so
  allowing array entries below zero introduces no additional restriction.
