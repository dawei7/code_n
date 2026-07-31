## General

The requested output is only a length, and every occurrence of the same letter evolves identically. Store `counts[i]`, the number of occurrences of the letter with alphabet index `i`, instead of storing their positions or the full string.

For letters `a` through `y`, all occurrences shift to the next index. Every `z` creates one `a` and one `b`. If `old` is the frequency vector before a transformation and `next` is the vector afterward, then

$$
\texttt{next[0]}=\texttt{old[25]},
$$

$$
\texttt{next[1]}=\texttt{old[0]}+\texttt{old[25]},
$$

and

$$
\texttt{next[i]}=\texttt{old[i-1]}\qquad(2\le i\le25).
$$

Build a fresh vector for every round so all replacements use the same pre-transformation state. Reduce the only summed entry modulo $10^9+7$; every other entry is copied from a value that is already reduced. After exactly $t$ rounds, the sum of all 26 frequencies is the resulting length.

Initially, the vector exactly counts `s`. Assuming it represents the current string before a round, the transition sends every non-`z` occurrence to its unique successor and sends every `z` occurrence once to each of `a` and `b`. Therefore, it counts every character in the next string exactly once. Induction proves the final vector represents the string after all transformations, so its sum is the required length.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting the input takes $O(n)$ time. Each of the $t$ rounds processes the fixed 26-letter alphabet, so it takes $O(26t)=O(t)$ time. The total time is $O(n+t)$. The two 26-entry frequency arrays use $O(26)=O(1)$ auxiliary space.

## Alternatives and edge cases

- **Materialize every transformed string:** This follows the definition directly, but every `z` increases the text and future rounds repeatedly process those added characters, so time and memory depend on an exponentially growing output.
- **Per-character recursion:** Computing each input character's descendant length can work with memoization by letter and remaining rounds, but the iterative frequency transition is simpler and naturally combines duplicates.
- **Simultaneous updates:** Reusing a count changed earlier in the same round would transform some characters more than once; every next count must come from the previous vector.
- **No `z` reaches the boundary:** The length remains unchanged until at least one character becomes `z` and is transformed.
- **One `z`:** A single transformation produces two characters, while later transformations evolve both descendants independently.
- **Modulo arithmetic:** Counts, not only the final sum, must stay reduced so large intermediate populations remain bounded.
