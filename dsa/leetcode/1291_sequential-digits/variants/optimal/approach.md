## General

**Every sequential-digit number is determined by its first and last digit**

A positive decimal number with sequential digits must look like `12`, `2345`, or `6789`. Once the first digit is chosen, every later digit is forced to be one greater. Digits cannot pass nine, and valid multi-digit numbers cannot begin at zero under the problem's range.

The outer loop chooses starting digit `i` from one through eight. Starting at nine cannot produce a two-digit sequential number because ten is not a digit.

Variable `x` begins as that one-digit start. The inner loop chooses successive digits `j` from `i + 1` through nine and performs `x = x * 10 + j`. Multiplication shifts existing decimal digits left, and addition appends the forced next digit.

For start two, `x` evolves through `23`, `234`, `2345`, and so on through `23456789`.

**Filter each generated candidate by the inclusive range**

After every appended digit, the code checks `low <= x <= high`. Passing candidates are added to `ans`. The initial one-digit `i` is never checked, which is appropriate because `low >= 10` and answers require at least two digits.

The generation loops do not stop when `x > high`, although they safely could because further appends only increase it. The decimal alphabet is fixed and tiny, so continuing has constant cost.

Likewise, the algorithm does not restrict starting lengths based on the digit counts of `low` and `high`. It generates the complete fixed universe and filters afterward. That choice keeps boundary logic simple: the inclusive comparison alone decides membership, while the constant 36-candidate limit keeps unnecessary work negligible.

**Why generation is complete**

Take any sequential-digit number in the requested range. Its first digit is some `i` from one through eight, and its remaining digits must be `i + 1, i + 2, ...` up to at most nine. The corresponding outer iteration constructs exactly that prefix at one inner-loop step, where the range check includes it.

Conversely, every constructed `x` begins at `i` and appends consecutive increasing digits, so every value admitted to `ans` satisfies the definition. No number is duplicated because its first digit and length uniquely identify it.

**Why a final sort is necessary for this generation order**

The loops group candidates by starting digit, not by numeric magnitude. For example, the start-one branch generates `12,123,1234,...` before the start-two branch generates `23`. That order is not globally increasing because `23 < 123`.

Returning `sorted(ans)` restores the required numerical order. All values are positive integers, so ordinary integer sorting matches ascending decimal magnitude.

**There are only thirty-six possible candidates**

There are eight length-two candidates, seven length-three candidates, down to one length-nine candidate:

$$
8+7+\cdots+1=36.
$$

The loops therefore perform a fixed number of iterations independent of `low` and `high`. This finite decimal universe is why the manifest uses constant complexity.

The count also proves there are no hidden candidates involving repeated or skipped digits. A start digit $i$ offers exactly $9-i$ possible ending digits, each choosing one prefix length of the forced sequence. Summing $9-i$ for $i=1$ through eight again gives 36, matching the nested loop iterations one-for-one.

For range `100` through `300`, constructed candidates `123` and `234` pass, while `12` is too small and `345` is too large. Sorting returns `[123,234]`.

## Complexity detail

With decimal digits fixed to one through nine, at most 36 candidates are constructed and at most 36 values are sorted. Both runtime and output capacity are bounded by constants, so time is $O(1)$ and total space is $O(1)$ under the problem's fixed base and constraints.

More explicitly, sorting at most 36 integers costs $O(36\log36)$, still constant. The result list itself also holds at most 36 integers.

If the concept were generalized to an alphabet of $D$ ordered digits, the bounds would depend on $D$; the constant claim is specific to base ten.

## Alternatives and edge cases

- **Sliding windows over `"123456789"`:** Every sequential number is a substring. Enumerating window lengths and starts can produce values directly by length and often already in sorted order.
- **Precompute all 36 values:** Store the fixed universe once and filter it for each query. This is useful for many calls but unnecessary for one.
- **Breadth-first digit extension:** Seed digits one through nine and append the next digit. It is more general but adds queue machinery.
- **Inclusive boundaries:** Values equal to `low` or `high` are retained by the chained comparison.
- **No candidate in range:** Sorting an empty list returns `[]`.
- **Range near ten:** `12` is the smallest possible answer.
- **Upper bound one billion:** The largest sequential candidate is `123456789`; no ten-digit sequential number exists.
- **Starting digit nine:** It cannot extend and is correctly omitted from the outer range.
- **Generation order:** A final numerical sort is required because grouping by first digit is not globally ascending.
- **No duplicates:** First digit plus length uniquely determines each generated number.
