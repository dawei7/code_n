## General

**Identify the only comma threshold inside the domain**

Standard decimal formatting groups digits in blocks of three from the right. A number gets its first comma when it reaches four digits:

$$
1000=\text{"1,000"}.
$$

The second comma does not appear until seven digits:

$$
1{,}000{,}000=\text{"1,000,000"}.
$$

This problem limits `n` to `100000`, which is below one million. Therefore every integer in the complete input domain belongs to exactly one of two categories:

- values from one through 999 contain zero commas;
- values from 1000 through `n` contain exactly one comma.

No valid input can produce a number with two or more commas. This bounded-domain fact reduces the total from a formatting problem to counting how many integers lie in one suffix of the range.

**Count the inclusive suffix**

When `n\ge1000`, the comma-bearing integers are

$$
1000,1001,\ldots,n.
$$

The number of integers in an inclusive interval `[a,b]` is `b-a+1`. Substituting `a=1000` and `b=n` gives

$$
n-1000+1=n-999.
$$

Every one of those integers contributes exactly one comma, so the interval size is also the total comma count.

When `n<1000`, that interval is empty and the answer is zero. The source combines both cases as

`max(0, n - 999)`.

If `n-999` is negative, `max` selects zero. If it is positive, it is exactly the inclusive suffix length. At the boundary `n=999`, the expression is zero; at `n=1000`, it is one.

**Why there is no hidden digit-length correction**

Four-, five-, and six-digit numbers all have one comma:

- `1000` formats as `"1,000"`;
- `10000` formats as `"10,000"`;
- `100000` formats as `"100,000"`.

The number of digits in the leftmost group changes from one to three, but the number of boundaries between three-digit groups remains one. Therefore the contribution does not change anywhere between 1000 and the maximum input.

Ordinary decimal notation has no leading zeros. A value such as one is `"1"`, not `"000,001"`, so smaller values do not acquire artificial comma groups.

**Examples and boundary checks**

For `n=1002`, the contributing values are 1000, 1001, and 1002. Their count is

$$
1002-999=3,
$$

and each has one comma.

For `n=998`, `n-999=-1`. The maximum with zero returns zero, consistent with every number having at most three digits.

For the largest input `n=100000`, the answer is

$$
100000-999=99001.
$$

Those are exactly the integers from 1000 through 100000 inclusive, each contributing one comma.

**A direct indicator derivation**

Let `c(x)` be the comma count of one formatted integer. Within the stated domain,

$$
c(x)=
\begin{cases}
0,&x<1000,\\
1,&x\ge1000.
\end{cases}
$$

The requested answer is

$$
\sum_{x=1}^{n}c(x).
$$

This sum counts one for each $x\ge1000$ and zero otherwise, so it equals the cardinality of $[1000,n]$ when nonempty. That cardinality is exactly the source expression. Each possible formatted number is accounted for once, and no actual string formatting is required.

## Complexity detail

The method performs one subtraction and one maximum comparison. Its running time is `O(1)` and it stores only constant-sized integer values, giving `O(1)` auxiliary space. These bounds match the manifest.

The solution's constant-time nature depends on the explicit upper bound below the second comma threshold. In a generalized version with arbitrarily large `n`, additional thresholds at powers of 1000 would need to be counted; ID 3871 uses that general method.

The answer fits comfortably in the stated range. Python integer arithmetic is exact, and no strings or collections are allocated.

## Alternatives and edge cases

- **Format every integer:** Loop from one through `n`, call a comma formatter, and count characters. This is direct but takes time proportional to all formatted output instead of constant time.
- **Count decimal digits per integer:** Computing `(\text{digits}-1)//3` for every value still takes `O(n)` iterations. The range bound makes a single threshold count sufficient.
- **General power-of-1000 loop:** Add `n-x+1` for thresholds `x=1000,1000000,\ldots`. It is correct here but performs only the first iteration because later thresholds exceed the domain.
- **Use `n-1000`:** This misses one endpoint. Inclusive range `[1000,n]` has `n-1000+1` values.
- **Use `n-999` without clamping:** It becomes negative below the threshold, but a count cannot be negative. `max(0,\cdot)` represents the empty interval.
- **`n=1`:** Every number in the range has one digit, so the result is zero.
- **`n=999`:** This is the largest no-comma bound and returns zero.
- **`n=1000`:** Exactly one formatted number contains a comma and the result is one.
- **`n=100000`:** Six digits still require only one comma; the second threshold is one million.
- **Leading zeros:** They are excluded by ordinary decimal representation. Treating numbers as fixed-width strings would solve a different problem.
- **Locale-dependent formatting:** The problem defines comma placement explicitly. Do not rely on locale conventions that may use periods, spaces, or different grouping.
- **Bound dependence:** Extending the constraint to one million or above invalidates the one-comma-per-number simplification; use the threshold-superposition method instead.
