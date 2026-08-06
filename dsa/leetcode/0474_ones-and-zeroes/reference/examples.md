## Examples

**Example 1**

- Input: `strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3`
- Output: `4`
- Explanation: The four strings `"10"`, `"0001"`, `"1"`, and `"0"` fit both budgets, giving a largest valid
  subset. Smaller valid choices include `{"0001", "1"}` and `{"10", "1", "0"}`. The one-element choice
  `{"111001"}` is invalid because that string alone contains four ones, exceeding the budget of three.

**Example 2**

- Input: `strs = ["10", "0", "1"], m = 1, n = 1`
- Output: `2`
- Explanation: Selecting `"0"` and `"1"` uses exactly one zero and one one, and no valid subset can contain more
  strings.
