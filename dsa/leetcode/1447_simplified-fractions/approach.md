## General

**Translate the interval into numerator and denominator bounds.** A positive fraction `i / j` lies strictly between zero and one exactly when `0 < i < j`. The denominator must also satisfy `j <= n`. The list comprehension directly enumerates those inequalities:

- `i` ranges from `1` through `n - 1`.
- For each `i`, `j` ranges from `i + 1` through `n`.

Starting `i` at one excludes zero, so the fraction cannot equal zero. Starting `j` at `i + 1` guarantees that the denominator is larger than the numerator, so the fraction cannot equal or exceed one. Ending the denominator range at `n` enforces the required maximum.

The outer range excludes `n` because no denominator at most `n` could then be larger than the numerator. This is a useful example of designing loops from mathematical constraints: invalid fractions are not generated and filtered later; most are excluded structurally by the range boundaries.

**Use the greatest common divisor to recognize reduced form.** A fraction is simplified when its numerator and denominator share no integer factor greater than one. This is exactly the condition `gcd(i, j) == 1`. Such integers are called coprime.

If the greatest common divisor were `d > 1`, both numbers could be divided by `d`, producing an equivalent fraction with smaller numerator and denominator. For example, `2/4` has greatest common divisor two and reduces to `1/2`, so the comprehension excludes it. If the greatest common divisor is one, there is no common factor available, and the fraction is already in lowest terms.

The `gcd` function uses the Euclidean algorithm. It repeatedly replaces a pair by the smaller value and a remainder until the remainder becomes zero. The final nonzero value is the greatest common divisor. The stored source relies on the environment's standard `gcd` implementation rather than reimplementing this reliable primitive.

**Format only accepted candidates.** The condition appears after both loops in the comprehension. Python considers one candidate pair `(i, j)`, evaluates its greatest common divisor, and creates the string only if the pair is coprime. The expression `f'{i}/{j}'` places the decimal numerator, a slash, and the decimal denominator into the exact requested representation.

No numerical division is performed. Using floating-point values would introduce rounding, lose the original numerator-denominator form, and make exact duplicate detection difficult. Keeping the pair as integers until string formatting preserves exact rational identity.

**Why the output contains no duplicate values.** Every accepted pair is already reduced. Suppose two accepted pairs `i/j` and `p/q` represented the same rational number. Cross multiplication would give `i q = p j`. For two positive fractions in lowest terms, uniqueness of reduced representation implies `i = p` and `j = q`. But the nested ranges visit each integer pair only once. Therefore no two produced strings represent the same fraction.

Non-reduced pairs are precisely where apparent duplicates would arise. For example, `1/2`, `2/4`, and `3/6` have the same value, but only `1/2` has coprime numerator and denominator. Filtering with `gcd == 1` both satisfies the word “simplified” and removes those equivalent expansions.

**Why every required fraction appears.** Take any simplified positive fraction between zero and one whose denominator is at most `n`. Its numerator is at least one, is smaller than its denominator, and is therefore at most `n - 1`. The outer loop reaches that numerator, and the corresponding inner loop reaches its larger denominator. Because the fraction is simplified, their greatest common divisor is one, so the condition accepts it and formats it.

Conversely, every output pair has positive numerator, larger denominator no greater than `n`, and greatest common divisor one. It is therefore a simplified fraction strictly inside the requested interval. These two directions establish completeness and soundness.

**Understand the enumeration order.** The numerator is the outer loop, so output is grouped by numerator. For `n = 4`, the candidates begin with `1/2`, `1/3`, and `1/4`. With numerator two, `2/3` is accepted but `2/4` is rejected. With numerator three, `3/4` is accepted. This produces `["1/2", "1/3", "1/4", "2/3", "3/4"]`.

The problem permits any order, so grouping by numerator is valid even though another natural method might group by denominator. There is no need to sort the list afterward. Avoiding a final sort also avoids additional time and space.

