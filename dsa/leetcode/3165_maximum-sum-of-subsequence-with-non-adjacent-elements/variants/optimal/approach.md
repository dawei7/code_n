## General

A point update can change the best non-adjacent sum across the whole array, so recomputing the ordinary linear dynamic program after every query is too expensive. A segment tree makes the dynamic program composable: each node summarizes exactly the information its parent needs at the boundary between two adjacent intervals.

For an interval, store four values $F_{ab}$, where $a$ says whether the interval's left endpoint is allowed to be selected and $b$ says the same for its right endpoint. A zero bit forces that endpoint to be excluded; a one bit permits it but does not require it. For a one-element interval, only $F_{11}$ may select the value, so its state is `(0, 0, 0, max(0, value))`. Taking the maximum with zero represents the allowed empty subsequence.

Suppose adjacent child intervals have states $L$ and $R$. Their touching endpoints cannot both be selected. For every outer permission pair $(a,b)$, either force the right endpoint of the left child out while allowing the left endpoint of the right child, or do the symmetric choice:

$$
F_{ab}=\max\bigl(L_{a0}+R_{1b},\;L_{a1}+R_{0b}\bigr).
$$

These two alternatives cover every valid selection: any selection excludes at least one of the touching endpoints. They also create only valid selections because one endpoint is explicitly excluded. Inductively, each merged state is therefore the correct optimum under its endpoint permissions. The root state $F_{11}$ imposes no endpoint restriction and is the answer for the entire array.

Build all states once. For an update, replace the affected leaf and recompute only the nodes on its root path. Add the new root optimum to the answer after each update, applying the modulus to the accumulated total rather than to individual tree states.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$. Building the tree takes $O(n)$ time. Each point update visits $O(\log n)$ nodes and combines a constant four states at each node, so all queries take $O(q\log n)$ time. The total time complexity is $O(n+q\log n)$.

The segment tree contains $O(n)$ nodes, and its recursion depth is $O(\log n)$. The total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Recompute the linear dynamic program:** Run the usual take-or-skip recurrence after each update. This is simple and correct but takes $O(nq)$ time in the worst case.
- **Maximum-plus transition matrices:** Encode the same boundary dynamic program as small matrices in a segment tree. This is equally asymptotic but usually less transparent than the four permission states.
- **All values non-positive:** The empty subsequence keeps every root answer at zero.
- **Single-element array:** The only leaf is also the root; every update contributes `max(0, value)`.
- **Adjacent positive values:** The merge forbids choosing both sides of a child boundary, even when both values are individually attractive.
- **Repeated updates:** Each assignment changes the persistent current array; queries are not evaluated against the original input independently.
- **Modulo placement:** Keep tree values as exact sums because maxima must compare true values, and reduce only the accumulated answers modulo $10^9+7$.
