## General

The encoding uses two token shapes:

- one digit from `1` through `9` represents `a` through `i`;
- two digits from `10` through `26` followed by `#` represent `j` through `z`.

Because every two-digit token announces itself with a `#` exactly two positions after its first digit, the string can be decoded in one left-to-right pass. The Optimal solution uses index `i` to point to the first character of the next undecoded token.

**Recognizing a three-character token**

The condition

`i + 2 < n and s[i + 2] == "#"`

first checks that a position two characters ahead exists. Python's `and` short-circuits, so `s[i + 2]` is never accessed when it would be outside the string.

If that position contains `#`, the next token is `s[i : i + 2]` followed by the marker. The slice includes characters `i` and `i + 1` but excludes `i + 2`, so it extracts the two decimal digits without `#`.

The contract guarantees a valid, uniquely decodable string. Therefore, a marker two places ahead means those digits form a value from 10 through 26. After decoding it, `i += 3` skips both digits and the marker.

For `"10#11#12"`, the first condition sees the marker at index two, decodes `"10"`, and advances to index three. It then sees the marker after `"11"`, decodes it, and advances to the final single digits `"1"` and `"2"`.

**Recognizing a single-digit token**

If no marker lies two positions ahead, the current token is just `s[i]`. Under the valid-input promise, it is a digit from `1` through `9`. The code converts that one character and advances `i` by one.

This lookahead rule resolves apparent ambiguity. When the current character is `1` or `2`, it might begin a two-digit number, but only the presence of `#` after the next digit confirms that interpretation. Otherwise, the current digit stands alone.

A literal `#` is never reached as the start of a token because the three-character branch consumes it together with its two preceding digits.

**Converting a number into a lowercase letter**

For either token shape, `int(...)` produces a number $v$ from 1 through 26. Lowercase English letters occupy consecutive Unicode code points. `ord("a")` is the numeric code for `a`, so

`v + ord("a") - 1`

is the code point for the $v$th lowercase letter.

When $v=1$, the expression is exactly `ord("a")`. When $v=10$, it is nine positions after `a`, which is `j`. When $v=26$, it reaches `z`.

`chr(...)` converts that code point back to a one-character string, which is appended to `ans`.

The subtraction of one is essential because alphabet positions are one-based while code-point offsets from `a` are zero-based. Omitting it would shift every result one letter forward.

**Why characters are collected in a list**

Python strings are immutable. Repeatedly concatenating a growing answer can copy the existing prefix many times. The solution instead appends one decoded character at a time to `ans` and performs `"".join(ans)` once at the end.

The list preserves token order. Each loop iteration consumes exactly the next token and appends exactly its corresponding letter, so joining produces the decoded text in the original sequence.

**Following the second example**

For `s = "1326#"`:

- at index zero, position two contains `"2"` rather than `#`, so `"1"` becomes `a`;
- at index one, position three contains `"6"` rather than `#`, so `"3"` becomes `c`;
- at index two, position four is `#`, so `"26"` becomes `z` and the index advances past the end.

The result is `"acz"`.

**Why the scan is correct**

At the beginning of each iteration, `i` points to the first character of the next token. Valid encoding grammar gives exactly two possibilities.

If a `#` appears at `i + 2`, the token has the required two digits plus marker form, and the three-character branch decodes it correctly. Otherwise, the next token is a one-digit code, and the single-character branch decodes it correctly. The chosen increment moves `i` to the next token boundary.

By induction, every encoded token is consumed once, no character is skipped or reused, and each appended letter matches its numeric position. When `i == n`, the entire valid encoding has been decoded, so joining `ans` gives the required string.

## Complexity detail

Let $n$ be the encoded string length. Every loop iteration advances `i` by either one or three, so there are at most $n$ iterations. Each slice has length two, integer conversion covers at most two digits, and character conversion is constant-time under this fixed alphabet. Running time is $O(n)$.

The list `ans` contains one character per decoded token. There can be $O(n)$ tokens, and the joined output itself has the same length, so total storage is $O(n)$, matching the manifest.

Excluding required output, `ans` is still an intermediate $O(n)$ list in the exact Python implementation. The short temporary slices use $O(1)$ bounded space.

## Alternatives and edge cases

- **Right-to-left parsing:** A `#` encountered from the end can signal that the two preceding digits form one token. This works but requires reversing the collected letters or prepending inefficiently.
- **Dictionary lookup:** Prebuild mappings for `"1"` through `"9"` and `"10#"` through `"26#"`. It is correct but unnecessary when arithmetic conversion is direct.
- **Repeated string concatenation:** Simpler-looking code may become less efficient because strings are immutable; list append plus one join is the standard linear construction.
- **Single-character input:** A valid one-digit code takes the single-token branch and returns one letter.
- **Token `"10#"`:** The marker confirms the two-digit token and maps it to `j`, rather than decoding `1` and then encountering an invalid zero.
- **Token `"26#"`:** It maps to the final lowercase letter `z`.
- **Adjacent three-character tokens:** Advancing by three places lands exactly at the next token's first digit.
- **A one-digit token followed by a two-digit token:** Lookahead at the first digit sees no marker two positions ahead for that token; after advancing one, the next iteration detects the later marker correctly.
- **Bounds safety:** `i + 2 < n` must be evaluated before indexing `s[i + 2]`. Short-circuit evaluation prevents an out-of-range access near the end.
- **Valid-input guarantee:** The code does not reject malformed zeroes, misplaced markers, or values above 26. Its simple parsing proof relies on the promised valid unique encoding.
- **Unicode arithmetic:** Lowercase ASCII letters are consecutive Unicode code points, so `ord` and `chr` arithmetic is valid for `a` through `z`.
