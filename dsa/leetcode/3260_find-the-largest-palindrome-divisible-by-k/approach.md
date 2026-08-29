## General

A palindrome is determined by its first half. Choosing a digit on the left also fixes the mirrored digit on the right, except for the single center digit of an odd-length number. The solution expresses each half-position's effect on the number modulo $k$, uses dynamic programming to record which suffix remainders are achievable, and then chooses digits greedily from left to right.

**Precompute decimal place values modulo `k`.** `powers[e]` equals $10^e\bmod k$. It begins with one for exponent zero and repeatedly multiplies by ten modulo `k`. Using remainders prevents constructing enormous $n$-digit integers.

For half index `i` measured from the left, its mirrored index is `n - 1 - i`. In decimal notation, the left digit occupies exponent `n - 1 - i` and its right mirror occupies exponent `i`. Therefore choosing digit $d$ contributes

$$
d\left(10^{n-1-i}+10^i\right)\pmod k.
$$

The corresponding `weights[i]` stores the parenthesized value modulo $k$. At the center of an odd-length palindrome, the two positions are the same, so the code includes only one power rather than doubling it.

If the independent half digits are $d_i$, the complete palindrome remainder is

$$
\sum_i d_i\cdot\texttt{weights[i]}\pmod k.
$$

The task is now to find the lexicographically largest half with a nonzero first digit whose weighted sum is zero modulo $k$. Equal-length decimal strings compare by their first differing digit, so lexicographically largest is numerically largest.

**Suffix feasibility DP.** `reachable[i][r]` is true when positions `i` through the end of the half can contribute remainder `r`. After all positions, only remainder zero is possible, so `reachable[half_length][0] = 1`.

Processing positions backward, for every remainder achievable by the later suffix and every digit zero through nine, the code marks

`(digit * weight + suffix_remainder) % k`

as achievable from the current position. Each row is a `bytearray(k)`, using compact zero-or-one entries.

This DP allows digit zero even at position zero. That may mark leading-zero possibilities in `reachable[0]`, but greedy reconstruction separately restricts the first digit to one through nine. Only suffix table `reachable[index + 1]` is consulted after a proposed legal current digit, so illegal leading-zero numbers are never chosen.

**Greedy reconstruction with a proof of feasibility.** The method maintains `prefix_remainder` from already fixed positions. At each index it tries digits from nine downward. For index zero, `minimum_digit` is one; elsewhere it is zero.

After tentatively choosing `digit`, the prefix would have

`next_remainder = (prefix_remainder + digit * weight) % k`.

The unchosen suffix must contribute the additive inverse

`needed = (-next_remainder) % k`

so that prefix plus suffix is congruent to zero. If `reachable[index + 1][needed]` is true, at least one completion exists. The digit is appended, `prefix_remainder` is updated, and the algorithm advances.

Because digits are tested from largest to smallest, the first feasible one is the greatest digit compatible with some complete divisible palindrome. Fixing it cannot sacrifice a larger answer: any number with a smaller digit at the first differing position is numerically smaller regardless of later digits. Repeating this argument at every position yields the lexicographically and numerically largest feasible half.

For `n = 3` and `k = 5`, half length is two. The outer digit affects the hundreds and ones places, while the center affects the tens place. Divisibility by five forces the last digit, and therefore the first digit, to be zero or five. Leading zero is forbidden, so greedy chooses five. The center can then be nine, producing `"595"`.

For one digit and `k = 4`, the half has one center position. Feasibility rejects nine and accepts eight as the largest digit with remainder zero, returning `"8"`.

**Mirror the chosen half correctly.** `left` contains all independent digits. For even $n$, `n // 2` equals the entire half length, so all of `left` is reversed and appended. For odd $n$, the slice `left[: n // 2]` excludes the center before reversing. This prevents duplicating the middle digit.

The DP guarantees reconstruction will find a digit at every position for the problem's valid domain. The source has no explicit failure branch inside the digit loop; it relies on existence of an $n$-digit palindrome divisible by each allowed `k`.

**Why modulo state is sufficient.** Future divisibility depends on the already chosen digits only through their remainder modulo $k$. Two prefixes with the same remainder require exactly the same suffix remainder. This collapses an exponential digit search into $k$ states per half position.

## Complexity detail

Let $h=\lceil n/2\rceil$. Computing powers and weights takes $O(n)$ time. The feasibility DP processes $h$ positions, $k$ remainders, and ten digits, taking $O(10hk)=O(nk)$ time. Reconstruction tries at most ten digits at each half position, adding $O(n)$.

Since $k\le9$, $O(nk)$ is $O(n)$ under the problem constraints. The `reachable` table has $(h+1)k$ bytes plus row-object overhead, and powers, weights, and output-half storage are linear. Total auxiliary space is $O(nk)=O(n)$.

The algorithm never converts the final string to an integer and therefore handles $n$ up to $10^5$ without large-number division.

## Alternatives and edge cases

- **Try palindromes in descending order:** There are exponentially many half strings, so brute force is impossible even for moderate $n$.
- **Digit DP from the front without suffix feasibility:** Greedily choosing nine whenever the current remainder looks good can reach a dead end. The backward table proves a completion exists before committing.
- **Store predecessor choices during DP:** A conventional digit DP can reconstruct one solution from parent pointers. The suffix-feasibility table is especially convenient for lexicographically largest greedy reconstruction.
- **Build the huge integer and test divisibility:** Python cannot practically materialize and repeatedly test exponentially many $10^5$-digit candidates. Place weights keep all arithmetic below $k$.
- **Even length:** Every independent digit appears twice at symmetric powers, and the full half is mirrored.
- **Odd length:** The center weight contains only one power and the center is excluded from the reversed suffix.
- **`n = 1`:** Half length is one, the first digit is also the center, and leading-zero prevention still applies.
- **`k = 1`:** Every remainder is zero, so greedy chooses nine at every half position and returns all nines.
- **Leading zero:** Only the first greedy position raises `minimum_digit` to one. Zeros remain legal everywhere else.
- **Weight equal to zero modulo `k`:** That digit position does not affect divisibility, so greedy chooses nine because every suffix feasibility result is unchanged.
- **Multiple feasible completions:** The DP stores only existence. Descending digit selection chooses the largest prefix, and later positions repeat the same optimal rule.
- **Memory scaling:** Even though `k` is tiny, one row is stored per half position. Rolling rows would suffice only for feasibility computation; reconstruction needs later suffix rows unless decisions or parent information are stored another way.
- **Missing solution guarantee:** The reconstruction loop has no fallback if every digit fails. Correctness relies on the problem domain ensuring a valid result; a generalized implementation should detect and report impossibility.
