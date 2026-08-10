## General

The choice for one house affects the next house only through its color: the next house may use either of the other two colors, and no earlier detail matters. This is the key dynamic-programming compression. Instead of remembering every complete color sequence, remember the cheapest valid cost for the processed prefix under each possible color of its final house.

The exact solution uses three scalars:

- `a`: minimum cost for all processed houses when the latest house uses color 0;
- `b`: minimum cost when the latest house uses color 1;
- `c`: minimum cost when the latest house uses color 2.

The names of the colors do not affect the recurrence. They correspond in order to the three entries in each cost row.

Before any house is processed, `a = b = c = 0`. The empty prefix costs zero, and treating all three prior-ending states as zero lets the first house choose any color without a special branch.

**Derive the transition for one house**

Suppose the next row is `[ca, cb, cc]`.

If the current house is painted color 0, the previous house cannot also be color 0. The only legal predecessor states are the ones ending in colors 1 and 2, whose best costs are `b` and `c`. The cheapest valid prefix ending in color 0 is therefore

$$
a_{new}=\min(b,c)+ca.
$$

By the same reasoning,

$$
b_{new}=\min(a,c)+cb
$$

and

$$
c_{new}=\min(a,b)+cc.
$$

Every transition adds the cost of painting the current house and chooses the cheaper of exactly the two predecessor colors that satisfy the adjacency rule.

**Why tuple assignment is essential**

The source writes all three updates in one assignment:

```text
a, b, c = min(b, c) + ca, min(a, c) + cb, min(a, b) + cc
```

Python evaluates the entire right-hand side using the old `a`, `b`, and `c` before assigning any new value. This is crucial because all three new states describe the same number of processed houses and must depend only on the previous row's states.

If the code assigned `a` first and then calculated `b`, that calculation could mix the new cost ending at the current house with old costs ending at the previous house. Such a mix could effectively paint the current house twice or violate the adjacency model. Simultaneous assignment preserves clean layer boundaries without allocating explicit `new_a`, `new_b`, and `new_c` variables.

**Trace through the example**

For

```text
[[17, 2, 17], [16, 16, 5], [14, 3, 19]]
```

the state evolves as follows:

| Houses processed | `a` | `b` | `c` | Meaning |
|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | empty prefix |
| 1 | 17 | 2 | 17 | cost of each possible first color |
| 2 | 18 | 33 | 7 | cheapest valid prefix ending in each second-house color |
| 3 | 21 | 10 | 37 | cheapest valid full painting ending in each final color |

For the second house, the color-2 state is `min(17, 2) + 5 = 7`, corresponding to color 1 for the first house followed by color 2. For the third house, the color-1 state is `min(18, 7) + 3 = 10`, continuing from color 2. This represents total cost `2 + 5 + 3 = 10`.

After every house is processed, the final house may use any of the three colors. The answer is therefore `min(a, b, c)`, which returns `10` in this trace.

**Why the three values contain all necessary history**

Many different valid paintings can end with the same color. Only the cheapest one matters for the future. Any more expensive prefix ending in that same color gives the next house exactly the same legal color choices, so it can never overtake the cheaper prefix after both add the same future costs. Discarding dominated prefixes is safe.

The state still must distinguish the three ending colors, because they forbid different choices for the next house. Keeping only one overall minimum would lose the last color and could accidentally extend it with the same color.

**Why the recurrence is correct**

After zero houses, each state value zero correctly represents the empty cost. Assume `a`, `b`, and `c` are the minimum costs for valid paintings of the first `k` houses ending in their corresponding colors. Any valid painting of house `k + 1` with color 0 must extend a valid prefix ending in color 1 or 2; choosing the cheaper such prefix and adding `ca` therefore gives the minimum possible color-0 state. The same argument applies to colors 1 and 2.

Thus the meaning of all three states remains true after each row. At the end, every valid full painting belongs to exactly one of the three ending-color classes, and taking their minimum gives the global optimum.

The solution does not need to reconstruct the chosen color sequence because the contract requests only the minimum cost. If the actual colors were required, predecessor choices would need to be retained.

## Complexity detail

Let $n$ be the number of houses. The loop processes each cost row once. Because there are exactly three colors, every iteration performs a fixed number of comparisons and additions. Total time is $O(n)$.

Only three dynamic-programming values and three current row values are needed. Their count does not grow with $n$, so auxiliary space is $O(1)$. The input matrix is read without modification, unlike an in-place table update.

If the number of colors were a variable $k$ rather than the fixed constant three, a direct transition checking every different previous color would take $O(nk^2)$ time. More advanced minimum/second-minimum tracking can reduce the generalized problem to $O(nk)$, but that machinery is unnecessary here.

## Alternatives and edge cases

- **Enumerate all valid colorings:** The first house has three choices and every later house has two, creating $3\cdot2^{n-1}$ assignments. Scoring them is exponential and repeats equivalent ending-color subproblems.
- **Top-down memoization:** Cache the minimum remaining cost for `(house index, previous color)`. It reduces time to $O(n)$ for three colors but uses $O(n)$ cache and recursion-stack space.
- **Full DP table:** Store three values per house. It makes every subproblem visible and can support reconstruction, but uses $O(n)$ space when only the previous row is needed for the cost alone.
- **Overwrite `costs`:** Update each row with accumulated optimal costs. This also uses constant auxiliary space but mutates the caller's input; the exact scalar solution preserves it.
- **One house:** Starting from zero makes the first update equal the three raw costs, and the final minimum chooses the cheapest color.
- **Adjacent equal colors:** No transition ever reads the old state for the same color, so such assignments are excluded by construction.
- **Tied costs:** `min` may choose either predecessor implicitly. Since only the minimum numeric cost is returned, no tie-breaking rule is needed.
- **All costs positive:** The recurrence does not rely on positivity for correctness, but positivity ensures totals grow normally and is part of the contract.
- **Empty input outside the constraints:** The loop would not run and `min(0, 0, 0)` would return `0`, a sensible extension even though the documented minimum is one house.
- **Sequential assignment bug:** Updating `a`, then using that new `a` to compute `b` or `c`, would mix DP layers. Tuple assignment prevents this subtle error.
- **Recovering the painting plan:** Three scalars intentionally discard predecessor identities. To output colors, store back-pointers for each house and ending color, increasing space to $O(n)$.
