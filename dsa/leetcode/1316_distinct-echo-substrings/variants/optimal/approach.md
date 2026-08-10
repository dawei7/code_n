## General

An echo substring has even length and consists of two equal consecutive halves. The exact Optimal solution enumerates every even-length substring, compares its halves through a polynomial rolling hash, and stores the hash of each matching half in a set.

Storing the half is sufficient for distinctness: an echo string is exactly `half + half`. Two echo strings are equal exactly when their halves are equal.

**Building powers and prefix hashes**

Each lowercase character is converted to an integer from one through 26. With base 131, a string behaves like a number whose digits are those character values.

`h[i + 1]` is the polynomial hash of the prefix ending at original index `i`. `p[i + 1]` stores $131^{i+1}$ modulo `mod`.

The update

`h[i + 1] = (h[i] * base) % mod + t`

shifts the previous polynomial by one base position and adds the new character. The final addition is not reduced immediately, so `h` can temporarily be slightly larger than `mod`, but it remains congruent to the intended modular hash. The later arithmetic and next multiplication apply modulo, so hash comparisons still use the same residue class.

Arrays have `n + 10` slots, more than the needed `n + 1`. The extra constant padding is harmless.

**Extracting any substring hash**

`get(l, r)` uses one-based inclusive positions. The prefix `h[r]` contains everything through `r`. Multiplying `h[l - 1]` by `p[r - l + 1]` aligns the earlier prefix with that same polynomial degree. Subtracting cancels all characters before `l`:

`(h[r] - h[l - 1] * p[r - l + 1]) % mod`.

Python's modulo returns a nonnegative residue, so equal substrings receive equal returned hashes even when the raw subtraction is negative.

After preprocessing, `get` performs constant-time array access and arithmetic instead of comparing every character in a candidate half.

**Enumerating only even lengths**

`i` is the original zero-based start. The end `j` begins at `i + 1` and advances by two:

`range(i + 1, n, 2)`.

Therefore, `j - i` is odd, and the inclusive substring length `j - i + 1` is even. No odd-length substring is examined because it cannot be split into two equal-length halves.

The midpoint `k = (i + j) >> 1` is the last original index of the first half. The halves are:

- original indices `i` through `k`, hashed by `get(i + 1, k + 1)`; and
- original indices `k + 1` through `j`, hashed by `get(k + 2, j + 1)`.

Both one-based conversions add one to each original endpoint. The second half begins one original position after `k`, hence `k + 2` in the hash coordinate system.

**Recording distinct echoes**

If the two hashes match, the code adds `a`, the first-half hash, to `vis`. A set automatically ignores repeated insertions.

The same echo text can occur at many positions. Because its half text is the same, it produces the same hash and contributes one set entry. Echo strings with different half texts normally produce different hashes and contribute separately.

For `"abcabcabc"`, candidates include `"abcabc"`, `"bcabca"`, and `"cabcab"`. Their halves are `"abc"`, `"bca"`, and `"cab"`, so three hashes enter the set.

**The rolling-hash limitation**

A modular hash is a compact fingerprint, not the substring itself. Different strings can theoretically have the same residue modulo $10^9+7$. The exact source uses one fixed base and one modulus and neither verifies characters after a hash match nor stores the actual substring.

Consequently, it can mistake unequal halves for equal ones or merge distinct echo substrings that collide. The algorithm is highly likely to be correct on ordinary inputs, but it is probabilistic rather than collision-free.

A deterministic explanation cannot claim that equal hashes logically imply equal strings. Exact correctness requires direct verification after a hash match, storing actual substrings for distinctness, a collision-free suffix structure, or another deterministic comparison method. Double hashing lowers risk but still does not make a mathematical proof absolute.

Subject to the no-collision assumption, enumeration covers every possible echo interval, half comparison recognizes exactly those intervals, and the set counts each distinct half once.

## Complexity detail

Let $n$ be the text length. Prefix preprocessing takes $O(n)$ time and space.

There are $O(n^2)$ start-end pairs with even length. Each pair performs constant-time hash extraction, comparison, and expected constant-time set insertion. Total expected time is $O(n^2)$.

In the worst case, `vis` can contain $O(n^2)$ distinct hash values, so space is $O(n^2)$, matching the manifest. The prefix and power arrays add only $O(n)$.

These bounds treat fixed-width modular arithmetic and hash-set operations as constant expected time. Direct substring verification would add character-comparison work in adversarial cases unless paired with a stronger deterministic structure.

## Alternatives and edge cases

- **Direct half comparison:** Compare slices or characters for every candidate. It is deterministic but can take $O(n^3)$ time because each of $O(n^2)$ candidates may compare $O(n)$ characters.
- **Double rolling hash:** Two independent moduli make collisions vastly less likely while retaining $O(n^2)$ expected time, but do not provide absolute collision freedom.
- **Suffix array or suffix LCP structure:** Deterministic longest-common-prefix queries can compare halves efficiently after heavier preprocessing.
- **Store actual echo substrings:** It avoids hash-based distinctness collisions but slicing and hashing full strings can increase total time and memory.
- **Length one text:** No even nonempty candidate exists, both loops add nothing, and the answer is zero.
- **Length two text:** The only candidate compares its two characters and counts one only when they match.
- **Overlapping occurrences:** Each interval is tested, and equal text across overlapping positions is deduplicated by the set.
- **Same half at different lengths is impossible:** A string's content determines its length, so identical half text also has identical length and defines the same echo.
- **One-based hash coordinates:** Every original endpoint must be shifted by one; the second half's start uses `k + 2`.
- **Modulo subtraction:** Applying `% mod` normalizes negative raw differences.
- **Hash collision:** The exact source has a probabilistic correctness caveat that should not be omitted from an expert explanation.
