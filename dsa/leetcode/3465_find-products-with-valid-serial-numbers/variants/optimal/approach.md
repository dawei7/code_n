## General

**Filter rows with one pattern that expresses the whole token contract.** The query reads `product_id`, `product_name`, and `description` from `products`, then applies MySQL's `REGEXP` operator to each description. The regular expression is:

`(?-i)\\bSN[0-9]{4}-[0-9]{4}\\b`

The doubled backslashes belong to the SQL string literal. They cause the regular-expression engine to receive the word-boundary marker `\b` rather than treating the backslash as a string escape. Each remaining component has a specific role.

**Force case-sensitive letters.** `(?-i)` is an inline regular-expression mode modifier that disables case-insensitive matching. This matters because database text comparisons and regular expressions can otherwise inherit case-insensitive behavior from a collation or default mode. With the modifier, only uppercase `SN` matches. Text such as `sn1234-5678` or `Sn1234-5678` is rejected, exactly as the statement requires.

**Match the fixed internal structure.** Literal `SN` must be followed by `[0-9]{4}`, meaning exactly four ASCII decimal digits. The literal hyphen must come next, followed by another `[0-9]{4}`. Using `[0-9]` makes the accepted character set explicit instead of depending on a broader digit category. There are no optional pieces and no wildcards between these components, so `SN1234-5678` matches while `SN123-5678`, `SN12345-5678`, `SN1234_5678`, and `SN1234-567` do not.

The regular expression is not anchored with `^` or `$`. Therefore, the serial number can occur anywhere inside the description. The engine scans until it finds a complete qualifying occurrence, which supports leading or trailing prose such as `"Model uses SN1234-5678 today"`.

**Word boundaries prevent a valid-looking prefix of a longer token.** `\b` means a transition between a word character and a non-word character, or between a word character and the start or end of the string. Letters, digits, and underscore are word characters in the relevant token model. The boundary before `S` prevents a serial from being embedded immediately after another letter, digit, or underscore. The boundary after the fourth trailing digit prevents the pattern from accepting only the first four digits of a longer run.

This last condition explains why `SN1234-56789` is rejected. Although its prefix visually contains `SN1234-5678`, the position after the eighth matched digit lies between two digits, so it is not a word boundary. The same rule rejects `SN1234-5678A` and `SN1234-5678_extra`. By contrast, punctuation, whitespace, parentheses, and string boundaries are legitimate surroundings because they create word boundaries.

The hyphen itself is a non-word character, but that causes no problem because boundaries are checked only before `S` and after the final digit. The pattern deliberately specifies the internal hyphen literally.

**Return exactly the qualifying rows in deterministic order.** The `WHERE` clause retains a row if its description contains at least one match. A description containing several serial numbers still produces only one output row because filtering does not join or expand matches. The `SELECT` clause returns the three requested columns without modifying the description or extracting the token.

`ORDER BY 1` orders by the first selected expression, which is `product_id`. Ascending order is SQL's default when neither `ASC` nor `DESC` is written, so this is equivalent to `ORDER BY product_id ASC`. Because `product_id` is unique, the result order is fully determined.

For the example row containing `"Product SN1234-56789 is available now"`, the trailing boundary fails and the row is excluded. Rows containing `SN1234-5678`, `SN9876-1234`, and `SN4321-8765` surrounded by spaces or the end of the description match and are returned in increasing product ID.

**Why the query is correct.** Any row returned by the query contains a case-sensitive uppercase `SN` token, exactly four digits, one hyphen, and exactly four more digits with word boundaries on both sides. It therefore satisfies every encoded serial-number rule and is not merely a prefix inside a longer word-like token. Conversely, any valid serial described by those rules has exactly the character sequence accepted by the internal pattern and valid token boundaries, so the regular-expression scan will find it wherever it occurs in the description. Finally, sorting by the first selected column produces the required ascending `product_id` order.

## Complexity detail

Let $S$ be the total number of characters across all descriptions and let $r$ be the number of rows that match. The regular expression has fixed length and contains no ambiguous nested repetition, so scanning the descriptions takes $O(S)$ under the regular-expression engine's normal linear scan model. Sorting the $r$ qualifying rows by `product_id` costs $O(r\log r)$ unless an execution plan can already deliver them in index order. The manifest's stated time bound $O(S+r\log r)$ is therefore an appropriate worst-case logical bound.

Database space accounting depends on the chosen execution plan. The result contains $r$ rows and their selected text, and a sort may materialize qualifying rows or sort keys. The manifest records $O(S+r)$ space as a conservative bound that includes text/result handling. From the query author's perspective, the SQL statement declares no growing in-memory data structure; the database engine owns the scan and sort workspace.

An index on `product_id` helps ordering in some plans, but a leading-wildcard-style substring regular expression generally requires examining descriptions because the serial can begin anywhere. Exact optimizer choices remain database-dependent and do not change the query's logical correctness.

## Alternatives and edge cases

- **Use `LIKE 'SN____-____'`:** Underscores match any character, not specifically digits, and anchoring or surrounding-token rules become awkward.
- **Omit `(?-i)`:** On a case-insensitive setup, lowercase or mixed-case prefixes could be accepted even though `SN` is case-sensitive.
- **Omit the final word boundary:** `SN1234-56789` would incorrectly match through its first four trailing digits.
- **Omit the initial word boundary:** Text such as `ASN1234-5678` or `1SN1234-5678` could be accepted as an embedded suffix.
- **Use `\d` instead of `[0-9]`:** Some regular-expression engines give `\d` broader Unicode semantics; the explicit range clearly expresses the required decimal characters.
- **Anchor the whole description:** `^...$` would reject valid descriptions containing ordinary text before or after the serial number.
- **Punctuation around the serial:** Parentheses, commas, periods, and whitespace create valid boundaries and should be accepted.
- **Underscore next to the serial:** Underscore is a word character, so the boundary fails; the token is treated as embedded in a larger identifier.
- **Multiple valid serials in one description:** `WHERE` is Boolean, so the product appears once rather than once per occurrence.
- **A valid and an invalid serial together:** The row qualifies if at least one complete valid occurrence matches.
- **`NULL` description:** SQL regular-expression evaluation yields unknown rather than true, so such a row is not selected; the reference schema does not state a separate null requirement.
- **`ORDER BY 1` readability:** It is concise and correct here, though spelling out `product_id ASC` can be clearer when a select list is later rearranged.
