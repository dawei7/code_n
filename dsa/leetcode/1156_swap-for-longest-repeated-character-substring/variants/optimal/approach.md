## General
**Count the available copies.** First count each lowercase character in the entire string. Any repeated-character substring made from a character `c` is capped by that global count: a swap can move an outside `c` into place, but it cannot increase how many copies exist.

**Examine one gap between equal runs.** Starting at a maximal run of one character, find its right boundary `j`. Then skip exactly the character at `j` and measure the immediately following run of the original character. If that second run exists, swapping the one-character gap with another copy joins the two runs. If it does not, an outside copy can still extend the first run by one. Both situations are captured by `min(left_run + right_run + 1, total[character])`.

Every useful swap has one of those forms. If it extends a single run, that run is examined at its start. If it joins two runs, they must be separated by exactly one different character, because one swap cannot remove a wider gap; the scan examines that pair when it starts at the left run. Taking the maximum capped candidate therefore covers every achievable answer. Advancing to `j` processes each original run once.

## Complexity detail
Counting characters takes $O(n)$ time. The run pointers only move to the right, and each position participates in a constant number of scans, so the second phase is also $O(n)$. The frequency table has at most 26 entries and all pointers are scalar, giving $O(1)$ auxiliary space for the fixed lowercase alphabet.

## Alternatives and edge cases
- **Try every swap:** Testing all position pairs and rescanning the result takes at least quadratic time and repeats equivalent choices.
- **Sliding window for every character:** Keeping at most one non-target character in a window is correct and still $O(n)$ because the alphabet has fixed size 26, but it scans the string once per possible target.
- **Ignore the global frequency cap:** This can claim a run was extended even when every copy of its character already lies inside the candidate region.
- **Gap wider than one:** One swap cannot make two equal-character runs contiguous when two or more intervening characters remain.
- **All characters equal:** No swap is needed, and the answer is the full string length.
- **Single occurrence:** A character appearing once can never form a repeated block longer than one.
