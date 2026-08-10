## General

**The requirement is about an entire digit run, not any three-digit slice.** A product name qualifies when it contains a maximal consecutive run of digits whose length is exactly three. Merely finding three adjacent digits is insufficient. For example, `"ABC123XYZ"` qualifies, but `"Product56789"` does not: although `"567"`, `"678"`, and `"789"` are three-character digit slices, all of them belong to one five-digit run.

The query expresses the exact-run condition with this regular expression:

`(^|[^0-9])[0-9]{3}([^0-9]|$)`.

It helps to read the expression as three consecutive pieces.

**Require a safe left boundary.** `(^|[^0-9])` means either the match is at the beginning of the name, represented by `^`, or the character immediately before the digit run is not a digit, represented by `[^0-9]`. The square-bracket expression `[0-9]` denotes one decimal digit, while the caret inside the brackets negates that character class.

This boundary prevents the regex engine from beginning a supposed three-digit match in the middle of a longer digit run. In `"A1234"`, for example, a candidate beginning at `"2"` has a digit before it and therefore fails the left boundary.

**Match exactly three digit characters.** `[0-9]{3}` requires three consecutive occurrences of the digit class. Leading zeros are ordinary digit characters, so `"003"` is a valid run. The query tests text structure, not whether the three characters form a three-digit numeric value.

**Require a safe right boundary.** `([^0-9]|$)` says that the character after the three digits must be a non-digit or the end of the name. This prevents taking the first three digits from a longer run. In `"1234"`, the candidate `"123"` fails because its next character is `"4"`. A candidate `"234"` fails the left boundary because `"1"` precedes it. Thus no location inside a four-or-more-digit run can satisfy both boundaries.

The beginning and end alternatives make digit runs at the edges work. `"789Product"` qualifies through the start-of-string branch on the left and the non-digit `"P"` on the right. `"Product789"` qualifies through a non-digit on the left and the end-of-string branch on the right. A name consisting only of three digits also satisfies both anchors.

**Filter rows, then project only required columns.** The `WHERE name REGEXP ...` condition is true when MySQL finds at least one substring satisfying the expression. A name may contain multiple qualifying runs, but `WHERE` does not duplicate the row; it only decides whether the product is included. The `SELECT` list returns `product_id` and `name` exactly as requested.

The query ends with `ORDER BY 1`. In SQL positional ordering, `1` refers to the first expression in the select list, which is `product_id`. The default direction is ascending, so this is equivalent to `ORDER BY product_id ASC`.

For the sample:

- `"ABC123XYZ"` has non-digit boundaries around `"123"` and qualifies;
- `"A12B34C"` has only runs of lengths two and two, so it fails;
- `"Product56789"` has a five-digit run, and every possible three-digit slice fails at least one boundary;
- `"789Product"` uses the beginning anchor and qualifies;
- `"Item003Description"` contains an exact run `"003"` and qualifies.

**Why the condition is necessary and sufficient.** If the regex matches, its central portion contains exactly three digits. The left portion proves no digit is immediately before them, and the right portion proves no digit is immediately after them. Those three digits are therefore a complete maximal run of length three.

Conversely, suppose a name contains a maximal digit run of exactly three characters. If it starts at the beginning, `^` satisfies the left boundary; otherwise maximality guarantees the preceding character is a non-digit. The same reasoning uses `$` or a following non-digit on the right. The run necessarily satisfies all three regex pieces, so the row is selected.

Using explicit `[0-9]` rather than a broad character such as `.` is important: the middle must contain digits, while the boundary must contain either no character because of an anchor or a character outside the digit class.

## Complexity detail

Let $S$ be the total number of characters across all product names scanned, and let $r$ be the number of matching rows. With a normal linear regex scan for this fixed-size pattern, filtering takes $O(S)$ time. Producing ascending order may require sorting the $r$ matching rows, costing $O(r\log r)$ time and $O(r)$ working space. This gives $O(S+r\log r)$ time and $O(r)$ sort space, consistent with the manifest's $O(S+n\log n)$ notation when $n$ denotes the result count or a safe upper bound on rows.

Actual database plans can differ. A usable index on `product_id` may let MySQL produce rows in order without an explicit sort, while the leading arbitrary-position regex normally requires inspecting names rather than using a simple prefix index. SQL complexity is therefore plan-dependent, but the stated bounds describe the direct scan-and-sort execution model.

## Alternatives and edge cases

- **Three digits without boundaries:** `[0-9]{3}` alone incorrectly accepts any run of four or more digits because it can match a three-character portion.
- **Word-boundary token:** A regex word boundary does not mean “digit versus non-digit”; letters, digits, and underscores are all word characters in common regex rules. Explicit digit negation is the correct boundary.
- **String-length arithmetic:** Removing non-digits or splitting names can solve the task procedurally, but it is more verbose and easier to mishandle multiple runs than the direct regex.
- **Leading zeros:** `"007"` is exactly three digit characters and must qualify. Numeric conversion would erase the structural leading zeros and is inappropriate.
- **Run at the start:** The `^` alternative allows `"123ABC"` even though there is no preceding character.
- **Run at the end:** The `$` alternative allows `"ABC123"` even though there is no following character.
- **Name of exactly three digits:** Both anchors match, so the row is correctly included.
- **Several valid runs:** A name such as `"A123B456C"` is returned once, not once per regex occurrence, because `WHERE` filters rows.
- **Mixed run lengths:** A name qualifies if it has at least one exact three-digit run, even when another part of the same name contains a longer or shorter run.
- **Ordering syntax:** `ORDER BY 1` is concise but depends on select-list position. Writing `ORDER BY product_id ASC` would be more self-documenting while producing the same result.
