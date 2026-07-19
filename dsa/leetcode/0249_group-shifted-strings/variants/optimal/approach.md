## General
**Encode the shape, not the starting letter**

For each neighboring pair, record how far the second character lies after the first modulo 26. The resulting tuple captures every relative step while ignoring the absolute first letter. Strings of different lengths naturally produce keys of different lengths.

After processing a string, its key records its complete shift-invariant shape, and the hash bucket contains exactly the earlier strings with that shape.

**Equal step sequences are exactly equal shift groups**

A uniform alphabet shift preserves every adjacent modular difference, so shifted strings must share a key. Conversely, suppose two strings share every recorded step. Shift the first string so its first character matches the second; because their first steps agree, their second characters then match, and repeating this argument aligns every later character. Equal keys are therefore sufficient as well as necessary.

## Complexity detail
If `L` is the total number of input characters, building all keys and groups takes $O(L)$ time and space including the returned grouping.

## Alternatives and edge cases
- **Shift each string until it starts with `a`:** is also linear but constructs another normalized string.
- All one-character strings share the empty-difference key; wraparound such as `az` and `ba` is handled modulo 26.
