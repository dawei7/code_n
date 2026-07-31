## General

**Reduce each value to one parity bit**

For an integer $x$, let $p(x)$ be the parity of its set-bit count: zero for an even count and one for an odd count. At every binary position, XOR is addition modulo two. Taking parity across all positions therefore gives

$$
p(x \mathbin{\mathrm{XOR}} y)=p(x)\mathbin{\mathrm{XOR}}p(y).
$$

Extending the identity to three values means the triplet XOR has an even set-bit count exactly when `p(a[i]) XOR p(b[j]) XOR p(c[k])` is zero. The actual XOR value is irrelevant once each element's parity is known.

**Count the four successful parity patterns**

Scan each array once and count values with even and odd popcount parity. Write these counts as $E_a,O_a,E_b,O_b,E_c,O_c$. Three parity bits XOR to zero when either none or exactly two are odd. Thus the answer is

$$
E_aE_bE_c + E_aO_bO_c + O_aE_bO_c + O_aO_bE_c.
$$

Each product independently chooses one index from the three required parity classes. The four patterns are disjoint and exhaust every parity triple with XOR zero, so their sum counts every valid index triplet exactly once. Counting indices rather than distinct values also handles duplicates correctly.

## Complexity detail

Computing popcount parity for every input value takes $O(A+B+C)$ time. Values are at most $100$, and Python's integer `bit_count` is constant time over this bounded domain. Six counters and a fixed number of products use $O(1)$ auxiliary space.

The result can be as large as $ABC=10^6$, which fits comfortably in the supported integer types.

## Alternatives and edge cases

- **Enumerate every triplet:** Directly computing all $ABC$ XOR values is simple and matches the official hint, but it takes $O(ABC)$ time.
- **Pair-parity aggregation:** First count even and odd XOR parity among pairs from two arrays, then combine with the third. This is correct but still unnecessary because the pair counts can be derived directly from the six single-array counters.
- **Full XOR frequency table:** Counting every possible XOR value uses more state than needed because only popcount parity affects acceptance.
- **Zero:** Its set-bit count is zero, which is even.
- **Repeated values:** Equal values at different indices remain different triplet choices and must all be counted.
- **All-even classes:** If every value has even popcount parity, all $ABC$ triplets qualify.
- **All-odd classes:** Three odd parities XOR to odd, so no triplet qualifies.
- **Two odd arrays:** If every value in exactly two arrays has odd parity and the third is even, every triplet qualifies.
- **Set-bit count versus numeric parity:** Whether a value is numerically even does not determine whether its binary representation has an even number of ones.
