## General
**Match the prefix only at token boundaries**

Because condition codes are separated by spaces, `DIAB1` can begin a token in exactly two ways: at character zero, or immediately after a space. The accepted MySQL predicate represents those alternatives with `conditions LIKE 'DIAB1%'` and `conditions LIKE '% DIAB1%'`.

The trailing `%` is intentional. The contract identifies a family of codes by prefix, so strings such as `DIAB100` and `DIAB1A` qualify. Conversely, the leading boundary is essential: `XDIAB100` contains the same characters but is a different code, and neither predicate accepts it.

**Keep the app result deterministic**

The same two `LIKE` predicates are valid in SQLite, so the app-local query preserves the remotely Accepted filter without translating it into a different tokenization scheme. It adds `ORDER BY patient_id` only because local expected tables need stable row order; LeetCode itself permits any order.

Every returned row is therefore sufficient because one predicate proves that a `DIAB1` prefix occurs at a valid token start. Every qualifying row is necessary because its matching token must start either at the beginning of `conditions` or after a separator, covering the two predicates exhaustively.

## Complexity detail
Scanning the condition text costs $O(S)$ across all rows. The native query may emit qualifying rows in arbitrary order. The app-local deterministic ordering contributes a conservative $O(n\log n)$ term, for $O(S + n\log n)$ total time.

The filter uses constant-sized patterns. A general-purpose database sort can retain up to $n$ qualifying rows, so auxiliary space is conservatively $O(n)$, excluding the returned table.

## Alternatives and edge cases
- **Regular expression with a boundary:** `(^| )DIAB1` states the same condition directly, but the two `LIKE` branches are simpler and portable between the native and app-local engines.
- **Substring-only search:** `conditions LIKE '%DIAB1%'` incorrectly accepts `XDIAB100` because it ignores the start of the condition token.
- **Split every code:** normalizing the string into rows can work, but it adds recursive or engine-specific machinery for a two-boundary test.
- **Code at the beginning:** `DIAB100 MYOP` must match without a leading space.
- **Code after another condition:** `ACNE DIAB100` must match through the second branch.
- **Permitted suffix:** any token starting with `DIAB1`, including `DIAB1`, `DIAB100`, and `DIAB1A`, qualifies.
- **Lookalike token:** `XDIAB100` and `ACNE XDIAB100` do not qualify even though they contain the target characters.
- **Empty condition list:** an empty `conditions` value matches neither predicate.
