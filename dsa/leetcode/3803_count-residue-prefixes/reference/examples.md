## Examples

**Example 1**

- Input: `s = "abc"`
- Output: `2`
- Explanation:
  - Prefix `"a"` has one distinct character, and its length modulo $3$ is also $1$, so it is a residue.
  - Prefix `"ab"` has two distinct characters, and its length modulo $3$ is $2$, so it is a residue.
  - Prefix `"abc"` does not meet the equality. Therefore the answer is `2`.

**Example 2**

- Input: `s = "dd"`
- Output: `1`
- Explanation:
  - Prefix `"d"` has one distinct character and length modulo $3$ equal to $1$, so it is a residue.
  - Prefix `"dd"` still has one distinct character, whereas its length modulo $3$ is $2$. It is not a residue, leaving an answer of `1`.

**Example 3**

- Input: `s = "bob"`
- Output: `2`
- Explanation:
  - Prefix `"b"` has one distinct character and length modulo $3$ equal to $1$, so it is a residue.
  - Prefix `"bo"` has two distinct characters and length modulo $3$ equal to $2$, so it is also a residue.
  - Prefix `"bob"` does not satisfy the condition. Thus the answer is `2`.
