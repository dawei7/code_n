## General

**Reduce adjacent pairs one level at a time**

For a current array of length $m>1$, allocate its $m/2$-element successor.
At successor index $i$, read exactly the pair at old indices `2 * i` and
`2 * i + 1`. Store the smaller value when $i$ is even and the larger value
when $i$ is odd.

After every pair has contributed once, make the successor the current array
and repeat. Since the length is a power of two, halving eventually reaches
exactly one element without an unmatched pair.

Each constructed level follows the definition at every index, so it is
identical to the corresponding game round. Replacing the current level only
after all pairs are evaluated also preserves the required simultaneous
semantics. Induction over the levels shows that the final stored value is
exactly the game's last remaining number.

## Complexity detail

The successive level lengths are $n/2,n/4,\ldots,1$, whose sum is less than
$n$. The total running time is therefore $O(n)$. Materializing successive
arrays uses at most $O(n)$ auxiliary space, including all temporary output
references over one round.

## Alternatives and edge cases

- **In-place prefix reduction:** Writing each new level into the front of a copied array also takes $O(n)$ time and can reduce auxiliary allocations.
- **Recursive tournament tree:** Recursion expresses the same levels but adds call structure without improving the linear work.
- **Repeated prefix rescans:** Locating every pair by scanning from the beginning each time is correct but can take $O(n^2)$ time.
- **Single element:** No round is performed, and that element is returned directly.
- **Two elements:** The only new index is zero, so the result is their minimum.
- **Parity resets:** Minimum versus maximum depends on the new array's index, not an index retained from the previous level.
- **Equal pair:** Both operations produce the same value.
- **Power-of-two length:** The guarantee ensures every round consists entirely of complete adjacent pairs.
