## General

**A binary palindrome is determined by its first half**

For a binary string of length `L`, the second half must mirror the first.

If `L` is even, the first `L / 2` bits determine all remaining bits. If `L` is odd, the first `ceil(L / 2)` bits include the center and determine the rest.

Let

`h = ceil(L / 2) = (L + 1) // 2`.

Any positive `L`-bit integer must begin with one, so the first bit of this `h`-bit prefix is fixed. The other `h - 1` prefix bits are free.

Therefore the number of positive binary palindromes of length `L` is

`2^(h - 1)`.

The source writes the equivalent exponent

`(L - 1) // 2`.

**Count zero separately**

Positive binary representations have a leading one and are covered by the length formula. Number zero is special: its representation is `"0"` and it is declared palindromic.

For `n > 0`, the source initializes `answer = 1` to count zero.

For `n = 0`, it immediately returns one because there are no positive candidates to process.

**Add every shorter binary length**

Let `length = n.bit_length()`. Every positive integer with fewer than `length` bits is automatically at most `n`.

For each `shorter_length` from one through `length - 1`, the source adds

`1 << ((shorter_length - 1) // 2)`,

which is the count derived above.

After this loop, `answer` includes zero and every binary palindrome shorter than `n`’s representation. Only palindromes of exactly `length` bits remain to be bounded against `n`.

**Extract the decisive first half of `n`**

Set

`half_length = (length + 1) // 2`.

The source shifts `n` right by `length - half_length` bits, leaving its top `half_length` bits as `prefix`.

Every valid length-`L` palindrome has an `h`-bit first half ranging from

`2^(h - 1)`

through `2^h - 1`. Prefixes smaller than `prefix` generate palindromes smaller than `n` because the first differing bit occurs within the leading half and determines numeric order before the mirrored suffix matters.

The number of valid leading-one prefixes strictly below `prefix` is

`prefix - 2^(half_length - 1)`.

The source adds this count directly.

**Construct the palindrome belonging to the equal prefix**

There is one remaining candidate whose first half equals `n`’s prefix. It may be at most `n` or may exceed it depending on the mirrored suffix.

The source starts `palindrome = prefix` and prepares bits to mirror:

- For even `length`, mirror the whole prefix.
- For odd `length`, do not mirror the center bit, because it appears only once.

Expression

`remaining = prefix >> (length & 1)`

implements both cases. `length & 1` is zero for even lengths and one for odd lengths.

While `remaining` is nonzero, the source takes its lowest bit, shifts `palindrome` left, and appends that bit:

`palindrome = (palindrome << 1) | (remaining & 1)`.

Then it shifts `remaining` right. Reading prefix bits from low to high appends them in reverse order, creating the mirrored suffix.

**Why the equal-prefix comparison is the only final check**

All smaller prefixes have already been counted and definitely produce smaller numbers. All larger prefixes produce larger numbers and must not be counted.

Only the palindrome built from the equal prefix can fall on either side of `n`. If

`palindrome <= n`,

the source adds one. Otherwise it does not.

This completes the count without enumerating individual palindromic integers.

**Trace `n = 9`**

Nine is binary `1001` with length four.

Start with one for zero. Shorter palindrome counts are:

- Length one: one, representing `1`.
- Length two: one, representing `11`.
- Length three: two, representing `101` and `111`.

The subtotal is five.

For length four, `half_length = 2` and the top prefix of `1001` is `10`, numeric two. The smallest valid two-bit prefix is also two, so no smaller same-length prefix is added.

Mirroring `10` produces `1001`, equal to nine, so one more is included. Total is six.

**Trace an equal prefix whose mirror is too large**

Suppose `n`’s second half is lexicographically smaller than the reflection of its first half. The constructed palindrome shares the prefix but has a larger suffix, so it exceeds `n` and is rejected.

The next smaller prefix’s palindrome was already counted in the arithmetic prefix difference, ensuring there is no gap or double count.

**Why no leading-zero cases appear**

All positive prefixes begin at `1 << (h - 1)`, which forces the highest bit to one. The algorithm never constructs shorter representations padded with zeros.

Zero is handled separately with its canonical one-character representation.

## Complexity detail

Let `L = bit_length(n)`, which is `O(log n)` for positive `n`.

The shorter-length loop runs `L - 1` times. Constructing the equal-prefix palindrome mirrors at most `ceil(L / 2)` bits. Total time is `O(L) = O(log n)`.

Only a fixed number of integer variables is stored, so auxiliary space is `O(1)` under the standard arbitrary-precision integer model.

Python shift and bitwise operations on `L`-bit integers technically cost time proportional to machine-word length. In the usual problem analysis they are treated as constant per step; with `n <= 10^15`, `L <= 50` and all values fit in a small fixed number of machine words.

## Alternatives and edge cases

- **Enumerate every integer through `n`:** Convert each to binary and test it, costing `O(n log n)` time.
- **Generate every palindrome explicitly:** It is much better than checking every integer but still unnecessary when prefix counts give a direct formula.
- **Mirror the center bit twice:** For odd lengths this creates one extra bit and the wrong number. Shift the prefix by one before mirroring.
- **Count prefixes from zero:** That introduces leading-zero strings representing shorter numbers and double-counts them.
- **Forget zero:** Positive-length formulas do not include it, but the statement explicitly declares it palindromic.
- **`n = 0`:** Return one immediately.
- **`n = 1`:** Count zero and binary `1`, returning two.
- **`n` itself palindromic:** The equal-prefix construction reproduces it and `<=` includes it.
- **Equal-prefix palindrome larger than `n`:** Do not add the final candidate.
- **Even length:** Mirror every prefix bit.
- **Odd length:** Exclude the center bit from the mirrored portion.
- **Power of two:** Its leading prefix may mirror to a number larger than it; the final comparison handles this boundary.
- **No leading zeros:** The prefix lower bound forces a leading one for every positive candidate.
- **Large constraint:** `10^15` needs at most 50 binary digits, so the logarithmic method is very small in practice.
- **Input preservation:** The integer is never modified outside local derived variables.
