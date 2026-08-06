## Examples

**Example 1**

- Input: `d = 1, low = 1, high = 13`
- Output: `6`
- Explanation: The digit `1` appears in `1`, `10`, `11`, `12`, and `13`. It occurs twice in `11`, so those five contributing numbers contain six occurrences altogether.

**Example 2**

- Input: `d = 3, low = 100, high = 250`
- Output: `35`
- Explanation: There are 35 written occurrences of `3` in the interval. The source illustrates the contributing numbers with `103`, `113`, `123`, `130`, `131`, …, `238`, `239`, and `243`.

**Additional Examples**

**Digit zero without leading placeholders**

- Input: `d = 0, low = 1, high = 10`
- Output: `1`

Only the ones position of `10` is a written zero. The one-digit values do not contribute an unwritten tens-place zero.
