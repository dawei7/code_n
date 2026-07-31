## General

The contract supplies exactly five cards and explicitly orders the four
possible result labels. Test the categories from strongest to weakest so that
the first match is automatically the best hand.

**Separate suit and rank evidence**

A flush depends only on suits: compare every suit with the first. If they all
match, return `"Flush"` immediately, even if some ranks also repeat.

Otherwise count each rank in a fixed 14-entry array. Let $f$ be the largest
rank frequency. If $f\ge3$, return `"Three of a Kind"`; if $f=2$, return
`"Pair"`; and if $f=1$, return `"High Card"`.

These cases are exhaustive because five cards always provide a high card.
After a flush has been excluded, the maximum rank multiplicity exactly
distinguishes the remaining three labels. Testing in the required strength
order also handles four equal ranks, a triple accompanied by a pair, and a
flush containing repeated ranks without inventing categories outside the
problem's four-label hierarchy.

## Complexity detail

Both input arrays always contain exactly five entries, ranks use the fixed
domain 1 through 13, and suits use four fixed characters. The bounded work and
storage are therefore $O(1)$ time and $O(1)$ auxiliary space. This is verified
through the package's `bounded_domain` certificate rather than runtime scaling.

## Alternatives and edge cases

- **Sets and a frequency map:** `set(suits)` plus a hash counter for ranks is
  equally clear and remains constant under the fixed contract, but fixed arrays
  make the finite domains explicit.
- **Sort the five ranks:** Adjacent duplicates expose the maximum
  multiplicity, but sorting is unnecessary even though five elements keep its
  actual work bounded.
- **Four equal ranks:** The available label is still `"Three of a Kind"`,
  because no separate four-of-a-kind result exists in this problem.
- **Category priority:** A flush must be returned before inspecting rank
  frequency.
- **Case-sensitive labels:** Return the exact spaces and capitalization shown
  in the contract.
