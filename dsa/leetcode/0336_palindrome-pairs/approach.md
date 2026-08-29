## General

**Avoid testing every pair by deriving what the partner must be.**

For two words to form a palindrome, the characters outside the combined string's center must mirror each other. If one word is longer than the other, part of the longer word must match the complete shorter word in reverse, and the unmatched part of the longer word must itself be a palindrome.

That observation lets the exact source examine every split of one word and look up the only possible matching partner in a dictionary. It never guesses arbitrary second words.

The dictionary `d` maps each complete word to its input index. This gives a direct expected-time lookup from a required partner string to its index. The input strings are unique, so each key maps to exactly one candidate; no list of duplicate indices is needed.

**Split one current word in every possible place.**

For a current word `w` of length $L$, the loop tries `j` from `0` through $L$, inclusive. It defines

- `a = w[:j]`, the prefix before the split;
- `b = w[j:]`, the suffix after the split;
- `ra = a[::-1]`, the reversed prefix;
- `rb = b[::-1]`, the reversed suffix.

Including both endpoints matters. At `j = 0`, `a` is empty and `b` is the whole word. At `j = L`, `a` is the whole word and `b` is empty. Those boundary splits find full reverse-word pairs and pairs involving the empty string.

For each split, the source examines two orientations.

**First orientation: the current word comes first.**

Suppose the unmatched suffix `b` is a palindrome, meaning `b == rb`, and suppose the dictionary contains `ra`, the reverse of prefix `a`. Then

$$
w + ra = a + b + \operatorname{reverse}(a).
$$

The outer `a` and `reverse(a)` mirror each other. The middle `b` mirrors itself. Therefore the whole concatenation is a palindrome, and the source appends

`[i, d[ra]]`.

The dictionary membership check appears before the palindrome comparison in the `and` chain. Logically, both are required. The index comparison `d[ra] != i` enforces the contract that a word cannot pair with itself. This is especially important when `w` is itself a palindrome: its reverse may be the same dictionary key, but using the same occurrence twice is forbidden.

For `w = "lls"` split as `a = "ll"` and `b = "s"`, the suffix `s` is a palindrome and `ra = "ll"`. If `ll` were present, `llsll` would be a palindrome. In the actual first example, the useful unequal-length pairing is found from a corresponding split such as `w = "sssll"`, where a palindromic unmatched region surrounds the reverse-matched partner.

At `j = L`, `b` is empty, and the empty string is a palindrome. The first orientation simply asks whether the complete reverse of `w` exists. This handles equal-length reverse pairs such as `bat` followed by `tab`.

At `j = 0`, `ra` is the empty string. If an empty word exists and `w` itself is a palindrome, the source appends `[i, empty_index]`, placing the palindrome before the empty word.

**Second orientation: the matching word comes first.**

Suppose prefix `a` is a palindrome, meaning `a == ra`, and the dictionary contains `rb`, the reverse of suffix `b`. Then

$$
rb + w = \operatorname{reverse}(b) + a + b.
$$

The outer reversed suffix and suffix mirror each other, and the middle prefix is palindromic. The whole concatenation is therefore a palindrome. Because the looked-up word comes first, the appended pair is

`[d[rb], i]`.

At `j = L`, `b` is empty. If the current complete word `a` is a palindrome and the empty string exists, this branch appends `[empty_index, i]`. Together with the first orientation at `j = 0`, both valid orders around an empty string are produced.

**Why the second condition requires `j` to be nonzero.**

The test begins with `if j and ...`, so it skips the second orientation at the split before the first character. At `j = 0`, `a` is the empty palindrome and `rb` is the reverse of the complete word. That would find a standard full reverse pair in one orientation.

But the same ordered pair is already found when the reverse word itself is processed by the first orientation at its `j = L` split. Allowing the `j = 0` second branch would therefore duplicate equal-length reverse pairs. Skipping it removes that duplicate while preserving all needed results.

The `j = L` second branch is not skipped because it produces the empty-word-first order, which differs from the current-word-first order produced at `j = 0` by the first branch.

**Walk through `bat` and `tab`.**

When `w = "bat"` and `j = 3`, `a = "bat"`, `b = ""`, and `ra = "tab"`. The empty suffix is palindromic, `tab` is in the dictionary at the other index, and the first branch emits `[bat_index, tab_index]`.

