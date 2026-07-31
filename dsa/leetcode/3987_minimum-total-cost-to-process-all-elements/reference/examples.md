## Examples

**Example 1**

- Input: `nums = [1,2,3,4], k = 4`
- Output: `3`
- **Explanation:** The initial `4` units leave `3` after processing `nums[0]`, then `1` after `nums[1]`. The next requirement is `3`, so the first operation costs `1`; after adding `4` and processing that element, `1 + 4 - 3 = 2` units remain. The final requirement is `4`, so the second operation costs `2` and raises the resource from `2` to `6`, which is enough. The total cost is `1 + 2 = 3`.

**Example 2**

- Input: `nums = [1,1,7,14], k = 4`
- Output: `15`
- **Explanation:** Processing the first two elements leaves `3` and then `2` units. The requirement `7` needs two operations, whose costs are `1 + 2 = 3`; afterward, `2 + 4 + 4 - 7 = 3` units remain. The requirement `14` then needs three more operations, costing `3 + 4 + 5 = 12`; these raise the resource to `3 + 4 + 4 + 4 = 15`, which is sufficient. The complete cost is `3 + 12 = 15`.

**Example 3**

- Input: `nums = [1,2,3,4], k = 10`
- Output: `0`
- **Explanation:** The initial `10` resource units cover the total requirement, so every element can be processed without an operation and the cost is zero.
