## General
**Group words by the character they await**

Create an iterator for every candidate word, consume its first character, and place the iterator in that character's bucket. Each bucket therefore contains exactly the word states that can advance when that source character appears.

**Advance only relevant states**

Scan `s` from left to right. Remove the current character's bucket as a snapshot, advance every iterator in it once, and move unfinished iterators to the bucket for their next required character. Increment the answer when an iterator is exhausted. Removing the bucket before processing is important: a word awaiting the same character again must wait for a later source position.

Each iterator always represents the longest prefix of its word matched by the processed prefix of `s`. Advancing it on the next matching source character is the greedy subsequence choice and cannot make completion harder. By induction, exhausted iterators are exactly the candidates that can be matched; separate iterators also preserve duplicate list entries.

## Complexity detail
Let `S` be `len(s)`, `L` the sum of all word lengths, and `W` the number of words. Every source character is scanned once and every word character advances at most once, for $O(S + L)$ time. The buckets hold one iterator per unfinished word, using $O(W)$ auxiliary objects.

## Alternatives and edge cases
- **Indexed source positions:** Store each character's positions in `s` and binary-search the next position for every word character; this takes $O(S + L \log S)$ time.
- **Scan the source per word:** A two-pointer subsequence test for each candidate is simple but can take $O(S \cdot W)$ time.
- **Deduplicate candidates:** Count identical words first and test each distinct value once; this can help repeated inputs but does not remove worst-case rescanning.
- **Duplicate words:** Each occurrence contributes independently when it matches.
- **Repeated required character:** A state moved back to the same bucket must not consume the current source character twice.
- **Candidate longer than `s`:** It cannot finish and contributes zero.
- **No matching first character:** The iterator remains waiting and is never counted.