Later, processing `w = "tab"` at its final split finds reverse `bat` and emits `[tab_index, bat_index]`. These are distinct ordered pairs, and both concatenations are palindromes. The guarded second branch at `j = 0` does not emit either pair a second time.

**Why every emitted pair is valid.**

The two branch derivations explicitly write each concatenation as mirrored outer strings around a palindromic center:

$$
a+b+\operatorname{reverse}(a)
$$

or

$$
\operatorname{reverse}(b)+a+b.
$$

Dictionary membership ensures the required outer word actually occurs in the input, and the unequal-index test ensures two distinct positions are used. Therefore every appended pair satisfies all conditions.

**Why every valid pair is found.**

Take any valid ordered pair of strings $(U,V)$.

If $\lvert U\rvert\ge\lvert V\rvert$, split $U=A+B$ so prefix $A$ has the same length as $V$. Because $U+V$ is a palindrome, the outer $A$ and $V$ portions must mirror, so $V=\operatorname{reverse}(A)$. The remaining center $B$ must be a palindrome. When the algorithm processes $U$ at this split, the first orientation looks up exactly $V$ and emits the pair.

If $\lvert U\rvert<\lvert V\rvert$, split $V=A+B$ so suffix $B$ has the same length as $U$. Palindromic symmetry gives $U=\operatorname{reverse}(B)$, while the unmatched prefix $A$ must be a palindrome. When the algorithm processes $V$ as the current word, the second orientation looks up exactly $U$ and emits `[U_index, V_index]`.

These two relative-length cases are exhaustive. Equal lengths belong to the first case and are handled by reversing the complete word. Thus no valid ordered pair is missed.

## Complexity detail

Let $N$ be the number of words, let $L_i$ be the length of word $i$, let $S=\sum_i L_i$, and let $K=\max_i L_i$. For a word of length $L$, there are $L+1$ splits. Python slicing and reversing create strings whose total length is $O(L)$ per split, and hashing a newly created lookup string can also take $O(L)$. Palindrome equality checks are linear in the compared piece in the worst case. Therefore one word costs $O(L^2)$, and the exact total time is

$$
O\!\left(\sum_i L_i^2\right),
$$

which can also be bounded by $O(SK)$ or $O(NK^2)$.

The dictionary has $N$ entries. Temporary slices and reversals use $O(K)$ peak space because only one split's strings are needed at a time. If $P$ is the number of output pairs, `ans` uses $O(P)$ space. Total additional storage including output is $O(N+K+P)$, or $O(N+K)$ excluding required output.

The variant manifest describes a reverse trie with $O(S+P)$ time and space. That is not the checked-in optimal source. The source performs all string splits, reversals, and palindrome comparisons directly, so its actual time is quadratic in individual word lengths as described above.

## Alternatives and edge cases

- **Reverse trie with palindrome-remainder lists:** Insert reversed words and store indices whose unmatched portions are palindromes. Properly preprocessed palindrome information can approach output-sensitive linear work in total characters. This matches the manifest summary but is not the exact source.

- **Test all ordered word pairs:** Concatenate and reverse every pair in $O(N^2K)$ time. The split dictionary method replaces the factor of $N$ partners with $O(K)$ structurally forced lookups per word.

- **Precompute palindromic prefixes and suffixes:** A table or linear-time palindrome algorithm can avoid repeating slice-reversal comparisons. It adds preprocessing machinery but can reduce the work of deciding which splits have palindromic unmatched pieces.

- **Empty string:** It pairs in both orders with every other word that is itself a palindrome. The boundary splits generate both orientations without a special branch.

- **A word pairing with itself:** Even if a unique word is palindromic, `d[candidate] != i` prevents using one index twice.

- **Duplicate input strings:** The contract guarantees uniqueness. Without it, the dictionary would overwrite indices, and each word key would need a list of occurrences.

- **Ordered results:** `[i,j]` and `[j,i]` are separate possibilities. The method emits both when both concatenations are palindromes, as with complete reverse words.

- **Output order:** The contract does not require sorting. Pairs appear in word order, split order, and branch order, which is valid.

- **Single empty word:** Both branch candidates refer to the same index and are rejected, so the result is empty as required.
