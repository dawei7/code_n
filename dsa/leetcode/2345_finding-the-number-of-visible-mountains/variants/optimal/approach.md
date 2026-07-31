## General

For a peak $(x,y)$, define its mountain interval as $[x-y,x+y]$. A peak $(a,b)$ lies inside or on another mountain centered at $(x,y)$ exactly when

$$
b \le y-\lvert a-x\rvert,
$$

which is equivalent to both $a-b\ge x-y$ and $a+b\le x+y$. Therefore, one mountain hides another precisely when the hidden mountain's interval is contained in the hiding interval.

Sort intervals by increasing left endpoint and, crucially, decreasing right endpoint when left endpoints tie. After this order, any possible containing interval appears before the interval it contains. The decreasing tie-break prevents a shorter interval with the same left endpoint from being counted before its longer container.

Scan while remembering the greatest right endpoint seen. A nonduplicate interval is visible exactly when its right endpoint extends strictly beyond that frontier. An endpoint equal to the frontier is contained on the border and is not visible. Identical intervals require separate handling: their peaks hide one another, so none of them is counted even if the interval extends the frontier. Because equal intervals are adjacent after sorting, checking either neighbor detects every duplicate group.

## Complexity detail

Let $n$ be the number of mountains. Building the intervals takes $O(n)$ time, sorting takes $O(n\log n)$, and the frontier scan takes $O(n)$. The interval list and sort workspace use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Compare every pair:** Direct geometric containment checks take $O(n^2)$ time and exceed the $10^5$-peak limit.
- **Sort equal left endpoints by increasing right endpoint:** This counts a shorter interval before encountering its container; the right endpoint must decrease on ties.
- **Duplicate peaks:** Identical intervals represent mountains whose peaks lie within one another, so every copy is invisible rather than one representative being visible.
- **Border containment:** Equality at either boundary still hides the peak, which is why the frontier comparison is strict.
- **Overlapping without containment:** Crossing intervals that each extend beyond the other's opposite endpoint represent separately visible peaks.
