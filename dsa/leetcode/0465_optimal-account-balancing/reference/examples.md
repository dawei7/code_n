## Examples

**Example 1**

- Input: `transactions = [[0, 1, 10], [2, 0, 5]]`
- Output: `2`
- **Explanation:** Person `0` gave person `1` ten dollars, and person `2` gave person `0` five dollars. Two settlement transactions are necessary. For example, person `1` can pay five dollars to person `0` and five dollars to person `2`.

**Example 2**

- Input: `transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]`
- Output: `1`
- **Explanation:** Person `0` gave person `1` ten dollars; person `1` then gave one dollar to person `0` and five dollars to person `2`; finally, person `2` gave five dollars to person `0`. After these transfers are combined, only a four-dollar payment from person `1` to person `0` is needed.
