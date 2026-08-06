## Examples

**Example 1**

- Input: `prices = ["0.700","2.800","4.900"], target = 8`
- Output: `"1.000"`
- Explanation: Choose floor, ceiling, and ceiling, respectively. The resulting error is $(0.7-0)+(3-2.8)+(5-4.9)=0.7+0.2+0.1=1.0$.

**Example 2**

- Input: `prices = ["1.500","2.500","3.500"], target = 10`
- Output: `"-1"`
- Explanation: No permitted combination of floors and ceilings reaches the target.

**Example 3**

- Input: `prices = ["1.500","2.500","3.500"], target = 9`
- Output: `"1.500"`
