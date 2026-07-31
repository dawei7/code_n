## General

**No vowel means an immediate loss.** Every substring then contains zero vowels, which is even. Alice requires an odd count, so she has no legal first move.

**Any positive vowel count gives Alice control.** If the whole string contains an odd number of vowels, Alice removes the entire string and wins immediately. If the total is positive and even, she can remove a substring containing exactly one vowel, leaving an odd number of vowels.

From a position with an odd total on Bob's turn, every legal Bob move removes an even number of vowels, so the remaining string still has an odd number. It is also nonempty: removing the whole string would remove an odd total and is illegal for Bob. Alice therefore always receives a nonempty string with an odd vowel count and may remove it completely. Thus Bob can never turn a positive-vowel starting position into a win, and checking for one vowel is both necessary and sufficient.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. In the worst case, the scan inspects all $n$ characters, taking $O(n)$ time. Membership is tested against the fixed five-vowel set, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate substrings:** Testing every possible removal can establish whether Alice has a move, but takes $O(n^2)$ substring exploration instead of using the parity proof.
- **Count the exact number of vowels:** This works, but only whether the count is zero matters for the final winner.
- A consonant-only string makes Alice lose immediately even though Bob would have legal even-vowel substrings if he had a turn.
- A single vowel lets Alice delete the whole string.
- Zero vowels is even, so Bob may remove consonant-only substrings.
- Vowels need not be adjacent; one occurrence anywhere is sufficient.
