## General

**Validate the entire email with one anchored pattern.** The query selects `user_id` and `email` only when `email REGEXP ...` succeeds:

`^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\.com$`.

The anchors `^` and `$` require the match to cover the complete email string. Without them, a malformed address could contain a valid-looking substring and still pass.

**Read the local part before the at sign.** `[A-Za-z0-9_]+` accepts one or more uppercase letters, lowercase letters, digits, or underscores. The `+` prevents an empty local part. Because `@` is not in this class, the following literal `@` is the first and only at sign the pattern can contain.

An address such as `"bob_at@example.com"` can satisfy this local-part rule, while `"bob-at@example.com"` cannot because hyphen is absent from the allowed class. The sample's `"bob_at_example.com"` fails for a different reason: it has no literal at sign at all.

**Read the domain and suffix.** After `@`, `[A-Za-z]` requires the first domain character to be a letter. `[A-Za-z0-9]*` then permits zero or more additional letters or digits. The domain is therefore non-empty and cannot begin with a digit.

The pattern `\\.com` represents a literal dot followed by `com`. The backslash prevents regex dot from meaning “any character.” The end anchor requires `.com` to be the final suffix, so `.net` or trailing characters fail.

Together, the character classes exclude a second at sign, whitespace, underscores in the domain, and punctuation other than the required dot before `com`.

**Project and sort qualifying rows.** `WHERE` filters rows without duplicating them. `ORDER BY 1` orders by the first selected expression, `user_id`, in ascending order because no descending direction is specified.

For `alice@example.com`, the local letters, literal at sign, letter-starting domain, and final suffix all match. `charlie@example.net` fails the suffix. `eve@invalid` has no final `.com`.

**There is a source/reference discrepancy about domain digits.** The local reference description says the part after `@` and before `.com` contains only letters. The exact protected SQL permits digits after the first domain letter because it uses `[A-Za-z0-9]*`. For example, `user@a1.com` matches this query even though a literal “letters only” reading would reject it.

The query does enforce that the domain starts with a letter, which matches the sample explanation's emphasis, but its later positions are alphanumeric. This approach documents the SQL that actually runs rather than silently claiming a stricter predicate. If the reference contract is authoritative as written, the implementation would need `[A-Za-z]+` for the whole domain; that change is not made here because the task is to explain the protected source.

**Why the regex's structural guarantees hold.** A successful anchored match consumes the local class, exactly one literal `@`, the domain class, and the literal final suffix. None of the surrounding classes can consume `@` or a dot, so there is no alternate parse hiding extra separators. Conversely, every address satisfying those exact source-level character rules can be divided into those pieces and matches.

MySQL string escaping determines how backslashes reach the regex engine. In the shown SQL, the doubled backslash in the string literal is intended to deliver an escaped dot to the regular expression under standard MySQL behavior.

**Character classes are deliberately ASCII-specific.** `A-Z` and `a-z` enumerate English letters, and `0-9` enumerates decimal ASCII digits. This is narrower and more predictable than a locale-dependent “word character” shortcut. It also explains why underscore has to be listed explicitly in the local part. Case is accepted in both local and domain text, while the suffix itself is written as lowercase `com`; whether regex comparison is case-sensitive can depend on MySQL collation, so the exact database environment governs whether uppercase suffix variants match.

The unique `user_id` key is unrelated to validation but guarantees each selected table row identifies one user. The regex is evaluated independently per row, and no grouping or deduplication step is needed.

## Complexity detail

Let $S$ be the total number of characters across scanned email strings and $r$ the number of matching rows. A fixed anchored regular expression can be tested in $O(S)$ total scanning time. Ordering qualifying rows may require $O(r\log r)$ time and $O(r)$ sort space. The overall direct-plan bound is $O(S+r\log r)$ time and $O(r)$ auxiliary space.

An index on `user_id` or a particular query plan may reduce sorting work, while regex filtering generally requires examining email text. Exact SQL costs remain optimizer-dependent, but these bounds match the manifest's scan-and-sort model.

## Alternatives and edge cases

- **Unanchored regex:** It could accept a valid fragment inside an otherwise invalid email. Both `^` and `$` are essential.
- **Unescaped dot:** Regex `.` matches any character, so `exampleXcom` could pass. The suffix dot must be literal.
- **Empty local part:** The `+` quantifier rejects `@domain.com`.
- **Empty domain:** The mandatory first letter rejects `user@.com`.
- **Multiple at signs:** Character classes on both sides exclude `@`, so exactly one literal separator is possible.
- **Local underscore:** It is explicitly allowed before `@`.
- **Domain underscore:** It is not in either domain class and is rejected.
- **Domain beginning with a digit:** The first-domain-letter class rejects it even though later digits are accepted.
- **Digits later in domain:** The exact query accepts them; this differs from the reference's “only letters” wording and should not be hidden.
- **Ordering syntax:** `ORDER BY user_id ASC` would be clearer than positional `ORDER BY 1` but is equivalent here.
