## General

**Accumulate two totals in one pass**

`x` is the element sum and `y` is the digit sum. Both begin at zero.

For every array value `v`:

1. add the complete value to `x`;
2. repeatedly extract its decimal digits and add them to `y`.

After all values, `x-y` is returned.

The statement asks for an absolute difference, but positivity guarantees the element sum is never below the digit sum. The proof appears below, so no `abs` call is necessary.

**Extract decimal digits arithmetically**

The last digit of positive integer `v` is `v%10`. Adding this remainder contributes that digit to `y`.

Integer division `v//=10` removes the last digit. Repeating until `v` becomes zero visits every decimal digit exactly once.

For 15:

- remainder 5 contributes five, quotient becomes one;
- remainder 1 contributes one, quotient becomes zero.

Its digit-sum contribution is six.

**Why rebinding `v` does not change the input**

`v` is the local loop variable referencing an immutable Python integer. `v//=10` rebinds that local name to a new integer; it does not assign into `nums`.

The full original value has already been added to `x` before digit extraction begins.

**Trace the first sample**

For `[1,15,6,3]`:

- element sum becomes $1+15+6+3=25$;
- digit contributions are $1$, $1+5$, $6$, and $3$, totaling 16.

The returned difference is $25-16=9$.

**Why element value is at least its digit sum**

Write positive integer `v` with decimal digits $d_0,d_1,\ldots,d_p$, where $d_0$ is the units digit:

$$
v=\sum_{j=0}^{p}d_j10^j.
$$

Its digit sum is

$$
\sum_{j=0}^{p}d_j.
$$

Since $10^j\ge1$ and every digit $d_j\ge0$,

$$
d_j10^j\ge d_j
$$

for each position. Summing gives `v>=digitSum(v)`.

This holds independently for every positive array element. Summing across the array yields `x>=y`. Therefore,

$$
\lvert x-y\rvert=x-y,
$$

which justifies the exact return expression.

**When equality occurs**

For a one-digit positive number, its value equals its sole digit, so its individual difference is zero.

Any multi-digit positive number with a nonzero digit beyond the units position has a strictly larger place-value contribution than that digit alone, producing a positive difference. Since multi-digit numbers have a nonzero leading digit, every such number makes the total difference positive.

Thus an array has result zero exactly when all its values are single-digit under the positive-input contract.

**The difference can be accumulated per digit position**

Subtracting a number's digit sum from the number gives

$$
v-\operatorname{digitSum}(v)
=
\sum_{j=0}^{p}d_j(10^j-1).
$$

The units-position factor is $10^0-1=0$, so a units digit never creates any difference by itself. Tens and higher positions have positive factors, explaining exactly where the result comes from.

Summing this identity over all array elements shows that computing two global totals and subtracting them is equivalent to summing each element's nonnegative individual difference. No cancellation between different elements can make the result negative.

For 15, the tens digit contributes $1(10-1)=9$ and the units digit contributes $5(1-1)=0$, matching $15-(1+5)=9$.

**Every digit occurrence counts**

Repeated digits within or across numbers each contribute separately. The loop adds remainders by position and does not deduplicate them.

This matches the digit-sum definition.

**Why string conversion is not needed**

One could convert each number to text and sum converted characters. Arithmetic remainder and quotient operations avoid allocating those strings and keep auxiliary space constant.


After processing some prefix of `nums`, `x` equals the sum of its original values and `y` equals the sum of all their decimal digits. Adding the next original value and extracting each of its digits preserves the invariant.

At completion, these are exactly the two defined totals. Their difference is nonnegative by the place-value proof, so the returned `x-y` equals the requested absolute difference.

## Complexity detail

Let $S$ be the total number of decimal digits across all elements. The outer loop visits each number, and the inner loops perform exactly one iteration per digit. Time is $O(S)$.

Only `x`, `y`, and local `v` are stored, so auxiliary space is $O(1)$.

With values at most 2000, each has at most four digits, so $S\le4n$ and runtime is also $O(n)$ under the given bound.

## Alternatives and edge cases

- **String conversion:** Sum `int(c)` for every character of every decimal representation; it is simpler but allocates strings.
- **Single-digit array:** Element sum and digit sum are equal, producing zero.
- **Multi-digit value:** It guarantees a positive individual difference.
- **Repeated digits:** Count every occurrence.
- **Positive inputs:** They make the no-`abs` proof straightforward.
- **Local mutation:** Dividing loop variable `v` does not alter `nums`.
- **Value 1000:** Zero digits contribute zero but are still naturally extracted.
- **No overflow:** The stated sums fit ordinary integer ranges, and Python grows automatically.
- **Absolute difference:** `x-y` is already nonnegative.
- **One pass:** Both totals are accumulated together.
