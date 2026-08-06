## Examples

**Example 1**

- Input: `text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]`
- Output: `[[3,7],[9,13],[10,17]]`

**Example 2**

- Input: `text = "ababa", words = ["aba","ab"]`
- Output: `[[0,1],[0,2],[2,3],[2,4]]`
- Explanation: The occurrences of `"aba"` occupy `[0,2]` and `[2,4]`, while the occurrences of `"ab"` occupy `[0,1]` and `[2,3]`. The reported pairs include both overlaps and are ordered by start index and then end index.

**Additional Examples**

**No matching word**

- Input: `text = "abc", words = ["d"]`
- Output: `[]`
- Explanation: No supplied word occurs in `text`, so there are no index pairs to return.
