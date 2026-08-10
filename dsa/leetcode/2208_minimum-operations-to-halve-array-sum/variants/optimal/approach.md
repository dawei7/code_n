## General

Halving a current value $x$ reduces the array sum by exactly $x/2$. To gain the greatest reduction from the next operation, choose the largest current value.

After halving that value, its new value is placed back among the candidates because it may still be optimal to halve it again. The exact solution maintains current values in a max-heap simulated with negative numbers.

**Track the remaining reduction target**

`s = sum(nums) / 2` is the amount by which the original sum must still be reduced.

Rather than recomputing the changing array sum after each operation, the code subtracts each achieved reduction from `s`. The loop ends when `s <= 0`, meaning accumulated reduction is at least half the original total.

**Build a max-heap with negative values**

Python's `heapq` is a min-heap. Pushing `-x` makes the numerically smallest heap item correspond to the largest positive current value.

The source pushes all $n$ values individually. Popping and negating returns the current maximum.

**Apply one halving operation**

`t = -heappop(pq) / 2` is half of the largest current value.

This quantity serves two roles:

- it is the new value after halving;
- it is also the reduction achieved, because $x-x/2=x/2$.

The code subtracts `t` from the remaining target and pushes `-t` back into the heap. The chosen array element can therefore be selected again in a later operation.

After every iteration, the heap contains exactly one entry for each original array position: its current value after however many times that position has been selected. This invariant means the next pop compares all legal next operations, including another halving of a previously chosen element, rather than comparing only untouched originals.

**Why the largest current value is the best next choice**

Among all currently available values, halving larger $x$ produces larger immediate reduction $x/2$.

Each original element supplies a diminishing sequence of possible reductions:

$$
\frac{x}{2},\frac{x}{4},\frac{x}{8},\ldots
$$

A later reduction from that sequence becomes available only after earlier halvings of the same element. The heap always contains the next available reduction for every element, represented by half its current value.

Choosing the largest current value therefore chooses the largest available marginal reduction.

**Why greedy minimizes the number of operations**

For any fixed number $q$ of operations, selecting the largest available marginal reduction at every step maximizes total reduction. If a schedule chooses a smaller available reduction while a larger one exists, swapping the larger choice earlier cannot invalidate its prerequisites—they were already satisfied—and cannot reduce the total gained in $q$ steps.

Repeating this exchange transforms an optimal $q$-operation schedule into the heap's greedy prefix without lowering reduction.

Therefore, if the greedy process has not reached half after $q$ operations, no other $q$ operations could have reached it. When greedy first crosses the target, that operation count is minimum.

For `[5,19,8,1]`, the heap first halves 19 for reduction 9.5, then its remaining 9.5 for 4.75, then eight for four. Total reduction 18.25 crosses the required 16.5 in three operations.

**Understand floating-point values**

Halving integers repeatedly produces dyadic rational numbers whose denominators are powers of two. Binary floating-point represents such fractions naturally, and the input totals remain within a moderate magnitude.

The exact source uses division producing Python floats. An alternative fixed-point formulation could double values or track rational reductions, but is unnecessary for the given constraints.

## Complexity detail

Let $n$ be the number of elements and let $q$ be the number of halving operations performed.

The exact source inserts $n$ elements one by one, costing $O(n\log n)$. Each of the $q$ iterations performs one heap pop and one push, costing $O(\log n)$. Total time is $O((n+q)\log n)$.

The heap always stores $n$ current values, so auxiliary space is $O(n)$. The manifest bounds match the exact implementation.

## Alternatives and edge cases

- **Use `heapify`:** Construct the negative-value heap in $O(n)$ time instead of $n$ individual pushes, improving the setup constant and bound.
- **Sort after every operation:** It finds the maximum but repeated sorting is much slower than heap updates.
- **Fixed-point arithmetic:** Represent values with scaled integers to avoid floats, though repeated halvings require managing growing powers of two.
- **One element:** Repeatedly halve it; the first operation already reduces its sum by exactly half, so the answer is one.
- **Several equal maxima:** Choosing any one gives the same reduction; the heap may break ties arbitrarily.
- **Choose the same element repeatedly:** Reinsertion allows this whenever its reduced value remains largest.
- **At least half:** The loop stops at zero or below, so exact equality and overshoot both qualify.
- **Positive inputs:** The heap never contains a zero starting value, though repeated halves approach zero.
- **Large original total:** Python's sum and integer-to-float conversion handle the constraint magnitude.
- **Operation counter:** It increments exactly once per pop/halve/push cycle.
- **Input preservation:** Current values live in the separate heap; `nums` is not modified.
- **Diminishing returns:** Each element's next reduction is half its previous one, supporting the marginal-gain greedy rule.
