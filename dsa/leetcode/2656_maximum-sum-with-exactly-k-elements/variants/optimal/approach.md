## General

**The current maximum is always the best choice**

One operation selects value $m$, adds $m$ to the score, removes that occurrence, and inserts $m+1$.

Let $x$ be the largest value currently present. Choosing any smaller $y<x$ gives fewer points immediately:

$$
y<x.
$$

It also produces $y+1\le x$, while choosing $x$ produces $x+1$, a value at least as strong for every future operation.

Therefore, selecting a smaller value cannot recover the points lost now and cannot create a better future maximum. An optimal strategy always chooses the current maximum.

**After the first choice, the same evolving element stays maximal**

Let:

$$
x=\max(\texttt{nums})
$$

be the original maximum.

After selecting it once, it is replaced by $x+1$. Every untouched array element is at most $x$, so the replacement is strictly maximal.

Selecting it again replaces it by $x+2$, which remains maximal. Repeating this reasoning shows that the optimal selected values are:

$$
x,\ x+1,\ x+2,\ \ldots,\ x+k-1.
$$

No heap or repeated search is needed after finding the original maximum.

**Exchange argument for the greedy choice**

Consider any strategy that, at some operation, selects value $y$ while a current maximum $x\ge y$ exists.

Modify the strategy to select $x$ at this operation instead.

- The modified score gains $x$ rather than $y$, so it is no smaller.
- The modified array contains $x+1$ instead of retaining $x$ and creating $y+1$.
- Since $x+1\ge x$ and $x+1\ge y+1$, the modified state has a candidate at least as large as every value relevant to the original strategy's next choice.

Future selections can continue from this larger evolving value. Replacing every nonmaximum choice this way never decreases total score, proving that an all-maximum strategy is optimal.

**Sum the arithmetic progression**

The score is:

$$
x+(x+1)+\cdots+(x+k-1).
$$

Separate the common $x$ term:

$$
kx+(0+1+\cdots+(k-1)).
$$

The sum of the first $k-1$ nonnegative integers is:

$$
\frac{k(k-1)}2.
$$

Therefore:

$$
\text{answer}
=
kx+\frac{k(k-1)}2.
$$

The source returns this formula directly after computing `x = max(nums)`.

**Why integer division is exact**

One of $k$ and $k-1$ is always even, so product $k(k-1)$ is divisible by two.

Python's `// 2` therefore performs exact integer arithmetic with no rounding loss.

**Trace the first example**

For `nums = [1,2,3,4,5]` and $k=3$, original maximum is five.

The optimal selections are five, six, and seven. Formula gives:

$$
3\cdot5+\frac{3\cdot2}{2}
=
15+3
=
18.
$$

The conceptual array changes are unnecessary to perform because the chosen progression is already known.

**Trace duplicate maxima**

For `[5,5,5]` and $k=2$, choosing any one of the fives is equivalent.

After the first selection, its replacement six is larger than the two untouched fives, so the second selection must use six. Formula gives:

$$
2\cdot5+\frac{2\cdot1}{2}=11.
$$

The identity of the selected occurrence does not matter; only its value affects score and future values.

**Why exactly $k$ creates no stopping decision**

All input values are positive, so every operation increases the score. More importantly, the contract mandates exactly $k$ operations regardless of whether another operation seems desirable.

The formula contains exactly $k$ progression terms. It does not optimize the number of operations or stop early.

**No array mutation is required**

The described operation changes the array, but the function only needs the maximum achievable score. Once the greedy structure is proved, simulating removals and insertions adds work without adding information.

The exact implementation reads `nums` to find its maximum and leaves the list unchanged.


The exchange argument proves an optimal strategy can select a current maximum at every operation.

After selecting the original maximum $x$, its replacement $x+1$ is a current maximum; inductively, operation $r$ selects $x+r$ for $0\le r<k$.

Summing those forced optimal rewards gives the returned arithmetic-series formula. Hence the result is both achievable and at least as large as every other strategy's score.

## Complexity detail

Finding the maximum scans $n$ values in $O(n)$ time. The arithmetic formula then takes $O(1)$ time.

The algorithm stores only `x` and fixed arithmetic temporaries, using $O(1)$ auxiliary space. It does not modify or copy the array.

## Alternatives and edge cases

- **Max-heap simulation:** Correctly performs $k$ selections in $O(n+k\log n)$ time, but the persistent-maximum observation makes it unnecessary.
- **Sort the array:** Finding only the maximum does not require $O(n\log n)$ sorting.
- **Choose different equal maxima:** They are interchangeable on the first operation.
- **`k = 1`:** The formula returns the original maximum.
- **Single-element array:** The same element evolves through every operation.
- **Duplicate maximum values:** After one is incremented, that occurrence becomes the unique larger choice.
- **Exactly `k` operations:** The progression has precisely $k$ terms.
- **Positive input:** Every reward is positive, though optimality follows from comparison even without this.
- **Large total:** Python integers avoid overflow.
- **Input preservation:** The conceptual operation is not simulated on `nums`.
