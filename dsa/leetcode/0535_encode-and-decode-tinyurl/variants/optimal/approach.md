## General

The contract requires a reversible mapping created and used by the same object. It does not require the short code to be derived from the long URL, so the solution assigns each encoded URL a new increasing integer identifier and stores the association in memory.

The object maintains three fields:

- `self.idx` is the number assigned most recently, starting at zero;
- `self.m` maps an identifier string to its original long URL;
- `self.domain` is the fixed prefix `"https://tinyurl.com/"`.

**Encode with a fresh identifier.** Each call to `encode` first increments `self.idx`. Therefore the first call receives identifier one, the next receives two, and so on.

The counter is monotonically increasing for the lifetime of the object. Two encode calls never receive the same numeric identifier, even if they contain equal or different long URLs. This uniqueness makes the mapping unambiguous.

The code stores:

`self.m[str(self.idx)] = longUrl`.

The dictionary key is the decimal string form of the counter because that same text will appear at the end of the short URL. The value is the exact original URL, including its scheme, path, query, and any other valid URL characters.

It then returns:

`f'{self.domain}{self.idx}'`.

For the first call, this is `"https://tinyurl.com/1"`. The visible numeric suffix is only a lookup key; it does not need to encode the long URL's characters itself because the dictionary retains the information.

**Decode by recovering the suffix.** The contract guarantees that `shortUrl` was produced by the same object. The expression:

`shortUrl.split('/')[-1]`

splits the short URL at slash characters and selects the final component. For a generated URL ending in `/17`, this yields identifier string `"17"`.

The dictionary access `self.m[idx]` returns the exact long URL stored during the corresponding encode call.

**Why round-trip recovery is exact.** Suppose an encode call receives long URL `u` and assigns current counter `c`. It stores `m[str(c)] = u` and returns the fixed domain followed by `c`. Decoding that returned string extracts exactly `str(c)` and looks up the value `u`. Therefore:

`decode(encode(u)) == u`.

The proof does not depend on the content or length of `u` because it is stored rather than transformed.

**Why identifiers cannot collide.** Before each assignment the counter increases by one, and no operation decreases or resets it. Distinct encode calls use distinct positive integers. Decimal representations of distinct integers are distinct strings, so no new mapping overwrites an earlier mapping.

If the same long URL is encoded twice, this implementation creates two different short URLs that both decode to the same original. The problem does not require deduplicating repeated inputs, so this remains valid. A reverse map could reuse an existing code, but it is not necessary for correctness.

The use of `defaultdict()` without a factory behaves like a regular dictionary for these operations. Encoding assigns explicit keys, and decoding uses bracket lookup. The guarantee that every decoded short URL came from this object means lookup never needs a default value.

**State belongs to one codec instance.** The mapping is not global or persistent. A short URL from one object is not guaranteed to decode in another object because that other dictionary may associate the same suffix with a different long URL or no value. This matches the explicit same-object guarantee.

The domain text itself carries no decoding information beyond separating the suffix. The implementation trusts the supplied short URL guarantee and does not validate that its prefix equals `self.domain`.

For a sequence encoding `u1` and `u2`, the object returns suffixes one and two and stores two entries. Decoding the first later still returns `u1` because later insertions use different keys and do not alter entry one.

This design favors simplicity and deterministic uniqueness. It avoids random-code collision handling, hashing collisions, and variable-length base conversion, at the cost of maintaining an in-memory table and exposing sequential identifiers.

## Complexity detail

Let $L$ be the long URL length, $T$ the generated short URL length, and $C$ the number of encode calls stored in this object. Dictionary insertion and lookup are expected $O(1)$ with respect to entry count, while creating strings and splitting text costs time proportional to the involved string length.

An encode call stores the URL reference and creates a suffix/short string, taking expected $O(T)$ formatting time under a precise string-cost model. A decode call's `split` scans and allocates pieces from the short URL, taking $O(T)$ time and temporary space. Since $T$ grows only logarithmically with the counter and is usually treated as a small code length, these operations are often described as expected constant time per call.

Across $C$ distinct assigned identifiers, the dictionary has $O(C)$ entries, matching the manifest's entry-count interpretation of $O(C)$ space. Counting the retained URL text itself, storage is proportional to the total length of all encoded long URLs.

## Alternatives and edge cases

- **Random fixed-length code:** It hides sequential counts but must detect and retry collisions before storing a mapping.
- **Hash-derived code:** It is deterministic from the URL but still needs collision resolution because different URLs can share a hash.
- **Base-62 counter encoding:** It shortens large numeric identifiers while preserving collision-free sequential assignment.
- **Reverse URL map:** It can make repeated encoding of the same long URL return the same short URL, but consumes additional storage.
- **Repeated long URL:** This implementation assigns a fresh key each time; both keys decode correctly.
- **Long URL containing slashes:** It is stored only as a dictionary value, so its internal slashes do not affect suffix extraction.
- **First encode:** Increment-before-use assigns identifier one rather than zero.
- **Many encode calls:** Integer identifiers remain unique; Python integers do not overflow.
- **Decode before encode or foreign short URL:** The contract excludes these cases; ordinary dictionary lookup would raise an error.
- **Same-object guarantee:** It is essential because mappings are held only in instance memory.
- **Process restart:** No persistence is implemented, which is acceptable for this in-memory problem contract.
