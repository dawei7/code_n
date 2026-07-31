## General

Process the strings from left to right while storing previously unmatched words in a hash set. For the current word, compute its two-character reversal. If that reversal is already unmatched, the two strings form a pair; otherwise store the current word for a possible later partner.

Because all input strings are distinct, a non-palindromic word has at most one reverse partner in the entire array. Once the later member is encountered and counted, neither string can participate in another pair. A palindromic word is not already in the set before its own processing, so it is stored but never paired without a distinct duplicate, which the contract forbids.

Every counted match is therefore a legal disjoint pair. Conversely, whenever both members of a reversible pair exist, the earlier one is stored until the later one arrives, so that unique possible pair is always counted. Summing these independent matches produces the maximum.

## Complexity detail

Let $n$ be the number of words. Each two-character string is reversed, looked up, and possibly inserted once, so expected time is $O(n)$ under standard hash-table behavior. The unmatched-word set may contain $O(n)$ strings, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Compare every index pair:** Directly testing all $i<j$ combinations is correct but takes $O(n^2)$ time.
- **Boolean table:** A fixed $26\times26$ table can replace hashing and gives $O(n)$ time with $O(1)$ alphabet-bounded space.
- **Prebuild a set and divide by two:** Counting non-palindromic words whose reverse exists and halving works, but palindromic words must be excluded explicitly.
- A single word can never form a pair.
- A palindromic word has no partner because all strings are distinct.
- The two members may appear in either input order; streaming detects the pair when the later one arrives.
- Unrelated unmatched words do not interfere with one another.
- Each reversal class contains at most two distinct strings, so matching one class cannot reduce the optimum in another.
