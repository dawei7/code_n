## General
**A length prefix makes arbitrary content self-delimiting**

Write the decimal character length, a `#` separator, then exactly that many content characters. Lengths make content self-delimiting even when it contains digits, separators, or empty strings.

**Decode headers and payloads with one cursor**

Find the next separator, parse the preceding length, then slice exactly that many characters. Advance the cursor to the next header and repeat.

At each decoding iteration, the cursor points to the first digit of the next length header. Consuming the header and its declared payload moves it to precisely the following header.

**Declared length removes every delimiter ambiguity**

The first `#` after a header start terminates a decimal length, and that length—not any character inside the payload—determines the next boundary. The decoder therefore recovers the exact payload even when it contains `#`, digits, or is empty. Advancing by the declared size restores the header-start position for the next field, so all strings are reconstructed in order.

## Complexity detail
Every content and header character is produced or scanned a constant number of times, for $O(c)$ time and output-sized $O(c)$ space.

## Alternatives and edge cases
- **Join with a sentinel:** fails when content contains the sentinel unless escaping is carefully defined.
- Empty lists, empty strings, separator characters, digits, and Unicode content are all handled by lengths.
