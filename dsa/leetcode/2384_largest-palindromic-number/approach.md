## General

**A palindrome consumes digits in pairs plus at most one center**

Every position left of a palindrome's center must match a symmetric position on the right. Therefore, digit `d` can contribute `cnt[d] // 2` pairs. If any digit has an odd count, one leftover occurrence may occupy the center.

To maximize the resulting integer, the most significant left-side digits should be as large as possible. The palindrome should also use every available pair that can be placed without creating an invalid leading zero: adding a pair increases length, and a longer positive integer with a nonzero first digit is larger than a shorter one.

**Choose the largest possible center**

The first loop scans digits from nine down to zero and selects the first digit whose count is odd. It stores that character in `ans` and decrements its count by one.

Choosing a center from an odd count does not reduce how many pairs that digit can supply:

$$
\left\lfloor\frac{c-1}{2}\right\rfloor=\left\lfloor\frac{c}{2}\right\rfloor
$$

when $c$ is odd. Thus, all choices of an odd-count center leave the same multiset of usable pairs. The largest odd digit is therefore always the best center.

Only one center is possible. Other leftover single digits cannot be included without breaking symmetry, and the problem permits unused digits.

If every count is even, `ans` remains the empty string. The eventual palindrome then has even length unless zero cleanup reduces it.

**Build from the inside outward**

The second loop scans digits from zero upward. For digit `v`, it halves the remaining count and creates a string `s` containing that many copies. It wraps the current palindrome:

```python
ans = s + ans + s
```

Because low digits are processed first, they occupy inner layers. Later, higher digits wrap around them and become more significant. After the final iteration, the left half is in descending digit order and the right half mirrors it.

For example, suppose pairs are available for digits `4` and `7` and the center is `9`. Digit four first creates `"494"`. Digit seven then wraps it to `"7449447"`. Placing sevens outside fours makes the number larger than the reverse arrangement.

The code uses all pairs for a digit at once. Repeating the same digit in one block preserves the palindrome and places equal digits contiguously at the appropriate significance level.

**Handle zero pairs without leading zeroes**

Zero pairs are processed first and placed closest to the center. If a nonzero pair is later available, it wraps outside those zeros, so they become valid internal digits.

If no nonzero pair exists, wrapping zeros can produce a string such as `"00900"` or `"0000"`. Such a representation cannot be returned because it has leading zeroes. The final expression:

```python
ans.strip('0') or '0'
```

removes zeros from both ends. Since `ans` is a palindrome, invalid leading zeros always have mirrored trailing zeros; removing both preserves a palindrome. If a nonzero center exists, stripping reveals it. If the whole construction consists of zeros, stripping yields the empty string and `or '0'` returns the one valid single-digit zero.

When a nonzero pair exists, the palindrome starts and ends with that nonzero digit, so `strip` removes nothing, including any legitimate internal zeros.

**Trace `"00009"`**

Counts are four zeros and one nine. The center-selection loop chooses nine. The zero loop forms two copies on each side, temporarily creating `"00900"`. No nonzero pairs wrap outside it. Stripping outer zeros leaves `"9"`, which is larger than zero and is the best valid use of the digits.

**Why the construction is maximal**

Any palindrome can use at most `floor(cnt[d]/2)` pairs of digit `d`. The algorithm uses all of them, except zero pairs that would be forced outside every nonzero digit and hence create an invalid representation.

Among valid palindromes with the same available pairs, lexicographic comparison of their left halves determines numeric comparison. Arranging pair digits from largest to smallest on the left is optimal at the first position where two arrangements could differ. The outside-in construction produces exactly that order.

After the pair positions are fixed, only the center can differ. Selecting the largest available odd digit maximizes it without changing any pair count. Thus, no valid palindrome can be longer with a nonzero leading digit, have a larger outer pair sequence, or have a larger center under the same outer sequence. The returned value is globally largest.

## Complexity detail

Let $n$ be the length of `num`. Building the Counter takes $O(n)$ time and at most ten key entries. The two digit loops have fixed length ten.

String repetition and concatenation create up to $O(n)$ total output characters. There are only ten wrapping iterations, so even though strings are immutable, the constant number of whole-string copies keeps total construction time $O(n)$. Stripping also takes $O(n)$.

The result string uses $O(n)$ space. The Counter has constant-size digit-domain storage, while intermediate immutable strings can also occupy $O(n)$ peak space. The manifest reports $O(n)$ space.

## Alternatives and edge cases

- **Build a left-half list then mirror it:** Append pair digits from nine down to zero, choose a center, and concatenate left, center, and reversed left. This avoids repeated wrapping and is often easier to reason about.
- **Sort all input digits:** Sorting costs $O(n\log n)$ and still requires pair counting; the ten-value Counter is more efficient.
- **All digits zero:** Outer-zero removal empties the temporary string, and the fallback returns `"0"`.
- **Only one nonzero digit:** It becomes the center if its count is odd; unused zeros cannot surround it as leading digits.
- **Even counts only:** There is no center, and the palindrome is formed entirely from pairs.
- **Several odd counts:** Only the largest leftover digit is used as center; the rest may contribute their available pairs.
- **Zero pair plus nonzero pair:** The nonzero pair wraps outside, so zeros remain valid internal digits.
- **Unused digits:** Leftover singles beyond the center are intentionally discarded, as permitted.
- **Leading-zero cleanup:** `strip('0')` is safe because symmetry makes every stripped trailing zero the mirror of a forbidden leading zero.
