## General

**Recognize three alternatives in one file**

The competitive file contains three complete filtering commands: one using
`grep`, one using `sed`, and one using `awk`. They are demonstrations of
alternative one-line solutions, not three phases of a single algorithm.

If the entire file is executed as a shell script, all three commands run in
sequence and each reads `file.txt` independently. Every valid phone line is
therefore printed three times. That violates the required output even though
each command is individually correct for the intended input. A usable
submission must retain exactly one filtering command.

**Decode the shared format structure**

All three expressions anchor at `^` and `$`, requiring the whole input record
to match. Their grouped first part chooses between three digits plus a hyphen
and a literal parenthesized group of three digits followed by one space. The
shared remainder requires three digits, a hyphen, and four digits.

Expanding the alternatives yields exactly `xxx-xxx-xxxx` and
`(xxx) xxx-xxxx`. The pattern neither accepts a bare space between all digit
groups nor permits extra characters at either end.

**First alternative: PCRE `grep`**

`grep -P` asks GNU grep for Perl-compatible regular-expression syntax. In that
dialect, `\d{3}` describes three digit characters. Literal parentheses are
escaped, and the ordinary space after the closing parenthesis is part of the
required format.

`grep` prints matching lines by default and processes them in file order. The
command is concise, but `-P` is not specified by POSIX and is unavailable in
some grep implementations, notably many minimal or non-GNU environments.
Using `[0-9]` with `grep -E` is more portable for this ASCII-digit contract.

Depending on PCRE configuration, `\d` can have broader Unicode digit semantics
than `[0-9]`. The LeetCode file uses the intended ordinary digits, so that
difference does not affect the sample but matters in generalized validation.

**Second alternative: extended-regex `sed`**

`sed -n -E` suppresses normal automatic output with `-n` and enables extended
regular expressions with `-E`. Its address `/pattern/` selects matching lines,
and command `p` prints them.

This expression uses `[0-9]` for explicit ASCII digits. Parentheses that belong
to the phone text are escaped, while outer grouping parentheses remain regex
syntax. If `-n` were omitted, matching lines would print twice—once from the
explicit `p` and once from sed's default behavior—so the option is essential.

**Third alternative: `awk` pattern filtering**

The `awk` command uses the same POSIX extended expression as `sed`. It supplies
no action, so a matching pattern triggers `awk`'s default `{ print $0 }`
behavior. This prints the original line without reformatting it.

Among the three stored choices, this is also the exact command used by the
optimal variant. It avoids the nonportable PCRE flag and needs no explicit
print action.

**Trace the sample through any one command**

`987-123-4567` matches the unparenthesized branch and is printed.
`123 456 7890` matches neither branch because its separators are spaces rather
than the required hyphens and parentheses. `(123) 456-7890` matches the
parenthesized branch and is printed.

When exactly one command is selected, the output contains the first and third
lines once, in their original order. When the stored file runs unchanged, that
two-line result is repeated by each of the three commands.

**Why each individual pattern is sound and complete**

The anchors prevent substring acceptance. The first grouped branch fixes the
only permitted difference between formats, and the shared suffix fixes every
remaining character position. A match therefore has one of the two exact
allowed shapes.

Conversely, a valid phone number chooses its corresponding branch, satisfies
all exact digit counts and punctuation, and has no boundary characters to
violate the anchors. Each individual command prints it. All three tools stream
records in input order, so no separate ordering work is necessary.

**Use the input assumptions rather than trimming**

The Reference guarantees no leading or trailing whitespace. The expressions do
not trim; such spaces would be extra anchored characters and cause rejection.
Internal spacing is also exact: the parenthesized form contains one space after
`)`, while the hyphenated form contains none.

This strictness is appropriate for validation. Silently removing whitespace
would alter the original line and could accept data outside the stated format.

**Shebang and execution context**

The file begins with `#!/usr/bin/env bash`, which chooses Bash when the file is
executed directly on a Unix-like system. The commands themselves do not require
advanced Bash syntax, but they depend on the available `grep`, `sed`, and `awk`
implementations and on `file.txt` being in the current working directory.

The shebang does not make three alternatives mutually exclusive. Shell executes
every command unless the file is edited to retain one or explicit control flow
is added.

## Complexity detail

Let $c$ be the total number of characters and $n$ the number of records. Each
individual command scans the file once with a fixed-size regular expression,
so it takes $O(c)$ time, commonly stated as $O(n)$ for fixed-length candidates,
and $O(1)$ auxiliary space while streaming.

The unchanged competitive file performs three scans, taking $O(3c)=O(c)$
asymptotic time but tripling I/O and output. Its asymptotic class remains the
manifest's $O(n)$, yet its result is semantically wrong because of duplication.

## Alternatives and edge cases

- **Keep one command:** This is the required repair; three correct filters in sequence do not form one correct answer.
- **Portable `grep -E`:** Use `[0-9]` and extended grouping instead of nonportable `grep -P` and `\d`.
- **`sed -n -E`:** Correct individually; `-n` prevents default-plus-explicit duplicate printing.
- **`awk`:** Correct individually and uses default record printing.
- **Embedded valid substring:** Anchors reject it.
- **Leading or trailing spaces:** Rejected rather than trimmed, consistent with strict format matching.
- **Wrong internal spacing:** Parenthesized form requires exactly one space.
- **Additional digits or punctuation:** Exact counts and anchors reject them.
- **Empty file:** Each selected filter prints nothing.
- **CRLF portability:** A visible carriage return may interfere with the end anchor on some Unix toolchains.
