## General

**Apply one pure text conversion to every DataFrame row.** Inner helper `convert_text` receives one `content_text` string and returns its converted version. Pandas `apply(convert_text)` invokes it independently for each row, and the resulting series becomes new column `converted_text`.

**Split on the literal space delimiter.** `text.split(" ")` differs importantly from `text.split()`. Supplying an explicit delimiter preserves empty fields produced by leading, trailing, or repeated spaces. For example:

- `" a"` becomes `["", "a"]`;
- `"a  b"` becomes `["a", "", "b"]`;
- `"a "` becomes `["a", ""]`.

The final `" ".join(...)` inserts one space between every field. Empty fields therefore reconstruct the original number and placement of literal spaces. This directly supports the requirement that spacing remain unchanged.

**Normalize an ordinary whitespace token.** When a token contains no hyphen, `word.capitalize()` uppercases its first character and lowercases all remaining cased characters. `"SQL"` becomes `"Sql"` and `"qUICK"` becomes `"Quick"`.

Python's `capitalize` operates on the first character, not the first alphabetic character after arbitrary punctuation. The local rules give special semantics only to hyphens, so the exact behavior for tokens beginning with other allowed symbols follows Python's string method.

**Treat every hyphen-separated component as a part.** If `"-" in word`, the source executes `word.split("-")`. Each part is individually capitalized, and `"-".join(...)` restores the hyphens.

Thus:

- `"QUICK-brown"` becomes `"Quick-Brown"`;
- `"modern-day"` becomes `"Modern-Day"`;
- `"FRONT-end"` becomes `"Front-End"`.

The source is more general than only two-part words: `"a-b-c"` becomes `"A-B-C"`.

**Preserve unusual hyphen placement mechanically.** Explicit split retains empty components around consecutive, leading, or trailing hyphens. Capitalizing an empty string returns an empty string, and joining restores the delimiters. For instance, `"a--b"` becomes `"A--B"`. The code does not “validate a hyphen token” as the manifest summary claims; it transforms every component produced by splitting.

**Reconstruct every word and space in order.** The generator preserves the sequence of whitespace fields. Each field is replaced only by its case-normalized counterpart, then the literal-space join restores separators. Unlike the recursive SQL in ID 3368, this implementation preserves trailing spaces because the final empty field remains present.

**Create the required output schema.** After assigning `converted_text`, the source calls

`rename(columns={"content_text": "original_text"})`

and selects columns in exact order:

`content_id, original_text, converted_text`.

This both names the original text as requested and prevents unrelated DataFrame columns from leaking into the result.

**A caller-visible input mutation occurs.** Assignment

`user_content["converted_text"] = ...`

modifies the supplied DataFrame before `rename` and final projection return a new result object. The original input object retains its `content_text` column and gains `converted_text`. This does not alter text values, but it is a side effect that a faithful explanation should not hide.

**Trace repeated spacing.** For `"  TOP-rated "`, explicit splitting yields two leading empty fields, `"TOP-rated"`, and one trailing empty field. Conversion changes only the central token to `"Top-Rated"`. Joining returns `"  Top-Rated "` with all three spaces in their original positions.

**Why the output transformation is correct for the specified rule.** Every literal-space-delimited token is visited once. Ordinary tokens receive one capitalization, hyphenated tokens receive one capitalization per component, and explicit empty fields reconstruct spacing. Projection retains both original and converted strings for the same unique ID.

**The manifest complexity description does not match the executable steps.** It lists $O(SL+n\log n)$ and describes boundary tracking and token validation. The exact source performs direct Python splits, joins, and Pandas row application; it does not sort rows and does not run a validation search of length $L$.

## Complexity detail

Let $S$ be the total number of characters across all text rows. Each character participates in a constant number of split, capitalization, and join operations, so the core conversion is $O(S)$ time. Pandas `apply` adds per-row Python-call overhead, and column assignment/rename/projection add $O(n)$ object-management work.

Converted strings occupy $O(S)$ space, and the returned DataFrame has $O(n)$ row references/metadata in addition. Intermediate word and hyphen-part lists for one row use space proportional to that row's length. There is no algorithmic $n\log n$ sort in the exact file.

## Alternatives and edge cases

- **Regular-expression replacement:** It can capitalize word and post-hyphen letters in one pass but must carefully preserve spacing and lowercase all other letters.
- **Character-state machine:** It avoids temporary split lists and offers exact control over punctuation boundaries.
- **`split()` without a delimiter:** It would collapse repeated spaces and strip leading/trailing spaces, violating the formatting rule.
- **Multiple spaces:** Empty fields preserve them.
- **Leading and trailing spaces:** Explicit split plus join retains them.
- **Multiple hyphens:** Every nonempty component is capitalized and delimiters survive.
- **Leading or trailing hyphen:** Empty components preserve the boundary hyphen.
- **One-character part:** It becomes uppercase.
- **Already normalized text:** Conversion is idempotent.
- **Other allowed punctuation:** It remains present, but `capitalize` does not necessarily uppercase the first letter after it.
- **Empty string:** It splits to one empty field and reconstructs as empty.
- **Input DataFrame mutation:** `converted_text` is added to the supplied object.
- **Output column order:** The final bracket projection enforces it explicitly.
- **Pandas dependency:** The solution requires a compatible `pd.DataFrame` environment.
- **Manifest discrepancy:** No sort, boundary automaton, or hyphen validation exists in the exact source.
