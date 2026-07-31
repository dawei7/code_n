## Function Contract

**Inputs**

- `node`: App-local serialization of the suffix beginning at the non-tail node passed to the native function.

**Return value**

The native operation returns nothing and mutates the list. The app serializes the suffix after mutation so the removed value and one-node reduction can be judged.
