## General
**Extract maximal digit runs**

Scan from left to right. Skip letters. When a digit is found, advance a second pointer through every consecutive digit so that the substring is one complete integer token rather than several pieces.

**Normalize without converting to an integer**

Remove leading zeros from the token. If nothing remains, use the canonical representation `"0"`; otherwise use the remaining digit string. This makes numerically equal runs identical even when they contain many more digits than a fixed-width integer can hold.

**Count canonical strings in a set**

Insert each normalized token into a set and return its size. Every represented integer contributes its canonical decimal form, equal integers share one form, and distinct integers have different forms. The set size is therefore exactly the requested count.

## Complexity detail
The scanning pointers advance through each of the $n$ characters once. Normalizing and hashing all digit runs processes at most $n$ digits in total, giving $O(n)$ expected time. The canonical strings stored in the set contain at most $O(n)$ total characters, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Convert every run with `int`:** It is concise in arbitrary-precision languages, but string normalization is portable and avoids constructing large numeric objects.
- **Compare against a list of prior tokens:** It is correct but may compare every new value with every earlier distinct value and take $O(n^2)$ time.
- **No digits:** The set remains empty and the answer is zero.
- **One run spanning the string:** It contributes exactly one integer, regardless of its length.
- **All-zero runs:** Normalize `"0"`, `"00"`, and longer zero runs to the same `"0"`.
- **Letters between digits:** Each letter terminates the current run, even when the neighboring digit characters would otherwise form one number.
- **Repeated normalized value:** Leading-zero variants do not increase the set size.
