## General

**Keep the same DP meaning but aggregate predecessors**

`f[i][h]` is the best good subsequence ending at index $i$ with at most $h$ unequal transitions.

Scanning every earlier index is too slow for $n=5000$. The transition only needs:

- best earlier length with the same ending value and budget $h$;
- best earlier length with a different ending value and budget $h-1$.

`mp[h][x]` stores the first quantity: maximum length using budget $h$ and ending value $x$.

**Find the best different value in constant time**

For each budget, `g[h]` stores three fields:

- `g[h][0]`: value label of the globally best ending;
- `g[h][1]`: its best length;
- `g[h][2]`: best length ending in a value different from that label.

When current value is $x$, the best different predecessor is `g[h-1][1]` if its label differs from $x$; otherwise it is `g[h-1][2]`.

This avoids scanning all values.

The state begins from `mp[h][x]` for an equal-value extension. If $h>0$, it compares the best different-value predecessor at budget $h-1$. Adding current element contributes one.

**Update aggregates**

After computing `f[i][h]`, `mp[h][x]` is raised if this is a better subsequence ending in $x$.

Updating `g[h]` preserves its top-two interpretation:

- if $x$ differs from current best label and new length reaches or exceeds best, old best moves to second and $x$ becomes best;
- if it is smaller, it may improve second;
- if $x$ is already best label, only best length changes and second remains a different label's best.

**Why ascending h does not contaminate the transition**

Within one index $i$, budget layers are processed upward. By the time $h$ reads `g[h-1]`, current value $x$ may already have updated that aggregate. The transition explicitly asks for a different ending value and excludes the best label if it equals $x$. Current-index state ends in $x$, so it cannot be used as a different predecessor. Other-value aggregate entries still come from earlier indices.

`mp[h][x]` is read before current layer updates it, so equal-value extension also uses only earlier indices.


Every optimal state ends after either the same value, costing no change, or a different value, costing one. `mp` supplies the exact best same-value case by invariant, and `g` supplies the exact best different-value case through its best/second-best split. These exhaust all predecessors.

Updates then incorporate the new state without losing prior maxima. Induction over indices and budgets proves every `f` value exact. `ans` checks all layers and endpoints; using all $k$ is not required because budgets mean at most.

**Concrete best/second-best example**

Suppose at one budget the best ending groups are value 7 with length 10, value 4 with length 8, and value 9 with length 6. Then `g[h]` stores `[7,10,8]`.

For a new value 4, the best different predecessor is length 10 because label 7 differs. For a new value 7, that length cannot be used as a different-value transition, so the correct choice is second-best length 8.

If a value-4 state reaches length 11, the update moves old best 10 into the second slot and makes 4 the best label. Only one second length is needed: a query excludes at most the single current best label. If current $x$ differs from it, global best works; if it equals, the maximum among all other labels is precisely second-best.

The dictionaries also compress the observed value domain implicitly, avoiding an impossible array indexed up to $10^9$.

## Complexity detail

There are $n(k+1)$ state computations, each doing expected constant-time map access and fixed aggregate updates. Time is $O(nk)$.

Table `f` uses $O(nk)$ space. The `k+1` maps may collectively store up to $O(nk)$ value entries, while `g` uses $O(k)$. Total auxiliary space is $O(nk)$.

The full `f` table is not needed after aggregate updates; a more memory-conscious implementation could omit it and keep only current scalars plus maps, though maps remain potentially $O(nk)$.

Hash-map expected constant time is assumed.

## Alternatives and edge cases

- **Quadratic predecessor DP:** ID 3176's direct method is easier to derive but costs $O(n^2k)$.
- **Coordinate compression plus arrays:** Replace maps with dense value IDs for deterministic access.
- **Store only one global best:** Incorrect when its ending value equals current $x$; second-best different value is necessary.
- **k equals zero:** Only `mp[0][x]` extensions matter, producing maximum equal-value count.
- **All values equal:** Same-value states grow to full length; second-best stays zero.
- **All values distinct:** Each extension consumes a change, limiting length to at most $k+1$.
- **Tied best lengths:** Update logic keeps one label as best and the other tied length as second, sufficient for exclusions.
- **At most budget:** Larger layers may hold solutions using fewer changes.
- **Current index contamination:** Excluding current value from the different predecessor prevents self-extension.
- **One element:** Every layer computes length one.
- **Large numeric values:** Maps avoid allocating by the $10^9$ value domain.
- **Answer across h:** The code checks every computed layer, though `f[i][k]` alone would also capture at-most semantics.
