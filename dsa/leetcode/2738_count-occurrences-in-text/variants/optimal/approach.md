## General

**Count files, not repeated appearances inside one file**

The requested count for each target is the number of `Files` rows whose `content` contains at least one valid occurrence. A file containing `" bull bull "` must contribute one, not two.

The query handles this naturally with a `WHERE` predicate. Each matching table row reaches `COUNT(*)` once, regardless of how many places within its content satisfy the pattern.

**Match the exact space-delimited rule**

For `bull`, the predicate is:

`content LIKE '% bull %'`.

The leading and trailing percent signs permit arbitrary text before and after the match. The literal pattern inside them contains one ordinary space, then `bull`, then another ordinary space. Thus the target must have a space on both sides somewhere in the content.

The `bear` branch uses the analogous `'% bear %'` pattern.

This deliberately does not implement a general linguistic word boundary. A word at the very beginning or end lacks one required surrounding space. `"bull."` lacks a space immediately after the letters. `"bullet"` has extra letters rather than the required trailing space. All fail as specified.

Tabs and newlines are also not the same as the literal space characters in the pattern. The exact solution follows the source's space-delimited interpretation rather than a regular expression for all whitespace.

**LIKE returns one Boolean decision per row**

For each `Files` row, MySQL searches the content for some substring matching the pattern. If one exists, the row passes `WHERE`. `COUNT(*)` then counts the qualifying row.

No grouping by file name is needed because each input row represents one file. The aggregate select returns one row even when no file qualifies, with count zero.

**Create the required label**

The first select includes constant `'bull' AS word`. This labels its aggregate count. The second includes `'bear' AS word`.

Each aggregate has exactly the output columns `word` and `count`, so the two rows can be combined vertically.

**Why UNION preserves both rows**

The query uses `UNION`, which normally removes duplicate result rows. Here the labels are different: one row's `word` is `bull` and the other's is `bear`. They can never be identical as complete rows, even when their counts are equal.

Therefore `UNION` always preserves both target rows. `UNION ALL` would avoid an unnecessary duplicate-elimination step and produce the same logical result, but the exact source uses `UNION`.

The required output order is arbitrary, so no `ORDER BY` is needed.

**Trace the example**

Every sample content row contains the substring `" bull "` with spaces on both sides, so the first scan counts three files.

Only the second and third rows contain `" bear "` in that exact form, so the second scan counts two.

The final result contains `('bull', 3)` and `('bear', 2)` in whichever order MySQL returns the union branches.

**Case sensitivity follows the database collation**

The query does not call `LOWER` and does not specify a binary collation. In common default MySQL case-insensitive collations, `LIKE` treats `Bull` and `bull` as equal. Under a case-sensitive collation, only exact lowercase matches count.

The exact implementation therefore inherits collation behavior. The source examples and target literals are lowercase, and the local editorial assumes case-insensitive matching in the common environment.

**Why punctuation is intentionally excluded**

A regex word-boundary solution would normally count `bull` before a period. This problem explicitly says `"bull."` is not valid because it lacks a space on the right. Literal-space patterns encode that unusual contract exactly.

Likewise, adding spaces around the whole content before searching would incorrectly make beginning- or end-position occurrences valid. The solution correctly searches the original text unchanged.


A Files row enters the first aggregate exactly when its content contains the literal space-delimited substring `" bull "`, so it contributes one exactly when that file has at least one valid bull occurrence. The same is true for bear. Each aggregate counts matching files once, constants label the counts, and the union returns both distinct labels. Hence the two output rows contain exactly the required file counts.

## Complexity detail

Let $S$ be the total number of characters across all `content` values. Each branch may scan the table's text for its fixed pattern, so the total character-search work is $O(S)$ with a constant factor of two. The fixed pattern lengths do not grow with the input.

The aggregates maintain constant-size counters and return two rows, giving $O(1)$ logical auxiliary space. MySQL's execution engine may use internal buffers, and `UNION` may perform a tiny duplicate-elimination step over two rows, but neither grows meaningfully beyond the input scan.

Without a specialized full-text or pattern index, leading `%` prevents an ordinary prefix index from avoiding the content scan.

## Alternatives and edge cases

- **`UNION ALL`:** Produces the same two labeled rows and avoids duplicate elimination because labels are inherently distinct.
- **Regular expression with spaces:** Can encode the same contract but is more machinery than fixed `LIKE` patterns require.
- **Regex word boundaries:** Incorrect here because they would count punctuation-delimited or boundary-position words excluded by the statement.
- **Count string occurrences:** Incorrect because the task counts matching files, not how many times a word appears within each file.
- **Word at content start:** Does not match because no leading space exists.
- **Word at content end:** Does not match because no trailing space exists.
- **Punctuation after target:** Does not match the literal trailing space.
- **Plural or longer word:** `bears` and `bullet` do not match.
- **No matching files:** Each aggregate still returns its label with count zero.
- **Case behavior:** Depends on the column collation because the query does not normalize case explicitly.
