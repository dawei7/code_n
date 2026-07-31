## General

**Represent anagrams by one exact signature**

For each word, count the occurrences of all 26 lowercase English letters. Two
words are anagrams exactly when their frequency tuples are equal: reordering
does not change any count, and equal counts provide precisely the same
multiset of letters.

**Keep the first word from each consecutive signature run**

Scan `words` from left to right while storing the signature of the last word
that was retained. Always retain the first word. For every later word, append
the original word only when its signature differs from the stored signature;
when it is appended, replace the stored signature with its own.

If the signatures match, the current word may be deleted because it is an
anagram of the preceding survivor. The stored signature must not change after
that deletion. Consequently, every further word in the same anagram run is
still compared with the run's first survivor.

**Why the scan produces the unique stable result**

Within a consecutive run of equal signatures, any word after the first is an
anagram of the surviving first word and can eventually be removed. The first
word cannot be removed by an operation involving a later word because an
operation always deletes the right-hand member of a pair. At a boundary where
the signature changes, the two adjacent words are not anagrams, so neither run
can remove a word across that boundary. Thus exactly the first word of each
run survives, which is what the scan returns.

## Complexity detail

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Building all signatures examines each input character once, so the running
time is $O(S)$. Each signature has exactly 26 counters, giving $O(1)$ auxiliary
space because the alphabet is fixed. The returned list itself is output space
and may contain every input word.

## Alternatives and edge cases

- **Sort each word:** A sorted string is also a valid signature, but sorting a word of length $k$ costs $O(k \log k)$ instead of $O(k)$ counting time.
- **Compare with every word in the current run:** Anagram equivalence makes those repeated checks unnecessary, and a long run makes this strategy quadratic in the number of words.
- **Repeatedly mutate the list:** Simulating deletions directly is correct, but it changes the input structure and performs avoidable element shifts.
- **Compare with the previous input word:** This also identifies a run, but comparing with the last retained signature mirrors the operation directly and avoids relying on an unstated equivalence argument.
- **One word:** It is always retained because no valid deletion index exists.
- **Identical neighboring words:** Equality is a special case of being anagrams, so only the first survives.
- **Same letters with different multiplicities:** Words such as `"aab"` and `"abb"` are not anagrams and must both remain.
- **Separated matching signatures:** Equal signatures in different runs do not interact when a non-anagram word remains between them.
