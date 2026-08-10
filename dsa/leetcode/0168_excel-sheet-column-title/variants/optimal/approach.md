## General

**Recognize a base system without a zero digit**

Excel column titles resemble base 26, but their digits are `A` through `Z`
with values one through 26. Ordinary positional notation uses digit values zero
through 25. That difference matters at boundaries: 26 is `"Z"`, not `"BA"`,
and 27 is `"AA"`.

This system is called bijective base 26. Every positive integer has one
representation, but there is no symbol for zero. The source converts one digit
at a time from right to left.

**Shift to ordinary remainder arithmetic**

Before taking a remainder, the method decrements `columnNumber`. This maps the
current one-based digit range:

$$
1,\ldots,26
$$

to the ordinary zero-based range:

$$
0,\ldots,25.
$$

Then `columnNumber % 26` gives the rightmost letter offset. Adding
`ord('A')` converts offset zero to `A`, offset one to `B`, and offset 25 to
`Z`. `chr(...)` turns that code back into a character.

After appending the character, integer division by 26 removes the processed
rightmost digit. The loop repeats while a higher-order portion remains.

The order “subtract, take remainder, divide” is essential. Taking the remainder
before subtracting would map multiples of 26 to zero and incorrectly treat
them like an absent digit rather than `Z`.

**Why decrementing on every iteration works**

Suppose the current column number can be written as:

$$
N = 26q + r,
$$

where the desired rightmost Excel digit value is from one through 26. In
ordinary division, a multiple of 26 would have remainder zero, but the desired
digit is 26.

Using $N-1$ instead gives an ordinary remainder from zero through 25. The
letter offset is:

$$
(N-1) \bmod 26,
$$

and the remaining higher-order title is represented by:

$$
\left\lfloor\frac{N-1}{26}\right\rfloor.
$$

The same issue exists independently at every higher position, so the decrement
must happen during each loop iteration, not just once at the beginning.

**Trace boundary values**

For column one, decrementing gives zero. Remainder zero maps to `A`, division
leaves zero, and the loop stops.

For 26, decrementing gives 25. Remainder 25 maps to `Z`; dividing 25 by 26
leaves zero. The result is one letter.

For 27, the first decrement gives 26. Its remainder is zero, so the first
generated character is `A`; division leaves one. The next iteration decrements
one to zero and generates another `A`. The collected order is rightmost first,
but reversing yields `"AA"`.

For 28, the first generated character is `B` and the second is `A`, producing
`"AB"` after reversal.

**Trace 701**

Starting from 701, decrement to 700. `700 % 26` is 24, which maps to `Y`.
Integer division leaves 26.

Decrement 26 to 25. The remainder maps to `Z`, and division leaves zero. The
list was built as `['Y','Z']` because least significant letters are discovered
first. Reversing it produces `"ZY"`.

**Build backward, then reverse once**

Remainder extraction always finds the least significant digit first, just as
ordinary base conversion does. The source appends those characters to `res`.
After the number becomes zero, `res[::-1]` creates the reversed list, and
`''.join(...)` produces the title.

Prepending every newly found character to a Python string would repeatedly copy
the growing prefix. Appending to a list and reversing once gives linear work in
the number of output characters.

**Why the process terminates and is unique**

Every iteration replaces a positive number with
`(columnNumber - 1) // 26`, which is strictly smaller and nonnegative. It
eventually reaches zero.

The remainder uniquely determines the rightmost letter, and the quotient
uniquely determines the remaining prefix. Applying this argument recursively
shows that the constructed title is the unique Excel representation of the
input.

## Complexity detail

Let $k$ be the number of title characters. Each iteration divides the remaining
number by 26, so $k=O(\log_{26} n)=O(\log n)$. The loop, reversal, and join
each take $O(k)$ time, for total $O(\log n)$.

The character list and reversed slice each hold $O(k)$ items during
construction. Including output-building storage, space is $O(k)=O(\log n)$,
matching the manifest. If required output is excluded and reversal is done in
place, working space can be described more tightly, but the selected slice
does allocate another list.

## Alternatives and edge cases

- **Recursive conversion:** Recursively convert `(n - 1) // 26` and append the current letter; it avoids explicit reversal but uses $O(\log n)$ call-stack space.
- **String prepending:** Conceptually simple, but immutable strings can cause quadratic copying in the output length.
- **Ordinary base 26 without decrement:** Incorrect at every multiple of 26 because Excel has no zero digit.
- **Column one:** Produces `"A"` in one iteration.
- **Column 26:** Produces `"Z"`, the key boundary case.
- **Column 27:** Carries into a second digit and produces `"AA"`.
- **Large maximum input:** Repeated integer division safely terminates in logarithmically many steps.
- **Positive-input guarantee:** Zero has no Excel column title and is outside the contract.
- **Character arithmetic:** Offsets must be added to `ord('A')`, not treated as direct character codes.
- **Output order:** Extracted letters are least significant first and must be reversed.
