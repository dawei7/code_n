## General

**Maximize the stones removed at every operation**

Applying the operation to a pile of size $x$ removes $\lfloor x/2\rfloor$ stones and leaves

$$
x-\left\lfloor\frac x2\right\rfloor
=\left\lceil\frac x2\right\rceil.
$$

The number removed is nondecreasing with pile size. Therefore, at each step, choosing a currently largest pile gives the greatest immediate reduction in the total.

This greedy choice remains optimal across repeated operations. If a schedule applies an operation to smaller pile $a$ while a larger pile $b$ is available, exchanging that operation to $b$ cannot remove fewer stones. The updated $b$ can then participate in later choices. Repeated exchanges transform an optimal schedule into one that always takes a current maximum.

**Simulate a max-heap with negative values**

Python's standard heap is a min-heap. The solution stores `-x` for every pile size. The smallest negative number represents the largest original pile, so `pq[0]` is the current target.

`heapify(pq)` constructs the heap in linear time.

The update is compact:

`heapreplace(pq, pq[0] // 2)`.

`heapreplace` removes the smallest heap entry and inserts the supplied replacement in one operation while preserving heap order.

**Why floor division on a negative value gives the right remainder**

Suppose the largest pile is $x$, so the root is $-x$. Python floor division satisfies

$$
(-x)//2=-\left\lceil\frac x2\right\rceil.
$$

That is exactly the negative encoding of the remaining pile size. For $x=9$, `-9 // 2` is `-5`, representing five stones after removing four. For $x=4$, `-4 // 2` is `-2`.

Using truncation-toward-zero intuition would be dangerous here; Python's floor behavior is what makes the one-line update correct.

The expression `pq[0] // 2` is evaluated from the old root before `heapreplace` mutates the heap.

**Why the greedy sequence is correct**

At any state, the possible immediate reductions are $\lfloor x_i/2\rfloor$. A largest $x_i$ maximizes that value. After choosing it, the problem has the same form with one pile replaced by its ceiling half and one fewer operation.

An exchange argument shows any optimal first operation can be replaced by an operation on a maximum without worsening the remaining total; applying the same reasoning inductively to the residual state proves the full heap sequence optimal.

After exactly `k` replacements, negated heap entries represent all remaining piles. Their sum is negative, so `-sum(pq)` returns the positive remaining total.

**View operations as diminishing rewards**

For one pile, repeated operations offer a sequence of removable amounts. A pile of nine offers four stones first, then two from the remaining five, then one from three. These rewards never increase. Choosing a current largest pile also chooses a maximum available immediate reward because $\lfloor x/2\rfloor$ is monotone in $x$.

If an alleged optimal schedule chooses a smaller available reward before a larger one, swap the larger reward earlier. Taking it cannot make later choices worse: it only advances that pile to its next, no-larger reward, while the skipped smaller pile remains available. Repeating this exchange yields the heap order. This diminishing-return perspective makes the greedy proof robust even when the same pile is selected many times.

**Trace the first sample**

For `[5,4,9]`, the heap encodes `[-5,-4,-9]` and exposes `-9`. Floor division produces `-5`, so the positive piles are effectively `[5,4,5]`. A largest pile of five is selected next and becomes three. The remaining total is $5+4+3=12$. A different tie choice between the two fives gives the same total.

`heapreplace` is appropriate because heap size never changes. A separate pop followed by push would be equally correct but perform the same asymptotic work through two calls.

## Complexity detail

Let $N$ be the number of piles and $K$ the required operation count.

Building the negative list takes $O(N)$ time and `heapify` takes $O(N)$. Each `heapreplace` costs $O(\log N)$ and runs exactly $K$ times. Summing the final heap costs $O(N)$. Total time is $O(N+K\log N)$.

The negative heap contains $N$ integers, so auxiliary space is $O(N)$. Heap size never changes.

## Alternatives and edge cases

- **Sort after every operation:** Repeated sorting finds the maximum but costs roughly $O(KN\log N)$.
- **Scan for the maximum:** It uses constant extra space if mutating input, but costs $O(KN)$ time.
- **Frequency buckets:** Since pile sizes are bounded, counts by size can support operations efficiently, though repeated halving and maximum tracking add implementation complexity.
- **Same pile repeatedly:** The heap naturally selects it again whenever it remains largest, as the rules allow.
- **Odd pile:** Size $2q+1$ removes $q$ and leaves $q+1$; negative floor division encodes this ceiling.
- **Even pile:** Size $2q$ leaves exactly $q$.
- **Pile size one:** The operation removes zero and leaves one. Exact $k$ operations may eventually repeat such piles without changing the total.
- **Tied largest piles:** Choosing either removes the same number; heap ordering among equal values does not affect optimal total.
- **Diminishing removals:** Repeated gains from one pile never increase, which supports taking the currently best gain first.
- **Heap size:** Each operation replaces one entry rather than deleting a pile, so exactly $N$ entries remain.
- **One pile:** Every operation repeatedly replaces it by its ceiling half.
- **Exact operation count:** The loop always runs $k$ times, even when all piles reach one.
- **Input preservation:** A separate negative list is built, so `piles` itself is not mutated.
- **Final sign:** Heap entries stay nonpositive, so negating their sum recovers the total of represented positive pile sizes.
- **Imported heap helpers:** The exact source assumes `heapify` and `heapreplace` are available.
