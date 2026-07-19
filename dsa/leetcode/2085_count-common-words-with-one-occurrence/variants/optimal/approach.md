## General
**Why membership alone loses necessary information**

A set can reveal whether a word appears in both arrays, but it erases multiplicity. The condition distinguishes frequency one from frequency two or more, so retain a separate frequency count for each word in each array.

**Counting before comparing**

Scan `words1` into one frequency map and `words2` into another. Then inspect the keys from either one map. A word contributes one precisely when both stored counts equal $1$. Iterating one map is sufficient: a word absent from the other map has count zero there and therefore cannot qualify.

**Why every qualifying value is counted exactly once**

Each distinct word has one key in the inspected frequency map. The test accepts that key if and only if the word occurs once in both original arrays, matching the contract. Because map keys are unique, no qualifying value can contribute more than once, regardless of its positions in the inputs.

## Complexity detail
Building and querying hash maps processes the characters used to hash the input strings, for expected time $O(S)$. The maps can retain every distinct word and its characters, so their space usage is $O(S)$. The final pass over distinct keys is bounded by the number of input words and therefore by $S$, since every word is nonempty.

## Alternatives and edge cases
- **Sort both arrays:** Sorting exposes equal-value runs whose lengths can be compared, but it costs $O(S \log N)$ comparison work in a model with $N$ words and also requires careful two-pointer handling.
- **Repeated array counts:** Calling a linear count operation for every candidate is correct but can rescan both arrays for every word, producing quadratic behavior.
- **Set intersection:** Intersecting sets detects common values but incorrectly includes a word repeated in either input.
- A word repeated in only one array is disqualified even if it occurs exactly once in the other.
- Identical word positions are irrelevant; only the two independent frequencies matter.
- The two arrays may have no values in common, in which case the answer is zero.
