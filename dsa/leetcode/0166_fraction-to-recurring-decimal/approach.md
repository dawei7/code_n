## General

**Separate sign, integer part, and fractional part**

The output is easiest to build in the same order as ordinary long division.
The source first handles a zero numerator, returning `"0"` before any sign
logic. A zero fraction should never be rendered as negative zero.

For a nonzero numerator, the fraction is negative exactly when one operand is
positive and the other is not. Because the denominator is guaranteed nonzero,
`(numerator > 0) ^ (denominator > 0)` is true precisely when their signs differ.
The method appends `"-"` in that case.

It then works with absolute values `a` and `b`. The integer part is
`a // b`, which is appended as decimal text. The new `a = a % b` is the
remainder that begins the fractional calculation.

If that remainder is zero, division is exact. The integer text is already the
complete finite representation, so the method returns without adding a decimal
point.

**Generate decimal digits by long division**

For a nonzero remainder, the source appends `"."` and repeatedly performs the
familiar long-division step:

1. multiply the remainder by ten;
2. divide by the positive denominator to obtain the next decimal digit;
3. keep the modulus as the remainder for the following position.

Because the incoming remainder is smaller than `b`, multiplying by ten makes
the quotient an integer from zero through nine. Thus each appended quotient is
one decimal digit, including necessary internal zeros.

For $1/2$, the integer part is zero and the remainder is one. Multiplying by
ten gives ten; quotient five is appended and the next remainder is zero. The
loop ends with `"0.5"`.

**A repeated remainder means repeated future digits**

The next digit and next remainder are deterministic functions of the current
remainder and fixed denominator. If the same remainder occurs twice, every
subsequent long-division step will repeat in the same order forever.

The dictionary `d` maps each previously seen remainder to the position in
`ans` where the digit generated from that remainder begins. At the top of an
iteration, the source stores `d[a] = len(ans)`. It then generates one digit and
the next remainder.

If the new remainder already appears in `d`, the repeating cycle begins at the
saved output position. The method inserts `"("` there, appends `")"` at the
end, and stops.

The current remainder cannot already be present when the top assignment runs:
a repeat is detected immediately after the preceding step and breaks the loop.
Therefore the dictionary entry is not incorrectly overwritten.

**Trace the recurring example**

For $4/333$, the integer part is zero and initial remainder is four. The output
position for remainder four is recorded, multiplying by ten yields digit zero,
and the next remainder is 40.

Remainder 40 is recorded before generating another zero, leaving remainder
400. Remainder 400 is recorded before generating digit one, which leaves
remainder 67.

Continuing long division eventually regenerates remainder four. The dictionary
points to the position of the first fractional zero, so parentheses surround
the full repeating digit sequence `"012"`. The result is `"0.(012)"`.

A simpler example is $1/6$. Remainder one generates digit one and leaves
remainder four. Remainder four generates digit six and leaves remainder four
again. The saved position for four is immediately before six, producing
`"0.1(6)"`, not `"0.(16)"`.

**Why termination is guaranteed**

After taking the modulus by `b`, a nonzero remainder is one of
$1,2,\ldots,b-1$. There are finitely many possibilities. Long division must
therefore either reach zero, giving a finite decimal, or repeat a prior
remainder, giving a recurring decimal.

This also proves the cycle location is exact. Digits before the first occurrence
of the repeated remainder form the nonrepeating prefix; digits from that
position onward recur.

**Handle signs and integer extremes safely**

Using absolute values after deciding the sign keeps all division steps
nonnegative and avoids language-specific floor behavior for negative integer
division. Python integers can represent the absolute value of
$-2^{31}$ and any intermediate multiplication without overflow.

In a fixed-width 32-bit language, negating the minimum integer overflows; a
wider integer type is needed before taking absolute values.

The denominator-zero case requires no branch because the contract excludes it.

## Complexity detail

Let $k$ be the number of produced fractional digits before termination or cycle
detection. Each long-division iteration performs constant expected-time
dictionary operations and generates one digit, so time is $O(k)$.

The answer list and remainder dictionary each hold $O(k)$ entries. Auxiliary
space including construction storage is $O(k)$, matching the manifest. The
guarantee that the answer length is below $10^4$ bounds practical output size.

Inserting the opening parenthesis into a Python list shifts later entries and
costs $O(k)$ once; this does not change the total $O(k)$ bound.

## Alternatives and edge cases

- **Simulate with a string builder and saved positions:** Equivalent to the list representation; insertion may be expressed with final slicing instead.
- **Floating-point conversion:** Incorrect because finite precision cannot preserve arbitrary recurring structure or exact digits.
- **Reduce by the greatest common divisor first:** May shorten the denominator but is not required for correctness or asymptotic output work.
- **Zero numerator:** Return `"0"` without a negative sign or decimal point.
- **Exact integer:** A zero initial remainder omits the fractional part.
- **Terminating fraction:** The loop reaches remainder zero and adds no parentheses.
- **Recurring fraction:** The first repeated remainder marks the exact cycle start.
- **Negative operands:** Exactly one negative sign is emitted when signs differ.
- **Internal zero digits:** Quotient zero is appended normally during long division.
- **Fixed-width overflow:** Convert to a wider type before absolute value and multiplication outside Python.
