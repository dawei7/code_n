## Function Contract

**Inputs**

- `operations`: In cOde(n), an ordered list of `["inc", key]`, `["dec", key]`, `["getMaxKey"]`, and
  `["getMinKey"]` calls. Every `dec` entry names a currently stored key.

**Return value**

The app adapter constructs one `AllOne` instance, applies the operations in order, and returns the string produced
by each retrieval call. Update calls do not add entries to this returned list. The immutable native artifact exposes
the source-required `AllOne` constructor and four methods directly.
