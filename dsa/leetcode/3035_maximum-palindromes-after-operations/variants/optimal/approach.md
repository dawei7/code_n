## General

Because arbitrary character positions may be swapped, original word membership no longer constrains a letter. What remains fixed is the multiset of all letters and the list of target word lengths.

A palindrome of length $L$ needs exactly $\lfloor L/2\rfloor$ equal-character pairs for its mirrored positions. An odd-length palindrome also needs one center character, but that center can be any remaining letter, so it does not consume an additional pair. Count global letter frequencies and sum `count // 2` to obtain the complete pair budget.

Sort the word lengths. If a longer word can be built, replacing it with any shorter unchosen word never uses more pairs and never reduces the number of completed palindromes. Therefore an optimal selection is a prefix of the sorted lengths. Spend each prefix word's required pairs until the next cost exceeds the remaining budget; at that point every later cost is at least as large, so no further word can be added.

## Complexity detail

Counting the $S$ characters takes $O(S)$ time. Sorting $n$ lengths takes $O(n\log n)$ time, and the greedy scan takes $O(n)$, for $O(S+n\log n)$ total time. The frequency table has only 26 entries, while the sorted length list uses $O(n)$ space.

## Alternatives and edge cases

- **Length frequency buckets:** Since every length is at most `100`, count words by length and scan 100 buckets to obtain $O(S+n)$ time and $O(1)$ space; explicit sorting keeps the greedy order more direct.
- **Repeated shortest selection:** Calling `min` and removing one remaining length at a time preserves the greedy choice but costs $O(n^2)$ time.
- **Odd-length centers:** A center requires one character but no equal pair; tracking centers separately can incorrectly reject feasible odd palindromes.
- **Single-character words:** Their pair cost is zero, so they are always included before any positive-cost word.
- **No available pairs:** Even-length words cannot be made palindromic, but every length-one word still counts.
- **Input preservation:** Sorting derived lengths instead of `words` leaves the caller's array order unchanged.
