## Examples

**Example 1**

- Input: `s = ")ebc#da@f("`
- Output: `"(fad@cb#e)"`
- Explanation:
  - Reading only the letters gives `['e', 'b', 'c', 'd', 'a', 'f']`.
    - Reversing that sequence gives `['f', 'a', 'd', 'c', 'b', 'e']`.
    - Placing those values back into the letter positions changes `s` to `")fad#cb@e("`.
  - The special-character sequence is `[')', '#', '@', '(']`.
    - Its reversal is `['(', '@', '#', ')']`.
    - Filling the special-character positions with that reversed sequence produces `"(fad@cb#e)"`.

**Example 2**

- Input: `s = "z"`
- Output: `"z"`
- Explanation: The only character is a letter, so reversing the one-element letter sequence changes nothing. There are no special characters to reverse.

**Example 3**

- Input: `s = "!@#$%^&*()"`
- Output: `")(*&^%$#@!"`
- Explanation: There are no letters. Every character is special, so the second operation reverses the entire string.
