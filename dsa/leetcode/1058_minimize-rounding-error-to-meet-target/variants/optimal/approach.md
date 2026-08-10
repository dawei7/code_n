## General

**Begin from the smallest possible rounded sum**

Every non-negative price can be rounded either down to its floor or up to its ceiling. If all prices are rounded down, their sum is the smallest total that any permitted choices can produce.

The solution calls this floor sum `mi`:

```python
mi = 0
arr = []
for p in prices:
    p = float(p)
    mi += int(p)
```

Because every price is non-negative, Python's `int(p)` truncation is exactly the mathematical floor. That equivalence would not hold for negative non-integral values, but the input constraints exclude them.

The code parses each three-decimal string into a floating-point value. `mi` accumulates only the integer parts, so after the loop it is the sum obtained by flooring every price.

**Only non-integral prices create a choice**

Inside the same loop, the fractional part is computed and conditionally saved:

```python
if d := p - int(p):
    arr.append(d)
```

The walrus operator assigns the fractional part to `d` and then tests it. A zero fractional part is false, so an integral price is omitted. A positive fractional part is true and is appended to `arr`.

For an integral price such as `"4.000"`, floor and ceiling are both four. It contributes zero rounding error and cannot increase the rounded sum, so it creates no decision and does not belong in `arr`.

For a non-integral price with fractional part `f`:

- Rounding down contributes its floor to the sum and creates error `f`.
- Rounding up contributes one more than its floor and creates error `1 - f`.

Every non-integral price rounded up therefore adds exactly one to the all-floor sum. The actual integer part of that price no longer matters to the choice; only its fractional part determines the error.

**Check whether the target is reachable**

If `F = len(arr)`, the minimum possible rounded sum is `mi` and the maximum is `mi + F`. Every integer between them is reachable because each of the `F` independent non-integral prices can add either zero or one.

The code checks precisely that interval:

```python
if not mi <= target <= mi + len(arr):
    return "-1"
```

If `target < mi`, even rounding everything down is too large. If `target > mi + F`, even rounding every possible price up is too small. In either case, no selection can work.

If the target lies inside the interval, the required number of upward roundings is fixed:

```python
d = target - mi
```

This later assignment reuses the name `d`. From this point onward it no longer means one fractional part; it means the integer count of prices that must be rounded up.

Exactly `d` non-integral prices must use their ceilings. Fewer would make the total too small, and more would make it too large. The optimization question is therefore: which `d` fractional parts should be rounded upward?

**Larger fractions are cheaper to round upward**

For a fractional part `f`, floor error is `f` and ceiling error is `1 - f`. When `f` is close to one, its ceiling is close to the original price, so rounding up is cheap. When `f` is close to zero, rounding up is expensive.

The solution orders fractional parts from largest to smallest:

```python
arr.sort(reverse=True)
```

It then rounds the first `d` fractions up and all remaining fractions down.

An exchange argument shows why this is optimal. Suppose a smaller fraction `b` is rounded up while a larger fraction `a` is rounded down, where `a >= b`. Their current combined error is `a + (1 - b)`. Swapping their choices gives `(1 - a) + b`. The original error exceeds the swapped error by `2(a - b)`, which is non-negative.

Therefore, whenever an upward-rounded fraction is smaller than a downward-rounded one, exchanging their decisions never increases the error and usually decreases it. Repeating such exchanges leads exactly to the arrangement where the `d` largest fractions are rounded up. No other selection can have a smaller total error.

**Compute both parts of the error**

After sorting, `arr[:d]` contains the fractions rounded upward. Each contributes `1 - f`, so their total error is:

```text
d - sum(arr[:d])
```

The suffix `arr[d:]` contains the fractions rounded downward. Each contributes `f`, so its total error is simply:

```text
sum(arr[d:])
```

The code combines them:

```python
ans = d - sum(arr[:d]) + sum(arr[d:])
```

This formula also handles both extremes:

- If `d == 0`, the first slice is empty and every non-integral price is rounded down.
- If `d == len(arr)`, the second slice is empty and every non-integral price is rounded up.

