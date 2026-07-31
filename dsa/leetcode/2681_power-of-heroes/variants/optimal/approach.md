## General

Sort the strengths as $a_0 \leq a_1 \leq \dots \leq a_{n-1}$. Consider all groups whose largest indexed strength is $a_j$. The singleton group contributes $a_j^3$. If $a_i$ with $i < j$ is the group's smallest indexed strength, every element strictly between indices $i$ and $j$ may be independently included or omitted. There are $2^{j-i-1}$ such groups, each contributing $a_j^2 a_i$.

For the current maximum $a_j$, define the weighted-minimum total

$$
W_j = \sum_{i=0}^{j-1} a_i 2^{j-i-1}.
$$

All groups ending at $j$ therefore contribute $a_j^2(a_j + W_j)$. The definition also gives the constant-time transition $W_{j+1} = 2W_j + a_j$: every previous choice gains one new include-or-omit decision, and $a_j$ becomes the new immediately preceding minimum.

Scan the sorted values from left to right, add $a_j^2(a_j + W_j)$ to the answer, and then update the weighted minimum. This partitions all non-empty index subsets by their greatest sorted index, so every group is counted once. Equal values cause no ambiguity because their original indices still correspond to distinct subset choices captured by the doubling recurrence.

## Complexity detail

Let $n$ be `len(nums)`. Sorting costs $O(n \log n)$ time and the recurrence scan costs $O(n)$, for $O(n \log n)$ overall. Python's in-place sort can use $O(n)$ auxiliary space; the recurrence itself uses $O(1)$ space. All accumulated values are reduced modulo $10^9 + 7$.

## Alternatives and edge cases

- **Enumerate each minimum for every maximum:** Applying the $2^{j-i-1}$ formula with a nested loop is correct but takes $O(n^2)$ time.
- **Enumerate every subset:** Directly computing each group's extrema takes exponential time and is infeasible for $n$ up to $10^5$.
- **Equal strengths:** Equal-valued heroes at different indices remain distinct subset members; sorting and the recurrence preserve that multiplicity.
- **Singleton group:** Its minimum and maximum are the same value, so its contribution is the cube of that strength.
- **Modulo arithmetic:** Reduce both the answer and weighted-minimum recurrence throughout to prevent unbounded intermediate growth.
