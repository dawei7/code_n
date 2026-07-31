## General

**Reduce pairing to frequency parity**

Pairs never mix different values. For any fixed value, its occurrences can be partitioned into equal pairs exactly when its frequency is even: pair the occurrences two at a time. An odd final occurrence would have no equal partner.

Count the frequency of every distinct value, then check that every count is divisible by two. If all counts are even, pairing within each value group uses every occurrence exactly once. If any count is odd, no rearrangement can provide a partner for its leftover occurrence, so a complete division is impossible. This condition is therefore both necessary and sufficient.

## Complexity detail

Let $m$ be the length of `nums` and $v$ the number of distinct values. Building the frequency map and checking its values take $O(m)$ time in total under expected constant-time hash-table operations.

The frequency map stores $v$ entries, so it uses $O(v)$ auxiliary space. Here $v \le \min(m,500)$ because the input values lie in a bounded range.

## Alternatives and edge cases

- **Parity toggle set:** Add a value on its first unmatched occurrence and remove it on the next; an empty set at the end gives the same $O(m)$ expected-time result.
- **Fixed frequency array:** The bound `nums[i] <= 500` permits an array of 501 counters, using constant space relative to the input length.
- **Sorting adjacent values:** Sorting and checking consecutive pairs is correct but costs $O(m\log m)$ time.
- **Repeated full-array counting:** Counting a value again at every position is correct but takes $O(m^2)$ time.
- **One pair:** A two-element input succeeds exactly when its values are equal.
- **Several pairs of one value:** Any positive even frequency can be split into repeated equal pairs.
