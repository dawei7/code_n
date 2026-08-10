## General

The definition appears to require a frequency table:

$$
\operatorname{score}(n)
=\sum_{\text{distinct digits }d} d\cdot\operatorname{freq}(d).
$$

However, multiplication by the frequency simply means adding the digit once for each occurrence. If digit $d$ appears $f$ times, then

$$
d\cdot f
=\underbrace{d+d+\cdots+d}_{f\text{ copies}}.
$$

Summing this identity over all distinct digits shows that the score is exactly the ordinary sum of all decimal digit occurrences. The source uses this simplification and never builds a frequency array.

**Why grouping and direct summation are equivalent**

Suppose the digits are $1,2,2$. The frequency form groups the two copies of digit 2:

$$
1\cdot1+2\cdot2=5.
$$

The occurrence form adds them directly:

$$
1+2+2=5.
$$

Every position belongs to exactly one digit group. Expanding every product $d\cdot\operatorname{freq}(d)$ produces one $d$ for every position containing that digit, with no missing or duplicated occurrence. Therefore direct digit summation is not a shortcut that changes the definition; it is the same sum with its terms regrouped.

**Extract the least significant digit**

For a positive integer `n`, Python's

`divmod(n, 10)`

returns two values:

- the quotient after removing the least significant decimal digit;
- the remainder from zero through nine, which is that removed digit.

The assignment

`n, x = divmod(n, 10)`

simultaneously replaces the local `n` with its remaining prefix and stores the extracted digit in `x`. The source then adds `x` to `ans`.

For example, beginning with `n = 122`:

- `divmod(122, 10)` gives `(12, 2)`;
- `divmod(12, 10)` gives `(1, 2)`;
- `divmod(1, 10)` gives `(0, 1)`.

The accumulated total is $2+2+1=5$. Digits are visited from right to left, but addition does not depend on order.

**Loop meaning**

At the beginning of every iteration:

- `n` contains the decimal prefix whose digits have not yet been processed;
- `ans` is the sum of every digit already removed from the right.

`divmod` separates exactly one new digit. Adding it extends the processed suffix by one position and preserves this meaning for the next iteration.

Integer division by ten shortens a positive decimal integer by one digit. Eventually the remaining prefix becomes zero and `while n` ends. At that point no unprocessed digit remains, so `ans` is the sum of all original digit occurrences and therefore the required frequency score.

**Zero digits are handled correctly**

A zero in the middle or end of the decimal representation is still extracted as remainder zero. Adding it changes nothing, matching its grouped contribution:

$$
0\cdot\operatorname{freq}(0)=0.
$$

For `n = 101`, the extracted sequence is $1,0,1$, and the answer is two. The loop does not stop at the internal zero because its condition tests the remaining quotient `n`, not the current digit `x`.

**Why the local mutation is harmless**

The parameter name `n` is rebound to smaller quotients. Python integers are immutable values, so this does not alter an integer object owned by the caller. The original value is no longer needed once its digits are being consumed.

No string conversion is required. Arithmetic extraction avoids allocating a decimal-character representation and directly exposes each digit.

**The positive-input guarantee**

The contract says $n\ge1$, so the loop executes at least once. If zero were supplied outside the contract, the method would return zero without entering the loop, which also agrees with the natural digit-sum value, but no special case is necessary for the stated domain.

## Complexity detail

Let

$$
D=\left\lfloor\log_{10}n\right\rfloor+1
$$

be the number of decimal digits. Every loop iteration removes one digit, so there are exactly $D$ iterations. Each performs one division-with-remainder and one addition under the usual fixed-word arithmetic model. Time complexity is $O(D)$.

The method stores only `ans`, the shrinking local `n`, and one digit `x`. Additional space is $O(1)$.

Since the constraints limit `n` to $10^9$, there are at most ten decimal digits, but the $O(D)$ form explains how the method scales conceptually. The manifest's time and space bounds accurately describe the source.

## Alternatives and edge cases

- **Build a ten-entry frequency array:** Count each digit, then evaluate the definition literally. This is correct and still $O(D)$ time with $O(1)$ fixed-domain space, but the table is unnecessary because the weighted frequency sum equals the digit sum.
- **Convert to a string:** `sum(int(ch) for ch in str(n))` is concise and linear, but it allocates a $D$-character representation and iterator machinery.
- **Use a set of digits:** A set would discard repeated occurrences, yet frequency affects the score. For `122`, counting distinct digits only would incorrectly produce $1+2=3$.
- **Multiply each occurrence by its total frequency again:** Direct iteration already visits the digit once per occurrence. Multiplying during that scan would double-count frequency.
- **Repeated digit:** Every occurrence is extracted and added, producing exactly `digit * frequency` in total.
- **Internal zero:** It is extracted and adds zero; later more significant digits are still processed.
- **Trailing zero:** The first `divmod` returns zero as the digit, then continues with the quotient.
- **Number `10^9`:** The nine zero digits contribute nothing and the leading one contributes one.
- **One-digit input:** One iteration extracts that digit and returns it.
- **Digit zero as a distinct group:** Although it appears in the formal sum, its contribution is always zero, so not storing its frequency loses no score.
- **Right-to-left processing:** Addition is commutative, so reversing the digit visitation order has no effect.
- **Caller-visible mutation:** Reassigning the local integer parameter does not modify caller state because integers are immutable.
- **Out-of-contract zero input:** The loop would return zero naturally, though the formal constraints begin at one.
