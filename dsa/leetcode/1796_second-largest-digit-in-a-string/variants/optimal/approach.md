## General
**Separate digits from letters**

Scan `s` once. Ignore every lowercase letter. For a character between `"0"` and `"9"`, convert it to its integer value before comparing ranks; lexical and numerical order agree for these ten characters, but integer sentinels make the missing-value result direct.

**Maintain two distinct ranks**

Keep `largest` and `second_largest`, both initialized to `-1`. When a digit exceeds `largest`, move the old largest into second place and install the new value as the largest. Otherwise, replace `second_largest` only when the digit lies strictly between the two stored values.

The strict comparisons matter. A digit equal to `largest` or `second_largest` is a duplicate and must not occupy another rank.

**Preserve the prefix invariant**

After each processed prefix, `largest` is its greatest digit value and `second_largest` is its greatest distinct value below `largest`, or `-1` if none exists. A new maximum performs the necessary demotion. A nonmaximum digit can affect only second place, and exactly the strict-between test identifies when it improves that rank.

These cases cover every incoming digit and preserve the invariant through the full string. The final `second_largest` is consequently the requested value, with the sentinel already representing the missing case.

## Complexity detail
The scan performs constant work for each of the $n$ characters, taking $O(n)$ time. It stores two integer ranks and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Digit set plus sorting:** Collecting distinct digit values and sorting them is concise and still uses only fixed-domain storage, but it does more work than maintaining the top two directly.
- **Boolean presence array:** Mark ten possible digits, then scan from `9` downward for the second marked value; this is also $O(n)$ time and $O(1)$ space.
- **Sort every digit occurrence:** Sorting all occurrences takes $O(n\log n)$ time and still requires explicit duplicate removal.
- **Letters only:** No digit exists, so the result remains `-1`.
- **One distinct repeated digit:** Repetition does not create a second rank.
- **Zero as the answer:** The `-1` sentinel keeps a legitimate digit zero distinguishable from absence.
- **Arrival order:** The largest value may appear before or after the eventual second largest; both update paths must work.
