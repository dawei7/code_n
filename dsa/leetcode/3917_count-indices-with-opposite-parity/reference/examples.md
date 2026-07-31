## Examples

**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[2,1,1,0]`
- **Explanation:** At index `0`, the odd value `1` has the even values at indices `1` and `3` to its right, so its score is `2`. At index `1`, the even value `2` has only the odd value at index `2` later, giving `1`. At index `2`, the odd value `3` is followed by the even value at index `3`, also giving `1`. Index `3` has no later position, so its score is `0`. These scores form `[2, 1, 1, 0]`.

**Example 2**

- Input: `nums = [1]`
- Output: `[0]`
- **Explanation:** A one-element array has no index to the right of index `0`, so its only score is `0`.
