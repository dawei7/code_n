## General

Sort the weights. Let $d=n/4$ be the number of days, with $\lceil d/2\rceil$ odd days and $\lfloor d/2\rfloor$ even days.

An odd day scores its largest pizza, so assigning any weight other than the largest still available cannot help: swapping in the larger weight increases or preserves that day's gain and leaves the displaced smaller weight available as filler elsewhere. Thus the odd days should receive the largest $\lceil d/2\rceil$ weights as their scored pizzas. Each such day can consume three of the globally smallest unused weights as $W$, $X$, and $Y$ without affecting its score.

An even day scores the second-largest pizza in its group. Among the remaining large weights, two must be consumed per even day: the larger becomes the unscored $Z$, and the next becomes the scored $Y$. Giving an even day a smaller possible $Y$ cannot improve any later group, so process the remaining upper end in pairs, skip the first weight of each pair, and add the second. Two small unused weights fill $W$ and $X$. After the odd winners and these even-day pairs are selected, every unselected weight is exactly one of the required fillers.

## Complexity detail

Let $n$ be the number of pizzas. Sorting takes $O(n\log n)$ time, and selecting the scored weights takes $O(n)$ additional time, for $O(n\log n)$ overall. Python's in-place sort may use $O(n)$ auxiliary storage; the greedy selection itself uses $O(1)$ extra space.

## Alternatives and edge cases

- **Repeated maximum selection:** Finding and removing the needed largest weights with linear scans is correct but can take $O(n^2)$ time.
- **Always scoring the current maximum:** This is wrong on even days, where the maximum is the unscored $Z$ and the second maximum supplies the gain.
- **Grouping consecutive sorted blocks:** Fixed blocks can waste large weights as fillers and miss the optimal interleaving of large winners with small fillers.
- **One day:** With four pizzas, day one is odd and the answer is simply the maximum weight.
- **Odd number of days:** There is one more odd day than even days, which is why odd winners are selected first.
- **Duplicate weights:** Equal values make several groupings equivalent, but the same index movement and proof continue to apply.
- **Large total:** Up to $5\cdot 10^4$ scored pizzas may each weigh $10^5$, so the result can exceed 32-bit signed range.
