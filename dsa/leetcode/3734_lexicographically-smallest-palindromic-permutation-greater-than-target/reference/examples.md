## Examples

**Example 1**

- Input: `s = "baba", target = "abba"`
- Output: `"baab"`
- Explanation:

  - In lexicographic order, the palindromic permutations of `s` are `"abba"` and `"baab"`.
  - The smallest one strictly greater than `target` is `"baab"`.

**Example 2**

- Input: `s = "baba", target = "bbaa"`
- Output: `""`
- Explanation:

  - The palindromic permutations are again `"abba"` and `"baab"`, in that order.
  - Neither is strictly greater than `target`, so the result is `""`.

**Example 3**

- Input: `s = "abc", target = "abb"`
- Output: `""`
- Explanation: No permutation of `s` is a palindrome, so no qualifying result exists.

**Example 4**

- Input: `s = "aac", target = "abb"`
- Output: `"aca"`
- Explanation:

  - The only palindromic permutation of `s` is `"aca"`.
  - Because `"aca"` is strictly greater than `target`, it is the answer.
