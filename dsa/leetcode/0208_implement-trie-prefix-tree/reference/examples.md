## Examples

**Example 1**

- Input: `["Trie","insert","search","search","startsWith","insert","search"], [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]`
- Output: `[null,null,true,false,true,null,true]`
- Explanation: The calls operate on the same trie in sequence. Inserting `"apple"` makes it both searchable and a witness for prefix `"app"`, but `"app"` itself becomes searchable only after it is inserted.

| Call | Result | Reason |
|---|---:|---|
| `Trie()` | `null` | Create an empty trie. |
| `insert("apple")` | `null` | Store the complete word. |
| `search("apple")` | `true` | `"apple"` was inserted. |
| `search("app")` | `false` | A prefix is not automatically a stored word. |
| `startsWith("app")` | `true` | The stored word `"apple"` begins with this prefix. |
| `insert("app")` | `null` | Store the shorter word as a complete word. |
| `search("app")` | `true` | `"app"` is now present as a complete word. |
