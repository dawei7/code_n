## General

**Fold the title from most significant letter to least**

The competitive method scans the string by index. `result` always stores the
numeric value of the prefix before the current position.

For every new letter, it first multiplies `result` by 26. This shifts every
processed Excel digit one position toward higher significance. It then adds
the numeric value of the current letter.

This is the same pattern used to parse a decimal string: to append decimal
digit seven to 133, calculate `133 * 10 + 7`. Here the base is 26 and letter
digits range from one through 26.

**Map an uppercase letter to an Excel digit**

Python's `ord` converts a character into its integer code. Uppercase English
letters have consecutive codes, so:

`ord(s[i]) - ord('A')`

is zero for `A` and 25 for `Z`. Excel begins at one rather than zero, so the
source adds one.

The complete update is therefore:

`result = result * 26 + letter_value`.

It is split across two source lines, but the mathematics is one Horner-rule
step.

**Trace the smallest boundaries**

For `"A"`, zero is multiplied by 26 and one is added, returning one.

For `"Z"`, the letter value is 26, returning 26. This is the key distinction
from ordinary zero-based digits.

For `"AA"`, the first `A` produces one. The second shifts that prefix to 26
and contributes another one, producing 27.

For `"AB"`, the final contribution is two instead, producing 28.

**Trace `"ZY"`**

Processing `Z` sets `result` to 26. `Y` has value 25. The next update is:

$$
26\cdot26+25=701.
$$

The method returns 701. It never needs to construct the intermediate power
$26^1$ explicitly; multiplying the prefix applies the correct positional
weight.

For a longer title such as `"ABC"`, the evolution is:

$$
1,\quad 1\cdot26+2=28,\quad 28\cdot26+3=731.
$$

Expanding the final expression yields
$1\cdot26^2+2\cdot26+3$, exactly the positional interpretation.

**Prove the prefix invariant**

Before processing position `i`, assume `result` equals the value of
`s[0:i]`. This is true for `i = 0`, because the empty prefix has value zero.

Multiplying by 26 shifts that prefix left by one base position. Adding the
one-based digit value of `s[i]` fills the new lowest position. The result then
equals `s[0:i + 1]`.

Induction over every index proves that the final scalar equals the entire
column title's number.

**Relationship to number-to-title conversion**

The inverse problem repeatedly subtracts one, takes a remainder, and divides by
26 because Excel has no zero digit. This direction already receives explicit
letters with known one-based values, so it simply applies positional
accumulation.

No subtract-one step is needed here. Instead, the `+ 1` in letter decoding
preserves the bijective digit values.

**Exact-source behavior**

`range(len(s))` creates an index sequence and each iteration accesses
`s[i]`. The input is valid and nonempty, so all accesses are safe.

Calling `ord('A')` during every iteration repeats a constant calculation. It
could be stored once, but that changes only a tiny constant factor.

Python integers avoid overflow. The contract also restricts the title through
`"FXSHRXW"`, keeping the result within the expected signed 32-bit maximum.

**Why the representation has no ambiguous leading letter**

Every legal letter has a strictly positive digit value. A leading `A` is
therefore meaningful; it is never a disposable zero. The largest one-letter
title is `"Z"` with value 26, and the smallest two-letter title is `"AA"` with
value `1 * 26 + 1 = 27`. Similarly, each new title length begins immediately
after all shorter titles.

This is why the recurrence can return one unique integer without normalizing
or stripping a prefix. It also explains why `"A"` and `"AA"` are different
values rather than alternative spellings of one.

**Avoid rebuilding prefixes as strings**

At iteration `i`, the method needs only the numeric prefix value, not the
substring `s[:i]`. Repeatedly slicing those prefixes would allocate extra
memory and revisit characters. Keeping the scalar `result` summarizes all
earlier positions exactly, so each new character is processed once.

The loop's left-to-right order also matches significance: an unequal leading
letter changes the value by an entire power-of-26 block, and later letters
fill only lower positions.

## Complexity detail

For a title of length $n$, the source runs exactly $n$ loop iterations. With
the bounded result size, each multiplication, addition, and character-code
operation is constant time, so total time is $O(n)$.

Only `result`, index `i`, and temporary character-code values are maintained.
Auxiliary space is $O(1)$, matching the manifest. No title copy or alphabet
map is allocated.

## Alternatives and edge cases

- **Iterate characters directly:** Avoid the index variable with `for char in s`; the recurrence is unchanged.
- **Use `map(ord, s)`:** Lazily iterate integer codes, as the optimal variant does.
- **Right-to-left weighted sum:** Multiply each decoded letter by a growing power of 26; correct but more stateful.
- **Lookup dictionary:** Constant-sized and readable, but character-code arithmetic already gives the mapping.
- **`A`:** Must contribute one, not zero.
- **`Z`:** Must contribute 26, verifying bijective rather than ordinary base 26.
- **Multiple letters:** Every earlier prefix is shifted before the next digit is added.
- **Maximum valid title:** Fits the stated numeric limit.
- **Invalid lowercase input:** Outside the contract; its code offset would not represent a valid digit.
- **Empty title outside the contract:** The loop would return zero rather than a valid column number.
