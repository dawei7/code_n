## General

**Process one space-delimited token per recursive row.** The recursive common table expression `capitalized_words` creates several intermediate rows for each source row in `user_content`. Each intermediate row retains `content_id` and the complete `content_text`, while also storing:

- `word`: the next token to process;
- `remaining_text`: everything after that token and its following separator;
- `processed_word`: the converted prefix built so far.

The non-recursive part creates the first intermediate row. `SUBSTRING_INDEX(content_text, ' ', 1)` returns the characters before the first space. That value becomes the first `word`.

**Convert one word to title-style casing.** For any extracted token, the expression

`CONCAT(UPPER(LEFT(word, 1)), LOWER(SUBSTRING(word, 2)))`

handles the two required parts separately. `LEFT(word,1)` obtains the first character and `UPPER` capitalizes it. `SUBSTRING(word,2)` obtains every remaining character and `LOWER` normalizes them. Concatenating the pieces transforms `"qUICK"` into `"Quick"` and `"SQL"` into `"Sql"`.

A one-character token has an empty remainder, so it becomes just its uppercase form. An empty token, which can arise around repeated spaces, stays empty.

**Advance past the token and one separator.** The first token length is

`LENGTH(SUBSTRING_INDEX(content_text, ' ', 1))`.

Adding two gives the one-based MySQL position immediately after the token and the first separating space. `SUBSTRING` from that position becomes `remaining_text`.

The recursive part repeats the same extraction on the previous `remaining_text`. It appends one literal space and the newly converted token to `processed_word`. Recursion continues while `remaining_text != ''`.

**How repeated internal spaces are represented.** Consider `"a  b"`. After processing `"a"`, the remaining text begins with one space. The next `SUBSTRING_INDEX` therefore extracts an empty token. Appending `' ' + ''` records one separator, and advancing past that empty token consumes the next separator. The following iteration processes `"b"` and adds another separator before it. The constructed result is `"A  B"`. Empty tokens allow internal and leading runs of spaces to survive in this common case.

**Accumulate converted prefixes.** Every recursive row's `processed_word` is the previous converted prefix plus one separator and one converted token. For ordinary non-trailing content, the final recursive row contains the full transformed text, while earlier rows contain strict prefixes of it.

The outer query groups all recursive rows belonging to the same `content_id` and `content_text`. `MAX(processed_word)` selects the full prefix under the expected string collation because each later value extends the earlier value with additional characters. It is being used as a convenient “last recursive value” aggregate; there is no explicit recursion-depth column.

**Preserve the original alongside the conversion.** `content_text AS original_text` returns the source text without case changes. Grouping by ordinal columns `1,2` means grouping by `content_id` and `original_text`. Since `content_id` is unique, each source row produces one output row.

**Trace a normal phrase.** For `"the QUICK brown"`, the anchor produces `"The"` and leaves `"QUICK brown"`. The next row produces `"The Quick"` and leaves `"brown"`. The last produces `"The Quick Brown"` and leaves an empty string. The aggregate chooses the complete converted value.

**A genuine trailing-space defect.** The manifest says spaces are preserved verbatim, but the exact SQL does not retain spaces after the final nonempty word. For `"hello "`, the anchor extracts `"hello"` and computes an empty `remaining_text`. The recursive branch does not run, and `processed_word` is `"Hello"`, with the trailing space lost. Multiple trailing spaces are likewise not reliably represented once the remainder becomes empty.

This behavior conflicts with the stated requirement to preserve all existing spaces. The explanation must describe the executable query rather than claim perfect preservation. A fully faithful solution would need position-based character processing or explicit tracking of trailing separators.

**Why ordinary words are converted correctly.** Each nonempty token is transformed by the same first-character/rest rule, recursion preserves token order, and the aggregate returns the most complete constructed prefix. Therefore content whose relevant spaces occur before or between words receives the intended casing, subject to the trailing-space limitation above.

## Complexity detail

Let $S$ be the total number of characters and $w$ the number of extracted tokens across all rows. A high-level manifest estimate may treat the recursive scan as $O(S)$ plus grouping work. The exact SQL repeatedly scans suffixes with `SUBSTRING_INDEX` and copies growing prefixes with `CONCAT`. For a single long row, the cumulative character work can reach $O(Lw)$ and $O(L^2)$ in the worst case.

Recursive intermediate rows also retain growing `processed_word` values and shrinking `remaining_text` values, so materialized character storage can be quadratic for adversarial spacing/token patterns. Grouping and `MAX` add engine-dependent hashing or sorting cost. The manifest's $O(S+n\log n)$ time and $O(S+n)$ space are therefore an optimistic logical summary, not guaranteed physical bounds for this exact recursive query.

## Alternatives and edge cases

- **Position-based recursive CTE:** Process one character at a time with an “at word start” flag; it can preserve leading, repeated, and trailing spaces exactly.
- **Built-in title-case function:** MySQL has no universally equivalent built-in that also guarantees the required spacing behavior.
- **Split-and-reassemble:** It is conceptually simple but must retain empty tokens and trailing separators to meet the contract.
- **One-character word:** The first character is uppercased and the empty remainder is harmless.
- **All-uppercase word:** Every character after the first becomes lowercase.
- **Already converted word:** Applying the transformation again leaves it unchanged.
- **Repeated internal spaces:** Empty recursive tokens commonly reconstruct their multiplicity.
- **Leading spaces:** Empty initial tokens can carry them forward, though collation and substring behavior deserve explicit testing.
- **Trailing spaces:** The exact source drops them when `remaining_text` becomes empty.
- **Empty content:** The local description gives no explicit nonempty guarantee; behavior would depend on the anchor and aggregate collation.
- **No special characters:** Tokenization needs to distinguish only literal spaces and letters.
- **`MAX` as last-row selection:** It relies on each completed prefix comparing no smaller than its proper prefix under the active collation.
- **Ordinal grouping:** `GROUP BY 1,2` refers to `content_id` and `original_text`.
- **Unique key:** Grouping cannot merge two different source rows with the same text because IDs differ.
- **Manifest discrepancy:** Exact space preservation and linear character processing are not fully supported by the SQL.
