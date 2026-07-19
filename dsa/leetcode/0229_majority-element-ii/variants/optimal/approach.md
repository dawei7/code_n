## General
**More than one third allows at most two answers**

At most two distinct values can each occur more than $n/3$ times; three such frequencies would total more than $n$. Therefore generalized Boyer-Moore voting needs only two candidate slots.

**Cancel triples of different values**

For each value, increment its matching candidate count, claim an empty slot, or decrement both counts when it matches neither candidate. That final action cancels one occurrence of three different values, which cannot remove all occurrences of a true more-than-$n/3$ majority.

After any prefix, the two slots represent the only values that can remain above the one-third threshold after repeatedly deleting triples of distinct values from that prefix. The counters track the unmatched residue, not the candidates' actual frequencies.

**Cancellation finds candidates; counting certifies them**

Cancellation produces possibilities, not guaranteed answers. Count each distinct candidate in a second pass and retain it only when its actual frequency is strictly greater than $\lfloor n/3 \rfloor$.

Any qualifying value appears too frequently to be completely removed by distinct-value triple cancellations, so it must finish in a candidate slot. The verification pass removes every non-qualifying candidate. Hence the returned set is exactly the required set.

## Complexity detail
Two linear passes give $O(n)$ time. Candidate values, counters, and the at-most-two-element result use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Frequency hash table:** is linear but uses $O(n)$ auxiliary space.
- **Sorting:** can count runs but costs $O(n \log n)$ time or mutates the input.
- A one- or two-element array can return every distinct value; duplicate candidate slots must not produce duplicate output.
