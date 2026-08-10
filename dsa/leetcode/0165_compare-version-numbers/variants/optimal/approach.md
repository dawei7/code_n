## General

**Compare revisions, not text**

A version is not compared lexicographically as one string. For example,
`"1.10"` is greater than `"1.2"` because the second revision values are ten
and two, even though the character `"1"` comes before `"2"` at that textual
position.

Leading zeros also have no significance. Revisions `"01"` and `"001"` both
represent integer one. Finally, a missing revision is treated as zero, so
`"1.0"` and `"1.0.0.0"` are equal.

The selected solution processes both strings from left to right without
splitting them. `i` and `j` point to the next unprocessed character in
`version1` and `version2`.

**Build one revision value digit by digit**

At the start of each outer iteration, `a` and `b` are reset to zero. For
`version1`, the inner loop continues until `i` reaches the string end or a dot.
For each digit it performs:

`a = a * 10 + int(version1[i])`.

Multiplying the accumulated prefix by ten shifts its decimal place left; adding
the next digit appends that digit. Thus characters `"0010"` produce:
zero, zero, one, then ten. Leading zeros disappear naturally without a separate
trim.

The second inner loop constructs `b` by the same rule.

The validity guarantee means every non-dot character is a decimal digit and
each revision is valid, so conversion of a single character succeeds.

**Treat an exhausted version as zero**

The outer condition is `i < m or j < n`. It continues while at least one
version still has a revision to process.

If one string is already exhausted, its inner loop does not run and its
accumulator remains zero. This exactly implements the rule that missing
revision values are zero.

After processing the current revisions, the source advances both indices by
one to step over their dots. If an index was already at or beyond its string
end, incrementing it again is harmless: all later bounds checks remain false,
and that side keeps producing virtual zero.

The code never indexes at these beyond-end positions. Every character access
is protected by `i < m` or `j < n`.

**Return at the first unequal revision**

Version comparison is lexicographic over integer revision values. The earliest
position where the values differ decides the entire result; later revisions
cannot override a more significant earlier difference.

If `a < b`, the method returns `-1`. If `a > b`, it returns `1`. If they are
equal, it advances to the next pair.

If the outer loop ends without finding a difference, every explicit revision
and every necessary virtual zero matched, so the versions are equal and zero
is returned.

**Trace `"1.2"` against `"1.10"`**

The first iteration parses one from both strings. They match, and both pointers
move beyond the first dots.

The second iteration builds two from the single digit in the first version and
ten from the two digits in the second. Since two is smaller, the method returns
`-1` immediately. It does not compare the raw revision strings or their
lengths.

For `"1.01"` and `"1.001"`, the first revisions match. Both second
accumulators become one despite different counts of leading zeros, so the loop
finishes and returns zero.

**Trace unequal revision counts**

For `"1.0"` and `"1.0.0.0"`, the first two explicit revision pairs are equal.
The first index then passes its end. On later iterations, `a` remains zero
while the second parser reads its remaining zero revisions. All pairs match,
and the result is zero.

For `"1"` and `"1.0.1"`, the first revision matches, and the first missing
revision equals the explicit zero. At the following position, virtual zero is
smaller than explicit one, so the result is `-1`.

**Why the streaming comparison is complete**

Before each outer iteration, all earlier revision values have been parsed and
proved equal. The inner loops compute the next values exactly from their
decimal digits, or provide zero for an exhausted side. An unequal pair
therefore establishes the required order at the first significant position.

If no pair is unequal before both inputs are exhausted, all remaining missing
positions would be zero on both sides. The versions are equal under the stated
rules.

The algorithm reads the strings without modifying them and stores no array of
revisions.

## Complexity detail

Let $m$ and $n$ be the two string lengths. Each real character is visited at
most once by its parser, so total time is $O(m+n)$.

The method stores indices and two integer accumulators. Because every revision
fits a 32-bit integer by contract, these occupy constant auxiliary storage:
$O(1)$. This is tighter than the manifest's $O(m+n)$ space bound. A split-based
implementation would use that declared linear space, but the selected source
does not split.

## Alternatives and edge cases

- **Split both strings:** Convert dot-separated pieces to integers and compare with zero padding. It is simple but allocates $O(m+n)$ substring storage.
- **Strip trailing `.0` text:** Can normalize some cases, but still requires correct integer comparison and careful handling of leading zeros.
- **Lexicographic string comparison:** Incorrect for revisions such as two versus ten.
- **Leading zeros:** Digit accumulation removes their numeric effect automatically.
- **Different revision counts:** The exhausted side contributes virtual zeros.
- **Trailing zero revisions:** They do not change equality.
- **First unequal revision:** It decides the result regardless of later components.
- **Single revision:** The same parser works without encountering a dot.
- **Beyond-end indices:** They are incremented but never dereferenced.
- **Valid-input guarantee:** The source assumes digit-only nonempty revisions separated by dots.
