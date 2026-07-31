## General

**Make every jump span an extreme gap**

The squared cost grows convexly with the height difference, so large differences are disproportionately valuable. After sorting the heights, an optimal path can be uncrossed into one that alternates between the largest and smallest unvisited blocks. If two consecutive choices stay on the same side while an unused block exists at the opposite extreme, exchanging the nearer choice with that opposite extreme does not reduce either surrounding squared-gap contribution and strictly improves the path whenever the gaps differ.

Because every block is above the starting height `0`, orient this alternating path with the largest block first. This maximizes the initial squared jump and leaves the smallest block for the next, widest remaining gap. Continue with the next-largest block, then the next-smallest block, until every height has been used.

After sorting, two pointers implement exactly this order:

1. Take the value at the right pointer.
2. If a value remains, take the value at the left pointer.
3. Move the corresponding pointer inward after each choice and add the squared difference from the previously visited height.

Equal heights cause no difficulty: exchanging equal values changes no jump cost.

## Complexity detail

Let $n$ be the number of blocks. Sorting takes $O(n\log n)$ time, and the two-pointer traversal takes $O(n)$ time, for $O(n\log n)$ total time. The sorted copy uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Try every permutation:** This directly expresses the objective but requires factorial time.
- **Repeated extreme selection:** Alternating the current minimum and maximum without sorting first can be implemented by repeated scans, but that takes $O(n^2)$ time.
- **One block:** The only calorie contribution is its squared distance from the ground.
- **Equal heights:** The first jump contributes the common height squared, while every later jump contributes zero.
- **Input order:** The routine may visit blocks in any order, so the original array order has no semantic effect.
- **No return to ground:** Height `0` participates only before the first block; inserting it again would violate the source Note and inflate the score illegally.
- **Large result:** Squared differences accumulated over $10^5$ blocks require a 64-bit integer in fixed-width languages.
