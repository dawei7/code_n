## General

MySQL has `UPPER` and `LOWER` but no built-in title-case function that also guarantees preservation of every original space. Walk through each row one character at a time with a recursive CTE. The state retains the source columns, the current one-based character position, and the converted prefix.

At position one, or whenever the preceding source character is a space, append the uppercase form of the current character. At every other position append its lowercase form. A space itself is appended unchanged by either case function; because the query never splits, trims, or rejoins the string, leading, trailing, and repeated spaces remain at their exact positions.

Recursion continues through the final source character. The row whose position is one beyond the text length contains the complete conversion, including an immediate completed row for empty text. Project the original text under the required alias and order by the unique identifier.

Every character appears in exactly one transition. The boundary test classifies precisely the first character of each space-delimited word, so those and only those letters are uppercased; all other letters are lowercased. Concatenating transitions in position order therefore produces the unique required text without changing its spacing.

The remotely Accepted MySQL artifact uses `CONCAT` and a bounded character cast so its recursive result column can grow. The app-local SQLite artifact uses `||` and a text cast while preserving the same state and transformation semantics.

## Complexity detail

Let $n$ be the row count and $S$ the total number of source characters. The recursive relation emits one state per character plus one completed state per row, so character processing is $O(S)$. Ordering the $n$ completed rows costs $O(n\log n)$ in the general case, giving $O(S+n\log n)$ time. Recursive state and the ordered result require $O(S+n)$ working space.

The benchmark defines `size` as $n$ and gives every row the same fixed-length mixed-case text, so $S=\Theta(n)$. The reference transforms each character once and sorts completed rows. A correct correlated baseline that additionally counts an identifier prefix at every recursive character state repeatedly scans the table and requires $\Theta(n^2)$ work for fixed-length rows.

## Alternatives and edge cases

- **Split and rejoin words:** It can normalize case, but ordinary tokenization collapses or discards leading, trailing, and repeated spaces.
- **Uppercase only the first text character:** Later words would keep lowercase initials and fail the per-word rule.
- **Apply `LOWER` only:** This fixes internal capitals but does not capitalize word starts.
- **Fixed number of word expressions:** It fails when a row contains more words than the authored limit.
- **Correlated prefix counting:** It can be added without changing rows, but introduces quadratic repeated scans.
- **Repeated spaces:** Each space is copied, and the first following letter still sees a space boundary.
- **Leading and trailing spaces:** They remain in place; a letter after any leading run is capitalized.
- **One-letter words:** Their sole letter is a word start and becomes uppercase.
- **Empty text:** The anchor state is already complete and returns an empty conversion.
- **Output ordering:** Use the unique `content_id`, not table insertion order.
