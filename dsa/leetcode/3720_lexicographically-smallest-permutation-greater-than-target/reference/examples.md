## Examples

**Example 1**

- Input: `s = "abc", target = "bba"`
- Output: `"bca"`
- Explanation: Compare `target` with all permutations in order.
  - The permutations of `s`, in lexicographic order, are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`.
  - The first permutation strictly greater than `"bba"` is `"bca"`.

**Example 2**

- Input: `s = "leet", target = "code"`
- Output: `"eelt"`
- Explanation: The smallest permutation already exceeds the target.
  - The distinct permutations in lexicographic order are `"eelt"`, `"eetl"`, `"elet"`, `"elte"`, `"etel"`, `"etle"`, `"leet"`, `"lete"`, `"ltee"`, `"teel"`, `"tele"`, and `"tlee"`.
  - The first of these, `"eelt"`, is strictly greater than `"code"`, so it is the answer.

**Example 3**

- Input: `s = "baba", target = "bbaa"`
- Output: `""`
- Explanation: The target is already the greatest available permutation.
  - The distinct permutations in lexicographic order are `"aabb"`, `"abab"`, `"abba"`, `"baab"`, `"baba"`, and `"bbaa"`.
  - None is strictly greater than `"bbaa"`; equality is insufficient, so the result is `""`.
