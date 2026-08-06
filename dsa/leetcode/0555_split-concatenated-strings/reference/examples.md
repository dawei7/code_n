## Examples

**Example 1**

- **Input:** `strs = ["abc","xyz"]`
- **Output:** `"zyxcba"`
- **Explanation:** The four orientation choices produce the loops represented as `-abcxyz-`, `-abczyx-`,
  `-cbaxyz-`, and `-cbazyx-`, where the matching dashes indicate that the ends are connected. The answer comes from
  the fourth loop: opening it at the middle character `'a'` makes the next character the start and yields
  `"zyxcba"`.

**Example 2**

- **Input:** `strs = ["abc"]`
- **Output:** `"cba"`
