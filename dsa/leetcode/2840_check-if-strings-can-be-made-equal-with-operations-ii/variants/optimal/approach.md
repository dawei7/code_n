## General

**Separate the two reachable position groups**

An allowed pair satisfies $j-i$ even, which is equivalent to $i$ and $j$ having the same parity. Every operation therefore preserves the multiset of characters at even indices and independently preserves the multiset at odd indices. If either parity multiset differs between `s1` and `s2`, no sequence of swaps can make the strings equal.

The condition is also sufficient. Any permutation of a set of positions can be decomposed into swaps between positions in that set. Since every pair of even indices has even difference, arbitrary rearrangements among even positions are allowed; the same is true among odd positions. Equal character multisets in both groups therefore guarantee that the source can be rearranged into the target.

**Balance both strings in one pass**

Use 52 counters: the first 26 represent letters at even indices, and the second 26 represent letters at odd indices. At index `i`, increment the counter for `s1[i]` and decrement the corresponding counter for `s2[i]`, choosing the half by `i`'s parity.

After processing any prefix, each counter is the source frequency minus the target frequency for one letter and parity within that prefix. At the end, all counters are zero exactly when every parity-specific frequency agrees. By the necessity and sufficiency above, that is exactly when the strings can be made equal.

## Complexity detail

Let $n$ be the common string length. The algorithm visits each aligned character pair once and then checks a fixed array of 52 counters, giving $O(n)$ time. The lowercase alphabet and two parity groups fix the counter array at 52 integers, so auxiliary space is $O(1)$.

The benchmark uses $n$ as `size` and constructs legal pairs that require full parity-frequency verification. The optimal implementation scans the strings once. A correct calibration alternative manually recounts each character with a nested scan of its parity subsequence, taking $O(n^2)$ time. It completes all three tiers with correct answers but fails the scaling verdict.

## Alternatives and edge cases

- **Sort both parity subsequences:** Compare sorted even characters and sorted odd characters. This is concise but takes $O(n\log n)$ time and $O(n)$ auxiliary space.
- **Two hash maps per string:** Count `(parity, character)` keys and compare maps. It remains $O(n)$ expected time, but a fixed array is simpler for the known alphabet.
- **Repeated frequency scans:** Calling `count` for each encountered character is correct but repeats work and can require $O(n^2)$ time.
- **Length one:** No swap exists; equality of the sole character determines the result.
- **Length two:** Each parity group has one position, so the strings must already be identical.
- **Zero operations:** Already equal strings are valid.
- **Duplicate characters:** Multiplicity matters within each parity group, not only whether a letter appears.
- **Odd lengths:** The even group contains one more position than the odd group; the same independent frequency condition still applies.
- **Global anagrams:** Matching overall frequencies is insufficient when the required movement crosses index parity.
