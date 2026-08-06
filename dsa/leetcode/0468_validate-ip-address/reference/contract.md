## Function Contract

**Inputs**

- `queryIP`: The candidate address string.

**Return value**

- Return exactly `"IPv4"`, `"IPv6"`, or `"Neither"` according to the full-form grammars in the description.

IPv6 compression such as `::` is not part of the accepted grammar because all eight fields must be present and nonempty.
