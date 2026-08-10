## General

**Always take larger item values first**

The bag contains only three possible values:

$$
1>0>-1.
$$

Every selected item consumes one of the exactly $k$ required slots. Replacing a selected smaller value with an available larger one strictly increases the sum. Therefore an optimal selection takes as many ones as possible, then zeros, and uses negative ones only when forced.

No sorting or simulation is needed because the input already provides the count of each value.

**Case one: enough ones**

If `numOnes >= k`, choose $k$ one-valued items. Their sum is $k$.

No selection can do better because each individual item is at most one, so $k$ selected items have total at most $k$. The function immediately returns `k`.

Unused zeros and negative ones are irrelevant.

**Case two: ones plus zeros fill every slot**

If there are fewer than $k$ ones, every one should still be selected. This contributes `numOnes` to the sum and leaves

$$
k-\texttt{numOnes}
$$

slots.

If `numZeros` is at least this remainder, fill all remaining slots with zeros. They neither increase nor decrease the sum, so the maximum stays `numOnes`.

The second condition is written `numZeros >= k - numOnes` and returns `numOnes`.

**Case three: negative ones are unavoidable**

If ones and zeros together provide fewer than $k$ items, all of them must be selected. The number of still-empty slots is

$$
k-\texttt{numOnes}-\texttt{numZeros}.
$$

Every such slot must contain a negative one. Each decreases the sum by one, producing

`numOnes - (k - numOnes - numZeros)`.

The constraints guarantee that the bag contains at least $k$ total items, so enough negative ones always exist in this final branch. That is why `numNegOnes` does not need to appear in the formula.

**Exchange proof**

Suppose a candidate selection contains a zero while an unselected one exists. Swapping them increases the sum by one without changing the number of selected items.

Suppose it contains a negative one while an unselected zero exists. Swapping them also increases the sum by one.

Suppose it contains a negative one while an unselected one exists. Swapping increases the sum by two.

Applying these exchanges until none is possible yields exactly the priority order used by the three branches: all possible ones first, then zeros, then only unavoidable negative ones. Therefore no other selection has a larger sum.

**Trace the examples**

With three ones, two zeros, and $k=2$, the first branch applies. Select two ones and return two.

With the same bag and $k=4$, all three ones are selected and one zero fills the remaining slot. The second branch returns three.

As another example, suppose there are two ones, one zero, five negative ones, and $k=5$. Ones and zero fill three slots, so two negative ones are forced. The result is $2-2=0$.

**Why exact selection count matters**

If the rule allowed selecting at most $k$ items, negative ones would never be useful and the best choice might use fewer items. The requirement is exactly $k$, so the final branch must account for forced negative contributions.

The value of `k` may be zero. Then `numOnes >= k` is true and the function returns zero, correctly representing the empty selection of exactly zero items.

The three branches also partition all feasible inputs without overlap ambiguity. The first handles a nonnegative deficit after ones of zero. Reaching the second means at least one slot remains after taking every one, and its condition asks whether zeros cover that exact deficit. Reaching the final branch proves the remaining deficit is positive and can only be filled by negative ones.

**No identity distinctions are needed**

Items with the same written value are interchangeable for the sum. Counts completely describe all relevant choices. The function does not construct selected indices because only the maximum total is requested.

**Alternative compact formula**

The selected one count is `min(k, numOnes)`. After ones and zeros, the forced negative count is `max(0, k - numOnes - numZeros)`. The answer can be written

$$
\min(k,\texttt{numOnes})
-
\max(0,k-\texttt{numOnes}-\texttt{numZeros}).
$$

The branch structure is more beginner-friendly because it directly follows the descending value order.

## Complexity detail

The function performs a fixed number of comparisons and arithmetic operations. Its runtime is $O(1)$ and it uses $O(1)$ auxiliary space.

The counts may conceptually represent many items, but no collection proportional to them is built.

## Alternatives and edge cases

- **Expand and sort the bag:** This gives the same top-$k$ choice but wastes time and space proportional to the number of items.
- **Priority queue:** Repeatedly extracting the maximum is unnecessary when only three known values exist.
- **Zero selections:** `k=0` returns zero immediately.
- **No ones:** Zeros are taken first, followed by forced negative ones.
- **No zeros:** After all available ones, every remaining slot costs one.
- **Enough ones:** The theoretical upper bound $k$ is attained.
- **Exactly enough nonnegative items:** All ones and required zeros are used, with no negative penalty.
- **Negative result:** When forced negative ones outnumber selected ones, the optimal sum can legitimately be below zero.
- **Unused `numNegOnes` in code:** Feasibility constraints guarantee its count covers the final deficit.
