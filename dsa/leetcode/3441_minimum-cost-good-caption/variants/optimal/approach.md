## General

Changing a source letter with alphabet index $x$ into a target letter with index $y$ costs $\lvert x-y\rvert$. The difficulty is enforcing runs of at least three while also resolving equal-cost answers lexicographically.

Define `dp[last][i]` as the minimum cost to transform the suffix beginning at position `i`, assuming the already-written run of character `last` has length at least three. From that state there are only two meaningful actions:

- Extend the completed run by one position using `last`.
- Start a different run by writing its first three equal characters at once, after which that new run is complete.

This formulation represents every good caption. A run longer than three is formed by repeated extensions, and changing characters is allowed only through a three-character transition. For every position, compute the cheapest and second-cheapest new-run transitions among the 26 letters. Then each `last` state can exclude itself in constant time: use the cheapest transition unless it starts with `last`, in which case use the second cheapest. Together with the one extension transition, this fills all 26 states per position.

The caption must begin with a complete three-character run. Choose its character by minimum cost, with the ascending loop automatically favoring the smallest letter on a tie. During reconstruction, inspect every action that preserves the stored optimal cost and choose the smallest possible next output character. An extension emits `last` once; a switch emits the chosen new character three times. Because lexicographic order is decided at the first differing output position, this local smallest-character choice yields the globally lexicographically smallest minimum-cost caption.

Compact unsigned-integer arrays store the DP columns. The maximum possible cost is only $25n$, so the values fit safely while avoiding the much larger object overhead of millions of ordinary Python integers.

## Complexity detail

Let $n$ be the caption length. The alphabet size is the fixed constant 26. Each position evaluates 26 new-run costs and 26 completed-run states, and reconstruction evaluates at most 26 choices per emitted step, giving $O(n)$ time. The 26 DP arrays and numeric caption representation use $O(n)$ space.

## Alternatives and edge cases

- **Try every possible run length:** Enumerating all lengths of at least three at every position leads to $O(n^2)$ transitions.
- **Store the best suffix string in each DP state:** Repeated string construction and comparison can require quadratic space and time.
- **Choose median letters per fixed block:** The optimal run boundaries are not known in advance, and lexicographic ties may span several blocks.
- **Length below three:** No output of the same length can contain a valid run, so return `""`.
- **Already good caption:** Zero cost is optimal, and reconstruction preserves the original string.
- **Runs of four or five:** Repeated extension handles them directly; there is no need to restrict the answer to groups of exactly three.
- **Equal-cost captions:** Reconstruction selects the smallest feasible next character, including ties between extending and starting a new run.
