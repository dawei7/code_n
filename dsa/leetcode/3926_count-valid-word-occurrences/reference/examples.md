## Examples

**Example 1**

- Input: `chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]`
- Output: `[2,1,0]`
- Explanation: Concatenation creates `s = "hello world hello"`, whose complete words are `"hello"`, `"world"`, and `"hello"`.

The two `"hello"` words and one `"world"` word are counted. Although `"wor"` occurs inside `"world"`, it is not a maximal word and therefore contributes zero.

**Example 2**

- Input: `chunks = ["a-b a--b ","a-","b"], queries = ["a-b","a","b"]`
- Output: `[2,1,1]`
- Explanation: Concatenating the four chunks gives `s = "a-b a--b a-b"`.

In each copy of `"a-b"`, the hyphen lies directly between two lowercase letters and joins the whole substring into one word. In `"a--b"`, neither hyphen has letters on both sides, so they are separators and leave the separate words `"a"` and `"b"`. The word sequence is thus `"a-b"`, `"a"`, `"b"`, `"a-b"`.

**Example 3**

- Input: `chunks = ["-cat dog- mouse"], queries = ["cat","dog","mouse","cat-dog"]`
- Output: `[1,1,1,0]`
- Explanation: The leading hyphen before `"cat"` and trailing hyphen after `"dog"` lack a lowercase letter on one side and therefore act as separators.

The complete words are `"cat"`, `"dog"`, and `"mouse"`; no word equals `"cat-dog"`.
