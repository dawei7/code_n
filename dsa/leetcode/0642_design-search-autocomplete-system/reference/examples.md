## Examples

**Example 1**

- **Input:** `["AutocompleteSystem", "input", "input", "input", "input"] [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]`
- **Output:** `[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]`
- **Explanation:** Construct the system with the four listed sentences and frequencies. After typing `i`, all four histories match. `iroman` and `i love leetcode` both have hot degree `2`, but the space character has ASCII code `32` while `r` has ASCII code `114`, so `i love leetcode` ranks first; because only three suggestions are returned, `iroman` is omitted. After the following space, only `i love you` and `i love leetcode` match `i `. Typing `a` leaves no history matching `i a`. Finally, `#` returns an empty list, stores `i a` as a historical sentence, and resets the state so the next character begins a new search.
