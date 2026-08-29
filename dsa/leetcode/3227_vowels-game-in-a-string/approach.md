## General

**First identify the only immediate losing case.** Alice must remove a nonempty substring containing an odd number of vowels. If the string has no vowel, every substring has zero vowels, which is even. Alice has no legal first move and loses.

The exact source tests whether at least one character belongs to `{"a","e","i","o","u"}`. The surprising part is proving that this condition is also sufficient for Alice to force a win.

**If the total vowel count is odd, Alice wins immediately.** The entire current string is a nonempty substring. When it contains an odd number of vowels, Alice may remove all of it in her first turn. Bob receives the empty string, has no nonempty substring to remove, and loses.

**If the total vowel count is positive and even, Alice can leave an odd total.** Alice may remove a substring containing exactly one vowel—for example, the one-character substring consisting of any vowel. One is odd, so the move is legal. Subtracting an odd count from the positive even total leaves an odd number of vowels in the remaining string.

Now consider Bob's response:

- If Bob has no legal move, he loses immediately.
- If Bob moves, he must remove a substring containing an even number of vowels, possibly zero. Removing an even count from an odd total leaves the remaining vowel count odd.

After Bob's move, the remaining string is nonempty. Bob cannot have removed the whole string, because the whole string had an odd vowel count and his move requires even. Alice can now remove the entire remainder, whose vowel count is still odd. Bob then faces the empty string and loses.

Thus any positive vowel count lets Alice win in at most her second turn.

**Why Bob cannot change parity in his favor.** Alice's moves remove odd vowel counts and toggle total-vowel parity. Bob's moves remove even counts and preserve it. Alice deliberately hands Bob an odd-total position. Whatever legal substring Bob chooses, odd parity survives for Alice's winning whole-string move.

Consonant-only substrings contain zero vowels, and zero is even, so Bob may use them. They still preserve the odd number of vowels and cannot prevent the strategy.

**Reduce the game to existence rather than simulation.** Because the winning classification depends only on whether the original vowel count is zero or positive, the method need not count vowels, inspect possible substrings, or model turns. It returns

`any(c in vowels for c in s)`.

The generator examines characters left to right. `any` stops at the first vowel and returns true. If every character is a consonant, it consumes the full string and returns false.

**Trace `"leetcoder"`.** The string contains vowels, so the method returns true. Its example play removes an odd-vowel substring, Bob removes an even-vowel substring, and Alice removes the odd-vowel remainder. The proof shows Alice need not follow that exact substring choice; existence of a vowel already guarantees a strategy.

For `"bbcd"`, the generator finds no member of the vowel set. Every nonempty substring has zero vowels, so Alice truly has no move.

**The string's character order does not affect the winner.** Order affects which substrings realize particular vowel counts, but one vowel always supplies a legal one-character substring, and the entire string supplies Alice's final odd-total move. Presence alone is sufficient.

## Complexity detail

Let $n$ be string length. Constructing `set("aeiou")` creates five entries, which is $O(1)$ time and space. The generator examines at most $n$ characters, each with expected constant-time set membership, so worst-case time is $O(n)$.

Because `any` short-circuits, best-case time is $O(1)$ when the first character is a vowel. Only a fixed five-element set and generator state are stored, so auxiliary space is $O(1)$. The string is immutable and unchanged.

## Alternatives and edge cases

- **Membership in the literal string `"aeiou"`:** Since there are only five vowels, `any(c in "aeiou" for c in s)` also has $O(n)$ time and constant space.
- **Count every vowel:** Returning whether the count is positive is correct but scans the entire string even after finding the first vowel.
- **Game-state dynamic programming:** Exponential substring states are unnecessary once the parity strategy is recognized.
- **No vowels:** Alice cannot remove an odd-vowel substring and loses immediately.
- **Exactly one vowel:** The whole string has odd count, so Alice removes it and wins.
- **Positive odd total:** Alice can win on her first move by deleting everything.
- **Positive even total:** Alice removes one vowel, preserving an odd total through Bob's even-vowel move.
- **Bob removes zero vowels:** Zero is even and legal, but odd total remains odd.
- **Bob cannot remove the whole odd-total remainder:** Its vowel count violates his even requirement.
- **All vowels:** Presence is immediate; total parity selects whether Alice wins on her first or second turn.
- **Single consonant:** Alice has no move.
- **Single vowel:** Alice removes it.
- **Lowercase guarantee:** The set contains lowercase vowels only; uppercase handling is unnecessary under the contract.
