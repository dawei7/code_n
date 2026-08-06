## Examples

**Example 1**

- Input: `target = "apple", dictionary = ["blade"]`
- Output: `"a4"`
- Explanation: The shortest abbreviation of `"apple"` is the length-$1$ abbreviation `"5"`, but it also
  abbreviates `"blade"`. At length $2$, both `"a4"` and `"4e"` abbreviate `"apple"`, but `"4e"` also
  abbreviates `"blade"`; therefore, `"a4"` is a shortest valid answer.

**Example 2**

- Input: `target = "apple", dictionary = ["blade", "plain", "amber"]`
- Output: `"1p3"`
- Explanation: The length-$1$ abbreviation `"5"` represents all of `"apple"`, but it also abbreviates every listed
  dictionary word. The abbreviation `"a4"` also abbreviates `"amber"`, and `"4e"` also abbreviates `"blade"`.
  The next shortest possibilities are `"1p3"`, `"2p2"`, and `"3l1"`; none abbreviates a dictionary word, so any
  of them is acceptable.
