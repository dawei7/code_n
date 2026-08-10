## General

There may be up to `10^9` possible integers, so constructing a list of every allowed value is not acceptable. The solution instead creates a uniform virtual range of exactly the right size and remaps only the virtual positions that correspond to blacklisted values.

Let:

$$
N=n,\qquad B=\lvert\texttt{blacklist}\rvert,
$$

and define:

$$
k=N-B.
$$

There are exactly `k` allowed values. Each call draws one uniform integer `x` from `[0, k)`. A small dictionary translates certain drawn values into allowed values in the upper part of the original range.

**Splitting the original universe**

Divide `[0, N)` into:

- the low region `[0, k)`, containing exactly `k` positions;
- the high region `[k, N)`, containing exactly `B` positions.

Some low positions may be blacklisted and cannot be returned directly. The key counting fact is that there are exactly enough nonblacklisted high values to replace them.

Suppose `b` blacklisted values lie in the low region. The blacklist has `B-b` values in the high region. Since the high region contains `B` total positions, its allowed count is:

$$
B-(B-b)=b.
$$

So the number of bad low positions equals the number of usable high replacements.

**Building the blacklist set**

`black = set(blacklist)` supports expected constant-time membership tests while searching for high replacements.

This set is not used during `pick`. It exists only during initialization so pointer `i` can skip blacklisted high values efficiently.

**Constructing the remapping**

`i` begins at `k`, the first high-region value.

For every blacklist entry `b`, only entries satisfying `b < k` need a dictionary mapping. A blacklisted high value is never produced by `randrange(k)`, so it needs no key.

For a bad low value, the loop:

`while i in black: i += 1`

advances past unusable high values. The first allowed `i` is assigned:

`d[b] = i`.

Then `i` advances so the same replacement cannot be reused.

Because blacklist values are unique and pointer `i` only moves forward, the dictionary gives every bad low position a distinct allowed high value.

**The pick operation**

`x = randrange(self.k)` makes exactly one random call and gives every integer in `[0, k)` probability `1/k`.

The return expression:

`self.d.get(x, x)`

has two cases:

- If `x` is a blacklisted low value, the dictionary returns its allowed high replacement.
- Otherwise, `x` is an allowed low value and is returned unchanged.

No blacklisted value can be returned.

**Why the distribution is uniform**

The transformation from virtual values `[0, k)` to allowed original values is a bijection:

- every allowed low value maps to itself;
- every blacklisted low position maps to a different allowed high value;
- the counting argument proves all allowed high values needed for the bijection exist.

Each allowed output has exactly one virtual preimage. Since every virtual input is chosen with probability `1/k`, every allowed output also has probability `1/k`.

If two virtual values mapped to one result, that result would be too likely. If an allowed value had no preimage, it would never appear. Distinct pointer assignments and the equal-size counting argument prevent both failures.

**A trace**

Let `n = 7` and `blacklist = [2, 3, 5]`. Then `k = 4`.

The random domain is `[0, 4) = {0, 1, 2, 3}`. Values `2` and `3` are bad low positions.

The high region is `{4, 5, 6}`. Value `5` is blacklisted, leaving `4` and `6` as replacements.

Initialization can build mappings such as:

- `2 -> 4`;
- `3 -> 6`.

Then virtual draws `0, 1, 2, 3` return allowed values `0, 1, 4, 6` respectively. Each has probability one fourth.

**Why blacklist iteration order does not matter**

The input blacklist need not be sorted. Different iteration orders may pair bad low keys with different allowed high values, but every such one-to-one pairing yields the same uniform output set.

The pointer is concerned only with finding distinct allowed high values, not matching a specific replacement to a specific key.

**Why the algorithm is correct**

Initialization maps precisely the blacklisted values that can be randomly drawn, and maps them to distinct legal values that cannot otherwise be drawn directly. Every unlisted virtual value is already legal.

The resulting mapping is a bijection from a uniformly sampled set of size `k` to the legal output set of size `k`. Therefore, every pick is legal and uniformly distributed, using one random call.

## Complexity detail

Let `B` be blacklist length and `P` the number of `pick` calls.

Building the set takes `O(B)` expected time and space. The pointer `i` advances through the high region monotonically; across all mappings, it inspects each high position at most once. The constructor therefore takes `O(B)` expected time.

Each pick performs one random draw and one expected constant-time dictionary lookup:

$$
O(1)
$$

expected time per call, or `O(B+P)` total expected time.

The set and dictionary each contain at most `B` entries, so persistent construction space is

$$
O(B).
$$

The temporary set remains stored only as a local during construction and is released afterward.

## Alternatives and edge cases

- **Materialize all allowed values:** It enables direct random indexing but requires `O(n)` time and space, impossible when `n` is near `10^9`.

- **Rejection sampling:** Repeatedly draw from `[0,n)` until a nonblacklisted value appears. It is uniform but may make many random calls when most values are blacklisted.

- **Sorted blacklist rank mapping:** Binary-search virtual ranks among excluded values. It can avoid a dictionary but makes each pick logarithmic.

- **Empty blacklist:** `k = n`, the dictionary is empty, and every draw returns itself.

- **Only one allowed value:** `k = 1`, `randrange(1)` always draws zero, which either maps to the sole high allowed value or is itself allowed.

- **Blacklisted high values:** They need no dictionary key because the random domain never draws them, but the pointer must skip them as replacements.

- **Blacklisted low values:** Every one must receive a mapping or it could be returned illegally.

- **Unique blacklist guarantee:** It makes the counts and one-to-one construction straightforward; duplicates would distort `k`.

- **One random call:** `randrange(k)` is the only randomized operation per pick.

- **Expected hash-table bounds:** Set and dictionary operations rely on ordinary expected `O(1)` hashing behavior.
