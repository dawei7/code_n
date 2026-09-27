# Guided Example: Difference Between Element Sum and Digit Sum of an Array

## 1. The instance and the two quantities

Take the first official instance, `nums = [1,15,6,3]`, whose declared answer is
$9$. Two totals are needed:

- the **element sum** $E = \sum_{i} \texttt{nums}[i]$, which adds each value once
  as a whole number;
- the **digit sum** $D$, which adds every decimal digit appearing anywhere in
  `nums`, counting repeated digits separately.

For this instance $E = 1 + 15 + 6 + 3 = 25$ and $D = 1 + 1 + 5 + 6 + 3 = 16$, so
the required absolute difference is $\lvert 25 - 16 \rvert = 9$.

The instance is small but not trivial: `15` is the only value with more than one
digit, so exactly one element pulls the two totals apart. That single element is
enough to expose the whole mechanism, because every other element contributes
identically to both totals.

## 2. The state: one accumulator of per-element differences

The two totals never need to be materialized separately. Writing
$s(a)$ for the digit sum of a single value $a$, the target is

$$
\lvert E - D \rvert = \Bigl\lvert \sum_{i} \bigl(\texttt{nums}[i] - s(\texttt{nums}[i])\bigr) \Bigr\rvert ,
$$

so a single running accumulator can carry the whole computation: visit the
elements in order, and for each one add the difference between the value and its
own digit sum. The accumulator's meaning after $k$ elements is
$\sum_{i \le k} \bigl(\texttt{nums}[i] - s(\texttt{nums}[i])\bigr)$, and the
answer is its absolute value when the sweep ends. Nothing about one element
influences another, so the sweep order does not even matter to the result.

## 3. Where the per-element difference comes from

Decimal notation is a weighted sum of digits. If $a$ has digits
$d_{m-1} d_{m-2} \dots d_1 d_0$, then

$$
a = \sum_{k \ge 0} d_k \, 10^{k},
\qquad
s(a) = \sum_{k \ge 0} d_k ,
\qquad
a - s(a) = \sum_{k \ge 0} d_k \bigl(10^{k} - 1\bigr).
$$

Every weight $10^{k} - 1$ is non-negative: it is $0$ in the units place, $9$ in
the tens place, $99$ in the hundreds place, $999$ in the thousands place, and in
general $9$ times a repunit. The digits of $a$ therefore separate into two roles
— the units digit contributes to $a$ and to $s(a)$ equally, while every higher
digit contributes $9$, $99$, $999, \dots$ more to $a$ than to $s(a)$.

| Position $k$ | Place weight $10^{k}$ | Excess weight $10^{k} - 1$ | Meaning for one digit |
|---|---|---|---|
| 0, units | 1 | 0 | contributes the same amount to the value and to the digit sum |
| 1, tens | 10 | 9 | contributes 9 more to the value than to the digit sum |
| 2, hundreds | 100 | 99 | contributes 99 more |
| 3, thousands | 1000 | 999 | contributes 999 more |

| Value $a$ | Digits by position (thousands, hundreds, tens, units) | Excess contributions $d_k (10^{k} - 1)$ | $s(a)$ | $a - s(a)$ |
|---|---|---|---|---|
| 1 | 0, 0, 0, 1 | $0 + 0 + 0 + 0$ | 1 | 0 |
| 15 | 0, 0, 1, 5 | $0 + 0 + 1 \cdot 9 + 0$ | 6 | 9 |
| 305 | 0, 3, 0, 5 | $0 + 3 \cdot 99 + 0 + 0$ | 8 | 297 |
| 1000 | 1, 0, 0, 0 | $1 \cdot 999 + 0 + 0 + 0$ | 1 | 999 |
| 1999 | 1, 9, 9, 9 | $1 \cdot 999 + 9 \cdot 99 + 9 \cdot 9 + 0$ | 28 | 1971 |
| 2000 | 2, 0, 0, 0 | $2 \cdot 999 + 0 + 0 + 0$ | 2 | 1998 |

The zero digits are the point of the `305`, `1000`, and `2000` rows: a zero digit
adds nothing to the digit sum but the *position* it occupies still carries the
full place weight inside the value, so the excess is produced by the non-zero
digits alone while the value keeps every position's worth.

## 4. Executing the sweep on `nums = [1,15,6,3]`

| Step | Value `nums[i]` | Its digits | $s(\texttt{nums}[i])$ | Difference added | Running accumulator | Running element sum $E$ | Running digit sum $D$ |
|---|---|---|---|---|---|---|---|
| 0, before the sweep | — | — | — | — | 0 | 0 | 0 |
| 1 | `1` | 1 | 1 | $1 - 1 = 0$ | 0 | 1 | 1 |
| 2 | `15` | 1, 5 | 6 | $15 - 6 = 9$ | 9 | 16 | 7 |
| 3 | `6` | 6 | 6 | $6 - 6 = 0$ | 9 | 22 | 13 |
| 4 | `3` | 3 | 3 | $3 - 3 = 0$ | 9 | 25 | 16 |

