## General
**Measure the value of one assignment**

Adding one guaranteed pass to a class currently described by $(p,t)$ changes its ratio by

$$
\Delta(p,t)
=
\frac{p+1}{t+1}-\frac{p}{t}
=
\frac{t-p}{t(t+1)}.
$$

The overall average divides the sum of class ratios by the fixed number $n$, so maximizing the average is equivalent to maximizing that sum. The next student should therefore be judged by $\Delta(p,t)$ rather than by the class's current ratio alone.

**Exploit diminishing marginal gains**

After assigning a student, the number of failures $t-p$ stays unchanged while the denominator in the gain becomes larger. Thus

$$
\Delta(p+1,t+1)
=
\frac{t-p}{(t+1)(t+2)}
\le
\Delta(p,t).
$$

Each class consequently offers a non-increasing sequence of possible gains. Suppose an allocation uses a smaller currently available gain while leaving a larger one unused. Exchanging those two assignments cannot reduce the total ratio. Repeating this exchange shows that an optimal allocation always takes the largest available marginal gain at every step.

**Maintain the current maximum with a heap**

Build a max-priority queue containing each class's current gain together with its passing and total counts. A language with only a min-heap can store the negative gain. For every extra student, remove the class with maximum gain, increment both counts, recompute its now-smaller next gain, and put it back.

This process extracts the globally best $e$ gains from the interleaved diminishing sequences. After all assignments, sum the final ratios stored in the heap and divide by $n$. The exchange argument ensures that no other distribution can produce a larger sum.

## Complexity detail
Creating and heapifying the $n$ class records takes $O(n)$ time. Each of the $e$ assignments performs one heap removal and insertion, costing $O(\log n)$, and the final ratio sum takes another $O(n)$. The total is $O(n+e\log n)$ time. The heap holds one record per class, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Scan all classes for every student:** Recomputing every gain and selecting the largest directly is correct but takes $O(en)$ time.
- **Sort gains once:** Initial sorting is insufficient because assigning a student changes that class's next gain and may alter the priority order.
- **Assign to the lowest current ratio:** A low ratio does not necessarily imply the largest improvement; total class size and number of failures both affect $\Delta(p,t)$.
- **Binary-search an allocation threshold:** Diminishing gains can also support a more mathematical batched allocation, but handling rounding and the final residual students is substantially more intricate.
- **Perfect classes:** When $p=t$, the marginal gain is zero and remains zero; such a class is useful only when every available gain is zero.
- **Single class:** Every extra student must go to it, and the heap still applies without a special case.
- **Equal gains:** Either tied class may be chosen first; the exchanged assignments have equal value, and later gains are recomputed normally.
- **Floating-point output:** Compute ratios with floating-point division and return the unrounded average; the judge applies the stated $10^{-5}$ tolerance.
