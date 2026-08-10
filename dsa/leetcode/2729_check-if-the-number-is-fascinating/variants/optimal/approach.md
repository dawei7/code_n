## General

**Translate the digit condition into one canonical string**

The required concatenation is the decimal representation of `n` followed by `2 * n` and `3 * n`. The exact solution builds it directly:

`str(n) + str(2 * n) + str(3 * n)`.

Call this combined string `s`. Every decimal digit in the three numbers becomes one character of `s`, preserving multiplicity. Concatenation position does not matter for the final property because the question asks which digits occur, not their order.

**What a fascinating digit multiset must equal**

The condition says that digits one through nine each appear exactly once and zero never appears. There is only one sorted string with exactly that multiset:

`"123456789"`.

Therefore sorting all characters of `s` and comparing the result with this target simultaneously checks every requirement.

**Why equality checks the length automatically**

It might seem necessary to separately test that `s` has nine characters. String equality already does that. A string of eight, ten, or more characters cannot equal the nine-character target.

This catches cases where `2n` or `3n` has four digits. Although `n` itself has exactly three digits, its multiples are not guaranteed to. A longer concatenation fails without special branching.

**Why equality rejects zero**

If `s` contains `'0'`, sorting places it before `'1'`. The sorted result then differs from `"123456789"`. Even if all nonzero digits also occur, the extra zero changes both content and often length.

For `n=100`, the combined string is `"100200300"`. Its sorted form contains many zeros and repeated nonzero digits, so equality is false.

**Why equality rejects duplicates and missing digits together**

Suppose a nonzero digit appears twice. If `s` still has nine characters, some other required digit must be missing. Sorting exposes both facts as a mismatch at one or more positions.

If the duplicate is accompanied by extra length, equality also fails by length. There is no need for a separate frequency counter, uniqueness set, or explicit loop over digits.

Conversely, if sorted `s` equals the target, it has exactly nine characters, no zero, and one occurrence of every character one through nine. That is exactly the definition, so the test is sufficient as well as necessary.

**Trace n equal to 192**

The three numbers are 192, 384, and 576. Concatenating gives `"192384576"`.

Its characters are one, nine, two, three, eight, four, five, seven, and six. Sorting them produces `"123456789"`, so the function returns true.

The original groups do not each need consecutive or sorted digits. Only their combined multiset matters.

**Trace a duplicate-only failure**

Imagine a combined nine-character value containing every required digit except nine, with eight repeated. Sorting would end with `...88` rather than `...89`. The equality fails, correctly identifying that “nine characters with no zero” alone is insufficient; exact multiplicity matters.

**Why decimal string conversion is appropriate**

The operation itself is decimal concatenation. Arithmetic tricks with place values would need to know how many digits each multiple contains and would still need to inspect digits afterward. String conversion represents the problem's definition directly and avoids leading-place calculations.

Inputs are positive three-digit integers, so there are no minus signs. Standard decimal conversion also introduces no leading zeros that could obscure digit counts.


If the function returns true, sorting `s` produced `"123456789"`. Sorting preserves exactly the multiset of characters, so `s` contains each digit one through nine once and no other character, including zero; hence `n` is fascinating. If `n` is fascinating, its concatenation contains exactly that multiset, whose sorted order is `"123456789"`, so the function returns true. The Boolean equality is therefore equivalent to the definition.

## Complexity detail

Under the stated constraint $100\le n\le999$, all generated decimal strings have bounded length: `n` has three digits, and `3n` is at most 2997. Sorting this constant-size string takes $O(1)$ time and uses $O(1)$ space with respect to the legal input range, matching the manifest.

For a generalized $d$-digit input, the concatenation has $O(d)$ characters, string construction costs $O(d)$, and sorting costs $O(d\log d)$ time with $O(d)$ output or temporary space. The exact code chooses sorting rather than a linear frequency array, but $d$ is fixed here.

Python creates the three decimal strings, their concatenation, the sorted character list, and the joined sorted string. All are constant-bounded for this problem.

## Alternatives and edge cases

- **Nine-entry frequency array:** Scan the digits and require frequency one for one through nine and zero for zero; generalized time is $O(d)$.
- **Set comparison alone:** Insufficient because a set loses multiplicity; repeated digits could be hidden without also checking length.
- **Arithmetic digit extraction:** Avoids strings but is longer and must still track counts and zero.
- **n equal to 192:** Produces the canonical nine-digit multiset and returns true.
- **Contains zero:** Sorted equality necessarily fails.
- **Repeated digit:** Forces a mismatch because exact multiplicities are compared.
- **Missing digit:** The sorted string cannot equal the complete target.
- **Four-digit multiple:** Makes the combined length exceed nine and therefore returns false.
- **No leading zeros:** Positive integer conversion uses canonical decimal representations, matching numerical concatenation.
- **Fixed input range:** Justifies the stated constant complexity despite use of sorting.
