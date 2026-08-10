## General

**Track only the water currently in the can**

Plants must be watered from left to right, and the gardener's location before each plant is completely determined. Before watering plant 0, the gardener is at the river at coordinate $-1$. Before every later plant `i`, plant `i - 1` has just been watered, so the gardener is at coordinate $i-1$.

The variable `water` records how much water remains. It starts at `capacity` because the can is full at the river. The variable `ans` accumulates movement steps; watering itself does not cost a movement step.

For each pair `i, p` from `enumerate(plants)`, `p` is the exact amount needed by plant `i`. The algorithm has only two possible actions, matching the rules.

**Move forward one step when enough water remains**

If `water >= p`, the current supply can completely water plant `i`. The gardener moves from the previous position to `i`, which costs exactly one step, waters the plant, and retains `water - p` units.

The code performs

`water -= p`

and

`ans += 1`.

Equality belongs in this branch. When `water == p`, the current plant can be watered completely, leaving zero water. The gardener must not refill before watering it because early refills are forbidden.

If a next plant exists, its own iteration will observe the zero remainder, find it insufficient for that positive demand, and account for the required refill then.

**When water is insufficient, count the round trip directly**

If `water < p`, the gardener cannot partially water the current plant. From the position immediately before it, coordinate $i-1$, the gardener must return to the river at coordinate $-1$.

That return distance is

$$
(i-1)-(-1)=i.
$$

After refilling, walking from the river to plant `i` costs

$$
i-(-1)=i+1.
$$

The combined movement is therefore

$$
i+(i+1)=2i+1.
$$

This is exactly the source expression `i * 2 + 1`.

The gardener arrives with a full can and immediately waters the plant. The remaining amount becomes `capacity - p`, which the source assigns directly to `water`. There is no need to first assign `capacity` and then subtract `p` as two separate operations.

The input guarantees `p <= capacity` for every plant, so a full refill is always sufficient to water the current plant completely.

**Why there is no extra ordinary forward step in the refill branch**

In the enough-water branch, `ans += 1` represents the direct move from plant `i - 1` to plant `i`. In the insufficient branch, that direct move does not occur. Instead, `2 * i + 1` already includes the entire route from plant `i - 1` back to the river and then forward to plant `i`.

Adding another 1 in that branch would count part of the movement twice.

For `i = 2`, the gardener stands at plant 1, coordinate 1. Returning to $-1$ takes 2 steps, and walking from $-1$ to plant 2 takes 3 steps. The total is 5, which equals $2\cdot2+1$.

**Trace the first example**

For `plants = [2, 2, 3, 3]` and `capacity = 5`:

- At plant 0, `water = 5` is enough. One step is added, and 3 units remain.
- At plant 1, 3 is enough for demand 2. One step is added, and 1 unit remains. The total is now 2.
- At plant 2, 1 is insufficient for demand 3. The gardener travels 2 steps back to the river and 3 steps forward, so the code adds $2\cdot2+1=5$. After watering, 2 units remain. The total is 7.
- At plant 3, 2 is insufficient for demand 3. The code adds $2\cdot3+1=7$. After watering, 2 units remain. The final total is 14.

The compact arithmetic exactly matches the physical walk without simulating each coordinate.

**Why the one-pass state is correct**

Before iteration `i`, maintain two facts:

1. `ans` equals all steps taken through watering plant `i - 1`.
2. `water` equals the actual water remaining at that position.

They are true initially: before plant 0, no steps have been taken and the full capacity is available at the river.

If `water >= p`, the rules require one forward step and no refill. Subtracting `p` and adding one preserves both facts after plant `i`.

If `water < p`, the rules require a return and refill because the next plant cannot be completely watered, and they forbid any alternative early refill schedule. The distance calculation adds exactly the necessary route, and `capacity - p` is exactly what remains after watering. The facts again hold.

By induction, after the final iteration, `ans` is exactly the number of steps needed to water all plants.

The algorithm never changes `plants`. It models the evolving can state with one integer and derives movement from the current index.

## Complexity detail

Let $n$ be the number of plants.

The `for` loop processes each plant once. Every iteration performs only constant-time comparisons, subtraction, multiplication, and addition. It does not walk back through earlier array entries when a refill occurs; the round trip is accounted for arithmetically. Total time complexity is $O(n)$.

The method stores `ans`, `water`, the index `i`, and the current demand `p`. These values occupy constant space regardless of $n$, so auxiliary space complexity is $O(1)$.

The numerical answer can be quadratic in $n$ because far-away refill trips are long, but computing each trip still takes constant time. A large returned number does not imply a large number of algorithm iterations.

## Alternatives and edge cases

- **Step-by-step movement simulation:** Moving a coordinate one unit at a time would reproduce the story but spend work proportional to the potentially large answer. The formula `2 * i + 1` compresses each forced refill trip into constant time.
- **Refilling whenever the can is not full:** This violates the rule forbidding early refills and can change the total route. A refill occurs only when the remaining water cannot completely satisfy the current next plant.
- **Prefix-sum grouping:** One can divide plants into maximal segments watered by each full can using cumulative sums. The direct state loop is simpler and already linear.
- **Exact equality:** If `water == p`, water the plant immediately without refilling. The `>=` condition correctly leaves zero afterward.
- **First plant:** Capacity is guaranteed to cover every single demand, so plant 0 normally takes the enough-water branch and costs one step from the river. Even the refill formula at `i = 0` would equal one, but no refill is required.
- **One plant:** The method adds one step from coordinate $-1$ to 0, waters it, and returns 1. There is no need to walk back after the final plant.
- **Refill before every later plant:** When each remaining amount is too small for the next demand, every iteration adds its full $2i+1$ trip. The formula handles this worst travel pattern without extra loops.
- **Water left after the last plant:** It is irrelevant. The gardener is not required to return to the river, and the solution adds no final return trip.
- **Demand equal to capacity:** After a refill, `capacity - p` becomes zero. The next positive-demand plant then correctly forces another refill.
- **Large capacity:** If the can covers all demands, every plant costs one forward step and the answer is $n$.
- **Capacity guarantee:** Because every `plants[i] <= capacity`, one refill always suffices. Without this guarantee, the branch would need to handle an impossible-to-water plant.
- **No array mutation:** The source records only the remaining total in `water`; plant demands remain intact throughout the traversal.
