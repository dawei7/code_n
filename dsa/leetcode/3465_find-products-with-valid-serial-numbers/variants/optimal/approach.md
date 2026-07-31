## General

**Describe the complete token, not just its interior.** The MySQL regular expression is `\\bSN[0-9]{4}-[0-9]{4}\\b`. The two letters are literal uppercase characters. Each `[0-9]{4}` contributes exactly four decimal digits, and the hyphen between the groups is literal.

The word boundaries are material. A boundary exists between a word character—letter, digit, or underscore—and a non-word character, or at the end of the value. They allow punctuation and whitespace around a serial number while rejecting partial matches such as `SN1234-56789`, `ASN1234-5678`, `SN1234-5678X`, and `_SN1234-5678`. Because a MySQL column's collation may otherwise make regular-expression matching case-insensitive, pass the `c` match flag to `REGEXP_LIKE`; lowercase or mixed-case prefixes must not qualify.

Project the three requested source columns and finish with `ORDER BY product_id`. A row qualifies if any complete serial-number token occurs anywhere in its description, so multiple occurrences do not duplicate the product.

**Preserve the contract in the offline SQLite adapter.** SQLite does not provide MySQL's `REGEXP_LIKE` by default. The app-local query therefore uses a recursive common table expression to enumerate every possible one-based start position of an 11-character token. At each position it checks uppercase `SN`, both four-digit groups, the hyphen, and the word-character exclusions immediately before and after the token. `DISTINCT` collapses a product with several valid serial numbers back to one output row before the required sort.

## Complexity detail

Let $r$ be the number of product rows and let

$$
S=\sum_{p\in\texttt{products}}\lvert p.\texttt{description}\rvert.
$$

Scanning the descriptions costs $O(S)$. Sorting at most $r$ qualifying rows costs $O(r\log r)$, giving $O(S+r\log r)$ time. The conservative cross-engine bound includes the SQLite adapter's generated candidate positions and the result sort, so auxiliary space is $O(S+r)$; MySQL's direct regular-expression execution may use less temporary storage.

## Alternatives and edge cases

- **Plain `LIKE`:** SQL wildcard matching does not directly express four required decimal digits, case sensitivity, and word boundaries together.
- **Unbounded regular expression:** `SN[0-9]{4}-[0-9]{4}` alone accepts a valid-looking substring inside a longer invalid word or digit run.
- **Case-insensitive default collation:** Omitting MySQL's `c` match flag can admit `sn1234-5678`, `Sn1234-5678`, or `sN1234-5678`.
- **Anchoring the whole description:** `^` and `$` around the serial pattern would reject valid rows whose description contains surrounding prose.
- **Five digits in either group:** A word boundary after four digits and before `SN` prevents a four-digit portion of a longer numeric token from qualifying.
- **Punctuation around the token:** Parentheses, commas, periods, and whitespace are non-word characters and are valid separators.
- **Underscore adjacency:** An underscore is a word character, so `_SN1234-5678` and `SN1234-5678_` are not complete tokens.
- **Several matches in one description:** The product appears once, not once per serial number.
- **Output order:** The explicit ascending `ORDER BY product_id` is part of the result contract.
