## Function Contract

**Inputs**

- `operations`: In cOde(n), an ordered list of `["insert", val]`, `["remove", val]`, and `["getRandom"]` calls.

**Return value**

The app adapter returns one result per call. On LeetCode, construct `RandomizedCollection` and call its methods directly. Removal affects only one matching occurrence.
