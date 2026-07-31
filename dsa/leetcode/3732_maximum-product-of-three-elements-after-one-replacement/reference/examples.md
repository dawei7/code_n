## Examples

**Example 1**

- Input: `nums = [-5,7,0]`
- Output: `3500000`
- Explanation: Replace `0` with $-10^5$, producing `[-5,7,-10^5]`. The product is `(-5) * 7 * (-10^5) = 3500000`, which is maximal.

**Example 2**

- Input: `nums = [-4,-2,-1,-3]`
- Output: `1200000`
- Explanation: Two replacements that attain the maximum are:

  - Select `[-4,-2,-3]`, replace `-2` with $10^5$, and obtain `(-4) * 10^5 * (-3) = 1200000`.
  - Select `[-4,-1,-3]`, replace `-1` with $10^5$, and again obtain `(-4) * 10^5 * (-3) = 1200000`.

  Thus the maximum product is `1200000`.

**Example 3**

- Input: `nums = [0,10,0]`
- Output: `0`
- Explanation: The array has exactly three elements. Replacing either zero still leaves the other zero among the three required factors, while replacing `10` leaves both zeros. Every possible product is therefore `0`.
