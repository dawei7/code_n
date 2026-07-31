## Examples

**Example 1**

- Input: `s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]`
- Output: `[0,2]`
- Explanation:

  | `i` | `queries[i]` | `j` | `l` | `r` | `s` before query | `s[l..r]` | Result | Answer |
  |---:|---|---:|---:|---:|---|---|---|---:|
  | 0 | `[2,1,2]` | — | 1 | 2 | `"ABA"` | `"BA"` | The substring is already alternating. | 0 |
  | 1 | `[1,1]` | 1 | — | — | `"ABA"` | — | Flip `s[1]` from `'B'` to `'A'`. | — |
  | 2 | `[2,0,2]` | — | 0 | 2 | `"AAA"` | `"AAA"` | Delete any two `'A'` characters to leave `"A"`. | 2 |

  The two range-query results form `[0,2]`.

**Example 2**

- Input: `s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]]`
- Output: `[1,0]`
- Explanation:

  | `i` | `queries[i]` | `j` | `l` | `r` | `s` before query | `s[l..r]` | Result | Answer |
  |---:|---|---:|---:|---:|---|---|---|---:|
  | 0 | `[2,0,2]` | — | 0 | 2 | `"ABB"` | `"ABB"` | Delete one `'B'` to obtain `"AB"`. | 1 |
  | 1 | `[1,2]` | 2 | — | — | `"ABB"` | — | Flip `s[2]` from `'B'` to `'A'`. | — |
  | 2 | `[2,0,2]` | — | 0 | 2 | `"ABA"` | `"ABA"` | The substring is already alternating. | 0 |

  The resulting answer array is `[1,0]`.

**Example 3**

- Input: `s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]]`
- Output: `[0,1]`
- Explanation:

  | `i` | `queries[i]` | `j` | `l` | `r` | `s` before query | `s[l..r]` | Result | Answer |
  |---:|---|---:|---:|---:|---|---|---|---:|
  | 0 | `[2,0,3]` | — | 0 | 3 | `"BABA"` | `"BABA"` | The substring is already alternating. | 0 |
  | 1 | `[1,1]` | 1 | — | — | `"BABA"` | — | Flip `s[1]` from `'A'` to `'B'`. | — |
  | 2 | `[2,1,3]` | — | 1 | 3 | `"BBBA"` | `"BBA"` | Delete one `'B'` to obtain `"BA"`. | 1 |

  Therefore the returned results are `[0,1]`.
