## General
**Count choices at each digit position**

A valid decimal position may contain exactly nine digits: `0` through `8`. Consequently, all valid strings of a fixed width are counted like base-9 numerals. Increasing a rank through the filtered sequence changes these allowed digits in precisely the same order as incrementing a base-9 number.

**Reinterpret the rank's base-9 digits as decimal digits**

Repeatedly divide `n` by nine. Each remainder is a digit from zero through eight, so it is also a legal decimal digit. Place successive remainders into decimal ones, tens, hundreds, and so on. For example, rank `18` is `20` in base nine, and decimal `20` is the eighteenth positive integer without a `9`.

**Why the mapping preserves rank and order**

Every positive base-9 numeral maps to one decimal numeral containing no `9`, and reading any no-`9` decimal numeral's digits as base nine reverses the mapping. Both numeral systems compare equal-length representations lexicographically by their most significant digit, and shorter positive representations precede longer ones. The bijection therefore preserves increasing order, making the image of base-9 `n` exactly the `n`-th retained integer.

## Complexity detail
Each division removes one base-9 digit, so the algorithm performs $O(\log N)$ iterations. It stores only the remaining rank, result, digit, and decimal place multiplier, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Generate integers and reject those containing `9`:** follows the sequence definition directly, but examines every preceding candidate and takes time proportional to the answer rather than its digit count.
- **Build a base-9 string:** is concise and still takes $O(\log N)$ time, but allocates $O(\log N)$ temporary string space.
- **Digit dynamic programming plus binary search:** can count valid integers up to a bound, but is far more machinery than the direct order-preserving bijection.
- Ranks `1` through `8` map to themselves.
- Rank `9` is the first carry and maps to decimal `10`.
- Zero digits inside or at the end of the result are valid; only digit `9` is excluded.
