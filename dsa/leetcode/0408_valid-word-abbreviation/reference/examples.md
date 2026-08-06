## Examples

**Example 1**

- Input: `word = "internationalization", abbr = "i12iz4n"`
- Output: `true`
- Explanation: The literals `i`, `i`, `z`, and `n` stay in order, while `12` replaces `"nternational"` and `4`
  replaces `"atio"`. Expanding those parts reconstructs `"internationalization"`.

**Example 2**

- Input: `word = "apple", abbr = "a2e"`
- Output: `false`
- Explanation: Replacing two characters after the initial `a` leaves the next literal position at `l`, not `e`, so
  this abbreviation cannot represent `"apple"`.
