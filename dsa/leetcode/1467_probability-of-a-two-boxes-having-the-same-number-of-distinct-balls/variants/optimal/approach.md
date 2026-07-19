## General
**Counting assignments instead of simulating shuffles**

The exact order of balls inside either half of the shuffle does not affect which colors a box contains. It is enough to choose which $n$ of the $2n$ physical balls go to box 1; box 2 receives the rest. Every such subset has equal probability, so the denominator is

$$
\binom{2n}{n}.
$$

For a color with `count` physical balls, assigning `take` of them to box 1 can be done in $\binom{\texttt{count}}{\texttt{take}}$ ways. Multiplying these binomial coefficients across colors counts the physical subsets represented by one vector of per-color allocations. Omitting these weights would incorrectly treat, for example, taking one of six same-colored physical balls as only one outcome.

**Tracking only the information the event needs**

Process colors one at a time. A dynamic-programming state `(used, difference)` stores the total combinatorial weight of allocations in which box 1 currently contains `used` balls and

$$
\texttt{difference}=(\text{distinct colors in box 1})-(\text{distinct colors in box 2}).
$$

The individual distinct-color counts are unnecessary: the final event asks only whether they are equal, which is exactly `difference == 0`. This compression removes one state dimension from a formulation that tracks both counts separately.

**Updating a color allocation**

For a color occurring `count` times, try every `take` from `0` through `count`, provided that `used + take` does not exceed $n$. Box 1 contains this color precisely when `take > 0`, while box 2 contains it precisely when `take < count`. The difference changes by

$$
[\texttt{take}>0]-[\texttt{take}<\texttt{count}],
$$

where a bracketed true condition contributes one and a false condition contributes zero. Thus assigning all balls of a color to box 1 adds one, assigning all to box 2 subtracts one, and splitting the color between boxes changes the difference by zero.

Add `ways * comb(count, take)` to the updated state. A new dictionary or table is used for each color so that one color cannot be processed more than once in a layer.

**Extracting the probability**

After all colors, state `(n, 0)` contains the exact number of equally likely box-1 subsets that both fill the first box and give equal distinct-color counts. Divide this integer by $\binom{2n}{n}$ to obtain the requested probability. Python's unbounded integers preserve the numerator exactly until the final floating-point division.

**Why every outcome is counted exactly once**

Every physical subset of $n$ balls has one unique vector saying how many balls of each color it sends to box 1. The transitions enumerate that vector color by color, and the product of binomial factors equals the number of physical subsets with that vector. Therefore no subset is omitted or double-counted.

The `used` coordinate accepts exactly the equal-sized distributions, and the difference coordinate is zero exactly when the two boxes contain the same number of distinct colors. State `(n, 0)` consequently counts all and only favorable outcomes, making its ratio to the full subset count the correct probability.

## Complexity detail
After any layer, `used` has at most $n+1$ values and `difference` lies between $-K$ and $K$, giving $O(Kn)$ states. Each of the $K$ colors tries at most $B+1$ allocations for each state. Total time is $O(K^2nB)$.

Only the current and next color layers are retained, so the dynamic-programming map uses $O(Kn)$ states. Binomial coefficients and exact weights occupy bounded additional entries relative to this state map under the source constraints.

## Alternatives and edge cases
- **Backtracking over per-color counts:** Enumerating every allocation vector and weighting leaves by binomial products is correct, but may explore $\prod_i(\texttt{balls[i]}+1)$ combinations. Memoization or iterative state merging avoids repeating equivalent partial states.
- **Track both distinct counts:** A state containing `(used, distinct1, distinct2)` is correct but larger. Their difference alone completely determines the final equality test.
- **Enumerate shuffled sequences:** Treating all physical permutations explicitly introduces factorial growth and repeats many orders that yield the same two box contents.
- **Unweighted color allocations:** Counting each `take` choice once is incorrect because different choices represent different numbers of physical subsets. The factor $\binom{\texttt{count}}{\texttt{take}}$ is essential.
- **Boxes are distinguishable:** Assigning a set of colors to box 1 and its complement to box 2 is a different distribution from the swap, even though both may either be favorable or unfavorable.
- **A color split between boxes:** That color increases both distinct counts and therefore leaves their difference unchanged.
- **A color entirely in one box:** It changes the distinct-count difference by one in the corresponding direction, regardless of how many balls that color has.
- **Equal sizes are mandatory:** States with `used != n` after all colors do not correspond to the prescribed first-half/second-half distribution and must not enter the numerator.
- **Floating-point tolerance:** Keep favorable and total counts as exact integers and divide once. Accumulating approximate probabilities at every transition introduces avoidable rounding error.
