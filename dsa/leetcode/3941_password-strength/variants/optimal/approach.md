## General

**Separate identity from category.** A character's weight depends on its category, but its number of contributions depends only on whether that exact character appears. Build `set(password)` and iterate those distinct characters, so every identity is scored exactly once.

For each character, test the four disjoint source categories in order:

- `"a" <= character <= "z"` adds one;
- `"A" <= character <= "Z"` adds two;
- `"0" <= character <= "9"` adds three;
- the remaining legal symbols are exactly `!`, `@`, `#`, and `$`, so the final branch adds five.

The set removes repeated contributions but keeps case-sensitive identities, meaning `a` and `A` remain separate. Every distinct character reaches exactly one category branch, so it contributes its prescribed weight exactly once. Repeated occurrences collapse into the set and absent characters are never visited. Summing these contributions therefore produces precisely the defined password strength.

## Complexity detail

Let $n=\lvert\texttt{password}\rvert$. The scan performs expected $O(1)$ set work per character, while category scoring occurs at most 66 times: once for each possible lowercase letter, uppercase letter, digit, and special character. The total expected time is $O(n)$.

The distinct-character set contains at most 66 entries regardless of $n$. Because the complete source alphabet is fixed, this is $O(1)$ auxiliary space rather than $O(n)$.

For scaling evidence, the three benchmark tiers use strings of one repeated lowercase letter with lengths $32$, $128$, and $512$. The accepted-class method remains linear in $n$. A correct method that compares every position with every earlier position without stopping after finding a duplicate performs

$$
\sum_{i=0}^{n-1}i=\frac{n(n-1)}{2}
$$

comparisons, exposing $O(n^2)$ growth while still completing inside the legal source domain.

## Alternatives and edge cases

- **Fixed seen table:** A 128-entry Boolean table indexed by the ASCII code also gives $O(n)$ time and $O(1)$ auxiliary space; it is independently benchmarked but encodes the character representation more directly.
- **One-pass seen set:** Scan the original string, insert each first occurrence into a set, and score it immediately. This has the same bounds but needs an explicit duplicate check in the loop.
- **Repeated prefix scans:** Checking every prior position to decide whether each character is new is correct, but takes $O(n^2)$ time when the scan is not stopped after a match.
- **Count category occurrences instead of identities:** Adding points for every position overcounts repeated characters; deduplication must happen per exact character.
- **Case sensitivity:** Lowercase and uppercase versions are different symbols with different weights and may both contribute.
- **Repeated single character:** Any number of copies contributes exactly one category weight.
- **All legal characters:** The maximum strength is $26\cdot1+26\cdot2+10\cdot3+4\cdot5=128$.
