## General

**Separate complete weeks from the final partial week**

The seven-day deposit pattern repeats with one change: each new week's Monday amount is one dollar larger than the preceding week's Monday.

`k, b = divmod(n, 7)` computes both parts of division by seven:

- `k` is the number of complete weeks.
- `b` is the number of remaining days after those weeks.

Thus `n = 7k + b` with `0 <= b < 7`. The source calculates the total for the $k$ complete weeks as `s1` and the partial week as `s2`.

**Find the sum of one complete week**

In the first week, deposits are one through seven, totaling

$$
1+2+3+4+5+6+7=28.
$$

The second week starts at two and ends at eight, so its total is 35, exactly seven more. Every later complete week also increases each of seven daily deposits by one, increasing the weekly total by seven.

The complete-week totals form the arithmetic sequence

$$
28,\ 35,\ 42,\ \ldots
$$

with first term 28 and common difference seven.

**Sum all complete weeks in constant time**

If there are $k$ complete weeks, the last weekly total is

$$
28+7(k-1).
$$

An arithmetic sequence with first value $F$, last value $L$, and $k$ terms sums to $(F+L)k/2$. The source writes that formula as

`s1 = (28 + 28 + 7 * (k - 1)) * k // 2`.

The two 28 values are the first term and the constant part of the last term. Integer floor division is exact here because the sum of an integer arithmetic sequence is an integer.

When `k = 0`, the expression inside the parentheses describes a fictitious last term of 21, but multiplication by zero makes `s1 = 0` before division. No special branch is necessary.

**Describe the partial week's daily sequence**

After $k$ complete weeks, the next Monday deposit is `k + 1` dollars. If `b` remaining days exist, their deposits are

$$
k+1,\ k+2,\ \ldots,\ k+b.
$$

The first value is $k+1$, the last is $k+b$, and there are $b$ values.

The source's expression

`k + 1 + k + 1 + b - 1`

simplifies to $(k+1)+(k+b)$, exactly first plus last. Therefore

`s2 = (k + 1 + k + 1 + b - 1) * b // 2`

is the arithmetic-sequence sum of the partial week.

When `b = 0`, multiplication by zero makes `s2` zero even though there is no real last partial-day deposit. This again avoids a branch safely.

**Combine disjoint day ranges**

`s1` covers days one through `7k`. `s2` covers the next `b` days, from `7k+1` through `7k+b=n`. These ranges are disjoint and together contain exactly the first $n$ days, so `return s1 + s2` is the required total.

**Trace the ten-day example**

For `n = 10`, `divmod(10,7)` gives `k=1` and `b=3`.

The full-week formula gives 28. The next Monday starts at `k+1=2`, and the three remaining deposits are two, three, and four, totaling nine. The result is `28+9=37`.

For `n = 20`, there are two full weeks and six remaining days. Full-week totals are 28 and 35. The third partial week deposits three through eight, totaling 33. Their sum is 96.

**Why no day-by-day simulation is needed**

Both the weekly totals and the within-week deposits are arithmetic sequences. Once their first value, last value, and count are known from quotient and remainder, their sums contain all the same information as an explicit loop.

The derivation also shows that the rule about subsequent Mondays is not the same as continuing one ever-increasing daily sequence: after Sunday seven, the second Monday is two, not eight. Week decomposition captures that reset.

## Complexity detail

The method performs one `divmod` call and a fixed number of additions, multiplications, shifts implicit in arithmetic, and divisions. The number of operations does not depend on $n$, so time is $O(1)$ under the standard fixed-width arithmetic model.

Only `k`, `b`, `s1`, and `s2` are stored, giving $O(1)$ auxiliary space. These bounds match the manifest.

With `n <= 1000`, all values are small. Python integer arithmetic would also avoid overflow for larger generalized inputs, though its bit complexity would eventually depend on the number of digits.

## Alternatives and edge cases

- **Simulate every day:** Compute week and weekday deposits directly in $O(n)$ time. It is easy to verify but unnecessary once the arithmetic sequences are recognized.
- **Loop by week:** Sum at most seven days inside each week, taking $O(n/7)$ week iterations and constant space.
- **Closed formula expansion:** Algebraically simplify `s1+s2` into one polynomial in quotient and remainder. It is equally constant-time but less directly tied to the two sequences.
- **`n < 7`:** `k=0`, so only the first partial week contributes.
- **`n = 7`:** `b=0`, giving exactly the first full-week total 28.
- **Exact multiple of seven:** The partial formula is multiplied by zero and contributes nothing.
- **One day:** The partial sequence has first and last value one, returning one.
- **Week boundary:** Day eight deposits two dollars, which comes from the next Monday start `k+1`.
- **Integer division:** Both arithmetic-series products are even, so `//2` loses no fraction.
- **No mutation:** The input integer `n` is only read by `divmod`.
- **Variable meaning:** `k` counts completed full weeks, while `b` counts days in the unfinished week.
