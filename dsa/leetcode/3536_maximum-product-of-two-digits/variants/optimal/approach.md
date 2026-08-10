## General

**The best pair consists of the two largest digit occurrences**

All decimal digits are nonnegative integers from zero through nine. If two chosen digits are `p <= q` and an unchosen digit `r > p` exists, replacing `p` by `r` cannot decrease the product:

`r*q >= p*q`.

Applying this exchange repeatedly shows that a maximum-product pair must use the largest and second-largest digit occurrences.

“Occurrences” matters. If the largest digit appears twice, both copies may be selected. The problem permits using the same digit value twice only when it occurs more than once, and tracking two slots naturally enforces that multiplicity.

The source therefore scans digits once while maintaining:

- `a`: largest processed digit occurrence;
- `b`: second-largest processed digit occurrence;

with invariant `a >= b`.

**Extract digits from right to left**

`divmod(n,10)` returns quotient and remainder:

`n = 10 * quotient + remainder`.

The remainder `x` is the last decimal digit, and the quotient removes it. The assignment:

`n, x = divmod(n,10)`

therefore visits every digit exactly once from least significant to most significant.

Digit order is irrelevant because the task chooses any two digits, so right-to-left scanning loses nothing.

**Update the two best slots**

If `x > a`, the new digit becomes the largest. The old largest is still the best remaining occurrence, so:

`a,b = x,a`.

If `x` is not larger than `a` but `x > b`, it belongs in the second slot:

`b = x`.

Otherwise, at least two processed occurrences are already no smaller than `x`, so it can be discarded.

The source writes these comparisons as `a < x` and `b < x`, which are equivalent forms.

**Why equal maximum digits are preserved**

Suppose `a = 2`, `b = 0`, and the next digit is another two. The first condition `a < x` is false because they are equal. The second condition `b < x` is true, so `b` becomes two.

The state is now `a = b = 2`, representing two distinct digit occurrences. This is why `n = 22` returns four.

Using a set of distinct digit values would incorrectly discard multiplicity. Using `>=` in the first branch without careful shifting could also mishandle equal occurrences.

**The invariant after every processed digit**

Initially `a = b = 0`. Since actual digits are nonnegative, these are safe lower-bound placeholders. After processing at least two digits, they represent the two largest occurrences seen.

Assume the invariant holds before new `x`:

- if `x > a`, it is the new first, and old `a` is the second;
- otherwise, `a` remains first; if `x > b` it becomes second, and if not, old `b` remains second.

Every possible ordering relation is covered, so induction proves the invariant through the entire number.

The constraint `n >= 10` guarantees at least two decimal digits. Thus, when the loop ends, both slots correspond to actual occurrences even though they began as zeros. If a real digit is zero, the placeholder value coincides with it harmlessly.

**Why multiplying a and b is optimal**

The invariant says no digit occurrence outside the two stored slots is larger than `b`. For any chosen pair, its larger member is at most `a` and, after using one occurrence for that role, its other member is at most `b`. With all values nonnegative, their product cannot exceed `a*b`.

The two slots themselves are real distinct occurrences, so `a*b` is attainable. It is both an upper bound and a feasible product, establishing optimality.

**A trace for 124**

Digits arrive as four, two, one:

- four replaces `a`, leaving `(a,b)=(4,0)`;
- two does not exceed four but exceeds zero, giving `(4,2)`;
- one exceeds neither slot, so state stays `(4,2)`.

The result is eight.

## Complexity detail

If `D` is the number of decimal digits, the loop executes `D` times. Each iteration performs one `divmod` and a constant number of comparisons/assignments, so time is `O(D)`.

Since `D = floor(log10(n)) + 1` for positive `n`, this is conventionally written `O(log n)`. Under the explicit bound `n <= 10^9`, there are at most ten iterations.

The method stores only `a`, `b`, `x`, and the shrinking local integer `n`. Auxiliary space is `O(1)`. Reassigning the parameter does not mutate any caller-owned object because Python integers are immutable.

## Alternatives and edge cases

- **Convert to a string and sort digits:** Correct, but sorting costs `O(D log D)` and allocates digit storage where two running maxima suffice.
- **Count frequencies for digits zero through nine:** Also correct in `O(D)` time and constant space; scanning down from nine can select the top two occurrences.
- **Check every digit pair:** Costs `O(D^2)`, unnecessary when nonnegative ordering determines the best pair.
- **Use the two largest distinct values:** Wrong for repeated maximum digits such as `22` or `991`.
- **Largest digit appears once:** `b` correctly stores the next-largest occurrence.
- **Largest digit appears multiple times:** One copy occupies each slot, maximizing the product.
- **Zeros:** If every pair must include zero, the maximum product is zero and the initialized slots handle it.
- **Number ending in zero:** `divmod` extracts the zero as a real digit before removing it.
- **Exactly two digits:** The invariant ends with those two occurrences, so their product is returned.
- **Repeated second-largest digit:** Only one second slot is needed once the largest occurrence count is accounted for.
- **Positive n guarantee:** The loop would skip for zero, but zero is outside the documented `n >= 10` domain.
- **At least two digits:** This guarantee is what makes both result slots correspond to real selectable occurrences.
- **Strict comparisons:** They preserve ordering while still allowing an equal-to-`a` digit to enter `b` through the second branch.
