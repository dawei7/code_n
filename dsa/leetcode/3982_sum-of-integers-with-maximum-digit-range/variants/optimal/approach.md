## General

For each input value, two pieces of information are needed:

1. its decimal digit range;
2. whether that range is smaller than, equal to, or larger than the best range seen so far.

The source computes each number's minimum and maximum digit arithmetically, then maintains the sum of exactly those processed values tied at the current best range.

**Extracting decimal digits**

For a positive integer `x`, the last decimal digit is:

$$
x\bmod10.
$$

Removing that last digit is integer division by ten:

$$
\left\lfloor\frac{x}{10}\right\rfloor.
$$

The source copies `x` into `y` so the original value remains available for the answer:

```python
y = x
while y:
    v = y % 10
    y //= 10
```

Each iteration extracts one digit into `v` and shortens `y` by one decimal place. Since input values are positive, the loop executes at least once.

The digits are visited from right to left, but order is irrelevant when computing only their minimum and maximum.

**Minimum and maximum digit initialization**

Before scanning one number, the source sets:

```python
a, b = 10, 0
```

`a` is the smallest digit seen so far, and `b` is the largest.

Ten is larger than every real decimal digit, so the first extracted digit always replaces `a`. Zero is the smallest possible decimal digit, so repeated `max` updates correctly establish `b`. If the number contains only zeros after its leading digit, `b` still becomes that leading positive digit at some iteration.

For every extracted `v`:

```python
a = min(a, v)
b = max(b, v)
```

After all digits have been processed:

$$
a=\min(\text{digits of }x),
\qquad
b=\max(\text{digits of }x).
$$

The digit range is then:

$$
r=b-a.
$$

Internal zero digits are handled naturally. For `x=350`, extraction visits zero, five, and three; the minimum is zero, maximum is five, and range is five.

**Maintaining the best range and tied sum**

The variables have this invariant after processing any prefix of `nums`:

- `mx` is the greatest digit range among the processed values;
- `ans` is the sum of every processed value whose digit range equals `mx`.

Both begin at zero:

```python
ans = mx = 0
```

Digit ranges are always between zero and nine, so zero is a valid lower starting point.

For current number `x` with range `r`, there are three cases.

If `r>mx`, every previously accumulated value has a smaller range and must be discarded from the desired sum. The current value is the first member of the new best group:

```python
mx = r
ans = x
```

If `r==mx`, the current value ties the best range and must be included:

```python
ans += x
```

If `r<mx`, it does not qualify and neither variable changes.

These cases preserve the invariant. Once the final array value has been processed, `mx` is the global maximum range and `ans` is exactly the requested sum.

**Why initialization also handles range zero**

A number whose digits are all equal has digit range zero. If the first input value has range zero, `mx < r` is false but `mx == r` is true, so that value is added to the initially zero answer.

If all input values have range zero, every one is accumulated. If a later positive range appears, the greater-than branch replaces the old sum and begins the correct new group.

**A complete trace**

For `nums=[5724,111,350]`:

- `5724` has minimum two, maximum seven, and range five. It exceeds initial `mx=0`, so `mx=5` and `ans=5724`.
- `111` has range zero. It is smaller than five and is ignored.
- `350` has minimum zero, maximum five, and range five. It ties `mx`, so `ans` becomes `5724+350=6074`.

The source returns `6074`.

**Why a second pass is unnecessary**

A common method first computes every range and its maximum, then scans again to sum matching values. The invariant above performs the same selection online.

When a better range appears, assigning `ans=x` removes all obsolete smaller-range values at once. When a tie appears, adding `x` keeps it. No saved range array or second traversal is needed.

## Complexity detail

Let

$$
S=
\sum_{x\in\texttt{nums}}
\operatorname{digits}(x)
$$

be the total number of decimal digits across all input values.

Each digit is extracted and compared a constant number of times, so total time complexity is `O(S)`. The outer loop itself contributes one iteration per number, already covered because every positive number has at least one digit.

The algorithm stores the current copied number, current digit, minimum, maximum, range, best range, and answer. All are scalar values, so auxiliary space complexity is `O(1)`.

The input list and its integers are not modified. Assigning and repeatedly reducing local `y` does not change immutable integer `x` or the caller's array.

Under the fixed constraints, each input has at most six decimal digits, but `O(S)` states the work in the natural input-size measure.

## Alternatives and edge cases

- **Convert each integer to a string:** Taking `min` and `max` over digit characters also costs `O(S)` time but creates temporary strings. The exact source uses arithmetic extraction and constant auxiliary space.

- **Store every digit range:** This permits a later maximum and sum pass but uses `O(n)` extra space. Maintaining `mx` and `ans` online is sufficient.

- **Two passes without storage:** One pass can find the maximum range and another can recompute ranges to sum values. This keeps constant space but scans every digit twice.

- **Sort values by digit range:** Sorting costs `O(n\log n)` in addition to computing ranges and is unnecessary when only the maximum group matters.

- **Repeated equal digits:** A value such as `777` has minimum and maximum seven, so its range is zero.

- **Digits containing zero:** Zero participates in the minimum even when it is not a leading digit. `900` therefore has range nine.

- **Duplicate array values:** Each position is a separate contribution. If duplicated values tie the maximum range, each occurrence is added.

- **All ranges equal:** Every input value contributes to `ans`.

- **A better range appears late:** The assignment `ans=x` correctly discards the entire earlier tied sum.

- **Maximum possible range:** Decimal digits range from zero to nine, so the largest digit range is nine. The source still scans later values because every later range-nine value must also be summed.

- **Positive-input guarantee:** If `x=0` were allowed, `while y` would not execute and sentinel `a=10` would remain, producing an invalid range. The contract gives `x\ge10`, so this case cannot occur.

- **No leading zeros:** Ordinary integer representation has no leading zero digits. Only actual internal or trailing zeros extracted by modulo belong to the range.

- **Large answer:** The sum can exceed individual input bounds, but Python integers preserve it exactly.

- **Local destruction of `y`:** Repeated `y //= 10` is intentional and safe because `x` remains available for reset or accumulation.
