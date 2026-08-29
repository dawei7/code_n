## General

**Reduce strings to 26 letter frequencies**

Only the number of occurrences of each lowercase letter matters. Operations may change any character to any lowercase letter, so original positions have no effect on the three target conditions.

`cnt1[i]` counts letter index `i` in `a`, and `cnt2[i]` counts it in `b`, where zero represents `'a'` and 25 represents `'z'`.

The source fills these fixed arrays in one pass over each string.

**Condition three: make both strings one common letter**

Choose a target letter at alphabet index `i`. Existing occurrences of that letter in both strings can remain. Every other character must change.

The operation count is

$$
m+n-\texttt{cnt1}[i]-\texttt{cnt2}[i].
$$

The loop over `zip(cnt1,cnt2)` evaluates this for all 26 possible common letters and updates `ans`.

`ans` begins at `m+n`, a valid loose upper bound obtained by changing every character.

**Conditions one and two become alphabet-boundary choices**

To make every letter in the first string strictly less than every letter in the second, choose a dividing index `i` from one through 25:

- First-string letters must lie in indices zero through `i-1`.
- Second-string letters must lie in indices `i` through 25.

This creates a strict boundary because the allowed sets do not overlap.

Every first-string occurrence at index `i` or above must change, contributing `sum(cnt1[i:])`. Every second-string occurrence below `i` must change, contributing `sum(cnt2[:i])`.

The helper computes their sum and minimizes `ans`.

**Why every changed character can be repaired**

For a chosen boundary `i`, any invalid first-string character can be changed to `'a'` or another letter below `i`. Any invalid second-string character can be changed to the letter at index `i` or above.

Thus the counted changes are sufficient. They are also necessary because every occurrence outside its side's allowed range violates the universal ordering condition.

So the slice-sum formula is the exact minimum for that boundary.

**Evaluate both order directions**

`f(cnt1,cnt2)` evaluates “every letter in `a` is less than every letter in `b`.”

`f(cnt2,cnt1)` swaps roles and evaluates “every letter in `b` is less than every letter in `a`.”

The helper uses `nonlocal ans` so both calls update the shared best result.

**Why boundaries exclude zero and 26**

`i=0` would give the lower string no allowed letters. `i=26` would give the upper string no allowed letters. Because both strings are nonempty, neither can satisfy a meaningful strict split.

Indices one through 25 cover every split between adjacent alphabet letters, from `a < b..z` through `a..y < z`.

**Trace `a="aba", b="caa"`**

For condition three, choosing `'a'` preserves two letters in `a` and two in `b`, requiring two changes total.

For condition one, the boundary before `'c'` allows `a,b` in the first string and `c..z` in the second. Both `'a'` occurrences in `b` must change, also costing two.

The minimum remains two.

**Why frequency-only reasoning is complete**

Each target condition constrains only which letters may appear in each entire string, not their positions. Once a target letter or boundary is fixed, every original character can be judged independently as already allowed or needing one change.

No character ever needs more than one operation, and changing one position does not affect another. Frequency counts therefore retain all information relevant to cost.

**Implementation-specific constant alphabet work**

The helper calls `sum` on slices for every boundary. Those slices allocate short lists and repeatedly sum counts, which would be quadratic in alphabet size.

Here the alphabet size is fixed at 26, so this remains constant work. Prefix sums could make each boundary $O(1)$ for a generalized large alphabet, but are unnecessary for the stated domain.

## Complexity detail

Let $N=m+n$ be the combined string length. Counting characters costs $O(N)$. All later loops and slice sums operate on arrays of fixed length 26, so they take $O(1)$ with respect to input length. Total time is $O(N)$.

The two 26-entry count arrays and temporary constant-size slices use $O(1)$ auxiliary space because the alphabet is fixed. These bounds match the manifest.

The input strings are immutable and remain unchanged.

## Alternatives and edge cases

- **Prefix counts across the alphabet:** Precompute cumulative frequencies so each boundary cost is constant even when alphabet size is treated as a variable.
- **Try all replacement strings:** Exponential and unnecessary because positions are independent once a condition is selected.
- **Both strings already one same letter:** Condition three costs zero.
- **Each string uniform but different letters:** One ordering condition may already hold with zero operations.
- **All `a` greater than all `b`:** The second helper call finds zero.
- **Equal boundary letters:** Strict inequality forbids the same letter on both sides, which the disjoint ranges enforce.
- **Single-character strings:** All conditions and boundary formulas remain valid.
- **Best common letter absent from one string:** That string's every character may need change, while preserved occurrences in the other still reduce cost.
- **Boundary at one:** The lower side may contain only `'a'`.
- **Boundary at 25:** The upper side may contain only `'z'`.
- **Fixed lowercase alphabet:** It makes frequency arrays and slice overhead constant.
- **Nonlocal result:** Both helper directions contribute to the same global minimum.
