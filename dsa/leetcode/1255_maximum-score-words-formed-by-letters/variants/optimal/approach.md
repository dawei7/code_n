## General

**The small word count makes subset enumeration feasible**

There are at most 14 word entries, so there are at most \(2^{14}=16384\) subsets. The exact source evaluates every subset and keeps the highest score among those that can be formed from the available letter multiset.

`cnt = Counter(letters)` records how many copies of each lowercase character are available. Repeated letters are distinct resources and therefore must be counted rather than merely placed in a set.

**Represent each subset with a bitmask**

With \(n=\lvert\texttt{words}\rvert\), masks range from zero through \(2^n-1\). Bit `j` of mask `i` is one exactly when `words[j]` is selected:

`i >> j & 1`.

Mask zero represents selecting no words, which is always valid and has score zero. This gives a safe initial lower bound even if no nonempty subset can be formed.

Each word entry has its own bit. If identical strings occur at different indices, they may both be selected, consistent with the rule that each entry can be used once.

**Construct the selected letter multiset**

For a mask, the list comprehension selects all included words. `''.join(...)` concatenates them, and `Counter` counts every required character in the resulting string:

`cur = Counter(joined_selected_words)`.

The textual order does not affect feasibility or score, but concatenation is a convenient way for the exact source to gather all letters.

**Check the limited inventory**

The subset is feasible exactly when, for every required character `c`, `cur[c] <= cnt[c]`. The code checks:

`all(v <= cnt[c] for c, v in cur.items())`.

Only required characters need inspection. If a character is absent from `cnt`, Counter lookup returns zero, so any positive requirement correctly fails.

Unused available letters are permitted, so no equality requirement is imposed.

**Calculate a valid subset’s score**

For each character \(c\), the score array index is `ord(c) - ord('a')`. Multiplying the required count by that per-character score gives the contribution of all copies. Summing over `cur.items()` yields the selected words’ total score.

`ans = max(ans, t)` retains the best valid subset.

Scores are nonnegative. Even if zero-score words are selected, they cannot reduce the total, but they may consume letters and are harmlessly considered among all masks.

**Following the first example**

The mask selecting `"dad"` and `"good"` requires one `a`, three `d` characters, one `g`, and two `o` characters. The available multiset supplies all of them.

Their score is

\[
1\cdot1+3\cdot5+1\cdot3+2\cdot2=23.
\]

The exhaustive loop also evaluates `"dad"` plus `"dog"` and all other subsets, but none exceeds 23.

**Why evaluating every subset is correct**

Every allowed solution is a subset of word indices because each entry may be selected at most once. Binary masks form a one-to-one enumeration of those index subsets.

For each mask, `cur` exactly counts the letters needed. The availability test is necessary and sufficient for constructing those words from `letters`. The score calculation is the definition of that subset’s score. Taking the maximum across all feasible masks therefore returns the global optimum.

**What this exact implementation does not prune**

Even when an early selected word already requires an unavailable letter, the source finishes building the entire mask’s joined string and Counter. Backtracking could prune all supersets of an infeasible partial choice, but full enumeration remains practical under \(n\leq14\).

**Memory behavior per mask**

The selected-word list, joined string, and `Counter` are rebuilt for every mask. Objects from the previous iteration become reclaimable. The algorithm does not store all subsets simultaneously.

## Complexity detail

Let \(w\) be the number of word entries and

\[
S=\sum_{t\in\texttt{words}}\lvert t\rvert.
\]

For each of \(2^w\) masks, the list comprehension inspects \(w\) bits and the selected strings can contain up to \(S\) characters. Joining and counting cost \(O(S)\), and \(S\geq w\) because words are nonempty. Total time is \(O(2^wS)\).

The available-letter Counter uses at most 26 keys. For one subset, the selected list uses \(O(w)\) references, the joined string uses \(O(S)\) characters, and its Counter uses at most 26 keys. Peak auxiliary space is \(O(w+S)\), not \(O(2^w)\), because subsets are processed one at a time.

## Alternatives and edge cases

- **Backtracking with remaining letter counts:** Choose or skip each word, subtract letters when feasible, and undo on return. It has the same exponential worst case but prunes infeasible branches and uses \(O(w+26)\) state.
- **Precompute each word’s counts and score:** Avoid joining and recounting strings for every subset, substantially improving constants.
- **Dynamic programming by letter mask:** Not practical when counts, rather than simple presence, matter across 26 letters.
- **No nonempty word is feasible:** Mask zero keeps the answer at zero.
- **Duplicate word entries:** Each index has its own mask bit and may be selected once.
- **Repeated letters:** Counter comparison enforces the exact available multiplicity.
- **Zero-score letters:** They still consume inventory even though they add no score.
- **Unused letters:** They are allowed; requirements need only be at most availability.
- **Maximum subset count:** Fourteen words produce only 16,384 masks, making exhaustive evaluation viable.
- **Missing available character:** Counter returns zero and the feasibility check rejects any positive demand.
