# Minimum Adjacent Swaps to Reach the Kth Smallest Number

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/) |
| Frontend ID | 1850 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A digit string `num` represents a large integer. A wonderful integer uses exactly the same multiset of digits as `num` and has a greater numerical value. Order all wonderful integers by value, counting distinct digit arrangements in their ordinary lexicographic/numeric order.

The requested target is the $k$th smallest wonderful integer; the input guarantees that it exists. One operation swaps two adjacent digits in the current string. Return the minimum number of such swaps needed to transform `num` into that target arrangement.

### Function Contract

**Inputs**

- `num`: a digit string with $2 \le \lvert\texttt{num}\rvert \le 1000$.
- `k`: an integer with $1 \le k \le 1000$.
- The $k$th lexicographically larger distinct permutation of `num` is guaranteed to exist.
- Let $n=\lvert\texttt{num}\rvert$.

**Return value**

- Return the minimum number of swaps of neighboring positions required to change `num` into its $k$th next distinct digit permutation.

### Examples

**Example 1**

- Input: `num = "5489355142"`, `k = 4`
- Output: `2`

The fourth wonderful integer is `"5489355421"`, reachable with two adjacent swaps.

**Example 2**

- Input: `num = "11112"`, `k = 4`
- Output: `4`

The target is `"21111"`; the digit `2` must move four positions left.

**Example 3**

- Input: `num = "00123"`, `k = 1`
- Output: `1`

The next permutation is `"00132"`.

### Required Complexity

- **Time:** $O(kn+n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Generate the exact target**

Apply the standard next-permutation operation $k$ times. Find the rightmost pivot whose digit is smaller than its successor, exchange it with the smallest larger digit to its right, and reverse the non-increasing suffix. This produces the immediately next distinct lexicographic permutation even when digits repeat, so $k$ applications produce exactly the requested wonderful integer.

**Match repeated digits stably**

For each digit, record its source indices from left to right. Scan the target and map each occurrence to the earliest unused source index of the same digit. Pairing equal digits in any crossed order would add swaps without changing the target, so this stable occurrence matching is optimal.

The resulting index sequence states the order in which original positions must appear in the target. Every inverted pair in that sequence must cross once, and one adjacent swap can correct exactly one such crossing. Therefore its inversion count is both a lower bound and an achievable number of swaps.

**Count crossings efficiently**

Process mapped source indices from left to right with a Fenwick tree. For the current index, subtract the number of earlier indices at or to its left from the total already seen; the difference is the number of inversions ending here. Add the index to the tree and continue.

#### Complexity detail

Each next permutation scans at most $n$ digits, for $O(kn)$ time. Stable occurrence mapping is $O(n)$, and $n$ Fenwick queries and updates take $O(n\log n)$ time. The target, occurrence queues, mapped indices, and Fenwick tree use $O(n)$ space.

#### Alternatives and edge cases

- **Bubble the target digits into place:** Greedily locate each required digit and swap it left is simple and optimal, but takes $O(n^2)$ time in the transformation phase.
- **Quadratic inversion count:** Stable index mapping followed by two nested loops is correct but also costs $O(n^2)$.
- **Repeated digits:** Equal occurrences must be paired in their original order to avoid artificial crossings.
- **Leading zeros:** They remain ordinary digits in the fixed-width permutation and may be part of both source and target.
- **Long permutation suffix:** Reversing the suffix is required; merely swapping the pivot and successor does not produce the immediate next permutation.
- **Distinct-permutation order:** The next-permutation operation naturally skips duplicate arrangements created by equal digits.
- **Existence guarantee:** The algorithm may rely on every one of the requested $k$ successor permutations existing.

</details>
