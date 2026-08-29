## General

**Turn binary reflection into a numeric sort key**

Each input value needs two ordering components:

1. its binary reflection;
2. the original value, used when reflections tie.

The source computes the reflection arithmetically and sorts with key `(f(x), x)`. Python compares tuples lexicographically, so it first compares reflected values and consults the original values only when the first components are equal.

**Read the original bits from right to left**

The helper `f(x)` maintains an output accumulator `y`, initially zero. While `x` is positive, it repeats

`y = (y << 1) | (x & 1)`

and

`x >>= 1`.

`x & 1` extracts the least significant remaining bit of `x`. The right shift removes that bit from `x`. Therefore the loop sees the original binary digits from last to first, which is exactly the order required in the reflection.

Before appending a bit, `y << 1` makes room on the right. Bitwise OR places the extracted zero or one in that new position. This is the binary analogue of building a decimal number with `result = result * 10 + digit`.

Although the helper reassigns its local parameter `x`, integers are immutable and the array occurrence is not changed by these shifts.

**Trace a reflection one bit at a time**

Take `x=6`, whose binary representation is `110`.

- The first extracted bit is 0. Shifting zero and appending zero leaves `y=0`; `x` becomes binary `11`.
- The next bit is 1. `y` becomes binary `1`; `x` becomes binary `1`.
- The last bit is 1. `y` becomes binary `11`, which is decimal 3.

Thus 6 reflects to 3, matching the written reversal `110 -> 011` and the numeric interpretation of `011`.

For `x=5`, bits are read as 1, 0, 1, so `y` becomes binary `101` and remains decimal 5.

**Why leading zeros need no special case**

A positive integer's ordinary binary representation has no leading zeros. If it ends in one or more zeros, those become leading zeros after reversal.

The arithmetic construction processes those zeros while `y` is still zero. Shifting zero and OR-ing zero leaves zero, so the eventual numeric value naturally ignores them. For example, 8 is binary `1000`. The first three extracted zeros keep `y=0`, and the final one produces `y=1`.

This exactly matches “reverse the digits, then interpret the result as a number.” No binary string trimming is required.

**Sort by both required dimensions**

The call

`nums.sort(key=lambda x: (f(x), x))`

computes a tuple key for each occurrence. If two values have different reflections, the smaller reflection comes first. If they have the same reflection, the smaller original value comes first.

In the second example, 3 (`11`) reflects to 3, and 6 (`110`) also reflects to 3. Their first key components tie, so their second components order 3 before 6.

Equal input values have identical two-part keys and remain repeated. The task concerns occurrences, so the method must not convert the input to a set.

**Why the arithmetic helper returns the exact reflection**

After $t$ iterations, `y` consists of the last $t$ bits of the original number written in reverse order. This statement is true initially for zero processed bits.

At the next iteration, `x & 1` obtains the next original bit moving from right to left. Left-shifting `y` and appending that bit extends the reversed sequence correctly. Right-shifting `x` leaves precisely the unprocessed original prefix.

When `x` becomes zero, every bit from the original no-leading-zero representation has been processed. The accumulator is therefore its reversed bit sequence interpreted numerically. Any zeros now at the reflected sequence's front have already vanished in the normal integer representation, as required.

Python's tuple-key sort then implements the exact lexicographic key $(R(x),x)$. Every returned occurrence is present once because sorting only permutes the list.

**Recognize the in-place behavior**

`list.sort` mutates `nums` and returns `None`. The source performs the mutation and then explicitly returns `nums`. Callers therefore receive the same list object in its new order, not a separately allocated result list.

This is observably different from `return sorted(nums, ...)`, which would preserve the input and return a new list. Both could satisfy a value-only judge, but the documented explanation should match the exact source.

## Complexity detail

Let $N$ be the number of array occurrences and $B$ the maximum bit length of a value.

`f(x)` performs one iteration per binary digit, taking $O(B)$ time and $O(1)$ auxiliary space. Python's keyed sort computes each key once, so key creation totals $O(NB)$. Sorting the $N$ decorated entries takes $O(N\log N)$ comparisons.

The generalized time bound is $O(NB+N\log N)$. Since `nums[i] <= 10^9` gives $B\le 30$, bit reversal is bounded by a small constant and the manifest simplifies the total to $O(N\log N)$.

Python's Timsort and stored keys may use $O(N)$ auxiliary memory. The reflection helper itself uses only two integer variables. The input list is sorted in place, but “in place” does not mean the sorting implementation uses constant auxiliary memory.

## Alternatives and edge cases

- **Reverse a binary string:** `int(bin(x)[2:][::-1], 2)` directly mirrors the definition and has the same $O(B)$ key cost, but the exact source uses bit operations.
- **Precompute repeated reflections:** A cache can avoid recomputing `f` for duplicate values. Python's sort already calls the key once per occurrence, and $N\le100$ makes the simple form sufficient.
- **Sort only by reflection:** Reflection collisions exist, such as 3 and 6 both reflecting to 3. Omitting original `x` violates the required tie-break.
- **Sort only by original value:** Numeric order and reflected order can differ sharply; 8 must precede 3 in the example because its reflection is 1.
- **Deduplicate before sorting:** Repeated occurrences must remain repeated in the result.
- **Power of two:** Its binary form is one followed by zeros, so its reflection is 1.
- **Binary palindrome:** A value such as 5 or 7 reflects to itself.
- **Trailing binary zeros:** They become ignored leading zeros of the reflected numeral automatically.
- **Equal reflection, different bit lengths:** The original-value component still gives the specified order.
- **Equal original values:** Both key components tie; both occurrences remain in the list.
- **Positive-input guarantee:** The loop always processes at least one bit. In a generalized call with zero, `f(0)` would return zero because the loop is skipped.
- **Input mutation:** The returned ordering is also written into the caller-provided `nums` list.
- **Fixed bit width versus ordinary representation:** The method reverses only significant binary digits, not a padded 32-bit or 64-bit representation.
