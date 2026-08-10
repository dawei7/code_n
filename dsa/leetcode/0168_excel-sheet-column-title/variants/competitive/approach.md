## General

**Convert from bijective base 26**

The competitive method treats Excel titles as a positional system whose
symbols `A` through `Z` mean one through 26. Unlike ordinary base 26, no digit
represents zero.

To reuse standard quotient-and-remainder operations, every iteration shifts
the current positive number down by one. The expression `(n - 1) % 26`
produces an offset from zero through 25, and adding `ord('A')` maps it to the
rightmost letter.

The remaining higher-order portion is `(n - 1) // 26`. Both formulas use the
same decremented value, which is necessary for correct carry behavior.

**Derive the boundary behavior**

For values one through 26, `n - 1` ranges from zero through 25. The remainder
therefore maps directly from `A` through `Z`, and the quotient is zero.

At 27, the remainder of 26 by 26 is zero, giving rightmost `A`, while the
quotient is one. Processing one gives another `A`, so 27 becomes `"AA"`.

This demonstrates why using `n % 26` directly is wrong. For 26 it would yield
zero even though the required letter is `Z`, and the quotient would introduce
an unwanted higher digit.

**Append the least significant letter**

Inside the loop, the source writes:

`result += chr((n-1)%26 + ord('A'))`.

`result` is a list, and list `+=` extends the list with the iterable on its
right. A one-character string is an iterable containing exactly that one
character, so this has the same effect as `result.append(character)`.

If the expression ever produced a multi-character string, `+=` would add each
character separately, but `chr(...)` always returns exactly one character.

After adding the letter, `n = (n - 1) // 26` removes that position. The loop
continues until no higher position remains.

**Reverse the extraction order**

Remainder conversion discovers the rightmost title letter first. For 701, the
first iteration maps remainder 24 to `Y` and reduces the number to 26. The
second maps remainder 25 to `Z` and reduces it to zero.

The list therefore contains `['Y','Z']`. `result.reverse()` reverses that list
in place, and `"".join(result)` returns `"ZY"`.

Using in-place reversal avoids the additional reversed list allocated by slice
syntax, although the character list itself still grows with the required
output.

**Why every generated digit is correct**

For any positive current value $N$, define:

$$
r=(N-1)\bmod 26
\quad\text{and}\quad
q=\left\lfloor\frac{N-1}{26}\right\rfloor.
$$

Then $r$ uniquely selects a letter value $r+1$ from one through 26, and $q$
represents all positions to its left. The relation

$$
N=26q+(r+1)
$$

shows that combining that prefix and digit reconstructs the original value.

Repeating the calculation on $q$ proves every extracted letter and the final
title. Because $q<N$ for positive $N$, termination is guaranteed.

**Trace another carry**

For 52, subtracting one gives 51. Remainder 25 produces `Z`, and quotient one
remains. Processing one produces `A`, so reversal yields `"AZ"`.

For 53, the first remainder becomes zero and produces `A`; the quotient is two,
which produces `B`. The answer is `"BA"`. The transition from `"AZ"` to
`"BA"` is the bijective analogue of carrying in an ordinary base system.

**Do not confuse title length with numeric magnitude**

Each iteration shrinks the number by approximately a factor of 26. The maximum
32-bit column number therefore needs only a small number of letters. The method
never loops once per column and does not construct a lookup table.

The input is a positive integer by contract, so `while n` is equivalent to
`while n > 0`. A zero input would produce the empty string, but zero is not a
valid requested column.

All arithmetic remains integral.

## Complexity detail

Let $k$ be the returned title length. The loop has $k$ iterations, the in-place
reversal takes $O(k)$ time, and joining takes $O(k)$ time. Since repeated
division by 26 gives $k=O(\log n)$, total time is $O(\log n)$.

The result list contains $k$ characters. In-place reversal uses constant
additional working memory, while the returned string also has length $k$.
Including output construction, space is $O(k)=O(\log n)$, matching the
manifest. The source comment's $O(1)$ is only defensible when required output
storage is excluded.

## Alternatives and edge cases

- **List append plus slice reversal:** Equivalent result, but a reversed slice allocates another $O(k)$ list.
- **Recursion:** Build the prefix first and then the current letter; it uses logarithmic stack depth.
- **Prepend to a string:** Avoids a final reversal but may copy the growing immutable string repeatedly.
- **Forget the decrement:** Misrepresents 26, 52, and every other carry boundary.
- **One:** Converts directly to `A`.
- **Twenty-six:** Converts directly to `Z`.
- **Twenty-seven:** Produces two letters, `AA`.
- **Multiple carry boundary:** Values such as 52 and 53 verify the decrement at every iteration.
- **Zero outside the contract:** The current loop would return an empty title.
- **List `+=` semantics:** It works here only because `chr` yields one character; `append` would communicate the intent more directly.
