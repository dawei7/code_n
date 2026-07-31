## General

Consider a starting zero at index $i$. Let $L$ be the sum of the elements strictly to its left and $R$ the sum strictly to its right. These sums are the numbers of decrements that must eventually be performed on the two sides.

Each time the pointer encounters a positive value, it decrements that value and reverses direction. Consequently, successful decrements alternate between the left and right sides. The initial direction determines which side receives the first decrement. If $L=R$, either side may go first and both directions succeed. If $L=R+1$, only a left-first traversal can succeed; if $R=L+1$, only a right-first traversal can succeed. When $\lvert L-R\rvert>1$, alternating visits must exit while some positive mass remains, so neither direction is valid.

Compute the total array sum once. During a left-to-right scan, maintain `left`, the sum before the current position. At a zero, `right = total - left` because the current value contributes nothing. Add two when the sums are equal and one when their absolute difference is one. Then add the current value to `left` and continue.

Every possible selection begins at exactly one zero and chooses one of two directions. The side-sum conditions above classify both directions for that zero without simulating any pointer movement, so the accumulated count contains every valid selection exactly once.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Computing the total and scanning the array both take $O(n)$ time. Only the total, the running left sum, and the answer are stored, so auxiliary space is $O(1)$.

The benchmark size is $n$. Its all-zero inputs make all $2n$ selections valid. The prefix-sum method remains linear, while separately simulating every starting zero in both directions walks a total of $\Theta(n^2)$ positions.

## Alternatives and edge cases

- **Simulate every selection:** Copying the array and following the process is direct and correct, but repeated traversals and decrements are much slower than comparing side sums.
- **Prefix-sum array:** A stored prefix array also answers each side sum in constant time, but it uses $O(n)$ space when a running sum is sufficient.
- **Equal side sums:** Both initial directions alternate the same number of decrements and therefore both count.
- **Difference of one:** Exactly one direction works—the direction toward the side with the larger sum.
- **Several consecutive zeroes:** Each index is a distinct starting position and must be counted separately even though adjacent zeroes have the same surrounding nonzero values.
- **All zeroes:** Every index and both directions are valid, giving $2n$ selections.
- **Single element:** The guaranteed zero immediately exits in either direction, so the answer is two.
