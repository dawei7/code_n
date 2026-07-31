## Examples

**Example 1**

- Input: `s = "(())", k = 1`
- Output: `""`
- Explanation: For `k = 1`, the removable string is `"()"`.

| Step | Current `s` | k-balanced occurrence removed | Resulting `s` |
|---:|---|---|---|
| 1 | `"(())"` | The middle `"()"` | `"()"` |
| 2 | `"()"` | The complete `"()"` | `""` (empty) |

Thus the fixed-point string is empty.

**Example 2**

- Input: `s = "(()(", k = 1`
- Output: `"(("`
- Explanation: Again, the removable string is `"()"`.

| Step | Current `s` | k-balanced occurrence removed | Resulting `s` |
|---:|---|---|---|
| 1 | `"(()("` | The `"()"` at indices 1 and 2 | `"(("` |
| 2 | `"(("` | None | `"(("` |

No further occurrence remains, so the result is `"(("`.

**Example 3**

- Input: `s = "((()))()()()", k = 3`
- Output: `"()()()"`
- Explanation: With `k = 3`, the removable string is `"((()))"`.

| Step | Current `s` | k-balanced occurrence removed | Resulting `s` |
|---:|---|---|---|
| 1 | `"((()))()()()"` | The leading `"((()))"` | `"()()()"` |
| 2 | `"()()()"` | None | `"()()()"` |

The shorter `"()"` groups do not match `k = 3`, so the final string is `"()()()"`.
