## General

Process `s` from left to right so every stored letter position is automatically to the left of the current star. Maintain 26 stacks, one for each lowercase letter, and push each ordinary character's index onto its matching stack. Also maintain a Boolean deletion marker for every input position.

At a star, scan the letter stacks from `a` upward. The first nonempty stack identifies the smallest eligible character. Pop from that stack so that, among equal smallest letters, the rightmost occurrence is deleted; mark both that letter and the star itself. After the scan, emit exactly the positions that were never marked.

Deleting a smallest letter is forced by the operation. Among equal copies, deleting the rightmost one preserves an earlier equal character in the output. The two possible strings agree before that earlier position, but the rightmost-deletion choice retains the equal letter there while the other choice shifts a later character into its place, so it cannot be lexicographically larger. Applying this exchange argument at every leftmost star proves the greedy choices produce the smallest possible final string. The stacks contain exactly the currently undeleted letters to the star's left, so each operation implements that choice correctly.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each index is pushed at most once, popped at most once, and inspected once during final output. A star checks at most 26 buckets, a fixed alphabet size, so the total time complexity is $O(n)$. The position stacks and deletion markers require $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Minimum heap:** Store `(letter, negative_index)` pairs so the heap chooses the smallest letter and, among ties, the rightmost index. This takes $O(n\log n)$ time and $O(n)$ space.
- **Rescan every prefix:** At each star, search all still-live characters to its left for the rightmost smallest one. It is correct but can take $O(n^2)$ time.
- **Equal smallest letters:** Remove the rightmost eligible copy; removing an earlier equal copy can make the remaining string lexicographically larger.
- **No stars:** Every character remains and the result equals the input.
- **All letters removed:** A valid string such as `abc***` may produce the empty string.
- **Interleaved stars:** A letter removed by an earlier star must not be considered by any later star.
