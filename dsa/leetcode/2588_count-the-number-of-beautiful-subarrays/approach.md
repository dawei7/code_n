## General

**Analyze each bit independently**

An operation chooses a bit position $k$ that is one in two different elements and subtracts $2^k$ from both.

When bit $k$ of a nonnegative integer is one, subtracting $2^k$ clears exactly that bit without borrowing from higher bits or changing lower bits. Therefore, every operation removes two occurrences of one from the same bit position across the subarray.

For all values to become zero, every set-bit occurrence must be paired with another occurrence at the same position. A subarray is beautiful exactly when the number of ones is even at every bit position.

**Why even bit counts are also sufficient**

If every bit position contains an even number of ones, take any bit $k$ and pair its set occurrences arbitrarily. Apply one operation to each pair. This clears bit $k$ from every element.

Operations for one bit do not change other bit positions, so repeat independently for every bit. Eventually every set bit is cleared and all elements become zero.

Thus even parity at every bit is both necessary and sufficient, not merely a useful test.

**XOR stores all bit parities at once**

At each bit position, XOR is one exactly when an odd number of operands have that bit set. Therefore, the XOR of all elements in a subarray is zero exactly when every bit has even parity.

The operational definition of beautiful subarrays collapses to:

$$
\text{subarray is beautiful}
\quad\Longleftrightarrow\quad
\text{subarray XOR}=0.
$$

This transformation is the main insight. No operation sequence needs to be simulated.

**Convert subarray XOR into equal prefix XORs**

Let $P_r$ be the XOR of elements from index zero through $r$, and define the empty prefix $P_{-1}=0$.

The XOR of subarray $[l,r]$ is

$$
P_r\mathbin{\char94}P_{l-1}.
$$

XORing a value with itself gives zero, so this subarray XOR equals zero exactly when

$$
P_r=P_{l-1}.
$$

Every beautiful subarray therefore corresponds to a pair of equal prefix-XOR values: one prefix boundary before the subarray and one at its end.

**Count earlier equal prefixes online**

`mask` stores the current prefix XOR. Counter `cnt` records how many previous prefix boundaries had each XOR.

It begins with `cnt[0] = 1` for the empty prefix before index zero. This initial entry is essential: if the prefix from zero through the current index has XOR zero, pairing it with the empty prefix counts that whole prefix as a beautiful subarray.

For each value `x`:

1. `mask ^= x` extends the prefix XOR;
2. `ans += cnt[mask]` counts all earlier equal prefixes;
3. `cnt[mask] += 1` records the current prefix for later endpoints.

The count is added before inserting the current prefix so a zero-length subarray is never paired with itself.

**Why adding the frequency counts exactly the new subarrays**

Suppose the current prefix XOR is $v$, and $v$ appeared at $c$ earlier prefix boundaries. Each earlier boundary defines a different start index. Pairing it with the current endpoint produces $c$ different nonempty subarrays whose XOR is zero.

No other start produces zero XOR because its preceding prefix value differs from $v$. Thus `cnt[mask]` is exactly the number of beautiful subarrays ending at the current index.

Summing these endpoint-specific counts visits every nonempty subarray once, at its unique right endpoint.

**Trace the first sample**

For `[4,3,1,2,4]`, prefix XORs including the empty prefix are:

$$
0,4,7,6,4,0.
$$

Value $4$ appears twice, producing one zero-XOR subarray between those boundaries: `[3,1,2]`. Value $0$ also appears twice, producing the whole array. No other prefix value repeats, so the answer is two.

**All-zero behavior**

Every prefix XOR of an all-zero array is zero. At successive indices the Counter frequencies are one, two, three, and so on, contributing

$$
1+2+\cdots+n=\frac{n(n+1)}2
$$

beautiful subarrays. This matches the fact that every nonempty subarray is already all zero and needs no operations.

## Complexity detail

Let $n$ be the array length. The loop performs one XOR and expected constant-time Counter operations per element, giving expected $O(n)$ time. There can be up to $n+1$ distinct prefix XOR values, so the Counter uses $O(n)$ space.

All arithmetic on the answer is exact in Python. A fixed-width implementation should use a 64-bit count because the answer can reach $n(n+1)/2$.

## Alternatives and edge cases

- **Simulate operations:** Choosing bit pairs explicitly is unnecessary and combinatorial; parity completely characterizes feasibility.
- **Check every subarray:** Computing XOR for all $O(n^2)$ subarrays is too slow for $10^5$ elements.
- **Track parity per bit:** A vector of bit parities works, but XOR packs the same state into one integer.
- **Single zero:** Its XOR is zero, so the one-element subarray is beautiful.
- **Single nonzero:** At least one bit has odd parity, so it is not beautiful.
- **All zeros:** Every subarray counts, producing the maximum $n(n+1)/2$.
- **Repeated prefix XOR:** Each prior occurrence gives a distinct starting boundary and must be counted.
- **Empty prefix seed:** Omitting `cnt[0] = 1` would miss beautiful subarrays starting at index zero.
- **Nonempty requirement:** Updating the answer before the frequency prevents pairing a prefix with itself.
- **Expected hashing:** Linear time assumes standard expected constant-time Counter lookup.
