## Examples

**Example 1**

- Input: `balance = [5,1,-4]`
- Output: `4`
- Explanation:
  - One optimal sequence consists of these four unit transfers:
    1. Send one unit from `i = 1` to `i = 2`, producing `balance = [5, 0, -3]`.
    2. Send one unit from `i = 0` to `i = 2`, producing `balance = [4, 0, -2]`.
    3. Repeat the transfer from `i = 0` to `i = 2`, producing `balance = [3, 0, -1]`.
    4. Transfer once more from `i = 0` to `i = 2`, producing `balance = [2, 0, 0]`.
  - Four moves are therefore sufficient and minimal.

**Example 2**

- Input: `balance = [1,2,-5,2]`
- Output: `6`
- Explanation:
  - The following is one optimal six-move sequence:
    1. Move one unit from `i = 1` to `i = 2`, giving `balance = [1, 1, -4, 2]`.
    2. Do the same again, giving `balance = [1, 0, -3, 2]`.
    3. Move one unit from `i = 3` to `i = 2`, giving `balance = [1, 0, -2, 1]`.
    4. Repeat that transfer, giving `balance = [1, 0, -1, 0]`.
    5. Move one unit from `i = 0` to `i = 1`, giving `balance = [0, 1, -1, 0]`.
    6. Move that unit onward from `i = 1` to `i = 2`, giving `balance = [0, 0, 0, 0]`.
  - The minimum required number of moves is six.

**Example 3**

- Input: `balance = [-3,2]`
- Output: `-1`
- Explanation:
  - The array contains only two positive units in total but has a three-unit deficit. Consequently, it is impossible to make every balance non-negative, so the result is `-1`.
