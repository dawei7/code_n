## Examples

**Example 1**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `true`
- Explanation: Normalization produces `"amanaplanacanalpanama"`, which is a palindrome.

**Example 2**

- Input: `s = "race a car"`
- Output: `false`
- Explanation: The normalized string is `"raceacar"`, which is not a palindrome.

**Example 3**

- Input: `s = " "`
- Output: `true`
- Explanation: Removing the non-alphanumeric space leaves the empty string `""`. An empty string reads the same forward and backward, so it is a palindrome.
