## General

**Assign one distinct index to each role**

A result tuple has four ordered roles: top, left, right, and bottom. The source uses four nested loops over indices `i,j,k,h`.

The guards require every new index to differ from all earlier role indices. Because input words are distinct, this guarantees four distinct words and prevents one word from occupying two sides.

Role order matters. Swapping top and left may form another valid square, and the loops consider it as a separate tuple.

Distinctness guards run before deeper roles are tested. This prunes repeated-word choices early, although the worst-case enumeration remains fourth-power.

**Check exactly the four corners**

Once four distinct words are chosen, the source tests:

- `top[0] == left[0]` for the upper-left corner;
- `top[3] == right[0]` for the upper-right;
- `bottom[0] == left[3]` for the lower-left;
- `bottom[3] == right[3]` for the lower-right.

All words have length four, so indices zero and three are always valid. No interior-character condition exists in the contract; checking more positions would incorrectly reject legal squares.

Geometrically, only endpoint letters meet at the four corners. The two middle letters lie along an edge without intersecting another named word.

When all four comparisons pass, the role-ordered list `[top,left,right,bottom]` is appended.

**Sort input to generate lexicographic output**

The source first calls `words.sort()`. Each nested loop then traverses the sorted word list in ascending order.

The outermost top word is the first tuple component, so all tuples for a smaller top are generated before a larger top. Within one top, left words increase; within equal top and left, right words increase; finally bottom words increase.

This is precisely lexicographic order of the four-component tuple. Skipping indices because of distinctness removes invalid candidates but does not reorder the remaining ones. No final `ans.sort()` is needed.

Lexicographic comparison uses the first differing role, matching the loop nesting exactly: `i` changes slowest and `h` fastest.

The sort mutates the caller-provided `words` array, an observable property of the exact source.

**Why every valid square appears once**

Take any valid ordered square. Its four distinct input words have unique indices after sorting. The nested loops eventually choose those exact indices in their role order, pass all distinctness guards, and verify the four true corner equalities, so the square is appended.

Conversely, every appended tuple uses distinct indices and passed every required equality, so it is valid.

The same ordered tuple cannot be appended twice because its four distinct words correspond to only one ordered index quadruple. Therefore the result is complete and duplicate-free.

**Trace the first example**

After sorting `["able","area","echo","also"]`, the order is `["able","also","area","echo"]`.

The loops eventually choose top `"able"`, left `"area"`, right `"echo"`, and bottom `"also"`. Their corners are `a=a`, `e=e`, `a=a`, and `o=o`, so the tuple is appended.

They also find the role-swapped valid tuple beginning with `"area"`. Its larger top word places it later lexicographically.

**The manifest describes a different algorithm**

The manifest says boundary letters are indexed and compatible bottoms are retrieved after enumerating three roles, with $O(W^3+A)$ time.

The exact source builds no index. It loops through every ordered quadruple of distinct words and performs constant-time corner checks. Its actual dominant time is $O(W^4)$, acceptable only because $W\le15$.

## Complexity detail

Sorting $W$ words costs $O(W\log W)$ comparisons; fixed four-character comparison cost is constant under the constraints.

The four nested loops consider $O(W^4)$ index combinations. Distinctness and corner tests are constant time, so total actual time is $O(W^4)$.

The constant-time claim relies on the guaranteed word length four: each candidate reads exactly eight endpoint characters across four equality comparisons, independent of $W$.

Beyond the output, sorting uses implementation-dependent $O(W)$ temporary memory and loop state is constant. If $A$ valid squares are returned, `ans` stores $O(A)$ four-word lists. Total space is $O(W+A)$ including output.

## Alternatives and edge cases

- **Boundary-letter index:** Mapping required first/last letters to candidate words can reduce enumeration toward the manifest's bound, but it is not the exact source.
- **Permutations of four words:** This is conceptually equivalent to the nested distinct-index loops.
- **Check interior letters:** Only four corners are constrained; interior checks would solve a different word-square problem.
- **Reuse one word:** All four roles must use distinct entries.
- **Sort results afterward:** Unnecessary because sorted nested enumeration already produces tuple order.
- **Fewer than one valid quadruple:** The result remains an empty list.
- **Same corner letters:** Equal characters across many words may produce several role-distinct squares.
- **Distinct input guarantee:** Word identity and index identity agree.
- **Input mutation:** `words.sort()` changes the original list order.
- **Manifest mismatch:** The source is exhaustive $O(W^4)$ enumeration rather than indexed lookup.
- **Loop pruning:** Distinctness guards improve concrete work without changing the asymptotic bound.
- **No valid square:** Exhaustion simply leaves `ans` empty.
