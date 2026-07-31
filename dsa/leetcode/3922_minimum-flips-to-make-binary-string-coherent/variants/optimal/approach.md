## General

The two forbidden subsequences both contain exactly two `'1'` characters. Classifying a coherent target by its total number of ones reduces the problem to only three target families.

- With zero or one `'1'`, neither forbidden subsequence can exist.
- With exactly two `'1'` characters, every zero must lie between them. A zero before both ones would form `"011"`, while a zero after both would form `"110"`. Thus the only such target has the form `1 0* 1`.
- With at least three `'1'` characters, a coherent target cannot contain a zero. For any zero, the other ones split between its left and right sides. At least two would lie on one side: two on the right create `"011"`, and two on the left create `"110"`. Therefore this family consists only of the all-one string.

Now compute the cheapest member of each family:

1. To leave at most one one, keep any existing one and flip all the others. This costs $\max(c_1-1,0)$, where $c_1$ is the number of ones.
2. To make the string all ones, flip its $n-c_1$ zeros.
3. For the `1 0* 1` target when $n\ge2$, flip each zero endpoint to one and every interior one to zero.

Every coherent string belongs to one of these families, and each computed cost is exactly the Hamming distance to the cheapest target in that family. Taking their minimum therefore gives the global minimum number of flips.

## Complexity detail

Counting ones and evaluating the endpoint pattern each scan at most $n$ characters, so the total time is $O(n)$. The algorithm stores only counters and candidate costs, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Finite-state dynamic programming:** A DP can track whether appending each bit would complete either forbidden subsequence. It can also run in $O(n)$ time, but the three-family characterization is smaller and makes the minimum-flip choices explicit.
- **Enumerate every single-one target:** Measuring the Hamming distance separately for each possible location of the one is correct but takes $O(n^2)$ time without prefix counts.
- **Enumerate all binary targets:** Testing every transformed string is exponential and unnecessary once all coherent forms are characterized.
- **Subsequence versus substring:** The forbidden characters need not be adjacent; checking only contiguous occurrences gives incorrect answers.
- **Strings shorter than three:** They cannot contain a length-three subsequence, so the answer is always zero.
- **Exactly two ones:** Zeros are legal only between the two ones; `1 0* 1` includes `"11"` when the middle block is empty.
- **At most one one:** Its position is unrestricted, so an existing one can always be retained at no extra placement cost.
- **All-one target:** This is the only coherent possibility that can contain at least three ones.
