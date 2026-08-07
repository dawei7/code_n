## Function Contract

**Inputs**

- `operations`: App-local commands of the form `["insert", word]`, `["search", word]`, or `["startsWith", prefix]`, processed against one initially empty trie.

**Return value**

Return the boolean result of every `search` and `startsWith` command in command order; `insert` commands produce no result.
