## General

**Greedily cancel bracket pairs**

Scan from left to right while `x` counts opening brackets that have not yet been matched.

When the current character is `"["`, increment `x`. When it is `"]"` and `x` is positive, match it with one earlier opening bracket and decrement `x`. When it is `"]"` and `x` is zero, it cannot be matched with anything to its left, so the code leaves `x` unchanged.

This is equivalent to removing every balanced `[]` relationship possible while preserving order, but it needs only one counter rather than a stack.

After the scan, `x` is the number of unmatched opening brackets. Because the original string contains equal numbers of opening and closing brackets, the number of earlier unmatched closing brackets is also `x`.

**Understand the unmatched residual shape**

Once all possible ordered matches are removed, unmatched closing brackets conceptually appear before unmatched opening brackets:

`]]]...[[[`.

If an unmatched opening had appeared before an unmatched closing, the greedy scan would have paired them. The task is therefore to repair two equal groups of size `x` using arbitrary-index swaps.

**How one swap repairs up to two unmatched pairs**

Swap an early unmatched closing bracket with a suitably late unmatched opening bracket. Placing an opening near the front fixes a prefix deficit, while placing the closing near the back supplies a closing endpoint. In the residual arrangement, one swap can reduce the unmatched count `x` by two in the typical case.

Therefore the number of swaps is the ceiling of $x/2$:

$$
\left\lceil\frac x2\right\rceil
=\left\lfloor\frac{x+1}{2}\right\rfloor.
$$

The source writes this as `(x + 1) >> 1`. For nonnegative integers, right shift by one is floor division by two.

If `x` is even, every swap repairs two units. If it is odd, the final swap repairs the remaining one unit along with bracket structure already repositioned, giving the ceiling.

**Trace the examples**

For `"][]["`, the first closing is unmatched. The middle `"[]"` pair cancels, and the final opening leaves `x=1`. The formula returns one swap.

For `"]]][[["`, the three initial closings are ignored by the counter and the three final openings make `x=3`. The formula returns $(3+1)//2=2$, matching the required operations.

For an already balanced string, every closing finds an available opening, so `x` ends at zero and the result is zero.

**Why the count is minimum**

The unmatched structure has `x` misplaced openings and `x` misplaced closings. One swap exchanges only two positions and can reduce the relevant unmatched-opening measure by at most two, so at least $\lceil x/2\rceil$ swaps are required.

Choosing swaps between appropriately separated unmatched endpoints attains that number, as described above. The formula therefore meets both a lower bound and a construction.

The method does not need to produce the final balanced string, only the count.

**Connection to prefix balance**

Assign value $+1$ to `"["` and $-1$ to `"]"`. A balanced bracket string has nonnegative balance at every prefix and final balance zero. Whenever the raw prefix balance would go negative, the counter scan sees a closing bracket with `x=0` and leaves it unmatched.

The total number of such unmatched closings equals the number of openings left in `x` at the end. Greedy matching removes every pair that is already in the correct relative order, so `x` precisely measures the residual imbalance that arbitrary swaps must repair.

For `"[]]][["`, the scan matches the initial `"[]"`, ignores the next two unmatched closings, and finishes with two unmatched openings. One swap can exchange the first problematic closing with the final opening, yielding `"[][][]"`. The formula returns $\lceil2/2\rceil=1$.

**Why distant swapping changes two prefix deficits at once**

Swapping an early closing with a later opening raises the balance by two throughout the interval between those positions: the early character changes from $-1$ to $+1$, while the later compensating change occurs only at the interval's end. This can repair two levels of negative prefix depth in one operation. Repeating on the deepest remaining deficit gives the ceiling-half construction.

## Complexity detail

Let $N$ be the string length.

The loop visits each bracket once and performs constant-time counter operations. Total time is $O(N)$.

Only `x` and the current character are stored, so auxiliary space is $O(1)$. The input string is not copied or modified.

The counter may grow to $N/2$, but its numeric storage is constant-sized under the usual word-RAM model for the given constraints.

## Alternatives and edge cases

- **Explicit stack:** Push unmatched openings and pop on closings. It derives the same `x` but uses $O(N)$ space.
- **Track minimum prefix balance:** Treat `"["` as plus one and `"]"` as minus one; the deepest negative deficit leads to an equivalent ceiling formula.
- **Greedy matching interpretation:** Ignoring a closing only when no opening is available isolates exactly the brackets whose order must be repaired.
- **Simulate swaps:** Finding actual indices and rebuilding the string is unnecessary when only the minimum count is requested.
- **Already balanced:** No unmatched openings remain and the answer is zero.
- **Single pair `"[]"`:** The counter rises then falls to zero.
- **Reversed pair `"]["`:** One unmatched opening remains after cancellation, requiring one swap.
- **All closings then openings:** This maximizes imbalance and illustrates the ceiling formula.
- **Odd `x`:** Adding one before shifting implements ceiling rather than floor.
- **Even `x`:** Every swap can repair two units, so the result is exactly `x // 2`.
- **Equal bracket totals:** The proof relies on unmatched opening and closing counts being equal, guaranteed by the contract.
- **Arbitrary-index swaps:** One operation may exchange distant brackets; an adjacent-swap problem would require a different cost analysis.
- **Final balance:** Equal total bracket counts guarantee the completed string can reach balance zero after prefix deficits are fixed.
- **No mutation:** The scan calculates the count without changing `s`.
