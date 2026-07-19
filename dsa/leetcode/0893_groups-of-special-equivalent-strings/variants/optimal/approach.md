## General
**Identify what the allowed swaps preserve**

An even-indexed character can move to any other even index but can never move to an odd index; the same holds independently for odd positions. Therefore every string preserves one multiset of even-index letters and another multiset of odd-index letters.

**Use the two multisets as a canonical signature**

Create 26 frequency slots for even indices and 26 for odd indices. Scan a word, incrementing the slot determined by its character and index parity, then convert all 52 counts to a tuple and insert it into a set. The number of distinct tuples is the answer.

Equal signatures are necessary because swaps do not change either parity multiset. They are also sufficient: arbitrary swaps can permute the even positions into any ordering of their multiset and can do the same independently for odd positions. Thus two words share a signature exactly when one is transformable into the other, and distinct signatures correspond exactly to the maximal special-equivalence groups.

## Complexity detail
Each of the $N$ words contributes $L$ characters to one constant-size signature, so the running time is $O(NL)$. The set stores at most $N$ signatures; because the lowercase alphabet fixes each signature at 52 integers, the auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Sort the two parity slices:** Using `sorted(word[::2])` and `sorted(word[1::2])` is concise but costs $O(NL\log L)$ time.
- **Compare every pair of words:** Building equivalence groups by pairwise comparison can cost $O(N^2L\log L)$ time.
- **Generate reachable permutations:** Enumerating swap outcomes is unnecessary and grows factorially with the parity-class sizes.
- **One-character words:** Only the even-index frequency matters, so equal letters share a group and different letters do not.
- **Duplicate words:** Repeated identical strings add no new signature and therefore no new group.
- **Same overall letter multiset:** Two words can still be in different groups when letters occur in different index parities.
- **Odd word length:** The even-index class contains one more position than the odd-index class, which the separate counts handle automatically.
