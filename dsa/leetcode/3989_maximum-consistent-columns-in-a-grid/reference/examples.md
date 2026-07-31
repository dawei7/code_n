## Examples

**Example 1**

- Input: `grid = [[-2,0,3]], limit = 2`
- Output: `2`
- **Explanation:** Remove column `2` and retain columns `0` and `1`. Their only row has `abs(0 - (-2)) = 2`, which is at the inclusive limit. No three-column choice is consistent, so the maximum is `2`.

**Example 2**

- Input: `grid = [[1,-1,1],[2,2,2]], limit = 1`
- Output: `2`
- **Explanation:** Remove column `1` and retain columns `0` and `2`. Their difference is `abs(1 - 1) = 0` in row `0` and `abs(2 - 2) = 0` in row `1`; both meet the limit. Thus two columns can remain, and no valid choice retains all three.

**Example 3**

- Input: `grid = [[-5,5]], limit = 9`
- Output: `1`
- **Explanation:** The two columns differ by `abs(5 - (-5)) = 10`, which is greater than `9`. Either column may remain alone, so the maximum retained count is `1`.
