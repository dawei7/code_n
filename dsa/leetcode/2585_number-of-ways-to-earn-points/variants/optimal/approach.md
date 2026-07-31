## General

Let `ways[score]` count selections using only the question types already processed. Initially, only score zero is possible, so `ways[0] = 1`.

For a new type with limit `count` and value `marks`, the direct bounded-knapsack transition sums

$$
\texttt{ways}[s-k\cdot \texttt{marks}]
$$

over every feasible $k$ from $0$ through `count`. Scores with the same remainder modulo `marks` form independent sliding windows. While scanning scores upward, the next table therefore satisfies `next_ways[score] = ways[score] + next_ways[score - marks]`: the second term extends every valid selection at the previous score by one current-type question.

That addition temporarily includes selections using too many current questions. Once `score >= (count + 1) * marks`, subtract `ways[score - (count + 1) * marks]`, which is exactly the newly expired end of the window. Applying the modulus after the addition and subtraction keeps every state bounded.

Each type is processed into a fresh table, so a selection is counted once according to the number chosen from every type. Individual questions within one type are never distinguished, while separate rows remain separate choices even if their mark values match.

## Complexity detail

Let $n$ be the number of question types. Each type scans all scores from $0$ through `target` with constant work per score, giving $O(n \cdot \texttt{target})$ time. The previous and next tables each contain `target + 1` entries, so the auxiliary space is $O(\texttt{target})$.

## Alternatives and edge cases

- **Explicit bounded transition:** Trying every number from zero through `count` is straightforward and correct, but costs $O(n \cdot \texttt{target} \cdot C)$ time for maximum count $C$.
- **Two-dimensional dynamic programming:** Retaining a row for every processed type makes the state history explicit but increases space to $O(n \cdot \texttt{target})$ without improving the transition time.
- **Equal mark values:** Rows with the same `marks` value must still be processed separately because they represent distinct question types.
- **Unreachable targets:** Their table entry remains zero, including when every available mark exceeds the target or the total bounded capacity is too small.
- **Modulo subtraction:** The expired contribution may make the intermediate value negative, so normalization modulo $10^9 + 7$ is required after subtraction.
