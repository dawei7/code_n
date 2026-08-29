## General

A subarray of length at least three is valid when it contains some value at least $k$. It is enough to enforce this for every subarray of length exactly three:

- If every length-three window has such a value, every longer subarray contains a length-three window and therefore also has one.
- If a length-three window has all values below $k$, that window itself violates the condition.

Thus we need choose positions to “cover” every three-consecutive window. Choosing index $i$ costs

$$
c_i=\max(k-\texttt{nums}[i],0).
$$

After paying that many increments, its value reaches at least $k$. When it is already at least $k$, its cost is zero and it covers windows without any operation.

The condition that every three positions contain a chosen index is equivalent to never leaving three consecutive positions unchosen. The source solves this with three rolling dynamic-programming states.

**Meaning of the rolling states**

After processing an index, `f`, `g`, and `h` represent minimum costs of valid partial choices whose relevant most recent chosen position is respectively two steps behind, one step behind, or the current position.

Only these possibilities matter. Any choice older than the last three positions cannot cover the next window. We need only the cheapest way to arrive in each allowable recent-choice position.

The update for current value `x` is

`f, g, h = g, h, min(f, g, h) + max(k - x, 0)`.

Python evaluates the complete right side from the old tuple before assigning the left side, so the update is simultaneous.

**Understand each component**

Old `g` becomes new `f`: a chosen position that was one step behind becomes two steps behind.

Old `h` becomes new `g`: the previously current chosen position becomes one step behind.

To make the new current position chosen, extend the cheapest old state and pay its promotion cost. Hence new `h` is `min(f, g, h) + max(k - x, 0)`.

There is no transition that shifts old `f` without choosing the current position. That would make its last relevant choice three steps behind, leaving the newest length-three window uncovered.

**Why starting all states at zero works**

Before enough elements exist to form a length-three window, no coverage is required. Initial values `f = g = h = 0` act as zero-cost fictitious recent choices before the array. As the tuple shifts through the first two elements, these sentinels allow the algorithm not to pay prematurely.

By the time the third real element is processed, any surviving state corresponds to choosing at least one of the first three positions. From then onward, the forbidden “three unchosen” transition is excluded on every step.

For promotion costs `[2,1,4]`, after all three positions the minimum state is $1$, correctly choosing the middle position. The initialization does not permit a zero-cost uncovered first window because the fictitious states have shifted out.

**Why the final minimum is exact**

After the last element, a valid solution may have its last chosen position at any of the final three indices. These cases are stored in `f`, `g`, and `h`. Returning `min(f,g,h)` selects the cheapest.

Every DP path constructs a set with no gap of three unchosen indices, so every length-three window is covered. Conversely, take any valid chosen set. At each processed position, its last choice lies among the last three positions; following that state through the transitions reproduces its total cost. The DP minimizes over all such histories and finds the global optimum.

The transformation from increments to selection is exact. Raising a chosen value above $k$ costs more without covering additional windows, so an optimum raises it exactly to $k$. Incrementing a value without reaching $k$ contributes nothing to beauty and can be removed. Hence each useful decision has exactly cost $c_i$.

## Complexity detail

The loop processes each of the $n$ elements once. Every iteration performs a constant number of minimum, subtraction, maximum, and assignment operations. Time complexity is $O(n)$.

Only three DP values and the current element are stored. The simultaneous tuple has constant size, so auxiliary space is $O(1)$. The input is not mutated.

Costs and their total may be large, but Python integers safely represent them. In a fixed-width language, use a type large enough for up to $n$ increments of size near $k$.

## Alternatives and edge cases

- **Full dynamic-programming array:** Store the best cost when each index is the latest chosen position. It gives $O(n)$ time and $O(n)$ space, but only the last three entries are needed.
- **Greedy cheapest item in each window:** Independently choosing a minimum-cost position per window can be suboptimal because one selected position may cover three overlapping windows.
- **Track consecutive unchosen count:** A four-state formulation for zero, one, or two consecutive skips is equivalent. The source tracks the location of the recent choice.
- **Value already at least $k$:** Its cost is zero. Treating it as chosen is free and covers every containing window.
- **$k=0$:** Every legal value is already at least zero, every promotion cost is zero, and the answer is zero.
- **Exactly three elements:** At least one must reach $k$; the rolling transition returns the minimum of their promotion costs.
- **Longer windows:** They need no separate checks because each contains a covered length-three subwindow.
- **Partial increments:** Spending fewer than `k - nums[i]` on a below-threshold value never makes it useful.
- **Simultaneous assignment:** Updating `f` before calculating new `h` manually would mix old and new states. Tuple assignment avoids that error.
