## General
Every move preserves the combined number of occurrences of each letter. If all $N$ final words are identical, the global count of every character must therefore be divisible by $N$.

This condition is also sufficient. When every letter count is divisible by $N$, assign exactly one-$N$th of each letter's occurrences to every target word. The operation permits moving any character to any position, so characters can always be rearranged to realize those identical multisets and then ordered identically.

Count all letters across all words in one pass, and return whether every resulting count is divisible by `len(words)`.

## Complexity detail
The scan visits each of the $S$ input characters once, so it takes $O(S)$ time. Only counts for the 26 lowercase English letters are needed. Because that alphabet size is fixed independently of the input, the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Compare total length only:** Divisibility of $S$ by $N$ is necessary but not sufficient; each individual letter count must divide evenly.
- **Simulate moves:** Constructing a sequence of character transfers is unnecessary because the divisibility test completely characterizes feasibility.
- **Sort all characters:** Sorting can expose counts, but it costs $O(S \log S)$ time instead of a linear scan.
- **One word:** With $N=1$, every count is divisible and no operation is needed.
- **Different initial lengths:** The operation may empty or lengthen words, so unequal starting lengths do not by themselves make the answer false.
- **Repeated characters:** Multiplicity is the essential information; the original positions of equal letters do not matter.
