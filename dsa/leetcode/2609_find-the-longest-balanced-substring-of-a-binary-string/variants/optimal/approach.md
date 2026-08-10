## General

**Translate “balanced” into two exact tests**

A nonempty balanced substring must have the form

$$
0^q1^q
$$

for some positive integer $q$. In plain language, it contains one consecutive block of zeroes, followed by one consecutive block of ones, and the two block lengths are equal.

That definition has two independent requirements:

1. order: once a one has appeared, no later zero is allowed;
2. count: exactly half the characters must be ones, which then also means exactly half are zeroes.

The helper `check(i, j)` tests these requirements for the candidate substring from index $i$ through index $j$, inclusive.

**How the helper recognizes the required order**

The local variable `cnt` counts ones seen in the candidate. The loop visits every position from `i` to `j`.

- If the current character is `'1'`, it increments `cnt`.
- If the character is `'0'` and `cnt` is already positive, the helper immediately returns `False`.

That early return detects exactly the forbidden pattern: a zero occurring after at least one one. If no such position exists, all zeroes in the range precede all ones. The candidate may so far be all zeroes, all ones, or a correctly ordered zero-block followed by a one-block; the count test distinguishes these cases.

After the scan, the substring length is `j - i + 1`. The condition

`cnt * 2 == j - i + 1`

says that ones occupy exactly half of the positions. Because every other character is guaranteed to be zero, the number of zeroes is the same. Combining this equality with the ordering check proves that the candidate is balanced.

**Enumerate every possible nonempty candidate of useful length**

The outer loop chooses each starting index `i`. The inner loop chooses every ending index `j` strictly greater than `i`. Therefore, the solution checks every substring of length at least two.

A nonempty balanced substring cannot have length one: equal positive counts of zeroes and ones require an even length of at least two. Excluding `j == i` loses no valid nonempty answer.

For each candidate accepted by `check`, the solution updates `ans` with its length. The initial value is zero, which represents the empty balanced substring explicitly allowed by the contract. Thus no separate “not found” branch is needed.

**Why exhaustive checking is correct**

First, every length used to update `ans` belongs to an actually balanced substring, because the helper establishes both the ordering and equal-count requirements. The algorithm therefore never reports an invalid length.

Second, let $B$ be a longest nonempty balanced substring, with boundaries $(p,q)$. Its length is at least two, so the nested loops eventually choose `i = p` and `j = q`. The helper accepts it, and `ans` becomes at least $|B|$. No accepted substring can be longer than the longest one by definition, so the final answer equals $|B|$.

If no nonempty balanced substring exists, no update occurs and the initial zero correctly returns the empty substring's length. These two cases cover every input.

**Trace the mixed example**

For `s = "01000111"`, the range containing `"000111"` passes the helper:

- the first three positions are zeroes while `cnt` remains zero;
- the last three positions are ones, raising `cnt` to three;
- no zero occurs after that first one;
- `2 * cnt = 6` equals the candidate length.

The solution records six. A larger candidate such as the entire string fails because after the early one at index one, another zero appears. This illustrates why merely comparing total zero and one counts would not be sufficient.

For `s = "00111"`, substring `"0011"` is accepted with length four. The whole string has three ones and two zeroes, so it fails the final equality even though its ordering is correct.

For `s = "111"`, every examined range has only ones. It may pass the ordering scan, but `cnt` equals the full length rather than half the length, so every range fails and the result remains zero.

**The exact implementation versus the required bound**

The package's exact solution deliberately checks all boundaries and rescans each candidate. Its logic is straightforward and safe under the small limit $|s|\le50$, but it is not the linear run-tracking algorithm described by the manifest summary.

The linear observation is that every balanced substring lies across one `0`-run followed immediately by one `1`-run. If their lengths are $a$ and $b$, that boundary contributes `2 * min(a, b)`. A one-pass implementation can track these runs. That is the asymptotically optimal formulation, while this document explains the exact stored code rather than pretending it performs a scan it does not contain.

**Small implementation details that matter**

The helper closes over `s`, so only integer boundaries are passed. Its early return can save work on ranges containing a `10` transition, but worst-case ordered strings still require full scans.

The function does not construct substring copies. It works with indices and reads the original string, so its auxiliary storage stays constant even though it examines many ranges.

## Complexity detail

Let $n=|s|$. There are $\Theta(n^2)$ pairs $(i,j)$ with $i<j$. A call to `check(i, j)` can inspect $\Theta(n)$ characters in the worst case. The exact implementation consequently has $O(n^3)$ worst-case time.

The early return improves some concrete inputs but does not change that upper bound. For example, a string consisting of zeroes followed by ones makes many candidate scans reach their ends without encountering a forbidden zero.

The manifest records $O(n)$ time for the run-tracking method, but that bound does not describe this exact nested-loop solution. The local counter, loop indices, and answer use $O(1)$ auxiliary space. No substring array or prefix table is stored.

## Alternatives and edge cases

- **One-pass run tracking:** Count a zero-run and the immediately following one-run, then maximize `2 * min(zeroes, ones)`. This is the true $O(n)$ optimal method summarized by the manifest.
- **Regular-expression-shaped thinking:** Looking for blocks matching `0+1+` captures order, but run lengths must still be compared and a regex is unnecessary.
- **Equal counts alone:** A range such as `"0110"` has equal counts but is not balanced because a zero follows a one.
- **Correct order but unequal counts:** `"00111"` is not itself balanced, although its prefix `"0011"` is.
- **All zeroes:** No nonempty range contains equal positive counts, so the answer is zero.
- **All ones:** The final equality rejects every nonempty candidate, leaving zero.
- **Alternating characters:** Each `"01"` boundary can contribute length two, but a `"10"` transition prevents a larger balanced block across it.
- **Length one:** Only the empty substring is balanced, and `ans` remains zero.
- **Odd candidate length:** The equality `cnt * 2 == length` automatically rejects it.
- **No substring allocation:** Index-based checking avoids hidden $O(n)$ copies and keeps extra space constant.
