## General
**Keep punctuation anchored with two pointers**

Convert the string to a mutable character list. Place one pointer at each end. If the left pointer is on a non-letter, advance it because that character must stay where it is. Likewise, move the right pointer leftward whenever it is on a non-letter.

When both pointers identify English letters, swap those characters and move both pointers inward. Each swap places the next letter from the original right end into the next available letter position on the left, and symmetrically places the left letter at the matching position from the right.

Non-letters are never assigned or swapped, so their indices remain unchanged. The letter positions are visited from the outside inward, pairing the first with the last, the second with the second-last, and so on; therefore the resulting letter subsequence is exactly the reverse of the original one.

## Complexity detail
Let $n$ be the length of `s`. Each pointer moves in only one direction and crosses each index at most once, so the runtime is $O(n)$. The mutable character list and returned string require $O(n)$ space.

## Alternatives and edge cases
- **Letter stack:** Collecting all letters and popping them while rebuilding the string is also $O(n)$ time and space, but stores the letter subsequence separately.
- **Rescan for every letter position:** Searching from the end again for each replacement letter is correct but takes $O(n^2)$ time.
- **All non-letters:** No swaps occur, and the original string is returned unchanged.
- **One or zero letters:** Reversing the letter subsequence has no visible effect.
- **Mixed case:** Uppercase and lowercase characters are letters and reverse by position without changing case.
- **Fixed symbols:** Digits, hyphens, equals signs, punctuation, and other non-letters stay at their exact original indices.
