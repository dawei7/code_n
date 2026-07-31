## General

Only the first $h=\lceil n/2\rceil$ digits are independent; mirroring them determines the full palindrome.

**Convert each half position into a modular weight**

The digit chosen at half index $i$ occupies decimal positions $i$ from the left and $i$ from the right. Its contribution modulo $k$ is the digit multiplied by

$$
w_i=10^{n-1-i}+10^i \pmod{k}.
$$

For the unpaired middle digit of an odd-length palindrome, include its single power only once. Precompute all powers of ten modulo $k$ iteratively.

**Record which suffix remainders are achievable**

Let \`reachable[i][r]\` state whether digits for half positions $i$ onward can contribute remainder $r$. The empty suffix reaches only remainder zero. Working from right to left, try digits 0 through 9 at each position and combine their weighted contribution with every reachable suffix remainder.

**Greedily make the number largest**

Scan the independent positions from left to right. Try digit 9 down to 0, except that the first digit stops at 1. For a candidate, combine its contribution with the remainder already fixed. Accept the first digit for which \`reachable[i+1]\` can provide the complementary remainder needed to finish at zero.

At every position, the reachability table proves that the accepted prefix has at least one divisible completion. Any larger digit rejected there has no completion at all, so no valid palindrome can have a lexicographically larger first differing digit. Induction makes the constructed half the largest feasible half. Mirroring it preserves the computed weighted remainder and produces the largest full palindrome.

## Complexity detail

There are $\lceil n/2\rceil$ positions, at most nine remainders, and ten digit transitions. The work is $O(nk)=O(n)$ because $1 \le k \le 9$. The suffix table stores $O(nk)=O(n)$ bytes, and the output uses $O(n)$ characters.

## Alternatives and edge cases

- **Divisor-specific constructions:** Hand-derived patterns can achieve linear time but require separate, error-prone logic for each of nine divisors.
- **Enumerate palindromic halves downward:** The half contains up to 50,000 digits, so numeric enumeration is infeasible.
- **Greedy without suffix feasibility:** Choosing 9 at every position can leave a nonzero final remainder with no way to repair earlier digits.
- The first half digit must be at least one; later independent digits may be zero.
- Odd lengths have one unpaired center digit.
- For $k=1$, the answer is all nines.
- A one-digit answer is the largest digit divisible by $k$.
- Divisibility must be tracked incrementally; converting a $10^5$-digit result to a machine integer is invalid.
- Producing the required $n$-character result already imposes an $\Omega(n)$ time lower bound.
