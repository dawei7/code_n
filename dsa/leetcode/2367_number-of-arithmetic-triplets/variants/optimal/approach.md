## General

**Describe a triplet by its last value.** If `value` is `nums[k]`, the other
two values must be `value - diff` and `value - 2 * diff`. Strict increase and
positive `diff` guarantee that, when present, their unique indices occur
before $k$ in the required order.

Insert all array values into a set. For each possible endpoint, test membership
of both required predecessors and increment the answer when both exist.

Every counted endpoint yields exactly one valid triplet because values are
unique. Conversely, every valid triplet's endpoint passes both membership
tests, so none is missed or counted twice.

## Complexity detail

Building the set and scanning $n$ values takes $O(n)$ expected time. The set
uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Two pointers:** Maintain positions for the two predecessor values while
  scanning endpoints; strict ordering permits $O(n)$ time and $O(1)$ space.
- **Enumerate index pairs:** Testing possible first and middle indices with a
  membership lookup takes $O(n^2)$ time.
- **Enumerate triplets:** Applying the definition directly costs $O(n^3)$.
- **Missing middle:** Two values separated by `2 * diff` are insufficient
  without the intervening value.
- **Overlapping triplets:** Different triplets may share one or two indices.
