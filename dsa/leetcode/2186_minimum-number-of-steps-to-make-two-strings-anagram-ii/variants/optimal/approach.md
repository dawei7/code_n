## General

**Measure each letter's independent imbalance**

Maintain 26 signed counts. Increment the entry for every character in `s` and
decrement it for every character in `t`. A positive difference $d$ means `s`
contains $d$ excess copies of that letter, so those copies must be appended to
`t`. A negative difference means its absolute value must instead be appended
to `s`.

Each append changes the frequency of exactly one letter in exactly one string.
For a letter with difference $d$, at least $\lvert d\rvert$ operations are
therefore necessary, and appending that many copies to the deficient string
is sufficient. Letters cannot compensate for one another in an anagram, so
the minimum total is the sum of all 26 absolute differences.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert t\rvert$. Both strings are scanned once,
giving $O(n+m)$ time. The frequency-difference array always has 26 entries, so
the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort and merge:** Sort both strings, then merge their character sequences
  while counting unmatched entries. This is correct but takes
  $O(n\log n+m\log m)$ time.
- **Separate frequency maps:** Two counters followed by a union of their keys
  give the same result, but the fixed lowercase alphabet makes one signed
  array simpler and constant-sized.
- Strings that are already anagrams require zero steps even when their orders
  differ.
- When the alphabets used by the two strings are disjoint, every existing
  character must be appended to the other string.
- Different input lengths are allowed; their length difference is included
  automatically in the frequency imbalances.
- Appending cannot remove an excess, so copies are always added to the string
  that is deficient in that letter.