Integral prices contribute neither error nor a decision, so excluding them from both sums is correct.

**Format the required string**

The return statement is:

```python
return f'{ans:.3f}'
```

The format specification produces exactly three digits after the decimal point, including trailing zeros. The function returns a string rather than a numeric value, as required.

**Why the full algorithm is correct**

The floor sum and number of non-integral prices characterize every reachable rounded total. Passing the interval check proves that choosing exactly `target - mi` upward roundings meets the target.

The exchange argument proves that choosing the largest fractional parts for those upward roundings minimizes error among all choices with that required count. The final expression adds the ceiling errors for exactly that prefix and floor errors for exactly the remaining suffix. Thus it computes the minimum possible error for a valid target and formats it correctly.

## Complexity detail

Let `N` be the number of prices and `F` be the number of non-integral prices.

Parsing and scanning all prices takes `O(N)` time. Sorting the `F` fractional parts takes `O(F log F)` time. The two sums over disjoint slices process `F` values in total, although creating those Python slices also copies `O(F)` elements. The exact total time is therefore `O(N + F log F)`, which is `O(N log N)` in the worst case.

`arr` stores `F` floating-point fractions. Sorting and the two temporary slices can use additional linear memory. The exact auxiliary-space bound is `O(F)`.

The manifest records `O(N + K)` time and `O(K)` space, where `K = 1000` is the number of thousandths in one unit. Those bounds describe a counting approach that exploits the exact three-decimal input domain.

Instead of comparison-sorting fractions, parse each fraction as an integer number of thousandths from zero through 999 and count its frequency. Traverse frequency buckets from 999 down to one to choose the required number of upward roundings. Parsing takes `O(N)`, scanning all buckets takes `O(K)`, and the frequency array takes `O(K)` space. This achieves the manifest target and avoids floating-point arithmetic.

The exact source implements the same largest-fraction greedy choice through sorting, so its honest time bound differs from the bucketed optimal implementation.

## Alternatives and edge cases

- **Thousandths frequency buckets for the manifest target:** Parse prices as exact scaled integers, count fractional values from zero through 999, and consume buckets from largest to smallest for upward rounding. This gives `O(N + K)` time and `O(K)` space.
- **Exact integer parsing with sorting:** Convert each price string to thousandths and sort the nonzero remainder values. This retains `O(N + F log F)` time but avoids all binary floating-point representation concerns.
- **Maximum heap:** Keep fractional parts in a heap and extract the `d` largest. This takes `O(N + d log F)` time and `O(F)` space, which can help when `d` is very small but is not as strong as bounded-domain counting.
- **Dynamic programming:** A DP over price count and rounded sum can find a minimum, but every non-integral choice changes the sum by exactly one. The required number of ceilings is already known, so DP is unnecessary.
- **Target below the floor sum:** No rounding choice can reduce a price below its floor, so the function returns `"-1"`.
- **Target above the ceiling sum:** No rounding choice can exceed the ceiling of a price, so the function returns `"-1"`.
- **All prices integral:** `arr` is empty and the only reachable target is `mi`. For that target, `d` is zero and the formatted error is `"0.000"`.
- **Round everything down:** When `target == mi`, `d` is zero and every fractional part contributes its floor error.
- **Round every non-integral price up:** When `target == mi + len(arr)`, the suffix is empty and every fractional part contributes its ceiling error.
- **Equal fractional parts:** Any choice among equal fractions has the same error. Their relative order after sorting is irrelevant.
- **Zero-valued price:** `"0.000"` adds nothing to the floor sum, creates no choice, and contributes zero error.
- **Floating-point accumulation:** The exact source relies on final three-decimal formatting to round small representation noise. Parsing scaled thousandths as integers is a more explicit exact-arithmetic alternative.
- **Walrus-name reuse:** `d` first denotes a fractional part inside the loop and later denotes the number of ceilings. The earlier value is no longer needed, so reuse is safe even though separate names would be clearer.
- **Input preservation:** The list of price strings is not modified. Parsed fractions are stored separately in `arr`.
