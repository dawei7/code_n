## General

**A useful swap can repair at most one interruption**

The final repeated-character substring contains copies of one character, say `c`. With no swap, any existing run of `c` is a candidate. With one swap, there are two useful possibilities:

- bring another `c` from elsewhere to extend one run by one position;
- replace the single different character between two `c` runs, joining both runs.

One swap cannot remove two different interrupting characters. Therefore, for each run, it is enough to inspect the next run of the same character only when exactly one position separates them.

**Know how many copies of each character exist**

`Counter(text)` stores the total frequency of every lowercase letter. This global limit matters because a candidate substring cannot contain more copies of `c` than the complete string contains.

For example, in `"aaabaaa"` there are six `a` characters. The two runs have lengths three and three around one `b`. Replacing the gap would appear to create seven positions, but no seventh `a` exists to swap into that gap. The achievable repeated run is capped at six.

**Identify the first run**

At the start of an outer iteration, `i` points to the beginning of a run. The pointer `j` advances while `text[j] == text[i]`. When it stops, the half-open interval `[i, j)` is the entire first run, and

`l = j - i`

is its length.

If `j == n`, the run reaches the end. The later scan finds no second run, and the formula still evaluates this existing run correctly.

**Skip exactly one gap and inspect a matching second run**

The candidate gap is at index `j`, the first character after the current run. Because `j` stopped the equality loop, that character differs from `text[i]` whenever it exists.

The code sets `k = j + 1`, thereby skipping exactly that one different character. It then advances `k` while later characters equal `text[i]`. The second matching run is `[j + 1, k)`, with length

`r = k - j - 1`.

If the character immediately after the gap does not match, `r` is zero. The same formula then describes extending only the first run. If it does match, `l` and `r` can potentially be joined by swapping the gap with another copy of the desired character.

**Derive the candidate length**

The expression

`min(l + r + 1, cnt[text[i]])`

combines two limits.

The structural limit `l + r + 1` counts the first run, the second run, and the one gap position that could become the desired character after a swap. No one-swap result based on these runs can cover more contiguous positions.

The inventory limit `cnt[text[i]]` says the result cannot use more copies than the string owns. If another copy exists outside the two runs, it can be swapped into the gap and the full `l + r + 1` is attainable. If all copies already belong to the two runs, swapping the gap requires moving one of those copies away, so the length remains `l + r`. The minimum captures both cases without a separate condition.

When `r = 0`, the expression becomes `min(l + 1, total_count)`. It extends the run by one exactly when another copy of the same character exists elsewhere.

**Why every relevant candidate is considered**

After evaluating the current run, `i = j` moves to the start of the next run, which is the previous gap character. Thus every maximal run becomes the primary run of some outer iteration.

Any optimal one-swap repeated substring either uses one original run plus at most one imported character, or bridges two runs of the desired character separated by exactly one different position. The first case is evaluated when that run is primary. In the second case, the left run is primary and the scan after `j + 1` finds the right run. Cases with a gap of two or more different characters cannot be repaired with one swap and need not be joined.

Taking the maximum over all primary runs and all characters therefore finds the best achievable length.

**Why the algorithm is correct**

For each computed candidate, a construction exists. If an extra copy is available, swap it into the adjacent extension position or one-character gap. If no extra copy exists, the inventory cap returns only the number already available in the matching runs, which can be kept as an existing or joined-length result as appropriate.

Conversely, consider any repeated substring obtainable with at most one swap. Removing the swapped-in position leaves either one run or two runs of the repeated character separated by that single position. The algorithm evaluates exactly that configuration, and its two caps are upper bounds on its length. Hence no valid result exceeds `ans`, while every value used to update `ans` is attainable.

## Complexity detail

Let `n` be `len(text)`. Building the counter takes `O(n)` time. The primary run scan advances `i` through the string by complete runs. The lookahead scan may revisit characters as part of a neighboring iteration, but each position participates in only a constant number of these local scans. Total time is `O(n)`.

The counter contains at most 26 entries because the input uses lowercase English letters. All pointers and lengths are scalar values, so auxiliary space is `O(1)` under the fixed alphabet.

No substring slices or proportional arrays are created.

## Alternatives and edge cases

- **Try every possible swap:** There are quadratically many index pairs, and rescanning the resulting strings would be far too slow.
- **Sliding window with one mismatch:** A window can allow one nonmatching character, but it must also respect the global number of the target character. Running such logic per letter is possible but more elaborate.
- **Run-length encode the entire string:** A list of runs can make neighboring-run logic explicit, but it uses `O(n)` extra space in the worst case. The exact solution processes runs in place.
- **Join runs separated by two characters:** One swap can replace only one interruption, so such runs cannot form one repeated substring.
- **All characters equal:** The single run reaches length `n`, the frequency cap is `n`, and the answer is `n` without a swap.
- **Only one copy of a character:** Its candidate is capped at one even though a structural extension position exists.
- **Two matching runs with no spare copy:** The gap cannot be filled without removing a copy from one run, so the cap returns `l + r` rather than `l + r + 1`.
- **A spare copy elsewhere:** It can be swapped into the one-character gap, allowing the full joined length.
- **Run at the end:** `j == n` makes the second-run length zero, and the bounds remain valid.
- **Single-character input:** The only run has length one and the result is one.
- **Repeated gap character:** That gap is itself processed as a primary run on the next outer iteration, so candidates for every character are considered.
