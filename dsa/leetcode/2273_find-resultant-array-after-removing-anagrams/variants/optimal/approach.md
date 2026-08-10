## General

**Think in maximal runs of anagram-equivalent words**

Being anagrams is an equivalence relation: a word is an anagram of itself, the relationship is symmetric, and if two words each have the same character counts as a third, they have the same counts as each other.

Therefore, consecutive words can be divided into maximal runs sharing one anagram signature. Within such a run, every word after the first can eventually be deleted because it is adjacent to an anagram on its left. The first word cannot be deleted by another word in its run: the permitted operation always deletes the later index.

The final result is consequently the first word from each consecutive anagram run.

**Why comparing original neighbors is sufficient**

The exact list expression compares each pair of adjacent words in the original array rather than comparing a word with the last retained output.

If `words[i - 1]` and `words[i]` are anagrams, they lie in the same run and the later word should be removed. If they are not anagrams, index `i` begins a new run and must be retained. Transitivity guarantees that an entire run is recognized by every adjacent link inside it.

Deleting earlier members does not change this boundary classification. For example, if `A`, `B`, and `C` are consecutive anagrams, comparisons `A/B` and `B/C` both reject the later word, leaving `A`. If `C` is not an anagram of `B`, it begins a new signature run and remains, regardless of deletions inside the preceding run.

**Understand the helper's intentionally reversed Boolean**

The nested function `check(s, t)` returns true when the two words are different in anagram content and false when they are anagrams. This is the opposite of what a name like “is anagram” might suggest, but it matches the list-comprehension filter: retain `t` only `if check(s, t)` is true.

If the lengths differ, the words cannot use the same multiset of letters, so the helper immediately returns true.

**Compare equal-length words by frequency subtraction**

For equal lengths, `Counter(s)` records how many copies of every character occur in `s`. The loop over `t` subtracts one for each of its characters.

If some count becomes negative, `t` contains more copies of that character than `s`, so the words cannot be anagrams and the helper returns true immediately.

If the loop ends without a negative count, the helper returns false. Why is checking for leftover positive counts unnecessary? The two words have equal length, so the sum of all residual counts is zero. If any character had a positive remainder, some other character would need a negative remainder to balance the total, and that negative value would already have triggered true. Thus, no negative plus equal total length implies that every residual count is exactly zero.

**Build the output in original order**

`pairwise(words)` yields `(words[0], words[1])`, then `(words[1], words[2])`, and so on. The list comprehension keeps the second word `t` exactly when it differs in anagram signature from its predecessor `s`.

The complete expression prepends `[words[0]]`. The first word always survives because the deletion rule permits only indices greater than zero, and the constraints guarantee the input is nonempty.

The retained references stay in original order. No sorting is performed because “consecutive” is fundamental to which words may be deleted.

**Trace one run boundary**

For `["abba", "baba", "bbaa", "cd", "cd"]`:

- `"abba"` and `"baba"` have the same counts, so `check` returns false and `"baba"` is omitted.
- `"baba"` and `"bbaa"` are also anagrams, so `"bbaa"` is omitted.
- `"bbaa"` and `"cd"` have different lengths, so `check` returns true and `"cd"` is retained.
- The two copies of `"cd"` are anagrams, so the second is omitted.

Prepending the first word produces `["abba", "cd"]`.

**Why arbitrary deletion order gives this same result**

Inside a run, deleting any non-first member leaves the remaining words of the same signature adjacent, so deletions can continue until only the first remains. A deletion can never cross a boundary between different signatures because the words at that boundary are not anagrams.

Thus, operations inside one run do not affect neighboring runs, and every operation order yields one survivor per run. The comprehension computes that unique normal form directly without mutating the input step by step.

**Why the returned list is correct**

Every retained word is either the first input word or follows an original neighbor with a different signature, so it is the first member of a run. Every omitted word follows an anagram-equivalent original neighbor and is not a run start. Hence the output contains exactly, and only, the required run representatives.

## Complexity detail

Let `S` be the total number of characters across all words and `n` the number of words. For each adjacent pair, the helper counts the first word and scans the second unless their lengths differ. Each word participates in at most two neighboring comparisons, so total character work is `O(S)`. `pairwise` itself is lazy and adds `O(n)` constant-time pairing work, already bounded by `O(S)` because every word is nonempty.

Each `Counter` contains at most 26 lowercase-letter entries, so helper working storage is `O(1)` under the fixed alphabet. The returned list necessarily holds up to `n` references.

The exact expression also creates an intermediate list for the comprehension and then allocates a second list for `[words[0]] + tail`. At concatenation time, both can coexist, so actual additional list storage is `O(n)` even if the required output list is excluded. The manifest's `O(1)` describes the frequency workspace, not this Python list-construction behavior.

## Alternatives and edge cases

- **Compare with the last retained word:** It also works because run signatures are transitive, and appending incrementally avoids the extra concatenation list.
- **Sort each word as its signature:** It is concise but costs `O(L \log L)` per word of length `L` instead of linear counting.
- **Precompute 26-count tuples:** Comparing neighboring signatures becomes constant time after `O(S)` preprocessing, at the cost of storing one signature per word.
- **Simulate deletions in the input list:** Repeated removals shift elements and can lead to quadratic list operations.
- **Different lengths:** They cannot be anagrams, and the later word begins a new run.
- **Identical words:** They are anagrams, so only the first of a consecutive identical run survives.
- **Long chain of anagrams:** Adjacent original comparisons omit every word except the first, even though omitted middle words are used in later comparisons.
- **Same signature in separated runs:** If a different-signature word lies between them, both runs keep their first word; only adjacent anagrams may trigger deletion.
- **One input word:** The pairwise comprehension is empty and the output is `[words[0]]`.
- **No neighboring anagrams:** Every helper call returns true and the output equals the input order.
- **Counter becomes negative:** The early return proves a character multiplicity mismatch.
- **Positive remainder concern:** Equal word lengths ensure that no-negative subtraction implies all remainders are zero.
- **Helper naming:** `check` means “should retain because different,” not “these are anagrams.”
- **Output references:** Words are immutable strings and are reused rather than copied.
- **Input preservation:** The method constructs new lists and never deletes from or reorders `words`.
