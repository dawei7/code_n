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

### Required Complexity

- **Time:** $O(C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Assign a collision-free short code**

Maintain an increasing integer counter. The first unseen long URL receives the current counter rendered after a fixed short-domain prefix, then the counter advances. A counter value is never reused, so two different long URLs cannot receive the same short URL.

**Store both lookup directions**

Map each short URL to its long URL for decoding. A reverse map from long URL to short URL lets repeated encoding reuse the existing mapping rather than allocating redundant codes. Although reuse is not required by the platform contract, it makes the local behavior deterministic and economical.

**Decode by exact dictionary lookup**

The short URL is an opaque key; decoding does not need to reverse a hash or inspect the original URL. Looking it up retrieves exactly the value stored when the code was assigned.

**Why round trips and uniqueness hold**

When a new code is created, it is inserted into both maps as one bijective pair. The monotonic counter proves that no other long URL can own that short key. Repeated encodes return the already paired key, and decoding any issued key reads the same stored long URL, so `decode(encode(url))` always equals `url`.

#### Complexity detail

Let `C` be the total number of characters processed and retained across the URLs and operations. Expected hash-map operations are constant time after hashing their string keys, so processing the full trace takes $O(C)$ time and stores $O(C)$ characters. Each individual lookup is expected $O(1)$ aside from reading or hashing the URL string.

#### Alternatives and edge cases

- **Random short codes:** work when collisions are detected and retried, but deterministic counters make collision avoidance explicit.
- **Hash the long URL:** produces compact codes but must handle collisions because different strings can share a hash.
- **List of mappings:** can assign counter codes but linear search for decoding or repeated URLs makes a long trace quadratic.
- **Embed the complete URL:** makes decoding stateless but does not meaningfully shorten the value.
- **Repeated long URL:** may reuse one code; every returned code must still decode correctly.
- **Queries and fragments:** are part of the opaque long URL and must be preserved exactly.
- **Process lifetime:** this in-memory design retains mappings only while the codec instance exists, which matches the challenge interface.

</details>
