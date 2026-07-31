## Examples

**Example 1**

- Input: `s = "leetcode"`
- Output: `"leetcedo"`
- **Explanation:** The vowel sequence is `['e', 'e', 'o', 'e']`. Its frequencies are `e = 3` and `o = 1`, so all three copies of `'e'` precede `'o'`. Writing `['e', 'e', 'e', 'o']` into the original vowel positions produces `"leetcedo"`.

**Example 2**

- Input: `s = "aeiaaioooa"`
- Output: `"aaaaoooiie"`
- **Explanation:** The input vowels are `['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a']`. Their frequencies are `a = 4`, `o = 3`, `i = 2`, and `e = 1`; descending frequency therefore gives `['a', 'a', 'a', 'a', 'o', 'o', 'o', 'i', 'i', 'e']`, which is `"aaaaoooiie"`.

**Example 3**

- Input: `s = "baeiou"`
- Output: `"baeiou"`
- **Explanation:** Every vowel occurs once. Their frequencies tie, so their first-occurrence order is `'a'`, `'e'`, `'i'`, `'o'`, `'u'`. That is already their order in the vowel positions, and the string does not change.
