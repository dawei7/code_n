## General

Each log row must be classified from three independent properties of its IP string: the number of dot-separated octets, whether any octet starts with a leading zero, and whether any octet is numerically greater than $255$. After classification, invalid rows are grouped by their original `ip` value and counted.

**Native MySQL parsing.** `SUBSTRING_INDEX` extracts the four candidate octets, while the difference between the original length and the length after removing dots gives the delimiter count. Exactly three dots means exactly four dot-separated octets, including empty components. A regular expression detects a `0` followed by another digit at the start of the string or immediately after a dot. Numeric casts then test all four extracted values against $255$.

**Offline SQLite parsing.** The app-local query uses a recursive common table expression. Appending one terminal dot lets each recursive row remove one component from the front, including an empty component between adjacent dots. Grouping those components by `log_id` yields the octet count and the two per-row invalidity flags. This preserves the source semantics instead of imposing a stricter general IPv4 grammar: for example, `192.168..1` has four components and triggers none of the three stated conditions.

Every invalid log row then contributes once to its IP group. `COUNT(*)` produces `invalid_count`, and the two descending sort keys implement the required deterministic order.

## Complexity detail

Let $r$, $S$, and $k$ have the meanings defined in the function contract. Parsing and classifying all strings takes $O(S)$ time. Grouping is linear in the row count under ordinary database hashing, and ordering the distinct invalid groups takes $O(k \log k)$ time, giving $O(S + k \log k)$ overall. The parsed rows and grouped results use $O(S + k)$ working space in the app-local recursive formulation; the native database may use an equivalent temporary representation chosen by its optimizer.

## Alternatives and edge cases

- **Full IPv4 regular expression:** Enforcing a conventional nonempty-digit grammar is too strict for this task; LeetCode's contract rejects only the three enumerated conditions.
- **Correlated recount per IP:** Recounting the complete log table for every invalid row is correct but can require $O(r^2)$ work.
- **Boundary value $255$:** An octet equal to $255$ is allowed; only values strictly greater than $255$ are invalid.
- **Leading zero:** A single-character octet `0` is allowed, whereas `00` and `01` have leading zeros.
- **Empty octet:** Adjacent dots still delimit an empty component, which neither exceeds $255$ nor begins with a zero; it is not independently invalid.
- **Duplicate IP rows:** Classification happens per log row, and grouping afterward preserves the required occurrence count.
