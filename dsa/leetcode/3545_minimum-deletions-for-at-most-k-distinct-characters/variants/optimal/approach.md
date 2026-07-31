## General

Reducing the distinct count by one requires removing every occurrence of some character. Deleting only part of a character class spends deletions without eliminating that class, so an optimal solution consists of choosing complete classes to discard and leaving all occurrences of every retained class.

Count the 26 lowercase letters and collect the positive frequencies. If there are $d$ distinct letters, exactly $\max(0, d-k)$ classes must be eliminated; removing more cannot improve the minimum. To minimize the number of deleted characters, sort the frequencies and sum that many smallest values. Any solution discarding the same number of classes has cost equal to their frequency sum, and exchanging a discarded larger class for a retained smaller one never increases the distinct count while strictly lowering or preserving the cost. Therefore the least frequent classes are optimal.

## Complexity detail

Let $n$ be the length of `s`. Counting takes $O(n)$ time. Filtering and sorting at most 26 frequencies takes $O(1)$ time because the lowercase English alphabet is fixed, so total time is $O(n)$. The 26 counters and frequency list use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash map and heap:** Also finds the least frequent classes, but fixed arrays and a constant-size sort are simpler for the guaranteed alphabet.
- **Enumerate retained character subsets:** Correctly explores every choice but can take exponential time in the number of distinct letters.
- **Repeated `count` calls:** Recounting the full string for each position can take $O(n^2)$ time and duplicates work.
- **Already within the limit:** When the distinct count is at most `k`, the number of removed classes is zero and the answer is `0`.
- **Frequency ties:** Any tied class can be removed because all choices have the same deletion cost.
- **One retained class:** Keeping a most frequent class minimizes deletions when `k = 1`.
- **`k` larger than the distinct count:** The limit is “at most,” so unused capacity does not require adding or deleting anything.
