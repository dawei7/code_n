## General

**Only misplaced values constrain `k`.** Because the sorted permutation places value `i` at index `i`, every value currently at a different index must participate in at least one swap. If a value participates in a swap whose pairwise AND is `k`, that value contains every set bit of `k`. Consequently, every feasible `k` must be a bitwise submask of every misplaced value. Their combined bitwise AND is therefore an upper bound.

**The upper bound is attainable.** Let `answer` be the AND of all misplaced values. Since `answer` is itself an integer in $[0,n-1]$, that value occurs somewhere in the permutation. Every misplaced value `v` contains all bits of `answer`, so `v & answer == answer`. The value `answer` can therefore serve as a hub: allowed swaps with it can move and rearrange all misplaced values until each reaches its target index. Thus the upper bound is feasible and is the maximum possible `k`.

Scan the permutation once and AND only values for which `value != index`. An initially absent accumulator distinguishes an already sorted permutation from a genuine answer of zero.

## Complexity detail

The scan visits each of the $n$ values once and performs constant work per value, for $O(n)$ time. The accumulator uses $O(1)$ auxiliary space.

The benchmark sets size $N=n$ and uses rotations in which every value is misplaced. Tiers 32, 128, and 512 span 16x. The accepted method performs one linear scan. A correct placement simulation that linearly searches for each next target takes $O(N^2)$ time and must fail the scaling verdict despite returning the same answer.

## Alternatives and edge cases

- **Simulate sorting:** Repeatedly locating and placing the next target value can confirm sortability, but linear searches make it $O(n^2)$ and are unnecessary for a permutation.
- **Build swap components for candidate values:** Graph or disjoint-set checks can test one `k`, but enumerating candidates obscures the direct bitwise characterization and costs more time and space.
- **Already sorted:** No values constrain the accumulator; return `0` as required.
- **Maximum answer zero:** A genuine zero AND must not be confused with an uninitialized accumulator.
- **Correctly placed hub:** The value equal to the final AND may initially be correct; it may still be moved temporarily and restored while connecting the necessary swaps.
- **Permutation guarantee:** The proof relies on every value from 0 through $n-1$, including the computed AND value, being present exactly once.
