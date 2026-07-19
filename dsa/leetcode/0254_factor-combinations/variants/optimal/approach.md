## General
**Canonical order removes permutation duplicates**

Backtrack with a remaining product and a minimum allowed factor. Try divisors only through the square root of the remainder. For every divisor `f`, emit the completed pair `f, remainder / f`, then recurse so that the quotient may be split further.

The current path is nondecreasing, every chosen value divides the previous remainder, and `product(path) * remainder = n`. Passing `f` as the next minimum preserves canonical order.

**The smallest remaining factor is always discoverable**

In any nontrivial factorization of `remainder`, its smallest factor cannot exceed `sqrt(remainder)`. The divisor loop therefore reaches the first factor of every valid continuation. Emitting its paired quotient covers the two-factor completion; recursing covers decompositions of that quotient. Since factors may only be appended in nondecreasing order, every factor multiset follows one canonical path and cannot reappear as a permutation.

## Complexity detail
Divisor exploration is output-sensitive, with a top-level $O(\sqrt{n})$ scan and work proportional to generated combinations. Recursion depth is at most $O(\log n)$ because every selected factor is at least two, excluding returned output storage.

## Alternatives and edge cases
- **Generate ordered factor sequences:** repeats permutations and requires expensive deduplication.
- Prime numbers and values below four have no valid combination; repeated factors remain valid.
