## General

**Test exactly the index pairs the statement permits.** A pair $(i,j)$ is eligible only when $i<j$. The outer loop selects `words[i]` as the candidate smaller word `s`. The inner loop visits `words[i + 1:]`, so every later index $j$ is tested once and no reversed or self-pair is included.

For each later word `t`, the condition is written directly:

`t.endswith(s) and t.startswith(s)`.

Both sides must be true. A prefix match alone is insufficient, and a suffix match alone is insufficient.

**Length is handled automatically.** If `s` is longer than `t`, neither `startswith` nor `endswith` can accept it as the required full prefix or suffix, so the pair contributes false. No separate length test is needed.

If the two strings have equal length, being a prefix means they are identical, and the suffix test agrees. Thus duplicate words at different indices form a valid pair.

**Boolean addition counts matches.** Python's `and` expression returns a Boolean here, and Booleans act as integers. `True` adds one to `ans` and `False` adds zero. After each inner iteration, `ans` equals the number of valid pairs examined so far.

Python also short-circuits `and`. The source tests `endswith` first. If it fails, `startswith` is not called. This may save character comparisons but does not change the worst-case bound.

**Why the pair enumeration is complete and unique.** For every legal pair $(i,j)$, the outer loop eventually reaches $i$, and the suffix slice contains the element at $j$. It is tested once. It cannot appear under another outer index as the same ordered pair, and `j<i` combinations are never generated. Therefore all and only allowed index pairs are considered.

**A trace.** With `["a","aba","ababa","aa"]`:

- for `s="a"`, all three later words start and end with `"a"`, contributing three;
- for `s="aba"`, `"ababa"` starts and ends with it, while `"aa"` does not, contributing one;
- later outer words produce no additional match.

The result is four.

**Why direct checking is appropriate here.** Version I has at most 50 words, each at most length 10. Even testing every pair and scanning its characters is tiny. A trie or string-matching preprocessing would be more code without a meaningful benefit under these constraints.

**Prefix and suffix may overlap.** For `s="aba"` and `t="ababa"`, the prefix occupies positions 0–2 and suffix positions 2–4, sharing the middle character. The built-in operations correctly allow this. The definition does not require disjoint occurrences.

## Complexity detail

Let $N$ be the number of words and $L$ the maximum word length. There are $N(N-1)/2=O(N^2)$ index pairs. `startswith` and `endswith` can each compare up to $O(L)$ characters, so worst-case time is $O(N^2L)$.

The high-level test uses constant scalar state, but the exact source creates `words[i + 1:]` for every outer iteration. The largest suffix list contains $O(N)$ references, so peak auxiliary space is $O(N)$, with $O(N^2)$ cumulative slice allocation. This differs from the manifest's $O(1)$ claim.

An index-based inner loop would avoid slices and use constant auxiliary space. Strings themselves are not copied by a list slice; only references are copied.

## Alternatives and edge cases

- **Index-based nested loops:** It implements the same comparisons without suffix-list allocation and would meet $O(1)$ auxiliary space.
- **Paired-character trie:** The larger version uses one to process total input length efficiently, but it is unnecessary for these small limits.
- **Compare string slices manually:** Built-in prefix and suffix predicates are clearer and avoid creating substring objects.
- **Candidate longer than target:** The built-ins return false without special handling.
- **Equal words at different indices:** The candidate is both full prefix and full suffix, so the pair counts.
- **One-character candidate:** It counts when the target's first and last characters both match it.
- **Overlapping prefix and suffix:** Overlap is allowed and handled naturally.
- **Repeated words:** Indices define pairs, so identical content at several positions can produce multiple counts.
- **One-word array:** There are no later words and the answer is zero.
- **Order constraint:** A matching later word can pair with an earlier candidate, but the reverse index order is never counted.
- **Manifest mismatch:** The exact slicing implementation has $O(N)$ peak auxiliary space despite the constant-space high-level idea.
- **Suffix checked before prefix:** Short-circuit order affects only performance, not correctness. A target that fails its suffix test contributes false immediately; a target that passes still undergoes the required independent prefix test.
- **Character-comparison worst case:** Long repeated strings can make both built-ins inspect nearly all candidate characters for many pairs. That is why the length factor remains in the worst-case bound even though mismatches often terminate early.
- **Indices rather than distinct contents:** If the same candidate text occurs at two earlier positions and both qualify against one later word, they form two different $(i,j)$ pairs. Pair enumeration naturally counts both.
