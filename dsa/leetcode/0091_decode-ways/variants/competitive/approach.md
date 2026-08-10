## General

The selected competitive solution uses the same prefix dynamic programming recurrence as a full table, but retains only the two counts needed for the next character. A complete decoding can finish with a valid one-digit code or a valid two-digit code. The number of ways reaching the current prefix is the sum of the counts from those legal predecessor prefixes.

It first rejects an empty string or a string beginning with `0`. The stated constraints make the empty case unnecessary, but the guard makes the function defensive. A leading zero is conclusively invalid because no earlier digit exists with which it could form `10` or `20`.

**Meaning of the rolling variables**

Let $D(k)$ denote the number of ways to decode the first $k$ characters. The mathematical base is $D(0)=1$: there is one way to complete the empty prefix.

Before the first loop iteration, `prev = 1` represents $D(0)$. `prev_prev = 0` is a temporary sentinel because there is no prefix of length $-1$ and no two-digit transition can be used at index zero.

After processing character index `i`, the parallel assignment

`prev, prev_prev = cur, prev`

makes `prev` equal to $D(i+1)$ and `prev_prev` equal to $D(i)$. Python evaluates all right-hand expressions before either left-hand assignment, so the old `prev` is preserved correctly. Thus, from the second iteration onward, the two variables are exactly the preceding one-character and two-character prefix counts required by the recurrence.

**Adding the one-digit contribution**

Each iteration begins with `cur = 0`. If `s[i] != '0'`, the current digit maps to a letter by itself. Every decoding counted in `prev` can append that letter, so `cur = prev`.

If the digit is zero, this contribution remains absent. It would be incorrect to carry `prev` forward, because doing so would treat `0` as an independent code. A valid zero must instead arrive through the pair condition.

**Adding the two-digit contribution without integer conversion**

The code checks that `i > 0`, then recognizes a valid pair through character comparisons:

- any pair beginning with `1` is from `10` through `19`; or
- a pair beginning with `2` is valid only when its second character is at most `6`, giving `20` through `26`.

These are exactly the two-digit codes. The digit-only contract makes lexicographic comparison `s[i] <= '6'` equivalent to numeric comparison for a single character. If the pair is valid, `cur += prev_prev`, because each decoding ending before those two characters can append the pair's letter.

For `0` in `10` or `20`, the single transition contributes nothing but the pair transition contributes the earlier count. For zero after any other leading digit, neither transition contributes and `cur` becomes zero. Later characters may or may not recover from a zero count depending on whether a valid two-character boundary reaches back before the failed one-character prefix.

**Tracing the unusual initialization on `12`**

The initialization can look different from the more common pattern that processes the first character before entering a loop, so it is worth tracing.

1. Before index `0`, `(prev, prev_prev) = (1, 0)`.
2. Character `1` is nonzero, so `cur = 1`; no pair is checked. The update produces `(1, 1)`, representing $(D(1),D(0))$.
3. Character `2` contributes `prev = D(1)=1` as a single code. Pair `12` is valid, so it also contributes `prev_prev = D(0)=1`. The update makes `prev = D(2)=2`.

Returning `prev` therefore returns the count for the entire processed string.

**Why the count is complete and duplicate-free**

Every valid decoding of a prefix has a uniquely determined last code boundary. If its final code has one digit, removing that code yields a decoding counted by the immediately preceding prefix state. If it has two digits, removing it yields one counted by the state two characters back. The corresponding source condition recognizes exactly whether that final digit or pair is legal.

Appending an accepted code to any counted predecessor produces a valid decoding. The one-digit and two-digit families cannot overlap because they consume different numbers of characters at the end. Therefore adding their sizes counts all valid decodings exactly once. Rolling the state discards only older counts that no future recurrence can inspect; it does not discard any needed path information.

## Complexity detail

The loop processes each of the $n$ digits once. Each iteration uses a fixed number of character comparisons, integer additions, and assignments. It creates no variable-length slices and performs no nested traversal, so time is $O(n)$.

Only `prev`, `prev_prev`, `cur`, the index, and a few references are retained regardless of string length. The auxiliary space is $O(1)$, matching the manifest. The input string is read without modification, and the output is a single integer.

The answer may grow in a Fibonacci-like pattern for strings with many valid groupings, but the Reference guarantees that it fits a 32-bit integer. Python's arbitrary-precision arithmetic also prevents overflow in this implementation.

## Alternatives and edge cases

- **Full prefix table:** Store every $D(k)$ in an array. It is often easier to inspect and debug, and can reconstruct intermediate counts, but uses $O(n)$ rather than $O(1)$ auxiliary space.
- **Memoized suffix recursion:** At index `i`, recurse after one digit and optionally after two digits, caching each index. It is linear time but uses a memo plus a recursion stack.
- **Character tests versus parsing:** The selected condition avoids forming a two-character substring and converting it to an integer. Parsing `s[i - 1:i + 1]` and checking `10 <= value <= 26` is equally valid under the contract.
- **Leading zero:** The early return correctly handles `0`, `06`, and any longer string beginning with zero.
- **Internal zero:** Only `10` and `20` can include a zero. `30`, `00`, and `01` are invalid pairs, even though integer conversion might make `01` look like `1` if the leading-zero rule were forgotten.
- **Success after a locally zero state:** In `110`, the count for the full prefix receives a valid contribution from pair `10`; handling contributions separately is safer than declaring the entire string invalid whenever the current digit is zero.
- **Boundary values:** Both `10` and `26` are included. Pair `27` is excluded because a leading `2` accepts only a following digit at most `6`.
- **Single digit:** A nonzero single character passes the guard, runs once, and returns one. A single `0` returns zero immediately.
- **Empty string:** Although the Reference requires length at least one, the explicit guard returns zero for an empty call instead of indexing it.
