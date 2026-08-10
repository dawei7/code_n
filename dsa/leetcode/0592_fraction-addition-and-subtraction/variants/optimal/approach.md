## General

The usual way to add fractions is to repeatedly create a common denominator for the running result and the next term. This solution exploits a special constraint to make parsing and arithmetic simpler: every input denominator is an integer from 1 through 10. It chooses one fixed denominator divisible by every possible input denominator:

$$
y=6\cdot7\cdot8\cdot9\cdot10=30240.
$$

This is not the least common multiple—$\operatorname{lcm}(1,\ldots,10)=2520$—but it does not need to be minimal. It only needs to be divisible by each legal denominator. Since 30240 has that property, every input fraction can be converted exactly into units of $1/30240$.

The variable `x` stores the signed numerator of the running total over fixed denominator `y`. Initially, `x = 0`, so the represented value is $0/30240$.

**Normalizing the first sign**

Every later fraction begins with `+` or `-` because operators separate terms. A positive first fraction may omit its plus sign. The source makes all terms follow one parsing pattern:

```python
if expression[0].isdigit():
    expression = '+' + expression
```

After this normalization, index `i` always points to a term’s sign at the top of the loop. A leading negative expression already has a sign and is left unchanged.

**Extracting one term**

The sign becomes `-1` for `-` and `1` otherwise. The parser advances past it, then moves `j` until the next plus/minus sign or the end:

```python
while j < n and expression[j] not in '+-':
    j += 1
```

The substring `expression[i:j]` therefore contains exactly one unsigned fraction such as `"10/7"`. Splitting at `/` yields numerator text `a` and denominator text `b`.

The input grammar guarantees a valid sequence, positive raw numerators and denominators, and no embedded signs inside a fraction. The parser can consequently treat every plus or minus as a term boundary without needing a more general expression tokenizer.

**Converting into fixed-denominator units**

For signed fraction

$$
\text{sign}\cdot\frac{a}{b},
$$

the equivalent numerator over $y$ is

$$
\text{sign}\cdot a\cdot\frac{y}{b}.
$$

The update is:

```python
x += sign * int(a) * y // int(b)
```

Integer division is exact because every legal $b\in[1,10]$ divides 30240. No remainder is discarded. This is the critical reason the fixed denominator works; choosing an arbitrary large number that was not divisible by every denominator would silently corrupt fractions.

The parser repeats until every term has contributed its signed count of $1/y$ units. For `"1/3-1/2"`, the contributions are $10080$ and $-15120$, so `x = -5040` over 30240, equal to $-1/6$.

**Reducing only once**

The accumulated fraction `x/y` may be reducible. Let

$$
z=\gcd(x,y).
$$

Python’s `gcd` returns a nonnegative greatest common divisor even when `x` is negative. Dividing both values by `z` preserves the fraction and removes every common factor. Since `y` begins positive and `z` is positive, the output denominator remains positive; any negative sign stays on `x`.

For a zero result, `gcd(0,30240)=30240`, so reduction gives `0/1` automatically. For an integer result, all denominator factors cancel and the denominator similarly becomes one.

**Why the algorithm is correct**

Maintain the invariant that after processing some prefix of complete terms,

$$
\frac{x}{y}
$$

equals the arithmetic sum of exactly those terms. Initially both sides are zero. For the next term $\operatorname{sign}a/b$, divisibility gives an integer $y/b$, and the update changes the represented value to

$$
\frac{x+\operatorname{sign}a(y/b)}{y}
=
\frac{x}{y}+\operatorname{sign}\frac{a}{b}.
$$

Thus, the invariant is preserved. After the final term, `x/y` equals the whole expression. Dividing numerator and denominator by their GCD preserves its numeric value and makes them coprime, so the formatted string is exactly the required irreducible fraction.

This approach relies specifically on the denominator bound. If denominators could be arbitrary, 30240 would not be universal and the algorithm would need a running least common multiple or cross multiplication.

## Complexity detail

Let $n$ be the expression length and let $V$ bound the magnitude of the final accumulator values. The two indices move forward across the expression, so parsing takes $O(n)$ character work. Each legal fraction has very short bounded numeric fields under the given constraints. One Euclidean GCD costs $O(\log V)$ arithmetic iterations. A precise high-level bound is $O(n+\log V)$, which is safely covered by the manifest’s coarser $O(n\log V)$.

The numeric state `x`, `y`, indices, sign, and current fields is constant-sized under the stated bounded domain. However, the exact Python source executes `expression = '+' + expression` for a leading positive term. Strings are immutable, so that creates a new $O(n)$ string and makes the exact implementation’s peak auxiliary space $O(n)$ in that branch. With an implicit default first sign or index logic, the arithmetic/parser design itself would use $O(1)$ auxiliary space as declared by the manifest.

Substring `s` is bounded by one fraction’s syntax here, so it is constant under the constraints. Python integers also remain within controlled bounds, though formal bit-complexity could charge for large-integer arithmetic in a generalized version.

## Alternatives and edge cases

- **Running cross multiplication:** Maintain `num/den` and combine `a/b` as `(num*b + sign*a*den)/(den*b)`, reducing along the way or at the end. It works for arbitrary denominators but can grow intermediates.
- **Running LCM:** Use `lcm(den,b)` as the smallest next common denominator. It limits intermediate size and generalizes beyond denominators 1–10.
- **Regular-expression tokenization:** Extract signed numerator/denominator pairs directly. Concise, but manual scanning is easier to derive and avoids regex-specific knowledge.
- **Hard-coded 30240:** Correct only because every denominator is in $[1,10]$. If that contract changes, the constant must not be reused blindly.
- **First positive fraction:** The source prepends `+` so every loop starts at a sign.
- **First negative fraction:** Its existing sign is parsed directly.
- **Zero total:** GCD reduction produces exactly `"0/1"`.
- **Integer total:** Complete cancellation produces denominator 1, as required.
- **Negative result:** `gcd` is nonnegative, so the sign remains on the numerator rather than moving to the denominator.
- **Denominator 10:** It divides 30240 exactly; the fixed-denominator update remains integral.
- **One fraction:** It is converted to the common denominator and reduced back to its already irreducible value.
- **No intermediate reduction:** Safe under the small bounded term count and final 32-bit guarantee, though other languages might need wider intermediate integers.
- **Space fidelity:** Prepending to an immutable Python string is an actual $O(n)$ allocation; the manifest’s $O(1)$ target belongs to a parser that avoids copying the input.
