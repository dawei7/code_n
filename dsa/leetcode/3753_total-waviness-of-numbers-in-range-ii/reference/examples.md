## Examples

**Example 1**

- Input: `num1 = 120, num2 = 130`
- Output: `3`
- Explanation:

  Within `[120,130]`:

  - In `120`, the middle digit `2` is a peak, so its waviness is `1`.
  - In `121`, the middle digit `2` is a peak, so its waviness is `1`.
  - In `130`, the middle digit `3` is a peak, so its waviness is `1`.
  - Every other number in the range has waviness `0`.

  Thus, the total is `1 + 1 + 1 = 3`.

**Example 2**

- Input: `num1 = 198, num2 = 202`
- Output: `3`
- Explanation:

  Within `[198,202]`:

  - In `198`, the middle digit `9` is a peak, so its waviness is `1`.
  - In `201`, the middle digit `0` is a valley, so its waviness is `1`.
  - In `202`, the middle digit `0` is a valley, so its waviness is `1`.
  - Every other number in the range has waviness `0`.

  Thus, the total is `1 + 1 + 1 = 3`.

**Example 3**

- Input: `num1 = 4848, num2 = 4848`
- Output: `2`
- Explanation: In `4848`, the second digit `8` is a peak and the third digit `4` is a valley. The number's waviness is therefore `2`, which is also the one-value range total.
