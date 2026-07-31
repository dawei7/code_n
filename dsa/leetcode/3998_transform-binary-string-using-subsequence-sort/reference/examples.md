## Examples

**Example 1**

- Input: `s = "101", strs = ["1?1","0?1","0?0"]`
- Output: `[true,true,false]`
- **Explanation:** The source evaluates each pattern as follows.

| `i` | `strs[i]` | Replacement | Completed pattern | Operation(s) | Result |
|---:|---|---|---|---|---|
| 0 | `"1?1"` | `? -> 0` | `"101"` | The completion already equals `s`, so no operation is needed. | `true` |
| 1 | `"0?1"` | `? -> 1` | `"011"` | Select indices `[0..2]`, obtaining `"101"`; sorting that subsequence gives `"011"`. | `true` |
| 2 | `"0?0"` | `? -> 0` or `? -> 1` | `"000"` or `"010"` | Neither completion can be produced from `s`. | `false` |

Therefore, `ans = [true,true,false]`.

**Example 2**

- Input: `s = "1100", strs = ["0011","11?1","1?1?"]`
- Output: `[true,false,true]`
- **Explanation:** The three rows retain the source table's replacements and selected subsequences.

| `i` | `strs[i]` | Replacement | Completed pattern | Operation(s) | Result |
|---:|---|---|---|---|---|
| 0 | `"0011"` | None | `"0011"` | Select indices `[0..3]`, obtaining `"1100"`; sorting the selection gives `"0011"`. | `true` |
| 1 | `"11?1"` | `? -> 0` | `"1101"` | This completion is not feasible. | `false` |
| 2 | `"1?1?"` | First `? -> 0`; second `? -> 0` | `"1010"` | Select indices `[1,2]`, obtaining `"10"`; sorting them to `"01"` changes `s` into `"1010"`. | `true` |

Thus, `ans = [true,false,true]`.

**Example 3**

- Input: `s = "1010", strs = ["0011"]`
- Output: `[true]`
- **Explanation:** The sole pattern is transformed as shown below.

| `i` | `strs[i]` | Replacement | Completed pattern | Operation(s) | Result |
|---:|---|---|---|---|---|
| 0 | `"0011"` | None | `"0011"` | Select indices `[0,2,3]`, obtaining `"110"`; sorting that selection to `"011"` changes `s` into `"0011"`. | `true` |

Therefore, `ans = [true]`.
