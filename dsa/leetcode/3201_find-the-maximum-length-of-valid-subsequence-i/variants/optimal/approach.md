## General

**Discard magnitude and keep parity.** The validity condition compares adjacent sums modulo two. For any two integers, the remainder of their sum depends only on whether each integer is even or odd. Replacing every value by `value % 2` therefore preserves everything relevant while reducing the possible values to $0$ and $1$.

If every adjacent pair in a subsequence has the same sum parity, its element parities must follow one of four patterns:

- $0,0,0,\ldots$: all selected values are even, and every adjacent sum is even;
- $1,1,1,\ldots$: all are odd, and every adjacent sum is even;
- $0,1,0,1,\ldots$: parity alternates, and every adjacent sum is odd;
- $1,0,1,0,\ldots$: the opposite alternating start, again with odd adjacent sums.

The exact solution captures these possibilities with a $2\times2$ dynamic-programming table instead of four separate scans.

**Interpret the ordered-pair state.** `f[a][b]` represents the longest valid subsequence seen so far whose last selected parity is $a$ and whose alternating partner parity is $b$. Equivalently, its last two conceptual parity roles are $b,a$, and appending another $b$ would continue the same adjacent-sum pattern. The reverse state `f[b][a]` is exactly what can be extended by a new value of parity $a$.

The table begins with zeros. A first selected element can seed a length-one subsequence for any future partner parity; a one-element subsequence has no adjacent-pair condition to violate. This is why adding one to a zero reverse state is legitimate even when no actual preceding element of the partner parity exists.

**Follow the source's `j` and `y` variables.** For the current remainder `x`, the inner loop considers both possible target adjacent-sum remainders `j = 0` and `j = 1`. If the preceding selected parity is `y`, it must satisfy

$$
(x+y)\bmod2=j.
$$

Solving for `y` gives

`y = (j - x + 2) % 2`.

As `j` takes both values, `y` also takes both parities exactly once. The transition

`f[x][y] = f[y][x] + 1`

appends the current $x$ to the longest earlier subsequence whose last parity is $y$ and whose partner is $x$. Its previous last adjacent pair, when present, sums to $x+y$ modulo two; the new pair $y,x$ has the same sum. Validity is preserved.

**Why assignment rather than maximum is safe.** Normally a subsequence DP transition is written with `max` to avoid overwriting a better state. Here the reverse state `f[y][x]` represents the best compatible subsequence before this occurrence. Appending the current element always makes a subsequence one longer than that best reverse state, and processing later occurrences can only maintain or improve such lengths.

When $x\ne y$, the current iteration writes row `x` but reads row `y`, so it does not accidentally reuse the same current element. When $x=y$, the transition is `f[x][x] = f[x][x] + 1`. That is correct: another value with the same parity can extend the all-same-parity subsequence by one.

**Why every computed subsequence is valid.** The base length-one sequences are valid vacuously. Assume `f[y][x]` describes a valid sequence whose adjacent sums all have remainder $(x+y)\bmod2$. Appending current parity $x$ creates the pair $(y,x)$ with exactly that same sum remainder. All older pairs remain unchanged. By induction, every table value corresponds to a valid subsequence in original index order.

**Why the longest valid subsequence is represented.** Take any valid subsequence and look only at its parities. Its adjacent sum remainder is fixed. If its current final two parity roles are $y,x$, deleting the final $x$ leaves a valid subsequence represented by the reverse state `f[y][x]` at the time before that element is scanned. The transition can append the element and recover its length. Repeating this reasoning from the first element shows the DP can build every valid parity pattern. Since `ans` records the largest table value ever formed, it equals the requested maximum.

For `nums = [1,2,3,4]`, parities are `[1,0,1,0]`. The states with partner parities $1$ and $0$ alternately extend each other, reaching length four. Every adjacent selected sum is odd, so the entire array is valid.

For `[1,3]`, both parities are one. The self-state `f[1][1]` increments from zero to one for the first element and then to two for the second. Their sum is even, so length two is valid.

## Complexity detail

The constant `k` is fixed to two. Creating the $2\times2$ table takes constant time and space. For each of $n$ values, the inner loop performs exactly two transitions, each with constant arithmetic and table access. Total time is $O(n)$.

The table always contains four integers, and `ans` plus loop variables use constant storage, so auxiliary space is $O(1)$. The method reads but does not mutate `nums`; assigning `x %= k` changes only the local integer variable.

The result is at most $n$, so its numeric size is straightforward. The $O(n)$ scan is worst-case optimal because an unexamined final value can extend the best subsequence.

## Alternatives and edge cases

- **Enumerate four parity patterns:** For each of even-only, odd-only, even-odd alternating, and odd-even alternating, greedily scan for the next required parity. This is the editorial formulation and remains $O(n)$ time and $O(1)$ space.
- **Count evens and odds plus alternating run:** The same-parity answers are the total even and total odd counts. A greedy alternating subsequence can be measured by parity changes, with both start choices considered.
- **Quadratic subsequence DP:** Compare every pair of indices and extend compatible subsequences. It is unnecessary because modulo two leaves only four ordered states.
- **All values even:** `f[0][0]` grows once per element, so the whole array is selected.
- **All values odd:** `f[1][1]` behaves symmetrically.
- **Strictly alternating parity:** The entire input is valid with common adjacent-sum remainder one.
- **Long repeated blocks:** An alternating solution can take at most one useful element before each parity transition, while a same-parity solution may select every element of one parity; the DP compares both automatically.
- **Length-two subsequence:** Any two elements are valid because there is only one adjacent sum and therefore nothing unequal to compare.
- **Subsequence order:** Table updates occur in input order, so elements are never rearranged even though their full values are discarded.
- **Large values:** Modulo reduction makes values up to $10^7$ no harder than small ones.
- **Self-state update:** `f[x][x]` deliberately reads and increments itself, representing selection of another same-parity value rather than illegal reuse of the current index.
- **Input preservation:** Only local `x` is replaced by its remainder; the array remains unchanged.
