## General

**Count decimal digits without converting to text**

The source uses a ten-entry list `cnt`, where `cnt[d]` records how many times digit `d` appears in the decimal representation.

Repeatedly applying

`n, x = divmod(n, 10)`

does two things at once:

- `x` is the remainder after division by ten, which is the current last decimal digit.
- The new `n` is the quotient, which removes that last digit.

For example, starting with `155` gives digit five and remaining number fifteen; the next step gives another five and remaining number one; the final step gives digit one and remaining number zero.

The loop processes digits from right to left, but frequency does not depend on order. Each original digit contributes exactly one increment to its corresponding bucket.

**Consider only digits that actually occur**

The phrase “digit that occurs least frequently in its decimal representation” refers to present digits. A digit absent from `n` has frequency zero, but it is not a candidate.

This is why the selection condition includes

`0 < v`.

Without that check, the algorithm would almost always return the smallest absent digit, usually zero, instead of the least frequent present digit.

The constraint `n >= 1` guarantees that the counting loop runs at least once and some bucket is positive. If zero itself were an allowed complete input, the loop would need a special case to count its single decimal digit `0`, but that situation is outside the contract.

**Scan candidate digits in increasing order**

After counting, the source enumerates `cnt` from digit zero through digit nine. It stores the smallest frequency found so far in `f` and the associated digit in `ans`.

The update occurs only when

`0 < v < f`.

If a digit has a strictly smaller positive frequency, it becomes the new answer. If it ties `f`, the source does not replace the existing answer.

Because candidates are visited in increasing numeric order, the existing answer in a tie is always the smaller digit. Thus the strict update comparison implements both priorities:

1. Minimize frequency.
2. Among equal frequencies, minimize digit value.

This is equivalent to minimizing the pair `(frequency, digit)` over present digits, but the explicit scan avoids constructing pairs or sorting.

**Trace the first example**

For `1553322`, the positive buckets are:

- Digit one: frequency one.
- Digit two: frequency two.
- Digit three: frequency two.
- Digit five: frequency two.

The ascending scan first encounters digit one with frequency one and stores it. No later digit has a smaller positive frequency, so the answer remains one.

**Trace the tie example**

For `723344511`, digits two, five, and seven each appear once, while the others that occur have larger counts.

The scan encounters digit two before five and seven and records frequency one. The later ties do not satisfy `v < f`, so digit two remains selected, matching the required smallest-digit tie break.

**Why initializing with infinity is convenient**

The source sets `f = inf`. Every positive digit frequency is smaller than infinity, so the first present digit automatically initializes both `f` and `ans`.

Starting with an arbitrary finite bound could fail if a frequency exceeded that bound. Starting with the number of decimal digits plus one would also work, but would require retaining or deriving that count. Infinity directly represents “no candidate seen.”

`ans` begins at zero, but that value is only a placeholder. Since at least one digit occurs, the first positive bucket always replaces it before return unless zero itself is the first present digit, in which case zero is legitimately selected.

**Why a fixed array is preferable here**

There are exactly ten possible decimal digits. A list gives constant-time indexing, deterministic ascending iteration, and fixed storage.

A dictionary or `Counter` would also count correctly, but tie-breaking would still need an explicit minimum operation. Sorting its items would add work that the ten-bucket scan avoids.

The method modifies only its local integer variable `n`. Python integers are immutable, so the caller’s value is unaffected.

## Complexity detail

Let `d` be the number of decimal digits in `n`. The division loop runs exactly `d` times. Scanning all ten buckets takes constant time, so total time is `O(d)`.

Since `d = floor(log10(n)) + 1` for positive `n`, the bound may also be written `O(log n)` when measured against numeric magnitude.

The count list always has ten entries, and the remaining variables are scalars. Auxiliary space is `O(1)`.

Under the given 32-bit bound, there are at most ten digits, so even the digit loop has a small fixed practical maximum. The manifest uses `d` to describe the exact input-sensitive work.

## Alternatives and edge cases

- **Convert to a string and use `Counter`:** This is concise and still `O(d)`, but allocates the decimal text and a mapping.
- **Sort present `(frequency, digit)` pairs:** It produces the right lexicographic minimum but performs unnecessary sorting over a ten-value domain.
- **Include zero-frequency buckets:** This returns an absent digit and misinterprets “occurs least frequently.”
- **Replace on equal frequency:** Scanning upward and replacing ties would select the largest tied digit. The source updates only on a strict improvement.
- **Digit zero inside `n`:** Division and remainder count internal or trailing zeros normally, such as the two zeros in `100`.
- **Input `n = 1`:** Only digit one occurs, so it is returned.
- **All digits equally frequent:** The smallest digit that actually occurs is returned.
- **One repeated digit:** That digit is the only candidate even though its frequency may be large.
- **Complete input zero:** It would need special handling, but the constraint `n >= 1` excludes it.
- **Local mutation of `n`:** Replacing the local integer with its quotient does not mutate caller-owned state.
- **Missing import:** The stored source uses `inf` without importing it. Standalone Python needs `from math import inf` unless the harness supplies the name.
