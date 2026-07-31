## Examples

**Example 1**

- Input: `words = ["fusion","layout"]`
- Output: `1`
- Explanation:
  - Apply the operation to `"fusion"` six times. The complete sequence is:
    1. `"fusion"`
    2. `"gvtjpo"`
    3. `"hwukqp"`
    4. `"ixvlrq"`
    5. `"jywmsr"`
    6. `"kzxnts"`
    7. `"layout"`
  - Thus `words[0]` and `words[1]` are similar, so their single index pair contributes `1`.

**Example 2**

- Input: `words = ["ab","aa","za","aa"]`
- Output: `2`
- Explanation:
  - `words[0] = "ab"` and `words[2] = "za"` are similar, giving pair `(0, 2)`.
  - `words[1] = "aa"` and `words[3] = "aa"` are already equal, giving pair `(1, 3)` with zero operations.
  - No other index pair is similar, so the answer is `2`.
