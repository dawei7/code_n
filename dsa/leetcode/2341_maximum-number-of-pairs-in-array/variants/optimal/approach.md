## General

All occurrences of one value can be handled independently of every other
value. If a value occurs $f$ times, exactly $\lfloor f/2\rfloor$ pairs can be
removed and $f\bmod 2$ occurrences remain. Choosing different concrete
indices or processing the values in another order cannot change either number.

**Aggregate each frequency once**

The legal values are restricted to 0 through 100, so maintain a fixed array of
101 counters and increment the counter for every input value. Then sum integer
division by two across the counters to obtain the pair count. The leftover
count can be summed from the remainders, or derived as
`len(nums) - 2 * pairs`.

For every value, pairing arbitrary equal occurrences realizes all
$\lfloor f/2\rfloor$ counted pairs. Fewer pairs would leave at least two equal
occurrences available, while more pairs would require more than $f$
occurrences. Summing these independent per-value maxima therefore gives the
global maximum, and the length identity gives exactly the remaining elements.

## Complexity detail

Scanning the $n$ elements and the fixed 101-counter domain takes $O(n)$ time.
The counter array has contract-bounded size independent of $n$, so it uses
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Toggle an unpaired set:** Insert a value when first seen and remove it when
  its mate arrives. This is also expected $O(n)$ time but uses up to $O(n)$
  hash-set space when considered outside the bounded value domain.
- **Sort then group:** Consecutive equal values make pairs easy to count after
  sorting, but sorting costs $O(n\log n)$ time.
- **Repeated list removal:** Searching for and deleting each mate directly is
  correct, but can take $O(n^2)$ time.
- **Odd frequencies:** Every value with an odd count contributes exactly one
  leftover, regardless of how many pairs that value supplies.
- **Single input:** One element yields zero pairs and one leftover.
