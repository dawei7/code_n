## General

**Identify the positions that must become zero.** Let $Z$ be the total number of zeroes. Any valid final array has exactly those $Z$ zeroes in the suffix beginning at index $N-Z$. Values within the prefix and suffix need not otherwise be ordered.

Count the nonzero values currently occupying that required suffix. Every such value must leave the suffix, so each needs at least one swap. This count is a lower bound because one swap can correct at most one of these misplaced suffix positions.

The prefix contains exactly the same number of misplaced zeroes. Pair each nonzero in the suffix with one zero in the prefix and swap the pair. Every operation corrects both positions, and after exactly the counted number of swaps the entire suffix is zero. The lower bound is therefore achievable and equals the minimum answer.

The implementation first counts zeroes, computes the suffix boundary, and then counts nonzero entries from that boundary to the final index. It never needs to mutate the input.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Counting zeroes and inspecting the required suffix each take at most one linear pass, so the total time is $O(N)$. The implementation retains only counters and indices, using $O(1)$ auxiliary space.

The source domain caps $N$ at 100, which is too narrow for a stable multi-tier runtime trend at this amount of constant work. The package therefore uses a `bounded_domain` complexity certificate: the reference performs at most $2N$ element inspections, and exhaustive plus randomized property checks replace a noisy timing comparison.

## Alternatives and edge cases

- **Two explicit pointers:** Pairing a zero from the prefix with a nonzero from the suffix and performing each swap also takes $O(N)$ time and $O(1)$ space, but mutation is unnecessary when only the operation count is requested.
- **Adjacent-swap simulation:** Bubbling every zero rightward can take $O(N^2)$ time and counts adjacent exchanges. That count is generally too large because one permitted operation may swap arbitrary distant indices.
- **Stable compaction:** Rebuilding the nonzero prefix and zero suffix solves a stronger ordering task and uses additional storage without helping determine the minimum swap count.
- **No zeroes:** Then $Z=0$, the required suffix is empty, and the answer is zero.
- **All zeroes:** The required suffix is the complete array, but it contains no misplaced nonzero value, so the answer is also zero.
- **Repeated nonzero values:** Their magnitudes and multiplicities do not matter; every nonzero is interchangeable for this objective.
