## Examples

**Example 1**

- Input: `heights = [1,7,9]`
- Output: `181`
- Explanation: The optimal visiting sequence is `[9,1,7]`.

  - The initial jump goes from the ground to `heights[2] = 9`, burning $(0-9)^2=81$ calories.
  - The next jump goes to `heights[0] = 1`, burning $(9-1)^2=64$ calories.
  - The final jump goes to `heights[1] = 7`, burning $(1-7)^2=36$ calories.

  The total is `81 + 64 + 36 = 181` calories.

**Example 2**

- Input: `heights = [5,2,4]`
- Output: `38`
- Explanation: The optimal visiting sequence is `[5,2,4]`.

  - The initial jump goes from the ground to `heights[0] = 5`, burning $(0-5)^2=25$ calories.
  - The next jump goes to `heights[1] = 2`, burning $(5-2)^2=9$ calories.
  - The final jump goes to `heights[2] = 4`, burning $(2-4)^2=4$ calories.

  The total is `25 + 9 + 4 = 38` calories.

**Example 3**

- Input: `heights = [3,3]`
- Output: `9`
- Explanation: The optimal visiting sequence is `[3,3]`.

  - The initial jump goes from the ground to `heights[0] = 3`, burning $(0-3)^2=9$ calories.
  - The next jump goes to `heights[1] = 3`, burning $(3-3)^2=0$ calories.

  The total is `9 + 0 = 9` calories.
