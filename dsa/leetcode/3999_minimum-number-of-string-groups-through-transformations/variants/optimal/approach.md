## General

**Separate what the transformation can change from what it must preserve.**  For a word, collect:

- the characters at indices `0, 2, 4, ...` into its even-index sequence;
- the characters at indices `1, 3, 5, ...` into its odd-index sequence.

The operation cyclically rotates these two sequences independently and then places them back into their original parity positions. A character from an even index can never move to an odd index, or vice versa. Within one parity, however, any cyclic right shift is allowed.

Therefore, two words are equivalent exactly when:

1. their even-index sequences are cyclic rotations of each other; and
2. their odd-index sequences are cyclic rotations of each other.

Equal lengths are implicit in these conditions. A transformation never changes a word's length, and two sequence strings of different lengths cannot have the same canonical representation.

**Give every rotation class one canonical name.**  A sequence such as `"bca"` has rotations `"bca"`, `"cab"`, and `"abc"`. Instead of trying every shift whenever two words are compared, choose the lexicographically smallest rotation, `"abc"`, as the canonical form of the entire rotation class.

All rotations of a string have the same set of rotations, so they have the same smallest member. Conversely, if two strings have the same smallest rotation, each is a rotation of that common string and hence a rotation of the other.

The signature of a word is the pair

`(minimal_rotation(word[::2]), minimal_rotation(word[1::2]))`.

Two words are equivalent if and only if these signature pairs are equal.

**Why the number of signatures is the minimum group count.**  Rotation equivalence partitions the input into equivalence classes. Words with different signatures cannot share a valid group because they are not equivalent. Thus every distinct signature requires at least one group.

All words with one signature can be placed together because every pair has rotationally equivalent even and odd sequences. One group per signature is attainable. The lower and upper bounds agree, so the answer is simply the size of the `signatures` set.

**Find a minimal rotation without generating every rotation.**  A length-`L` string has `L` possible starting positions. Every rotation occurs as a length-`L` substring of

`doubled = text + text`.

A direct method could slice all `L` candidates and compare them, costing `O(L^2)`. The exact source uses the two-candidate elimination idea commonly known as Booth's algorithm.

The variables are:

- `first`: one candidate rotation start;
- `second`: another candidate start;
- `offset`: the number of leading characters currently known equal between those candidates.

The loop compares

`doubled[first + offset]`

with

`doubled[second + offset]`.

If they are equal, neither candidate can yet be rejected, so `offset` increases.

If the first character is larger at the first mismatch, the rotation beginning at `first` is lexicographically worse. More is true: candidate starts through `first + offset` can be skipped. They share the already-examined periodic overlap and cannot beat the second candidate at the first distinguishing position. The source advances

`first = first + offset + 1`.

If that lands on `second`, it advances once more so the two live candidates remain distinct.

The symmetric case applies when the second candidate has the larger mismatch character: advance `second` by `offset + 1` and avoid collision with `first`.

After rejecting either block of candidates, `offset` resets to zero and comparison begins between the new candidate pair. The loop ends when one candidate start leaves the original length or when `offset == length` shows that the rotations are identical over a full cycle. The smaller surviving start is used to slice one length-`L` rotation from `doubled`.

Although a comparison may advance `offset` one character at a time, a mismatch discards a whole interval of candidate starts. Candidate indices move only forward and never return. This amortized elimination keeps the work linear in `L`.

**Empty and one-character parity sequences.**  A word of length one has an empty odd-index sequence. The helper returns `""` immediately for empty input, which is the only possible canonical form. A one-character nonempty sequence has only one rotation, and the candidate loop naturally returns that character.

**Walk through the first example at the signature level.**  For `"ntgwz"`:

- the even sequence is `"ngz"`, whose rotations include `"gzn"`, the smallest;
- the odd sequence is `"tw"`, whose smallest rotation is `"tw"`.

For `"zwntg"`:

- the even sequence is `"zng"`, another rotation of `"ngz"`, so its smallest rotation is also `"gzn"`;
- the odd sequence is `"wt"`, a rotation of `"tw"`, so its smallest rotation is `"tw"`.

Both signatures are `("gzn", "tw")`, so the set contains one class and the result is `1`.

The transformation says “shift right,” but canonicalization considers every cyclic rotation. That is valid because applying a right shift any number of times reaches every rotation, including what could also be described as a left shift.

**Important defect in the exact stored source.**  The method annotation uses `List[str]`, but the file neither imports `List` from `typing` nor defines it. In a normal Python module, evaluating the class definition raises

`NameError: name 'List' is not defined`.

The canonical-rotation algorithm works if the platform injects `List`, but the exact file is not standalone as written. This source-level dependency is separate from the algorithm's correctness.

## Complexity detail

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

be the total number of input characters.

For a word of length `L`, the even and odd slices contain `L` characters in total. Minimal rotation is linear in the length of its input, so canonicalizing both slices costs `O(L)` time. Hashing and inserting the two canonical strings into a set also processes `O(L)` characters in the worst case.

- Total expected time complexity is `O(S)`.
- Auxiliary space complexity is `O(S)`.

The expected qualifier comes from normal hash-set behavior. The set retains canonical strings whose total length can be `O(S)` when every word has a distinct signature. During one helper call, `doubled` and the returned rotation use linear space in that parity sequence's length; these temporaries are also bounded by `O(S)` overall at any moment.

## Alternatives and edge cases

- **Generate and sort all rotations:** This is easy to describe but can create `L` strings of length `L` for one sequence, taking `O(L^2)` time and space. Candidate elimination finds the canonical rotation in linear time.
- **Compare every pair of words:** Pairwise equivalence tests can require quadratic work in the number of words. Hashing one canonical signature per word groups all equivalent words at once.
- **Polynomial rolling hashes for rotations:** Hashes can compare candidate substrings quickly, but collision handling and binary searches make the method more complex. The exact source returns collision-free canonical strings.
- **Sort characters instead of rotating them:** Cyclic shifts preserve circular order, not merely character counts. `"abc"` and `"acb"` have the same multiset but are not rotations.
- **Mix even and odd positions:** The operation rotates the two parity subsequences independently. Combining them into one character multiset loses the central invariant.
- **Different word lengths:** Transformations preserve length. Canonical sequence strings retain their lengths, so signatures from different lengths cannot accidentally match.
- **One-character words:** The even signature is the character and the odd signature is empty. Equal characters group together; different characters do not.
- **Two-character words:** Each parity subsequence has length one, so no nontrivial rotation is possible. Only identical words are equivalent.
- **Repeated characters and periodic strings:** Several starting positions may produce the same minimal rotation. The helper may keep either equivalent start, but the returned canonical string is identical.
- **Zero shift:** A word is always equivalent to itself because each parity sequence may be shifted by zero.
- **Right shifts versus left shifts:** Repeated right shifts traverse the full rotation cycle, so canonicalizing over all starting positions matches the allowed operation.
- **Set output:** The task asks only for the group count, not the membership lists. Storing signatures is sufficient; the source does not retain arrays of words per class.
- **Missing `List` import:** Complexity and grouping behavior assume the class can be defined. The exact source requires the environment to supply `List` or a separate import correction.