**Why the nested comprehension is still readable as an algorithm.** Python evaluates its clauses from left to right like nested loops. First choose `i`. Then choose each legal `j` for that `i`. Then apply the coprimality filter. Finally append the formatted string. Writing the same operations as explicit `for` loops with an `if` and `append` would produce the same result and complexity.

The upper constraint is small, but the approach does not rely on a hardcoded table. It derives all results from `n` and remains correct for every allowed value.

## Complexity detail

The number of candidate numerator-denominator pairs is
`(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2`, which is `O(n^2)`. Each pair runs a greatest-common-divisor calculation on values no larger than `n`. The Euclidean algorithm takes `O(log n)` time in the worst case, giving total time `O(n^2 log n)` under the manifest's analysis.

The list can contain `O(n^2)` simplified fractions, so storing the result requires `O(n^2)` entries. The loop variables and one `gcd` computation use `O(1)` auxiliary words. Thus the manifest reports `O(n^2)` space, dominated by the required output list.

If the cost of characters is counted rather than treating each bounded integer and output string as one word, each numerator and denominator can use `O(log n)` digits. The textual output can then occupy `O(n^2 log n)` characters. For the given limit `n <= 100`, every number has only a few digits, and the conventional complexity model records the number of result entries.

The number of coprime pairs is asymptotically quadratic, so an algorithm that explicitly returns every fraction already needs quadratic output work in the worst case. The greatest-common-divisor filter adds the logarithmic per-candidate factor in the stated implementation.

## Alternatives and edge cases

- **Denominator-first enumeration:** Loop `j` from two through `n` and `i` from one through `j - 1`, accepting coprime pairs. This is equally correct and naturally groups results by denominator rather than numerator.
- **Explicit nested loops:** Replace the comprehension with loops and `ans.append(...)`. It may be easier for beginners to debug, but it performs the same candidate tests and has the same bounds.
- **Generate a Farey sequence:** Farey-sequence methods enumerate reduced fractions in sorted numerical order and can avoid a `gcd` call for every possible pair. They are valuable when ordering or larger bounds matter, but are more complex than required here.
- **Store floating-point values in a set:** This risks rounding collisions, loses exact fraction formatting, and does unnecessary deduplication work. Coprimality gives an exact integer criterion.
- **Reduce every candidate and insert into a set:** Dividing by the greatest common divisor and deduplicating would eventually find the same rational values, but it creates many repeated forms. Rejecting non-coprime pairs directly is simpler.
- **Sort by numeric value:** The problem allows any order, so sorting adds cost without improving correctness. Lexicographic string sorting would also differ from true rational order.
- **n equals one:** No positive numerator can be smaller than a denominator at most one. Both ranges produce no accepted pair, so the returned list is empty.
- **n equals two:** The only legal pair is `1, 2`, whose greatest common divisor is one, producing `"1/2"`.
- **Numerator equals denominator:** Such a fraction equals one and is excluded structurally because `j` always begins at `i + 1`.
- **Zero numerator:** Such a fraction equals zero and is excluded because `i` begins at one.
- **Denominator above n:** The inner range ends at `n` inclusively through Python's exclusive stop `n + 1`, so no oversized denominator appears.
- **Non-reduced fraction:** Any pair such as `2, 4` has greatest common divisor above one and is omitted, even if its reduced value would otherwise be valid.
- **Prime denominator:** Every numerator from one through one less than that prime is coprime to it, so all of those fractions are included.
- **Composite denominator:** Numerators sharing any factor with it are excluded, while the remaining coprime numerators are included.
- **Any-order contract:** The numerator-major order produced by the comprehension is valid. Tests should not require the denominator-major or numerically sorted order of a different implementation.
- **Exact string form:** Each output uses decimal integers separated by one slash, with no spaces and no reduction step left for the caller.
- **Imported gcd:** The solution environment must provide `gcd` from the standard math utilities. Replacing it with division or a floating-point check would not test simplification correctly.
