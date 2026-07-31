## General

Validate the complete address with one anchored regular expression:

`^[A-Za-z0-9_]+@[A-Za-z]+[.]com$`

The start and end anchors require the pattern to consume the entire value. `[A-Za-z0-9_]+` makes the local part non-empty and restricts it to letters, digits, and underscores. The single literal `@` between the two parts, combined with those restricted character classes, guarantees that no second `@` can occur.

`[A-Za-z]+` makes the domain non-empty and letter-only. `[.]com` then requires the exact dot-plus-suffix structure; expressing the dot as a one-character class avoids SQL string-literal backslash differences while still treating it literally. Filter `Users` with this predicate, project the two required columns, and sort numerically by `user_id`.

The remotely submitted MySQL artifact uses that regular expression directly. The app-local SQLite adapter preserves the same validation contract with `INSTR` and `SUBSTR`, plus negated `GLOB` character classes, because SQLite does not provide MySQL's `REGEXP` operator by default. Keeping the sources separate preserves source-native execution while making the offline judge runnable.

## Complexity detail

Let $r$ be the number of rows and let $S$ be the total number of characters across their email values. Evaluating an anchored, non-backtracking structural pattern is linear in the inspected text, $O(S)$. Ordering at most $r$ qualifying rows contributes $O(r\log r)$ time and $O(r)$ working space in a conservative engine-independent model. Thus the manifest records $O(S+r\log r)$ time and $O(r)$ auxiliary space; a database may use the primary-key order to reduce the explicit sort cost.

## Alternatives and edge cases

- **Several `LIKE` predicates:** They can check the suffix and presence of `@`, but do not naturally enforce exact multiplicity or per-part character classes.
- **Unanchored regular expression:** It can accept an invalid address merely because a valid-looking substring occurs inside it.
- **Wildcard dot:** A plain regex `.` matches any character; `[.]` is required for the literal separator before `com`.
- **Empty local or domain part:** Both `+` quantifiers require at least one permitted character.
- **Underscore placement:** Underscores are permitted only before `@`, never in the domain.
- **Digits in the domain:** The local part permits them, but the domain character class deliberately does not.
- **Multiple `@` symbols:** Neither surrounding character class accepts `@`, so exactly one can match.
- **Output order:** The explicit ascending `ORDER BY user_id` is required even though `user_id` is unique.
