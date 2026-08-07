## Function Contract

**Inputs**

- `operation`: Either `"encode"` or `"decode"` in the offline app adapter.
- `value`: A list of strings for encoding, or a previously encoded string for decoding.

For encoding, let $c$ include all payload characters and decimal length-header characters. For decoding, let $c$ be
the encoded string's length.

**Return value**

For `"encode"`, return the codec's transport string. For `"decode"`, return the represented list of strings. The native interface exposes `Codec.encode(strs)` and `Codec.decode(s)` directly.
