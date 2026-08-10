## General

The task asks for every string reachable after exactly one legal move. A legal move chooses two adjacent plus signs, `"++"`, and changes those two positions to `"--"`. Nothing else in the string changes. The result is not asking who eventually wins the game and does not require exploring later turns. It asks only for the immediate neighbors of the given state in the game's state graph.

That observation turns the problem into a complete left-to-right scan of adjacent character pairs. Every move is identified by its starting index $i$: positions `i` and `i + 1` must both contain `"+"`. There are only $n-1$ adjacent pairs in a string of length $n$, so checking each pair once is enough to find every possible move.

**Why scanning adjacent pairs covers every move**

Two characters are consecutive precisely when their indices have the form $i$ and $i+1$. The iterator `pairwise(s)` produces exactly these pairs:

$$
(s[0],s[1]), (s[1],s[2]), \ldots, (s[n-2],s[n-1]).
$$

`enumerate` supplies the corresponding starting index `i`. Therefore, when the condition `a == b == "+"` succeeds, `i` is the first position of one legal flip. When it fails, that pair is one of `"--"`, `"+-"`, or `"-+"`, none of which the rules permit changing.

No other kind of move exists. Consequently, rejecting every non-`"++"` pair cannot omit a legal result, and accepting every `"++"` pair considers every legal result.

**Why the string becomes a character list**

Python strings are immutable: individual positions of `currentState` cannot be changed in place. The source first executes `s = list(currentState)`, producing a mutable list with one character per position. This conversion is useful because each candidate changes exactly two positions. The algorithm can temporarily assign `"-"` to those positions without rebuilding all unchanged characters through several slice expressions.

The list `ans` begins empty and collects the completed next-state strings. It is important that the results placed in `ans` are strings, not references to the mutable list. `"".join(s)` reads the list's current characters and creates a new immutable string, so a result remains unchanged after `s` is restored or edited for a later candidate.

**The temporary-change-and-restore cycle**

For a legal pair beginning at `i`, the source performs three conceptual steps:

1. Set `s[i]` and `s[i + 1]` to `"-"`.
2. Join the complete list and append that snapshot to `ans`.
3. Set the same two positions back to `"+"`.

The restoration is essential. Every answer must represent one move made from the original `currentState`, not a sequence of moves accumulated from earlier iterations. If the first flip were left in place, the next result could contain four changed positions and would describe two turns rather than one.

For example, consider `currentState = "++++"`:

| Pair start `i` | Original pair | Temporary list | Appended state | List after restoration |
| --- | --- | --- | --- | --- |
| 0 | positions 0 and 1 | `--++` | `"--++"` | `++++` |
| 1 | positions 1 and 2 | `+--+` | `"+--+"` | `++++` |
| 2 | positions 2 and 3 | `++--` | `"++--"` | `++++` |

Notice that legal pairs may overlap. The middle plus signs participate in more than one possible move. Restoring after each snapshot ensures that an earlier temporary flip does not hide an overlapping pair. This is why all three moves from `"++++"` are found.

`pairwise(s)` advances one adjacent pair at a time. During an iteration, the current values `a` and `b` have already been obtained. The source restores the list before requesting the next pair, so the iterator continues over the original character values rather than a permanently altered state.

**Why the generated list is exact**

Each appended string is valid because the condition confirms two adjacent plus signs, the assignments change exactly those two signs to minus signs, and every other list position is left untouched. Thus, the algorithm never appends an illegal state.

Conversely, take any valid one-move result. Its move starts at some index $i$ whose original characters are both plus signs. The adjacent-pair scan necessarily reaches that index, the condition succeeds, and the temporary mutation constructs exactly that result. Thus, every legal state is appended.

Different starting indices cannot accidentally produce the same output. If one move begins at $i$ and another at $j\ne i$, at least one position changed by one move is not changed in the same way by the other. Because the original positions at both legal pairs are plus signs, the resulting strings differ at that position. The algorithm therefore needs neither a set nor duplicate filtering.

The problem permits any result order. This implementation naturally emits states in increasing order of the flipped pair's starting index because the scan proceeds from left to right.

## Complexity detail

Let $n$ be the length of `currentState`, and let $m$ be the number of adjacent `"++"` pairs. The pair scan performs $n-1$ constant-time checks. For each of the $m$ legal pairs, `"".join(s)` visits all $n$ characters to materialize an immutable output string. The precise output-sensitive time is therefore

$$
O(n + mn).
$$

Because $m\le n-1$, the worst-case time complexity is $O(n^2)$. That worst case occurs for a string consisting entirely of plus signs: every adjacent pair is legal, and the answer contains $n-1$ strings of length $n$. The quadratic work is unavoidable when the caller requires those full strings, because the output itself contains $\Theta(n^2)$ characters in that case.

The returned list stores $m$ strings of length $n$, so output space is $O(mn)$ and is $O(n^2)$ in the worst case. This matches the manifest's total space bound. Excluding the required returned output, `s` is a mutable copy of $n$ characters, while the iterator and scalar variables use constant space. The auxiliary working space is therefore $O(n)$.

The temporary assignments do not create a new list for each candidate. They reuse the same $O(n)$ character list. However, every joined result must be a distinct string in the answer; reusing the working buffer cannot reduce the size of the required output.

## Alternatives and edge cases

- **Slicing and concatenation:** For every legal index `i`, construct `currentState[:i] + "--" + currentState[i + 2:]`. This is straightforward and has the same $O(n^2)$ worst-case time and output space, but it creates candidate strings through slices rather than reusing a mutable character buffer.
- **Regular-expression matching:** A pattern search can locate occurrences of `"++"`, but overlapping matches require special handling. A normal non-overlapping search would miss moves such as the pair beginning at index 1 in `"+++"`.
- **A set of results:** Duplicate elimination is unnecessary because distinct legal starting indices yield distinct next-state strings. A set would add hashing work and would discard the implementation's natural left-to-right order without improving correctness.
- **Recursive game exploration:** Searching future turns solves a different question, such as whether the current player can force a win. This problem stops after one move, so recursion would add irrelevant states and work.
- **Failure to restore the list:** Leaving a temporary flip in place makes later outputs depend on earlier ones. That generates states containing multiple moves and may also hide overlapping legal pairs.
- **Restoring before joining:** The snapshot must be created while the two positions contain minus signs. Restoring first would append the unchanged input instead of the next state.
- **Joining only the changed pair:** Every answer must be a full state string of length $n$, not merely `"--"` or a move index. Joining the complete list preserves all unaffected positions.
- **Length one:** There is no adjacent pair. `pairwise(s)` yields nothing, the loop body never runs, and the returned answer is correctly empty.
- **No adjacent plus signs:** Strings such as `"----"` or `"+-+-"` contain no legal move, so no result is appended and the method returns `[]`.
- **Exactly one legal pair:** A state such as `"--++-"` produces one result by flipping only those two plus signs, so the method returns a one-element list.
- **Overlapping legal pairs:** `"+++"` has moves starting at indices 0 and 1. They produce `"--+"` and `"+--"`; restoration ensures that both are included.
- **Disjoint legal pairs:** In `"++--++"`, either the left or right pair may be flipped, but one output must never flip both because the contract permits exactly one move.
- **All plus signs:** This maximizes the number of results at $n-1$ and realizes the $O(n^2)$ output size.
- **Allowed output order:** The contract accepts any order. The left-to-right order produced here is deterministic and requires no extra sorting.
