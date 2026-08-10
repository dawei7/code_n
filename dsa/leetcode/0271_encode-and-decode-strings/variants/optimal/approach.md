## General

**A reversible encoding must preserve boundaries**

Concatenating the input strings directly loses information. For example, both `["ab", "c"]` and `["a", "bc"]` would become `"abc"`. The decoder would know the characters but not where one original string ended and the next began.

A plain delimiter does not solve the general problem either. Each input string may contain any of the 256 valid ASCII characters, so any ASCII delimiter chosen by the codec could also occur naturally inside a payload. Splitting at every occurrence would then create false boundaries.

The reliable solution is length-prefixed framing. Before each payload, encode its exact character count in a header whose extent the decoder knows. The decoder reads the header first and then consumes exactly the stated number of payload characters. Payload contents never need to be inspected for separators, so digits, spaces, punctuation, control characters, and delimiter-like sequences are harmless.

The exact protected source uses a fixed-width four-character decimal header. It does not use the separator mentioned in the variant summary. The legal maximum payload length is 200, so every length fits comfortably in four decimal columns.

**Understand the four-character header exactly**

For a payload `s`, the encoder creates `"{:4}".format(len(s)) + s`. The formatting field has width four and right-aligns the decimal length, padding unused columns on the left with spaces:

| Payload | Length | Four-character header | Complete chunk |
|---|---:|---|---|
| `"Hello"` | 5 | `"   5"` | `"   5Hello"` |
| `"World"` | 5 | `"   5"` | `"   5World"` |
| `""` | 0 | `"   0"` | `"   0"` |
| a 200-character string | 200 | `" 200"` | header followed by 200 characters |

The spaces are structural padding in the header, not payload characters. Python's `int` accepts surrounding whitespace, so decoding `int("   5")` produces `5`.

The width specification is a minimum width rather than a maximum. A length of 10000 would format as five characters, not be truncated. The decoder always reads exactly four header characters, so such a payload would break this format. That is not a legal input here: the source is correct because the constraint `len(strs[i]) <= 200` guarantees every header is exactly four characters. A generalized unbounded format would need a separator, a larger agreed fixed width, or a different self-delimiting integer encoding.

**Encode as a sequence of self-contained chunks**

The encoder initializes an empty list `ans`. For every input string, it appends one chunk consisting of the four-character length header followed immediately by the unchanged payload. Finally, `"".join(ans)` concatenates all chunks into the transport string.

Building a list and joining once matters in Python. Strings are immutable, so repeatedly extending one growing encoded string can repeatedly copy its existing contents. Collecting chunks and joining them lets Python allocate and assemble the final result efficiently.

No escaping or payload transformation occurs. That makes the format easy to reason about: the character at each payload position is exactly the original character. The only added characters are the four header columns per list element.

For `["Hello", "World"]`, the conceptual encoded value is

```text
   5Hello   5World
```

The visual spaces before each `5` are real header padding. There is no separator between `Hello` and the next header; the first header's length tells the decoder exactly where `Hello` ends, so the next four characters must begin the following header.

**Decode with a cursor and the same framing agreement**

The decoder uses `i` as the index of the next unread header and `n` as the encoded string length. While `i < n`, it performs four steps:

1. Read `s[i : i + 4]`, the fixed four-character header.
2. Convert that header to integer `size`.
3. Move `i` forward by four, so it points at the payload's first character.
4. Append `s[i : i + size]`, then move `i` forward by `size` to the next header.

This is a framing protocol: both sender and receiver agree that every record begins with four header characters and that the header determines the following record length. The decoder never searches for a special character, so payload contents cannot interfere with cursor movement.

**Why empty strings remain distinguishable**

An empty payload still contributes a header: `"   0"`. The decoder reads size zero, appends the empty slice, and advances by zero payload characters. It has nevertheless already advanced four positions past the header, so the loop makes progress.

This distinguishes several cases that naïve concatenation cannot distinguish:

- `[""]` encodes to one zero-length header;
- `["", ""]` encodes to two consecutive zero-length headers;
- a hypothetical empty list encodes to the empty transport string.

Decoding those transport values yields one empty string, two empty strings, and an empty list respectively. List cardinality is therefore preserved even when payloads contain no characters.

**Why payloads containing digits or spaces are safe**

Suppose a payload begins with `"  12"` or contains four characters that look exactly like a header. Those characters occur after the real header. Once the decoder has read the declared size, it takes the next `size` characters as opaque payload data. It does not attempt to parse another header until the cursor has crossed that entire payload.

