## General

An alternating array can contain at most one more value of one parity than of the other. Therefore, if the even and odd counts differ by more than one, no sequence of swaps can succeed. If one count is larger by one, that parity must occupy indices $0, 2, 4, \ldots$. When the counts are equal, both the even-start and odd-start patterns are feasible.

For one feasible pattern, consider only the even values. Suppose their current indices in increasing order are $p_0, p_1, \ldots$, and their required indices are $t_0, t_1, \ldots$. The cheapest assignment pairs $p_i$ with $t_i$. Pairing them out of order would make two equal-parity values cross, which adds swaps without helping any parity constraint; uncrossing such a pair never increases the total distance.

Moving the $i$th even value from $p_i$ to $t_i$ crosses exactly $\lvert p_i-t_i\rvert$ odd values. Each such crossing is one adjacent swap, and every required even-odd inversion is counted once. Thus the cost of a pattern is

$$
\sum_i \lvert p_i-t_i\rvert.
$$

The positions do not need to be stored. Scan `nums` from left to right, maintain the next required even index (`0` for an even-start pattern or `1` for an odd-start pattern), and add the distance whenever an even value is encountered. Evaluate only the forced pattern when the counts differ, or both patterns and take their minimum when the counts are equal.

## Complexity detail

Let $n$ be the length of `nums`. Counting parity and evaluating at most two target patterns each take linear time, so the total time is $O(n)$. The scan keeps only counters and accumulated costs, giving $O(1)$ auxiliary space.

The answer can be quadratic in $n$ even though it is computed in linear time, because many values may each cross many opposite-parity values.

## Alternatives and edge cases

- **Explicit target arrays:** Recording current and target parity positions yields the same distance sum in $O(n)$ time, but uses $O(n)$ extra space unnecessarily.
- **Simulating adjacent swaps:** Repeatedly moving the next required parity into place is correct, but physically shifting values can require $O(n^2)$ time because the minimum answer itself may contain quadratically many swaps.
- **Parity-count imbalance:** A difference greater than one must return `-1` before evaluating a target pattern.
- **Equal counts:** Both starting parities are legal, and choosing only one can miss the minimum.
- **Odd length:** The more frequent parity is forced to occupy both endpoints, so only one starting pattern is legal.
- **Singleton input:** With no adjacent pair to violate alternation, the answer is `0`.
