# Encode and Decode TinyURL

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 535 |
| Difficulty | Medium |
| Topics | Hash Table, String, Design, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-and-decode-tinyurl/) |

## Problem Description
### Goal
Design a TinyURL codec with two operations. `encode(longUrl)` converts an arbitrary long URL into a shorter URL, and `decode(shortUrl)` must recover exactly the original long URL associated with that encoded value.

The short-code format and storage strategy are implementation-defined, but active mappings must not collide or decode to the wrong destination. Preserve enough persistent state across calls for every issued short URL to remain reversible. The task does not require validating or fetching network content; correctness is the identity `decode(encode(url)) = url` for supplied URLs.

### Function Contract
**Inputs**

- `long_urls`: for the app adapter, the chronological URLs passed to `encode`
- `decode_order`: indices selecting which generated short URLs are then passed to `decode`

**Return value**

- The app adapter returns the generated short URLs and the decoded long URLs; the native interface exposes `Codec.encode(longUrl)` and `Codec.decode(shortUrl)`

### Examples
**Example 1**

- Input: `long_urls = ["https://leetcode.com/problems/design-tinyurl"], decode_order = [0]`
- Output: `short_urls = ["https://tinyurl.com/0"], decoded_urls = ["https://leetcode.com/problems/design-tinyurl"]`

**Example 2**

- Input: `long_urls = ["https://example.com/a", "https://example.com/b"], decode_order = [1, 0]`
- Output: `short_urls = ["https://tinyurl.com/0", "https://tinyurl.com/1"], decoded_urls = ["https://example.com/b", "https://example.com/a"]`

**Example 3**

- Input: the same long URL is encoded twice
- Output: the deterministic app codec reuses its existing short URL, and either occurrence decodes correctly
