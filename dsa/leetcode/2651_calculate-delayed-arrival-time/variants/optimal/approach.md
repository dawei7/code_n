## General

**Clock hours repeat every 24 steps**

Adding the delay gives an absolute hour offset:

$$
T=\texttt{arrivalTime}+\texttt{delayedTime}.
$$

But a 24-hour clock displays only one of the canonical hour labels:

$$
0,1,2,\ldots,23.
$$

Hours that differ by a multiple of 24 refer to the same displayed time on different days. Therefore, the correct normalization is the remainder:

$$
T\bmod24.
$$

The exact solution implements this formula in one return statement.

**Why ordinary addition is not enough**

For an arrival at 15 delayed by five hours, the sum is 20, already inside the valid clock range. Remainder by 24 leaves it unchanged:

$$
20\bmod24=20.
$$

For arrival 13 delayed by 11, the sum is 24. The 24-hour clock rolls over:

$$
24\bmod24=0.
$$

Hour zero represents 00:00, exactly as required.

If the sum is 30, remainder produces six, representing 06:00 on the following day.

**Modulo captures the cyclic equivalence**

For any nonnegative integer $T$, Euclidean division writes:

$$
T=24q+r,
\qquad 0\le r<24.
$$

$q$ counts complete days passed, while $r$ is the hour within the current day. The problem asks only for the displayed hour, so $q$ is irrelevant and $r$ is the answer.

Python's `% 24` returns exactly this $r$ for the positive input sum.

**Why 24 maps to zero rather than 24**

In 24-hour notation, the labels run from zero through 23. `24:00` is another notation for the start of the next day, displayed here as zero.

Returning 24 would violate the output domain and treat the same instant differently from zero. Modulo chooses the canonical representative.

**The constraints limit wrapping but the formula is general**

`arrivalTime` is below 24 and `delayedTime` is at most 24, so their sum is at most 47. At most one full day boundary is crossed.

One could therefore write:

- add the values;
- subtract 24 when the sum is at least 24.

Modulo is shorter, less branchy, and continues to work if larger delays are later allowed.

**No minutes or dates are involved**

Both inputs are whole hours. There is no minute carry, time zone, calendar date, or daylight-saving adjustment.

The calculation is purely modular integer arithmetic on a fixed 24-hour cycle. Adding date APIs would introduce concepts absent from the contract.


Let:

$$
A=\texttt{arrivalTime},
\qquad
D=\texttt{delayedTime}.
$$

Without clock wrapping, delayed arrival is $A+D$ hours from the same reference midnight.

Every 24 elapsed hours returns the displayed clock to the same hour. Thus two totals represent the same displayed hour exactly when they are congruent modulo 24.

The unique representative of $A+D$ in the permitted range $[0,23]$ is:

$$
(A+D)\bmod24.
$$

That is exactly what the function returns, proving correctness.

**Boundary examples**

If arrival is 23 and delay is one:

$$
(23+1)\bmod24=0.
$$

If arrival is one and delay is 24:

$$
(1+24)\bmod24=1.
$$

A full-day delay changes the date but not the clock hour.

If arrival is 23 and delay is 24, the answer remains 23 for the same reason.

**Why integer overflow is irrelevant here**

Inputs are tiny, and Python integers are arbitrary precision in any case. The addition and remainder are exact.

In fixed-width languages, the stated bounds also keep the sum far below any integer limit.

**No mutation or state**

The function is pure: output depends only on its two arguments, and it stores no persistent state.

Repeated calls with the same inputs always return the same hour. The concise expression fully represents the algorithm.

**A compact normalization table**

The sum falls into one of two ranges under the constraints:

- for $2\le T\le23$, no day boundary was reached and `T % 24` equals $T$;
- for $24\le T\le47$, exactly one complete day passed and `T % 24` equals $T-24$.

This case view and the modulo expression are mathematically identical. Modulo is preferable because it encodes both cases without a conditional and automatically extends to sums of 48 or more.

It also shows that the operation discards only complete days. The remainder never changes the relative hour within a day: adding or removing any whole multiple $24q$ leaves the same result because

$$
(T+24q)\bmod24=T\bmod24.
$$

That identity explains why a 24-hour delay preserves the displayed arrival hour even though the train arrives on a later date.

## Complexity detail

The function performs one addition and one remainder operation on bounded integers. Time complexity is $O(1)$.

It allocates no data structure and uses only the expression's temporary integer value, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Conditional subtraction:** Add the inputs and subtract 24 if the sum is at least 24; correct under current bounds but less general.
- **Repeated subtraction loop:** Handles arbitrary delays but takes time proportional to crossed days, unlike modulo.
- **Date/time library:** Unnecessary because the problem contains only whole-hour cyclic arithmetic.
- **Exact sum below 24:** Modulo leaves it unchanged.
- **Exact sum 24:** Returns zero.
- **Sum above 24:** Returns the remaining hour after one wrap.
- **Delay exactly 24:** The displayed hour is unchanged.
- **Arrival 23 plus one:** Wraps to zero.
- **Output range:** Remainder guarantees a value from zero through 23.
- **Positive inputs:** Python modulo has the straightforward nonnegative-remainder behavior used by the proof.
