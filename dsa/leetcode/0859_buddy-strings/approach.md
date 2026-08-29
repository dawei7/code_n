## General

**One swap preserves length and character counts**

Swapping two positions cannot change string length or the multiset of characters. Therefore, two immediate necessary conditions are:

- `len(s) == len(goal)`;
- `Counter(s) == Counter(goal)`.

If lengths differ, the function returns false before indexing. If Counters differ, no rearrangement by swapping—let alone exactly one swap—can transform `s` into `goal`.

After these checks, only the positions of equal multiset characters remain to analyze.

**Count mismatched positions**

`diff` is:

`sum(s[i] != goal[i] for i in range(n))`.

Each Boolean contributes one exactly where the strings differ.

A swap touches two distinct indices, so there are only two successful structural cases:

1. exactly two positions differ, and swapping them repairs both;
2. no positions differ, but swapping two equal characters leaves the string unchanged.

**Case one: exactly two mismatches**

Suppose mismatch positions are `i` and `j`. Because the complete character Counters are equal and every other position already matches, the two characters must cross:

$$
s[i]=goal[j],\qquad s[j]=goal[i].
$$

Swapping `s[i]` and `s[j]` makes both positions correct and leaves all other positions unchanged.

Thus, after multiset equality has been established, `diff == 2` is sufficient.

It is also necessary for transforming two unequal strings with one swap: a swap can change at most two positions, and it cannot repair exactly one mismatch under equal character counts.

**Case two: strings are already equal**

If `diff == 0`, the result begins equal to `goal`. However, the problem requires swapping two distinct indices.

The only way to perform a swap without changing the string is to choose two equal characters. That is possible exactly when some Counter frequency is greater than one:

`any(v > 1 for v in cnt1.values())`.

For `"aa"`, swapping the two `a` positions preserves `"aa"`, so the result is true. For `"ab"`, the only distinct indices contain different letters; swapping them changes the string, so the result is false.

**Why other mismatch counts fail**

More than two mismatches cannot be repaired because one swap changes only two positions.

Exactly one mismatch cannot occur after equal lengths and equal Counters: one wrong character would create a character-count imbalance unless another position compensated.

With no mismatches and no duplicate character, every pair of distinct indices contains different letters, so every permitted swap changes the string away from `goal`.

**Trace `"ab"` and `"ba"`**

Lengths and Counters match. Both positions differ, so `diff=2`. The equal multiset guarantees the characters cross, and swapping indices 0 and 1 succeeds.

For `"abcd"` and `"badc"`, Counters match but four positions differ. One swap can fix at most one of the two exchanged pairs, so the answer is false.

**Why the Boolean expression is exact**

The final return:

`diff == 2 or (diff == 0 and duplicate exists)`

lists the two and only two possible successful forms after the necessary length and multiset checks. Each listed form supplies a concrete valid swap, and every valid one-swap transformation belongs to one of them.

Therefore, the result is both necessary and sufficient.

Another useful way to verify exhaustiveness is to compare the string before and after an arbitrary swap of indices `i` and `j`. Every position other than `i` and `j` is unchanged. If the swapped characters differ, exactly those two positions are candidates to differ from the original, yielding the two-mismatch transformation case. If the characters are equal, the entire string is unchanged, yielding the zero-mismatch duplicate case. There is no third behavioral outcome for a single required swap.

## Complexity detail

Let `n` be the common string length. Building both Counters takes `O(n)` time. Counting mismatches takes another `O(n)`. Total time is `O(n)`.

The strings contain only 26 lowercase letters, so each Counter has at most 26 keys. Under this fixed alphabet, auxiliary space is `O(1)`. The mismatch generator also uses constant iterator state.

If the alphabet were unbounded relative to input size, Counter storage would be `O(n)`; the manifest uses the stated lowercase domain.

## Alternatives and edge cases

- **Collect mismatch indices:** Store up to three and stop early. It makes the cross-character test explicit, though Counter equality already guarantees it when there are two.

- **Try every pair of indices:** This takes `O(n^2)` swaps and repeated comparison, unnecessary once mismatch structure is known.

- **Different lengths:** Return false immediately.

- **Different character multisets:** A swap cannot change counts, so return false.

- **Exactly two mismatches:** Equal Counters force a repairing cross-swap.

- **Zero mismatches with duplicate:** Swap two copies of the duplicated character.

- **Zero mismatches without duplicate:** Every distinct-index swap changes two characters, so return false.

- **One-character equal strings:** No two distinct indices exist and no duplicate frequency exceeds one, so false.

- **More than two mismatches:** One swap cannot repair them all.

- **Repeated characters elsewhere:** Any duplicate suffices only in the already-equal case; with two mismatches, the mismatch swap handles the transformation.

- **Input immutability:** Both strings are counted and compared without modification.
