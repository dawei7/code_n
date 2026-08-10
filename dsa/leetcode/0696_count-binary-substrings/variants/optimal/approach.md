## General

A valid substring has exactly two consecutive character groups: a run of zeroes followed by an equally long run of ones, or a run of ones followed by an equally long run of zeroes.

Examples include `"01"`, `"0011"`, and `"111000"`. A string such as `"001100"` is not valid as a whole because it contains three groups, even though its counts of zeroes and ones are equal.

The solution compresses the input conceptually into lengths of maximal equal-character runs, but it keeps only the current run length and the preceding run length rather than storing an array.

**Finding one maximal run**

The outer index `i` is the first position of the current run. The inner index starts at `j = i + 1` and advances while:

- `j < n`; and
- `s[j] == s[i]`.

When the inner loop stops, positions `i` through `j - 1` form one maximal run of identical bits. Its length is

`cur = j - i`.

The run is maximal because `j` is either the end of the string or a position holding the opposite bit.

At the bottom of the outer loop, `i = j` begins the next run. Every character is therefore part of exactly one discovered group.

**Counting substrings across one boundary**

Consider two adjacent runs with lengths `a` and `b`. Any valid substring centered on their boundary must take some positive number `x` of characters from the end of the first run and exactly `x` characters from the beginning of the second.

The possible values are:

$$
x=1,2,\ldots,\min(a,b).
$$

For each `x`, there is exactly one such substring at this boundary because its end portions are forced. Thus these two runs contribute

$$
\min(a,b)
$$

valid substrings.

They cannot contribute more: taking over `a` characters from the left or over `b` from the right is impossible, and extending past either maximal run would introduce a third group.

**What `pre` means**

`pre` stores the length of the immediately previous run. It begins at zero because no run precedes the first.

After discovering a current run of length `cur`, the code adds:

`ans += min(pre, cur)`.

For the first run, this adds `min(0, cur) = 0`, correctly reflecting that one group alone cannot form a valid substring.

Then `pre = cur` prepares the next boundary. Only the immediately preceding run matters; a valid substring cannot cross two group boundaries.

**Why every valid substring belongs to exactly one contribution**

Every valid substring contains one transition from `0` to `1` or from `1` to `0`. That transition lies at exactly one boundary between two maximal runs.

The substring is counted when the algorithm processes the run on the right side of that boundary. Its equal group size `x` is one of the values from one through the smaller run length.

It cannot be counted at any other boundary because it contains no other character transition. Therefore, summing `min(pre, cur)` over adjacent run pairs counts every valid occurrence once.

Occurrences are identified by position, not just text. If the same substring text appears at two different boundaries, each boundary contributes it separately, as the problem requires.

**A complete trace**

For `s = "00110011"`, the maximal run lengths are `2, 2, 2, 2`.

- First run length `2`: add `min(0, 2) = 0`.
- Second run length `2`: add `2` for `"01"` and `"0011"` across the first boundary.
- Third run length `2`: add `2` for `"10"` and `"1100"`.
- Fourth run length `2`: add `2` for the two occurrences ending in the final ones run.

The total is `6`.

For unequal runs, such as `"00011"` with lengths `3` and `2`, the boundary contributes two: `"01"` and `"0011"`. A third would require three ones, which do not exist.

**Why the two nested loops are still linear**

The inner loop does not restart from the beginning for each outer iteration. Once it advances through a run, the outer assignment `i = j` skips directly past those characters.

Across the entire execution, `j` advances over each character at most once as part of its run. The nested syntax therefore represents a partitioned scan, not quadratic repeated scanning.

**Why the algorithm is correct**

For every adjacent pair of maximal runs, the algorithm adds exactly the number of valid substrings whose unique transition lies at their boundary. The argument above shows this number is `min(pre, cur)`.

Every valid substring has exactly one such boundary, so it appears in one and only one term. No counted candidate is invalid because it takes equal positive lengths from two opposite-bit runs and does not extend into a third run.

Therefore, the accumulated `ans` is exactly the requested number of substring occurrences.

## Complexity detail

Let `n = len(s)`.

Each character is consumed as part of one maximal run. The total number of increments of `j` and changes to `i` is linear. All work per run besides scanning its characters is constant. Running time is

$$
O(n).
$$

The variables `n`, `ans`, `i`, `j`, `cur`, and `pre` occupy constant storage. No run-length array or substring is created. Auxiliary space is

$$
O(1).
$$

The input string is read only.

## Alternatives and edge cases

- **Store every run length:** Build a list such as `[2, 3, 4]` and sum minima of adjacent entries. It has the same time but uses `O(n)` worst-case space.

- **Character-by-character rolling counts:** Track current and previous run lengths in one for-loop and add a boundary contribution when the character changes, plus one final contribution. This is equivalent to the exact run-skipping implementation.

- **Enumerate every substring:** Checking counts and grouping for all substrings is at least quadratic and ignores the key one-boundary structure.

- **One-character string:** There is only one run and no transition, so `min(0, 1)` produces zero.

- **All characters equal:** The entire string is one run, and the answer is zero.

- **Alternating characters:** Every run has length one, so each adjacent pair contributes one and the result is `n - 1`.

- **Unequal neighboring runs:** Only the shorter side limits how many balanced substrings can expand from the boundary.

- **Repeated substring text:** Different positions are counted through different boundary contributions, even if their characters are identical.

- **Exactly two groups:** The answer is simply the smaller group length.

- **Three or more groups:** A valid substring may use any one adjacent pair but never spans an entire third group; summing per boundary handles all possibilities without overlap.

- **Binary-input guarantee:** Adjacent maximal runs necessarily contain opposite characters. With a larger alphabet, the same grouping count would count equal-length two-run substrings, but the original zero/one interpretation would differ.

- **First run handling:** Initializing `pre = 0` avoids a special case and ensures the first run contributes nothing.
