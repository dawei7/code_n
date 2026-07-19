## General
**Describe the whole address, not merely its suffix**

The verified MySQL query uses one anchored, case-sensitive regular expression. `^` fixes the match at the beginning, `[A-Za-z]` requires the first prefix character to be a letter, and `[A-Za-z0-9_.-]*` permits exactly the remaining prefix alphabet. The literal suffix `@leetcode[.]com` then consumes the rest of the address, and `$` prevents trailing characters.

Case sensitivity is material. Without it, a database collation may treat `@LEETCODE.COM` as equal to the required lowercase domain even though the contract rejects that address. The native predicate therefore requests case-sensitive matching explicitly.

**Express the same contract in SQLite**

The app-local engine uses SQLite, whose built-in `GLOB` matching is case-sensitive. The first condition requires a leading letter and the exact lowercase terminal suffix. Because a glob `*` can otherwise consume arbitrary characters, a second condition isolates the prefix with `substr(mail, 1, length(mail) - 13)` and rejects it if it contains any character outside `[A-Za-z0-9_.-]`.

Together, the two conditions are equivalent to the accepted regular expression: the first proves a nonempty letter-led prefix and exact domain placement; the second proves every prefix character belongs to the permitted alphabet. Selecting the original columns preserves the qualifying rows without transformation.

## Complexity detail
Each predicate inspects a mail value in time proportional to its length, using $O(S)$ filtering time across the table. The native query may return rows in any order. The app-local query adds deterministic ordering, which gives the conservative total bound $O(S + n\log n)$; an engine that can scan the integer primary key in order may avoid an explicit sort.

Filtering itself needs only constant-sized pattern and substring state. The deterministic sort may retain up to $n$ qualifying rows, so the conservative auxiliary-space bound is $O(n)$, excluding the returned table.

## Alternatives and edge cases
- **Suffix-only `LIKE`:** `mail LIKE '%@leetcode.com'` accepts prefixes beginning with digits or punctuation and permits forbidden characters, so it is insufficient alone.
- **Case-insensitive regular expression:** relying on a default collation may incorrectly accept uppercase or mixed-case domains; force case-sensitive matching.
- **Character-by-character conditions:** a recursive CTE can validate every prefix position but is more complicated and may add avoidable overhead.
- **Minimal prefix:** `a@leetcode.com` is valid because one initial letter is enough and the remaining-prefix repetition may be empty.
- **Allowed punctuation:** underscore, period, and dash are permitted only after the first prefix letter.
- **Forbidden punctuation:** characters such as `#`, `+`, spaces, and a second `@` invalidate the prefix.
- **Lookalike suffix:** missing dots, extra trailing text, subdomains, and different domains must fail even if they contain the word `leetcode`.
- **Domain case:** `@LEETCODE.COM` and other case variants are invalid.
