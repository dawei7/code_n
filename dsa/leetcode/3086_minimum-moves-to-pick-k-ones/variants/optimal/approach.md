## General

Creating a usable one always costs two moves: create it at a zero adjacent to Alice, then swap it onto her position. The same neighboring zero can be reused after every pickup. Original ones can be cheaper only in the immediate neighborhood: a one at Alice's index costs zero moves, and a one at either adjacent index costs one move.

**Measure the locally cheap originals.** For every index containing a one, count that one together with its immediate one-valued neighbors. Let $c$ be the largest such count, capped at `k`. Thus $0 \le c \le 3$. Alice can collect those $c$ consecutive original ones for $\max(0,c-1)$ moves: she starts on a one when $c>0$, takes it for free, and pulls each adjacent one inward with one swap.

If `maxChanges >= k - c`, fill all remaining pickups with created ones. This costs

$$
\max(0,c-1)+2(k-c).
$$

No other original one can improve this result: outside a length-three neighborhood, transporting an original one to Alice costs at least two moves, which is no cheaper than creating and collecting a new one.

**When changes are insufficient, gather original ones at a median.** Otherwise, all `maxChanges` changes should be used. After the locally cheap originals are exhausted, replacing any farther original by a created one costs no more. Therefore the number of required original ones is

$$
r = k-\texttt{maxChanges}.
$$

Store the indices of the original ones in increasing order. An optimal choice of $r$ originals is a consecutive window in this list: if a chosen set skipped an index lying between two chosen positions, replacing a farther endpoint by that skipped position cannot increase its distance from the gathering point.

For one window, the best `aliceIndex` is a median position. If the window occupies half-open index range $[l,q)$ in the positions list and $h=\lfloor(l+q-1)/2\rfloor$, its transport cost is

$$
p_h(h-l)-\sum_{i=l}^{h-1}p_i
\;+
\sum_{i=h+1}^{q-1}p_i-p_h(q-h-1).
$$

A prefix sum of the positions evaluates both sums in constant time. Scan every length-$r$ window, keep the minimum median cost, and finally add $2\,\texttt{maxChanges}$ for the created ones. Every original pickup contributes exactly its distance to the chosen median, and each created pickup contributes exactly two, so the minimum over all eligible windows is the global optimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building the positions and prefix-sum arrays and scanning all windows takes $O(n)$ time. These arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recompute every window's distances:** Summing distances to the median separately for each window is correct but can require $O(n^2)$ time; prefix sums reduce every window evaluation to $O(1)$.
- **Simulate swaps:** Moving individual ones step by step obscures the median structure and can take time proportional to the answer rather than the input size.
- **Use changes before nearby originals:** A created pickup costs two moves, while an initial one under Alice is free and an adjacent original costs one, so those local originals must receive priority.
- **No original ones:** The guarantee provides enough changes, and the answer is exactly $2k$.
- **One required pickup:** Alice starts on any existing one for zero moves; if none exists, one creation and one swap cost two.
- **Three consecutive ones:** Standing on the middle one collects all three in two swaps, the largest possible strictly-better-than-creation neighborhood.
- **Even-sized window:** Either central position is a median and gives the same total distance; consistently choosing the lower median keeps the formula simple.
- **Exactly `maxChanges` changes are not always needed:** The nearby shortcut may use fewer changes when enough cheap original ones exist; the median branch uses all changes only after that shortcut is impossible.
