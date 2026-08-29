## General

**Use the whole line as the candidate value**

The file contains one phone number candidate per line, and valid output must
preserve each accepted line exactly. `awk` is well suited to this streaming
filter: it reads lines in input order, tests each complete record against a
regular expression, and prints the record when the pattern matches.

The script names `file.txt` directly, matching the contract that input comes
from that relative file rather than from command-line arguments or standard
input.

**Anchor the pattern at both boundaries**

The regular expression begins with `^` and ends with `$`. These anchors mean
the match must cover the entire line from its first character to its last.

Without them, a line such as `abc987-123-4567xyz` would contain a valid-looking
substring and could be accepted even though the whole line is not a valid phone
number. Anchoring converts a substring search into full-format validation.

The Reference guarantees no leading or trailing whitespace. The anchors still
matter: they reject any extra digit, punctuation, or text, and they make the
format contract explicit.

**Express the two allowed prefixes as alternatives**

The parenthesized group contains:

`[0-9]{3}-|\([0-9]{3}\) `

The left alternative matches exactly three digits followed by a hyphen. It is
the beginning of the `xxx-xxx-xxxx` form.

The right alternative matches a literal opening parenthesis, exactly three
digits, a literal closing parenthesis, and exactly one ordinary space. The
parentheses are escaped because unescaped parentheses group regular-expression
syntax rather than matching punctuation. The literal space after `\)` is
essential to the `(xxx) xxx-xxxx` form.

Because the two alternatives are enclosed in one group, the surrounding
anchors and the remaining suffix apply to both of them. Without this grouping,
regular-expression alternation could bind too broadly and allow one branch to
escape an anchor.

**Match the common suffix**

After either prefix, `[0-9]{3}-[0-9]{4}` requires three digits, one hyphen, and
four digits. Combining it with the first prefix produces three digits, a
hyphen, three digits, another hyphen, and four digits. Combining it with the
second produces a parenthesized three-digit area code, one space, three digits,
a hyphen, and four digits.

`[0-9]` is used rather than a loose wildcard, so letters and punctuation cannot
occupy digit positions. `{3}` and `{4}` enforce exact counts rather than
minimum counts.

**Rely on `awk`'s default action**

The script supplies a pattern but no explicit action block. In `awk`, a record
whose pattern is true receives the default action `{ print $0 }`. `$0` is the
entire original input line.

Therefore the script preserves punctuation and character order exactly; it
does not reconstruct or normalize the phone number. Nonmatching records have
no action and produce no output.

**Trace the example**

`987-123-4567` takes the first prefix alternative: `987-` matches, then
`123-4567` matches the common suffix. Both anchors are satisfied, so the line
is printed.

`123 456 7890` fails because the first three digits are followed by a space
rather than the required hyphen, and they are not enclosed in parentheses.

`(123) 456-7890` takes the second prefix alternative. The literal parentheses,
single space, and remaining digit groups all match, so this original line is
printed.

**Why the filter is exact**

If a line is printed, it matched one of the two prefix alternatives and the
common suffix under both full-line anchors. Expanding those two possibilities
gives exactly the two formats allowed by the Reference, so no invalid line can
be printed.

Conversely, any line in either allowed format supplies exactly the characters
required by its corresponding prefix branch and by the shared suffix. With no
extra boundary characters, both anchors succeed and `awk` prints the line.
Thus every valid line is retained.

**Preserve order naturally**

`awk` processes records sequentially and prints a match immediately. There is
no sort, buffer, or associative-array iteration, so accepted lines appear in
the same relative order as they occurred in `file.txt`, as the local Function
Contract requires.

**Portability scope**

The pattern uses extended regular-expression constructs supported by standard
`awk`, including grouping, alternation, and interval counts. Extremely old awk
implementations historically differed on interval-expression support, but
modern POSIX environments handle this form. The script assumes Unix-style text
records; a carriage return left from CRLF input could become an extra character
before `$` in some toolchains and cause rejection unless text-mode handling or
normalization removes it.

## Complexity detail

Let $c$ be the total number of characters and $n$ the number of lines. The
regular expression has fixed size and each line is tested once, so processing
is $O(c)$, conventionally summarized as $O(n)$ when line length is bounded by
the fixed phone formats. No sorting or repeated scan occurs.

`awk` needs only the current record and fixed regex state. Because valid phone
lines have fixed maximum length, auxiliary space is $O(1)$ under the problem
model. Output storage is not counted as working memory.

## Alternatives and edge cases

- **`grep -E`:** The same POSIX extended expression can directly filter matching full lines.
- **`sed -n -E`:** Print only records satisfying the anchored expression; also a valid one-command solution.
- **PCRE `grep -P`:** Allows `\d`, but `-P` is not available in every grep implementation.
- **Missing anchors:** Would wrongly accept a valid phone substring embedded in a longer line.
- **Parentheses:** Must be escaped to match literal characters rather than create only a regex group.
- **Single required space:** `(123)456-7890` and `(123)  456-7890` are invalid.
- **Extra digits:** Exact interval counts and `$` reject them.
- **Blank line:** Matches neither branch and is omitted.
- **Input order:** Streaming default print preserves it automatically.
- **CRLF files:** A retained carriage return may require normalization in a generalized Unix environment.
