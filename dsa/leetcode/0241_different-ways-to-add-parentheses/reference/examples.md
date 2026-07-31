## Examples

**Example 1**

- Input: `expression = "2-1-1"`
- Output: `[0,2]`
- Explanation: `((2-1)-1) = 0`, while `(2-(1-1)) = 2`.

**Example 2**

- Input: `expression = "2*3-4*5"`
- Output: `[-34,-14,-10,-10,10]`
- Explanation: The five groupings evaluate as follows: `(2*(3-(4*5))) = -34`; `((2*3)-(4*5)) = -14`; `((2*(3-4))*5) = -10`; `(2*((3-4)*5)) = -10`; and `(((2*3)-4)*5) = 10`.
