## General

**There are only two possible alternating patterns.** A binary alternating string must be either `010101...` or `101010...`. The helper `calc(c)` measures swaps needed for the pattern whose first bit is `c`.

At index `i`, that pattern’s expected bit is `c XOR (i mod 2)`. Even indices keep `c` and odd indices flip it. The expression `c ^ i & 1` follows Python’s bitwise precedence as `c ^ (i & 1)` and produces exactly that expected bit.

**Count mismatched positions.** `map(int, s)` lazily converts the characters to zero or one, and `enumerate` provides their indices. The Boolean

`(c ^ i & 1) != x`

is true when the actual bit `x` differs from the target pattern. Summing Booleans counts mismatch positions.

**Why divide mismatches by two.** A valid swap exchanges any two positions. For a feasible target pattern, the mismatches come in complementary types:

- a position containing zero where the pattern needs one;
- a position containing one where the pattern needs zero.

Swapping one position of each type fixes both simultaneously. The counts of the two types are equal because source and target contain the same total numbers of zeros and ones. Therefore minimum swaps equal total mismatches divided by two.

No swap can fix more than two mismatched positions, so this number is also a lower bound. Pairing opposite mismatches realizes it, proving optimality.

**Check whether the character counts can fit an alternating string.** Let `n0` and `n1` be zero and one counts. Alternation places the two symbols in positions whose counts differ by at most one. If `abs(n0 - n1) > 1`, neither pattern can use the available multiset, so the method returns minus one.

If counts are equal, the length is even and both starting patterns use exactly those counts. The solution evaluates both and returns the smaller swap count.

If counts differ by one, the length is odd. The more frequent bit must occupy the first, third, fifth, and other even-index positions, so the pattern is forced. The code calls `calc(0)` when zeros are more numerous and `calc(1)` when ones are more numerous.

**Trace `"111000"`.** Counts are equal, so both patterns are possible. Against `101010`, positions one and four are mismatched: one contains one where zero is needed, and the other contains zero where one is needed. Two mismatches require one swap, matching the sample.

**Already alternating strings.** Every position agrees with one pattern, producing zero mismatches and zero swaps. If counts are equal, the other pattern may be much worse, but `min` selects zero.
Count feasibility is necessary and sufficient for at least one alternating target with the same characters. The branch logic evaluates exactly every feasible target pattern. For each target, mismatch pairing proves `calc` returns its minimum swaps. Selecting the smaller result when both patterns are possible therefore returns the global minimum, while an impossible count difference correctly returns minus one.

**No string construction is necessary.** The expected bit is calculated from index parity, so the method never allocates either target pattern. It compares lazily during the scan.

## Complexity detail

Counting zeros scans `s` once. `calc` scans it once per feasible pattern, at most twice. Total time is `O(n)`.

`map`, `enumerate`, and the generator used by `sum` are lazy. Only counters and scalar values are stored, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Construct both target strings:** It simplifies visual comparison but allocates `O(n)` extra space.
- **Track the two mismatch types separately:** Counting misplaced zeros alone gives the swap count, but total mismatches divided by two is more symmetric.
- **Count difference above one:** No alternating arrangement exists because one symbol lacks enough separating copies.
- **Equal counts:** Both zero-starting and one-starting patterns must be tested.
- **One extra zero:** Only the zero-starting odd-length pattern is feasible.
- **One extra one:** Only the one-starting odd-length pattern is feasible.
- **Single character:** Its majority bit determines the pattern and zero swaps are needed.
- **Already alternating:** Its matching pattern has no mismatches.
- **Arbitrary-position swaps:** Division by two relies on being allowed to swap nonadjacent mismatches directly.
- **Mismatch parity:** For a feasible pattern, mismatch count is always even because misplaced zeros and ones balance.
- **Bitwise precedence:** The expression computes `c ^ (i & 1)`; explicit parentheses could make this easier to read without changing behavior.
- **Input preservation:** The immutable source string is scanned but never changed.
- **Even-length position counts:** Each pattern has exactly `n / 2` zero positions and `n / 2` one positions. That is why equal source counts make both patterns feasible rather than merely one of them.
- **Odd-length position counts:** The starting bit owns one extra position because indices zero, two, and so on include both ends. The majority character must therefore be the starting bit.
- **Pairing construction:** Collect mismatched zero positions and mismatched one positions in corresponding pairs. Swapping each pair independently reaches the target in exactly the mismatch-count-halved total, demonstrating achievability rather than only a lower bound.
- **Why adjacent order is irrelevant:** Since a permitted swap can connect any two positions, the physical distance between complementary mismatches never changes its cost; every paired correction costs one swap.