Likewise, a payload may contain null characters, line breaks, or every possible ASCII symbol. Length-based slicing, rather than content-based splitting, decides the boundary. The codec therefore handles the full stated character set without reserving any character.

**Why decoding reverses encoding**

Each encoded chunk has the form `header(length(payload)) + payload`. At the start of a decoding iteration, assume `i` points to a chunk's header. The first four characters decode to the exact payload length because that is how the encoder formatted them. Advancing four reaches the payload start; slicing exactly that many characters recovers the whole payload and nothing from the following chunk. Advancing by that length reaches the next chunk header.

This argument repeats for every chunk. The cursor starts at the first header and ends exactly after the last payload, so decoded strings appear in the original order with their exact contents and multiplicity. Hence `decode(encode(strs)) == strs` for every legal input.

The decoder assumes its input was produced by the matching encoder, as the contract states. It does not validate malformed or truncated transport data. Protocol validation could be added in a production system, but it is separate from proving the required round trip.

## Complexity detail

Let $k$ be the number of input strings, let $P$ be the total number of payload characters, and let

$$
C = P + 4k
$$

be the encoded length. This matches the contract's intent that the encoded representation includes payload and header characters.

Encoding obtains each length, formats a constant-width header, stores one chunk per string, and joins all chunk characters once. Across all strings, this takes $O(C)$ time. The chunk list and final encoded string contain $O(C)$ characters or references, so encoding uses $O(C)$ space including its required output.

Decoding advances its cursor monotonically from zero to $C$. It reads each four-character header and copies each payload slice once. The total time is $O(C)$. The returned strings collectively contain $P$ characters and the result list has $k$ entries, so output storage is $O(P+k)=O(C)$. Apart from that output, the cursor, length, size, and temporary header state require $O(1)$ scalar space; Python payload slices themselves become the returned string objects.

The transport format adds exactly four characters per input element, so its framing overhead is $4k$ characters. Under the legal maximum length 200, header processing is constant time per string. The manifest's $O(c)$ time and $O(c)$ space bounds are therefore accurate when $c$ denotes the relevant total representation size.

## Alternatives and edge cases

- **Variable-length header plus separator:** Encode `str(len(payload))`, a non-digit separator such as `#`, and the payload. The decoder scans digits to the separator and then consumes the declared payload length. This supports lengths beyond four digits and remains safe even if `#` occurs in the payload, because the decoder searches for it only while reading the numeric header.
- **Escaped delimiter:** Reserve a terminator and escape every occurrence of the terminator and escape character inside payloads. This can work, but the encoder and decoder need more cases, and expansion depends on payload contents. Length framing is simpler here.
- **Non-ASCII delimiter:** Choosing a character outside the stated ASCII payload domain is tempting, but transport systems may normalize or encode Unicode differently, and the generalized follow-up allows no permanently safe delimiter. Length prefixes avoid that dependency.
- **Serialization helpers:** Formats such as JSON could represent the list, but the problem explicitly forbids solving it with serialization methods. The custom framing scheme demonstrates the required algorithm.
- **Empty payload:** It produces header `"   0"`; decoding appends `""` and continues correctly without consuming payload characters.
- **Several adjacent empty payloads:** Each has its own four-character header, so they remain separate list elements rather than collapsing together.
- **Payload containing header-like text:** Four digits or padded numbers inside a payload are never interpreted as headers because the cursor skips exactly the declared payload length first.
- **Payload containing any ASCII character:** No ASCII character is reserved, escaped, removed, or normalized. Boundaries depend only on lengths.
- **Maximum legal payload:** Length 200 formats as exactly four characters, `" 200"`, and decoding consumes the following 200 characters.
- **Length above 9999 outside the contract:** `{:4}` would emit more than four characters while the decoder would still read four. A generalized implementation must replace this fixed-width assumption rather than silently accepting such input.
- **Malformed encoded input:** A short or nonnumeric header makes `int(...)` fail, while an overstated size can yield a short slice. The required decoder receives its own encoder's output, so error detection and checksums are outside this contract.
- **Hypothetical empty input list:** Although the stated list has at least one element, the encoder returns `""` and the decoder returns `[]`, so the round trip extends naturally to this case.
- **Unicode generalization within Python:** `len` and slicing both count Python string code points consistently, so the same in-process codec can round-trip characters beyond ASCII as long as payload lengths remain at most four digits. A byte-oriented network protocol should instead define lengths in encoded bytes and use the same character encoding at both endpoints.
