## General

A string formed by repeating a shorter block has a nontrivial rotational symmetry. If `s = "abab"`, shifting it left by two positions still gives `"abab"`. If no shorter block repeats to form the string, the only shift that reproduces the whole string is a full-length shift, which is equivalent to making no change.

The exact solution exposes every rotation inside `s + s`, searches for another occurrence of `s` starting after position zero, and checks whether that occurrence begins before position `len(s)`.

**Why `s + s` contains rotations**

Let `n = len(s)`. Start at offset `d` inside the doubled string, where $0\le d<n$, and take the next `n` characters. The slice first takes the suffix `s[d:]`, then wraps into the second copy for the prefix `s[:d]`. It is therefore the left rotation

`s[d:] + s[:d]`.

As `d` ranges from zero through `n - 1`, the length-`n` windows in `s + s` represent every cyclic rotation of `s`.

The call `(s + s).index(s, 1)` asks for the first occurrence of `s` whose starting position is at least one. Starting at one deliberately ignores the trivial original occurrence at position zero.

There is always at least one later occurrence: the second literal copy begins at index `n`. Therefore `.index` cannot fail for a nonempty `s`; no exception handling is needed.

**Why an occurrence before `n` proves repetition**

Suppose the search returns an offset `d` with $1\le d<n$. Then the rotation of `s` by `d` positions equals `s` itself. Character equality around that rotation means positions repeat with period determined by `d`; more precisely, indices connected by repeatedly adding `d` modulo `n` carry equal characters. The string is therefore made from a block whose length is $\gcd(n,d)$.

Because `d` is strictly between zero and `n`, $\gcd(n,d)<n$. The block is a proper nonempty prefix, and it repeats exactly $n/\gcd(n,d)$ times, which is at least two. Thus a match beginning before `n` proves the required repeated-substring structure.

**Why every repeated string creates an early occurrence**

Conversely, suppose `s` consists of `k >= 2` copies of a block `p` of length `d`. Rotating `s` left by exactly `d` positions removes the first copy of `p` and appends an identical copy at the end, so the string does not change. The doubled string therefore contains `s` starting at offset `d`.

Since at least two copies exist, $1\le d<n$. The search begins at one and will find this occurrence or an even earlier nontrivial occurrence. Its index is consequently less than `len(s)`, and the method returns `True`.

These two directions show the exact equivalence:

$$
\text{proper repeated block exists}
\quad\Longleftrightarrow\quad
1\le\text{next occurrence index}<n.
$$

**Trace the examples**

For `s = "abab"`, the doubled string is `"abababab"`. Searching from index one finds `"abab"` at index two. Since $2<4$, the string is periodic; the repeated block is `"ab"`.

For `s = "aba"`, the doubled string is `"abaaba"`. No occurrence starts at one or two. The guaranteed second-copy occurrence starts at index three, and `3 < 3` is false, so the result is `False`.

For `s = "abcabcabcabc"`, a new occurrence starts at index three, revealing period three. Another valid repeated block, `"abcabc"`, corresponds to shift six, but finding any one proper shift is sufficient.

**Why the boundary comparison is strict**

Every string occurs at index `n` in its doubled copy, even a nonperiodic string. Accepting `index <= n` would therefore return true for every input. Requiring the found index to be strictly less than `n` excludes that trivial second copy and accepts only a proper rotation.

The solution also avoids allocating `(s + s)[1:-1]`. The common trimmed-string formulation checks whether `s` occurs after removing the doubled string's first and last characters. Searching from index one and comparing the returned position with `n` expresses the same condition with no additional slice.

## Complexity detail

Let $n$ be the string length. Constructing `s + s` creates a string of length `2n`, taking $O(n)$ time and $O(n)$ space.

The manifest assumes an efficient linear-time substring search, under which finding `s` inside the doubled text takes $O(n)$ time. Total time is then $O(n)$ and auxiliary storage is $O(n)$ for the doubled string. Python's concrete substring-search implementation is optimized; when reasoning independently of a language library's guarantee, one can use KMP to guarantee linear worst-case matching explicitly.

The returned value uses constant space, and the input string is immutable and unchanged.

## Alternatives and edge cases

- **Try every prefix length that divides `n`:** Repeat each candidate prefix and compare with `s`. It is easy to derive but can perform repeated full-string construction and comparison.
- **KMP prefix function:** Let `L` be the longest proper prefix of `s` that is also a suffix. The string repeats exactly when `L > 0` and `n % (n - L) == 0`. This guarantees $O(n)$ time and $O(n)$ space without depending on library substring search.
- **Rolling hash:** Hashes can test candidate periods efficiently, but collisions require verification or multiple hashes and add needless risk here.
- **One-character string:** The only later match starts at index one, equal to `n`, so it correctly returns false; a proper nonempty substring cannot exist.
- **All one character:** For length greater than one, the search finds `s` starting at index one, proving repetition of the one-character block.
- **Prime length:** A repeated pattern is possible only with block length one; the rotation test handles this without explicitly factoring `n`.
- **Overlapping occurrence:** `.index` considers overlapping matches, which is necessary for strings such as `"aaaa"` whose next occurrence starts at one.
- **Guaranteed nonempty input:** The proof assumes `n > 0`. The source contract supplies that guarantee.
- **Strict properness:** A match at exactly `n` represents merely the second copy and is intentionally rejected.
