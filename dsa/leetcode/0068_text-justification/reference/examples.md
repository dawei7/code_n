## Examples

**Example 1**

- Input: `words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16`
- Output: `["This    is    an", "example  of text", "justification.  "]`

**Example 2**

- Input: `words = ["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth = 16`
- Output: `["What   must   be", "acknowledgment  ", "shall be        "]`
- Explanation: The final line is `"shall be        "`, including trailing padding, because final lines are left-justified rather than fully justified. The one-word second line is also left-justified, so its padding follows the word.

**Example 3**

- Input: `words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth = 20`
- Output: `["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]`