The accumulator reaches $9$, and the separately tracked $E$ and $D$ confirm it,
since $25 - 16 = 9$. Single-digit values move the accumulator by nothing at all,
which is why an instance of single-digit values such as `nums = [1,2,3,4]`
answers $0$: both totals equal $10$ there, and no element can separate them.

Extracting the digits of one value is a repeated division-and-remainder sweep:
the units digit is the remainder modulo $10$, and the value is then shifted down
by a factor of $10$ to expose the next digit. Since every value in this problem
is at least $1$, the sweep terminates on the value becoming $0$.

## 5. The invariant, and a free correctness check

Two facts hold throughout the sweep and together justify the answer.

**Monotonicity.** Each added difference is non-negative, because
$a - s(a) = \sum_k d_k (10^{k} - 1) \ge 0$: every digit is non-negative and every
excess weight is non-negative. Consequently the accumulator is non-decreasing,
$E \ge D$ always, and the absolute value in the statement never actually flips a
sign. The partial accumulator is a rank-like quantity that only ever rises.

**Divisibility by nine.** Since $10^{k} - 1 = 9 \cdot (10^{k} - 1)/9$ for $k \ge 1$
and the $k = 0$ term vanishes, every excess weight is a multiple of $9$, so the
final answer is always a multiple of $9$. This is the congruence
$a \equiv s(a) \pmod 9$ aggregated over the array, and it gives a zero-cost audit
of any computed result.

| Instance | Element sum $E$ | Digit sum $D$ | $\lvert E - D \rvert$ | Multiple of 9? |
|---|---|---|---|---|
| `[1,15,6,3]` | 25 | 16 | 9 | yes, $9 \cdot 1$ |
| `[1,2,3,4]` | 10 | 10 | 0 | yes, $9 \cdot 0$ |
| `[2000]` | 2000 | 2 | 1998 | yes, $9 \cdot 222$ |
| `[10,101,1000]` | 1111 | 4 | 1107 | yes, $9 \cdot 123$ |
| `[7,42,305,1999]` | 2353 | 49 | 2304 | yes, $9 \cdot 256$ |

For `[10,101,1000]` the digit sum is only $1 + 0 + 1 + 0 + 1 + 0 + 0 + 0 = 4$
even though the values are large, because a digit of $0$ is counted as a digit
without adding anything; the accumulator is dominated by the place weights of the
lone non-zero digits.

## 6. Traps and boundary behaviour

| Situation | What goes wrong if handled carelessly | Correct behaviour |
|---|---|---|
| a value with trailing zeros, such as `10` or `1000` | stopping digit extraction when the value first becomes divisible by ten loses only zero digits, so $s$ is fine, but a positional shortcut that drops the whole position underestimates the value | extract digits position by position; the units digit of `1000` is $0$ and the higher digits are what remain |
| a value with an internal zero, such as `305` | treating the gap as "no digit" is harmless for $s$ but must not shorten the value | the hundreds digit $3$ still contributes $3 \cdot 100$ to the element sum |
| repeated digits, such as `1999` | counting the digit multiset as a set would give $s = 1 + 9 = 10$ | digits are summed with multiplicity, so $s = 28$ |
| the largest allowed value, `2000` | assuming at most three digits truncates it | four positions are needed; the largest per-element difference is $2000 - 2 = 1998$ |
| a single element, such as `[1]` | a sweep that expects at least two elements is unnecessary | one element yields $1 - 1 = 0$ |
| the absolute value in the statement | computing $D - E$ returns a negative number | $E \ge D$ always, so the difference is already non-negative; the absolute value is a formality that costs nothing |
| a wrong digit sum | a silent hand-computation error survives | the multiple-of-nine test rejects any result that is not divisible by $9$ |

One more semantic trap deserves a sentence: the digit sum is a property of the
*decimal writing* of the values, not of their binary or hexadecimal form. The
identity $a - s(a) = \sum_k d_k (10^{k} - 1)$ is specific to base $10$, and in a
base $b$ the excess weights would be $b^{k} - 1$, so the divisibility check would
become divisibility by $b - 1$. Using any other base here produces answers that
look plausible but are wrong.

## 7. Time and auxiliary space

Let $n$ be the number of elements and let $L(a)$ be the number of decimal digits
of a value $a$, so that $L(a) = \lfloor \log_{10} a \rfloor + 1$. The sweep does
constant work per element plus one step per digit, so the running time is
$O\bigl(\sum_i L(\texttt{nums}[i])\bigr) = O\bigl(n \log_{10} \max_i \texttt{nums}[i]\bigr)$;
with the documented bound $\texttt{nums}[i] \le 2000$ this is at most four digit
steps per element, hence effectively $\Theta(n)$.

Auxiliary space is $O(1)$: the accumulator, the current digit remainder, and the
loop index are the only stored values, and each value's digits are consumed as
they are produced rather than kept. Nothing proportional to $n$ is allocated
beyond the input, and the answer is a single integer.