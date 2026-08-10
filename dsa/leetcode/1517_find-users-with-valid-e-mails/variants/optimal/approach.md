## General

**Breaking the validity rule into a full-string pattern**

The query uses a regular expression to enforce the prefix grammar and domain shape:

`^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$`

Each part has a distinct job.

The caret anchors matching at the beginning of the mail string. `[a-zA-Z]` requires the first character to be an uppercase or lowercase English letter. This prevents a prefix beginning with a digit, underscore, period, or dash.

`[a-zA-Z0-9_.-]*` permits zero or more remaining prefix characters. The character class allows letters, digits, underscore, literal period, and dash. Zero repetitions are allowed, so a one-letter prefix is valid.

`@leetcode\\.com` represents the required domain. The period must be escaped for the regular-expression engine because an unescaped dot means any single character. The dollar sign anchors the match at the end, preventing extra text after `.com`.

Together, the two anchors ensure the entire mail value follows the grammar rather than merely containing a valid-looking fragment.

**Why the BINARY LIKE condition is also present**

MySQL regular-expression matching can be case-insensitive depending on the string collation. The contract requires the domain to be exactly lowercase.

`BINARY mail LIKE '%@leetcode.com'` converts the left operand to a binary string for a case-sensitive comparison. The percent wildcard permits any prefix, while the fixed suffix requires the exact lowercase domain at the end.

The regular expression already controls which prefix characters are legal and where the domain begins. The binary `LIKE` adds a separate case-sensitive suffix guard. A value ending in `@LeetCode.com` may pass a case-insensitive regex, but it fails the binary suffix test.

In a `LIKE` pattern, the period is an ordinary literal rather than the regex any-character operator, so it does not need backslash escaping there.

**Why both predicates together are sound**

If a row passes the regex, its prefix begins with a letter, every later prefix character belongs to the allowed set, and the remaining shape is the LeetCode domain. If it also passes binary `LIKE`, the actual ending characters have the exact required lowercase spelling.

Conversely, any mail satisfying the stated grammar matches every regex component and ends with the exact lowercase domain, so it passes both predicates.

The query returns `SELECT *`, which produces `user_id`, `name`, and `mail` from `Users`. No `ORDER BY` is required because output order is unrestricted.

**Examples of rejected forms**

`.shapo@leetcode.com` fails the first-character class. `quarz#2020@leetcode.com` fails because the hash character is absent from the permitted prefix class. `david69@gmail.com` fails the domain. A string without an at sign cannot match the anchored domain segment.

`sally.come@leetcode.com` is valid because periods are permitted after the first prefix letter.

Digits, underscores, and dashes are likewise permitted only after that first letter. The expression does not impose a minimum total prefix length beyond one, and it does not treat consecutive allowed punctuation marks as invalid because the reference grammar does not prohibit them.

**SQL escaping layers**

The source text contains `\\.` within the SQL string literal. One escaping layer is processed by MySQL's string parser, and the regular-expression engine must ultimately receive an escaped period. Exact behavior can depend on SQL modes such as `NO_BACKSLASH_ESCAPES`, so production SQL sometimes uses doubled escaping or a character class like `[.]` for clarity.

The stored query is written for the expected MySQL environment.

## Complexity detail

Let $N$ be the number of users and $S$ the total number of characters across their mail strings. With no usable index for this anchored regex-plus-suffix predicate, the engine typically scans each row and examines its mail value, giving roughly $O(S)$ matching work.

The query performs no explicit sorting, so the manifest's $O(S + N\log N)$ bound is conservative rather than a direct reflection of the source. Output construction uses space proportional to the number of qualifying rows, while regex evaluation itself needs bounded or pattern-dependent engine state.

Actual database complexity depends on collation, regex implementation, expression evaluation, row storage, and query planning. `SELECT *` may increase transferred data compared with selecting only named required columns, though all three columns are requested by the sample result.

## Alternatives and edge cases

- **Case-sensitive regex collation:** Apply a binary or case-sensitive collation to the entire regex and omit the extra `LIKE`. Syntax varies by MySQL version.
- **REGEXP_LIKE with match flags:** Newer MySQL versions can request case-sensitive matching explicitly, making intent clearer.
- **String functions without regex:** Prefix and suffix tests plus illegal-character detection are possible but more verbose and easier to get wrong.
- **One-letter prefix:** It is valid because the remainder class uses zero-or-more repetition.
- **Uppercase prefix:** It is permitted by `a-zA-Z`.
- **Uppercase domain letter:** The binary suffix predicate rejects it.
- **Period first:** The required initial letter rejects it.
- **Hash in prefix:** The allowed character class rejects it.
- **Extra suffix text:** The regex end anchor and suffix comparison reject it.
- **Null mail:** SQL predicates evaluate to unknown, so the row is not returned.
- **Unrestricted order:** No sorting clause is necessary.
