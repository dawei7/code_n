## Examples

In the following traces, “reader position” identifies the next unconsumed character.

**Example 1**

- Input: `s = "42"`
- Output: `42`
- Explanation: The reader advances as follows:

| Step | Consumed text | Reader position | Effect |
|---:|---|---|---|
| 1 | `""` | Before `4` | There is no leading whitespace. |
| 2 | `""` | Before `4` | There is no explicit sign. |
| 3 | `"42"` | End of string | The digits produce 42. |

**Example 2**

- Input: `s = " -042"`
- Output: `-42`
- Explanation: The leading whitespace is discarded, the minus sign makes the result negative, and the digits `042` produce magnitude 42. The source's step trace illustrates three leading spaces even though its displayed input contains one; either count is handled by the same whitespace rule.

| Step | Consumed text | Reader position | Effect |
|---:|---|---|---|
| 1 | `"   "` | Before `-` | Ignore the leading spaces. |
| 2 | `"   -"` | Before `0` | Record a negative sign. |
| 3 | `"   -042"` | End of string | Read `042`; its leading zero does not change the value. |

**Example 3**

- Input: `s = "1337c0d3"`
- Output: `1337`
- Explanation: No whitespace or sign is consumed. The reader accepts `1337` and stops when it reaches the non-digit `c`.

| Step | Consumed text | Reader position | Effect |
|---:|---|---|---|
| 1 | `""` | Before `1` | There is no leading whitespace. |
| 2 | `""` | Before `1` | There is no explicit sign. |
| 3 | `"1337"` | Before `c` | Convert `1337` and stop at the first non-digit. |

**Example 4**

- Input: `s = "0-1"`
- Output: `0`
- Explanation: The reader consumes the initial digit `0` and then stops at `-`; the remaining characters are ignored.

| Step | Consumed text | Reader position | Effect |
|---:|---|---|---|
| 1 | `""` | Before `0` | There is no leading whitespace. |
| 2 | `""` | Before `0` | There is no explicit sign. |
| 3 | `"0"` | Before `-` | Convert the zero and stop at the non-digit. |

**Example 5**

- Input: `s = "words and 987"`
- Output: `0`
- Explanation: The first character, `w`, is not a digit, so conversion stops before any digit is read and the result is `0`.
