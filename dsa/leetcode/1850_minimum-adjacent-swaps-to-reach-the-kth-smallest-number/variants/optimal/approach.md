## General
**Generate the exact target**

Apply the standard next-permutation operation $k$ times. Find the rightmost pivot whose digit is smaller than its successor, exchange it with the smallest larger digit to its right, and reverse the non-increasing suffix. This produces the immediately next distinct lexicographic permutation even when digits repeat, so $k$ applications produce exactly the requested wonderful integer.

**Match repeated digits stably**

For each digit, record its source indices from left to right. Scan the target and map each occurrence to the earliest unused source index of the same digit. Pairing equal digits in any crossed order would add swaps without changing the target, so this stable occurrence matching is optimal.

The resulting index sequence states the order in which original positions must appear in the target. Every inverted pair in that sequence must cross once, and one adjacent swap can correct exactly one such crossing. Therefore its inversion count is both a lower bound and an achievable number of swaps.

**Count crossings efficiently**

Process mapped source indices from left to right with a Fenwick tree. For the current index, subtract the number of earlier indices at or to its left from the total already seen; the difference is the number of inversions ending here. Add the index to the tree and continue.

## Complexity detail
Each next permutation scans at most $n$ digits, for $O(kn)$ time. Stable occurrence mapping is $O(n)$, and $n$ Fenwick queries and updates take $O(n\log n)$ time. The target, occurrence queues, mapped indices, and Fenwick tree use $O(n)$ space.

## Alternatives and edge cases
- **Bubble the target digits into place:** Greedily locate each required digit and swap it left is simple and optimal, but takes $O(n^2)$ time in the transformation phase.
- **Quadratic inversion count:** Stable index mapping followed by two nested loops is correct but also costs $O(n^2)$.
- **Repeated digits:** Equal occurrences must be paired in their original order to avoid artificial crossings.
- **Leading zeros:** They remain ordinary digits in the fixed-width permutation and may be part of both source and target.
- **Long permutation suffix:** Reversing the suffix is required; merely swapping the pivot and successor does not produce the immediate next permutation.
- **Distinct-permutation order:** The next-permutation operation naturally skips duplicate arrangements created by equal digits.
- **Existence guarantee:** The algorithm may rely on every one of the requested $k$ successor permutations existing.
