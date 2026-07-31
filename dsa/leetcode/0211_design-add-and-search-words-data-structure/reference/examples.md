## Examples

**Example 1**

- Input: `["WordDictionary","addWord","addWord","addWord","search","search","search","search"], [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]`
- Output: `[null,null,null,null,false,true,true,true]`
- Explanation: The three additions persist. `"pad"` has no match, `"bad"` matches exactly, and each dot in the final two queries stands for one arbitrary letter.

| Call | Result |
|---|---:|
| `WordDictionary()` | `null` |
| `addWord("bad")` | `null` |
| `addWord("dad")` | `null` |
| `addWord("mad")` | `null` |
| `search("pad")` | `false` |
| `search("bad")` | `true` |
| `search(".ad")` | `true` |
| `search("b..")` | `true` |
