## Function Contract

**Inputs**

- `operations`: In cOde(n), an ordered list of `["insert", val]`, `["remove", val]`, and `["getRandom"]` calls.

**Return value**

The app adapter returns one result per call. On LeetCode, construct `RandomizedSet` and invoke its methods directly. Each successful `getRandom` outcome must give every stored value equal probability.
