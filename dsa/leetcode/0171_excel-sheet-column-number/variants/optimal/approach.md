## General

**Read the title as bijective base 26**

Excel letters act like base-26 digits, except their values are one through 26:
`A = 1`, `B = 2`, and `Z = 26`. There is no zero-valued letter.

For a title with digit values $d_1,d_2,\ldots,d_k$, its column number is:

$$
d_1 26^{k-1}+d_2 26^{k-2}+\cdots+d_k.
$$

The source evaluates this expression from left to right without calculating
powers explicitly. This is Horner's rule: each new letter shifts the existing
prefix one base-26 position left, then fills the new last position.

**Convert character codes to values one through 26**

`map(ord, columnTitle)` yields the integer character code for each uppercase
letter. Uppercase English letters are consecutive in the character encoding
used by Python, so:

`c - ord("A")`

produces offsets zero through 25. Adding one changes them to Excel digit values
one through 26.

The validity guarantee ensures no lowercase letter, dot, digit, or other symbol
needs validation. Every mapped code corresponds to a legal Excel digit.

**Accumulate one prefix at a time**

`ans` begins at zero. For each character code `c`, the update is:

`ans = ans * 26 + c - ord("A") + 1`.

Suppose `ans` currently represents the title prefix already processed.
Multiplying by 26 appends a conceptual zero-valued base position. Adding the
current letter value replaces that position with the real Excel digit.

Although bijective base 26 has no actual zero symbol, zero is useful as the
temporary empty slot created by multiplication. The added digit is always at
least one.

**Trace `"AB"`**

Initially `ans = 0`. For `A`, the digit value is one, so:

$$
0\cdot26+1=1.
$$

For `B`, the digit value is two, so:

$$
1\cdot26+2=28.
$$

The returned column number is 28.

For a single `Z`, the update is `0 * 26 + 26`, yielding 26. This boundary
demonstrates why the letter offset must include the final `+ 1`.

**Trace `"ZY"`**

The first letter `Z` gives 26. The next letter `Y` has value 25, so:

$$
26\cdot26+25=701.
$$

That matches the example. It is also the reverse of ID 168's repeated
subtract-one conversion: that algorithm extracts rightmost letters from a
number, whereas this algorithm folds leftmost letters into a number.

For `"AA"`, the updates give one and then 27. The second `A` is not a zero
digit; it contributes one in the lowest position.

**Why Horner's rule matches the positional formula**

After processing the first $j$ letters, maintain the invariant that `ans`
equals the numeric value of exactly that prefix.

The empty prefix has value zero, establishing the base case. If the invariant
holds before a new digit $d$, shifting all existing digits one place left
multiplies their total by 26. Adding $d$ places the new digit in the units
position. Therefore the updated accumulator equals the extended prefix.

By induction, after the final letter `ans` equals the complete title's column
number.

**Why explicit powers are unnecessary**

A right-to-left method could multiply every letter value by
$26^0,26^1,\ldots$. Horner's rule folds the same polynomial using one
multiplication and addition per character. It avoids a power variable, a
mapping table, and reverse indexing.

The input length is at most seven and its maximum title fits the specified
numeric domain. Python integers would also handle larger results without
overflow.

**Input is read-only**

`map` lazily supplies codes as the loop requests them; it does not create a
list of all codes. The original string is never modified.

**Why title lengths do not overlap ambiguously**

In an ordinary written number, leading zeroes can create multiple textual
forms for one value. Excel has no zero letter, so every leading letter
contributes a positive multiple of a power of 26. The smallest two-letter
title, `"AA"`, evaluates to 27, immediately after the largest one-letter title,
`"Z"`, which evaluates to 26. The same boundary property continues at every
length. Horner's rule therefore maps valid titles into one continuous,
unambiguous positive sequence.

The seven-character constraint limits both the number of loop iterations and
the result magnitude. Still, the algorithm is written generically: its logic
does not contain seven special cases or a hard-coded table of column titles.

## Complexity detail

Let $n$ be the number of title characters. The loop processes each character
once, with constant-time arithmetic under the bounded result size. Time is
$O(n)$.

Only `ans`, the current code `c`, and the lazy iterator are stored. Auxiliary
space is $O(1)$, matching the manifest. The returned integer is scalar output.

## Alternatives and edge cases

- **Index the string directly:** Iterate positions and call `ord(columnTitle[i])`; it implements the same recurrence.
- **Right-to-left powers:** Sum each digit times an increasing power of 26. It is correct but needs more bookkeeping.
- **Alphabet dictionary:** Map each letter to one through 26; the table is constant-sized but unnecessary because codes are consecutive.
- **Single `A`:** Produces one.
- **Single `Z`:** Produces 26, verifying the one-based digit range.
- **Repeated `A`:** Each occurrence contributes one; `"AA"` is 27, not 26.
- **Maximum seven-letter title:** The loop remains linear and the result fits the stated range.
- **No zero digit:** Omitting `+ 1` would make `A` contribute zero and break every title.
- **Uppercase guarantee:** Character-code subtraction relies on the specified alphabet.
- **Empty string outside the contract:** The method would return zero, but no empty Excel title is valid.
