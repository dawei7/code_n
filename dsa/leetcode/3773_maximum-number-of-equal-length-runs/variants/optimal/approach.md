## General

**Treat maximal runs as the objects being counted**

A run is not any substring of repeated letters. It is the entire maximal block that cannot be extended with the same character. For `"aaabbcca"`, the runs have lengths 3, 2, 2, and 1. The two length-two runs may be selected together even though one contains `b` and the other contains `c`, because compatibility depends only on length.

The answer is therefore the largest frequency among run lengths:

1. identify each maximal run exactly once;
2. count one occurrence of its length;
3. return the largest count.

**Let `groupby` discover the boundaries**

`groupby(s)` groups consecutive equal characters. It starts a new group whenever the current character differs from the previous one. This is exactly the maximal-run boundary rule.

For each pair `(_, g)`, the key is the repeated character and `g` is an iterator over that run's occurrences. The character is irrelevant after the boundary has been determined, so the source names it `_`.

The expression `list(g)` consumes the current group iterator and materializes its characters. Its length is the run length. The update

`cnt[len(list(g))] += 1`

then records one more run of that length in a `Counter`.

Materializing the group is important to understanding the exact source: `g` does not already expose a stored length. It is a one-pass iterator tied to the surrounding `groupby` traversal, so the code consumes it before advancing to the next group.

**Count lengths rather than letters**

`cnt` maps a length to the number of maximal runs having that length. It does not use a pair such as `(character, length)`. This allows equal-length runs containing different letters to contribute to the same selectable collection, as required.

For `"hello"`, `groupby` yields lengths 1, 1, 2, and 1. The counter becomes `{1: 3, 2: 1}`, and the largest frequency is three.

For `"aaabaaa"`, the run lengths are 3, 1, and 3. The length-three counter reaches two, even though the two `a` runs are separated by `b` and are distinct maximal runs.

**Why every position belongs to exactly one counted run**

Consecutive grouping partitions the string: each character occurrence enters the group started by the nearest preceding boundary, and a new group begins precisely when the character changes. No group overlaps another, and no position is skipped.

Each emitted group is maximal on both sides. Its left side is either the beginning of the string or a different character; its right side is either the end or the next different character. Thus the groups are exactly the problem's runs, not merely convenient fragments.

For any fixed length $L$, `cnt[L]` equals the number of selectable runs of length $L$. A valid selection must choose one common length, so it can contain at most `cnt[L]` runs for that choice. Taking all runs of the most frequent length attains `max(cnt.values())`. The returned maximum is therefore both an upper bound and achievable.

**A nonempty string guarantees a maximum**

The input always contains at least one character, so `groupby` produces at least one group and `cnt` is nonempty. Calling `max(cnt.values())` is safe without a default.

The method does not need to remember the run locations or characters because the requested output is only a count. Once a run contributes its length frequency, its individual contents can be discarded.

## Complexity detail

Let $N$ be the string length. `groupby` visits each character once. Converting all group iterators to lists also processes each character exactly once across disjoint groups, so total time is $O(N)$. Finding the maximum over the counter's keys costs at most $O(N)$ and does not change the bound.

The counter may contain $O(N)$ distinct run lengths in a generalized worst case. At any moment, `list(g)` stores the current run and may contain $O(N)$ characters. Peak auxiliary space is therefore $O(N)$, matching the manifest.

The source could count each group without a list to reduce temporary storage, but the exact implementation explicitly materializes it.

## Alternatives and edge cases

- **Manual two-pointer scan:** Advancing an end pointer to each character change obtains the same lengths without materializing group lists.
- **Count total character frequencies:** Widely separated occurrences do not form one run, so global letter counts answer a different question.
- **Count by character and length:** This wrongly prevents different letters with equal run length from being selected together.
- **Split a long run into smaller runs:** Runs must be maximal and cannot be divided to increase a length frequency.
- **Merge separated equal letters:** A different intervening character creates two distinct runs that cannot be merged.
- **Single-character string:** It has one run of length one, so the answer is one.
- **All characters equal:** There is one run of length `N`, so the answer is one.
- **Strictly alternating characters:** Every run has length one, so the answer is `N`.
- **Same length, different letters:** Both runs increment the same counter entry.
- **Same letter in separated runs:** Each maximal group is counted separately.
- **Nonempty guarantee:** It ensures `max` never receives an empty sequence.
- **Iterator lifetime:** Each `g` must be consumed before `groupby` advances, which `list(g)` does.
- **Input preservation:** Strings are immutable; the scan creates counts but does not alter `s`.
