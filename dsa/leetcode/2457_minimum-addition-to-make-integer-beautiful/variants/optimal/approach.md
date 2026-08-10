## General

**Improve the digit sum by forcing carries**

The helper `f(x)` computes a decimal digit sum by repeatedly adding `x % 10` and removing the last digit with `x //= 10`. The outer loop stops as soon as `f(n+x) <= target`.

If the current number is not beautiful, small additions that do not create a useful carry cannot lower its digit sum enough. The algorithm repeatedly rounds the current value upward so that one more nonzero decimal position becomes zero. Carries replace a suffix by zeros and are the mechanism that can substantially reduce digit sum.

**Understand `y` and `p`**

At one iteration, `y = n+x` is the current candidate. The variable `p` begins at 10. While `y` ends in zero, the code removes that zero from `y` and multiplies `p` by 10.

If the current candidate has $z$ trailing zeros, after this loop:

- `y` is the candidate with those $z$ zeros removed;
- its last digit is nonzero;
- `p = 10^{z+1}`.

The update

`x = (y // 10 + 1) * p - n`

makes `n+x` the next multiple of `p`. It removes the current nonzero last digit of reduced `y` through a carry and leaves at least $z+1$ trailing zeros.

For 467, there are initially no trailing zeros, so `p=10` and the next candidate is 470. That is still not beautiful for target 6. Candidate 470 has one trailing zero; stripping it makes `y=47` and `p=100`, so the next candidate becomes 500. Its digit sum is 5.

**Why no smaller addition can work between roundings**

Let the current candidate have $z$ trailing zeros and nonzero digit $d$ immediately before them. The next rounding adds exactly $(10-d)10^z$, possibly continuing a carry farther left.

Any smaller positive addition cannot carry past digit $d$. It replaces some of the trailing zeros with a positive lower suffix while leaving the higher prefix and digit $d$ unchanged or insufficiently carried. Starting from zeros, that new suffix has positive digit sum, so the overall digit sum cannot be smaller than the current candidate's digit sum.

Since the current candidate is known not to be beautiful, no number before the next rounding boundary can be beautiful. Advancing directly to that boundary skips only impossible additions.

**Why the first beautiful candidate gives minimum `x`**

The candidate `n+x` increases strictly at every loop iteration and each update chooses the smallest number after the current candidate that can have a lower digit sum through a new carry. The preceding argument rules out every integer between consecutive candidates.

When the loop first finds digit sum at most `target`, all smaller additions were either previous non-beautiful candidates or numbers in skipped intervals whose digit sums could not improve over those candidates. Therefore the returned `x` is the minimum non-negative addition.

If `n` is already beautiful, the while condition is false initially and `x=0` is returned.

**Progress and termination**

Each iteration increases the number of trailing zeros by at least one. Eventually the candidate becomes a power-of-ten multiple with a small leading prefix. The input guarantee assures that some such value satisfies the target.

For `n=16` and target 6, the next multiple of 10 is 20, so `x=4` and digit sum 2 passes. No addition 1 through 3 creates the carry that zeros the 6 digit, so none can have a smaller digit sum than 16.

**The exact runtime differs from the manifest**

The manifest states $O(\log n)$ time. The source can perform $O(d)$ rounding iterations for a $d$-digit number, and each iteration recomputes `f(n+x)` by scanning $O(d)$ digits. The trailing-zero loop also rescans positions across iterations. A safe worst-case bound is $O(d^2)=O((\log n)^2)$.

An implementation maintaining digit sum incrementally could achieve the advertised linear-in-digits time, but this file deliberately recomputes it.

## Complexity detail

Let $d$ be the number of decimal positions processed, $O(\log n)$ with a possible extra carry digit. There are at most $O(d)$ rounding stages. Each digit-sum call takes $O(d)$ time, and the trailing-zero work is at most $O(d)$ per stage in the loose bound. Total worst-case time is $O(d^2)=O((\log n)^2)$.

Only integer scalars `x`, `y`, `p`, and the helper's accumulator are stored. Python integers grow with digit count, but no separate digit array or recursion is used. Under standard numeric-space conventions auxiliary space is $O(1)$; under bit complexity the integers occupy $O(\log n)$ bits.

## Alternatives and edge cases

- **Incremental decimal processing:** Walk digits from right to left, add the amount needed to round each position, and update the digit sum through carries. This can achieve $O(\log n)$ time.
- **Try every addition:** Increment `x` one by one until the digit sum qualifies. Numeric gaps can be enormous, making this infeasible.
- **Convert to a digit list:** Explicit digits can make carry logic clearer but uses $O(\log n)$ storage.
- **Already beautiful:** The method returns zero without rounding.
- **Trailing zeros:** They are skipped so the algorithm rounds the next nonzero digit rather than adding an unnecessary smaller place value.
- **Carry through nines:** The arithmetic formula naturally propagates the carry and may create additional zeros.
- **Target at least current digit sum:** Zero is the minimum allowed addition and is returned.
- **Large target:** Since digit sums of the bounded input are modest, many cases terminate immediately.
- **Strictly increasing candidates:** Every rounding moves to a larger multiple, ensuring progress.
- **Metadata mismatch:** Recomputing the full digit sum at each of up to $O(\log n)$ stages makes the exact worst-case time quadratic in digit count.
