## General

**Reduce each possible time to one substring equality.** After $t$ operations, exactly $tk$ leading positions of the original word have been removed, until that amount reaches the word length. If $i=tk<n$, the original suffix `word[i:]` survives and is forced to occupy the beginning of the current word. The appended characters are arbitrary, so restoration is possible exactly when that forced suffix equals the original prefix of the same length:

$$
\texttt{word}[i:n]=\texttt{word}[0:n-i].
$$

If they match, the missing final $i$ characters can be chosen during append operations to complete the original word. If they do not match, no appended suffix can repair the forced disagreement at the front.

The larger input limit makes repeatedly creating and comparing slices too expensive. The exact source uses polynomial rolling hashes so that each reachable offset can be checked in constant time after linear preprocessing.

**Build prefix hashes and powers.** Class `Hashing` receives a string, base 13331, and modulus 998244353. It creates arrays `h` and `p` of length $N+1$.

`h[i]` is the polynomial hash of the first $i$ characters. Its recurrence is

$$
h_i=(h_{i-1}\cdot B+\operatorname{ord}(s_{i-1}))\bmod P.
$$

`p[i]` stores $B^i\bmod P$, built by an analogous multiplication. Index zero represents the empty prefix: `h[0] = 0` and `p[0] = 1`.

Multiplying an earlier prefix hash by a power of the base shifts its polynomial positions. This allows the contribution before a substring to be subtracted from a longer prefix.

**Read `query(l,r)` as a one-indexed inclusive substring.** The method returns

`(h[r] - h[l - 1] * p[r - l + 1]) % mod`.

Here $l$ and $r$ are one-indexed character positions and both endpoints are included. `h[r]` hashes the prefix through position $r$. The product subtracts the prefix before $l$, shifted by exactly the substring length. The remainder is the normalized hash of positions $l$ through $r$, independent of where that substring occurred.

Therefore equal substrings of equal length have equal query values.

**Check only offsets reachable after whole seconds.** The loop visits `i = k, 2k, 3k, ...` while $i<n$. At offset $i$, the prefix of length $n-i$ occupies one-indexed interval $[1,n-i]$, and the surviving suffix occupies $[i+1,n]$. The exact comparison is

`hashing.query(1, n - i) == hashing.query(i + 1, n)`.

If it succeeds, restoration is possible after `i // k` seconds. Offsets are examined in increasing order, so the first returned time is minimal and is greater than zero.

**Fallback once no original overlap remains.** If every proper overlap fails, after

$$
\left\lceil\frac{N}{k}\right\rceil
$$

seconds all original positions have been removed. The appended characters can then be selected so that the entire current word is the original word. The source computes this ceiling as `(n + k - 1) // k`.

**A trace of the compared intervals.** For `word = "abacaba"` and $k=3$, offset 3 compares prefix `"abac"` with suffix `"caba"`, so it fails. Offset 6 compares prefix `"a"` with suffix `"a"`, so the method returns $6/3=2$.

For $k=4$, the first offset compares prefix `"aba"` and suffix `"aba"`, immediately returning one. The algorithm never has to construct the intermediate word or guess appended characters; hash equality establishes that the forced portion already fits.

**Important correctness limitation of the exact source.** Polynomial hashing modulo a single number is not an exact proof of substring equality. Equal substrings always hash equally, but two different substrings can theoretically collide modulo 998244353 and make the method return too early. The base and large modulus make accidental collisions unlikely for ordinary inputs, but the risk is not zero.

Consequently the overlap reasoning is deterministic, while the implementation's equality oracle is probabilistic. A Z-function implementation would remove this caveat. The local manifest in fact describes a Z-function, but the protected Optimal source does not build one; it builds a single-modulus rolling hash. An accurate explanation must distinguish those algorithms.

**Why hash preprocessing still scales.** The word may contain up to one million characters. Building `h` and `p` makes one pass, and every candidate time performs two constant-time range-hash queries. No slice proportional to the surviving suffix is created in the loop. This is the asymptotic improvement over the direct-comparison solution for problem I.

## Complexity detail

Let $N$ be the word length. Constructing both arrays takes $O(N)$ time. The loop checks at most $\lceil N/k\rceil-1$ offsets, each with two $O(1)$ hash queries, so it costs $O(N/k)$ and is bounded by $O(N)$. Total time is $O(N)$.

Arrays `h` and `p` each contain $N+1$ Python integers, so auxiliary space is $O(N)$. The input string is immutable and no substring copies are made during queries.

These bounds treat modular multiplication and subtraction as constant-time arithmetic, which is standard for the fixed modulus. The manifest's time and space bounds happen to match, but its stated Z-function mechanism does not match the source.

## Alternatives and edge cases

- **Z-function:** It computes the exact longest prefix match beginning at every offset in $O(N)$ time and $O(N)$ space. Testing multiples of $k$ then has no collision risk and matches the algorithm described by the manifest, but it is not the protected implementation.
- **KMP prefix function:** Borders can also be derived deterministically in linear time, though mapping them to the first reachable multiple of $k$ requires care.
- **Direct slicing:** Comparing `word[i:]` with `word[:-i]` is simple but can take $O(N^2)$ total time when $k$ is small, which is unsuitable for $N$ up to one million.
- **Double hashing:** Using two independent moduli makes collision probability dramatically smaller but still does not produce a mathematical equality proof.
- **Single-modulus collision:** The exact source can theoretically treat unequal substrings as equal. This is a genuine implementation caveat, not a property of the overlap criterion.
- **$k=N$:** No proper offset is checked; the fallback returns one because the complete word can be removed and re-appended.
- **First reachable overlap matches:** The method returns one and stops, satisfying the positive-time minimum.
- **No proper overlap:** The ceiling fallback is sufficient once all original characters have disappeared.
- **Offsets not divisible by $k$:** They are irrelevant because no whole number of operations removes that many leading positions.
- **Length-one word:** With $k=1$, the loop is empty and the correct answer is one.
- **Highly repetitive word:** Many hashes may match, but increasing offset order guarantees the earliest reachable candidate is returned.
