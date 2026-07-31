## Examples

**Example 1**

- Input: `s = "cooear"`
- Output: `2`
- Explanation:
  - The four vowels are `('o', 'o', 'e', 'a')`, so `v = 4`.
  - The two consonants are `('c', 'r')`, so `c = 2`.
  - Thus `floor(v / c) = floor(4 / 2) = 2`.

**Example 2**

- Input: `s = "axeyizou"`
- Output: `1`
- Explanation:
  - The five vowels are `('a', 'e', 'i', 'o', 'u')`, so `v = 5`.
  - The three consonants are `('x', 'y', 'z')`, so `c = 3`.
  - Therefore `floor(v / c) = floor(5 / 3) = 1`.

**Example 3**

- Input: `s = "au 123"`
- Output: `0`
- Explanation:
  - The string contains no consonants, so `c = 0`.
  - The zero-consonant rule makes the score `0`.
