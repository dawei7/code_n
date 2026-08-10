## General

**Rewrite the product equality as a ratio equality.** A valid quadruple uses indices $p<q<r<s$, leaves at least one unused index between every adjacent selected pair, and satisfies

$$
\texttt{nums}[p]\texttt{nums}[r]
=
\texttt{nums}[q]\texttt{nums}[s].
$$

Write $a=\texttt{nums}[p]$, $b=\texttt{nums}[q]$, $c=\texttt{nums}[r]$, and $d=\texttt{nums}[s]$. Because every value is positive, the equation can be rearranged without division-by-zero concerns:

$$
\frac{a}{b}=\frac{d}{c}.
$$

This turns a four-index search into matching a left pair $(p,q)$ with a right pair $(r,s)$. Fractions must be stored canonically: $2/4$ and $1/2$ represent the same ratio even though their raw numerator-denominator pairs differ. Dividing both parts by their greatest common divisor gives a unique reduced key.

For a left pair, the source computes

`(a // gcd(a, b), b // gcd(a, b))`.

For a right pair it computes

`(d // gcd(c, d), c // gcd(c, d))`.

The reversed order on the right is deliberate. Matching these keys expresses $a/b=d/c$, which is exactly the original cross-product condition. Storing $c/d$ instead would count the wrong relationship.

**Fix the second index and maintain all eligible right pairs.** The main sweep treats `q` as the current second index. Its loop is `range(2, n - 4)`, so $q$ runs from $2$ through $n-5$. These are precisely the values that can leave room for $p\le q-2$, $r\ge q+2$, and $s\ge r+2$.

Before that sweep starts, `cnt` is filled with every right pair satisfying $r\ge4$ and $s\ge r+2$. This is exactly the set eligible when the first possible $q$ is $2$, because the required gap says $r-q>1$, hence $r\ge4$. Each dictionary value records how many index pairs—not merely how many distinct value pairs—have that reduced ratio. Multiplicity matters because two equal-valued pairs at different indices create different subsequences.

For a fixed $q$, `for p in range(q - 1)` visits $p=0,\ldots,q-2$, enforcing $q-p>1$. The solution reduces $a/b$, looks up the same key in `cnt`, and adds the stored count to `ans`. Every matching right pair already satisfies both remaining gaps, so every unit added corresponds to one legal quadruple.

**Update the dictionary for the next value of \(q\).** After counting all quadruples whose second index is the current $q$, the sweep will advance to $q+1$. A right pair with $r=q+2$ is valid now because $r-q=2$, but it is invalid next time because $r-(q+1)=1$. The source therefore sets `c = nums[q + 2]` and decrements every pair $(r,s)=(q+2,s)$ with $s\ge q+4$.

No other right pair changes eligibility. Pairs with a larger $r$ remain far enough from the next $q$, while pairs with a smaller $r$ were removed on earlier iterations. Thus, immediately before each counting phase, `cnt` has a useful invariant: it contains exactly all pairs $(r,s)$ such that $r\ge q+2$ and $s\ge r+2$, grouped by the reduced value $d/c$.

For the first example, the valid quadruple $(0,2,4,6)$ has left values $(a,b)=(1,3)$ and right values $(c,d)=(3,1)$. Both become the key $(1,3)$. When $q=2$, the dictionary contains $(r,s)=(4,6)$, so the lookup contributes one.

**Why every answer is counted exactly once.** Any contribution uses a left pair visited by the current `q` loop and a right pair currently represented in `cnt`. The loop bounds and dictionary invariant establish all three spacing rules, and equal normalized keys establish the product equation. Therefore, nothing invalid is added.

Conversely, take any valid special subsequence $(p,q,r,s)$. During the unique iteration for its second index $q$, the left loop visits $p$. Since $r\ge q+2$, the pair $(r,s)$ has not yet been removed, and since $s\ge r+2$, it was inserted initially. Its key matches the left key because the product equality holds. The quadruple is therefore counted. It cannot be counted under another iteration because its second index is fixed, and the dictionary count distinguishes each right index pair. This proves both completeness and absence of double counting.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$, and let $V$ be the largest value in `nums`.

The initialization examines

$$
\sum_{r=4}^{n-3} O(n-r)=O(n^2)
$$

right pairs. Across the main sweep, the left-pair loops examine $O(n^2)$ pairs in total, and the removal loops also process $O(n^2)$ pairs in total. Each visit performs a greatest-common-divisor computation on values at most $V$, costing $O(\log V)$, plus expected $O(1)$ dictionary access. The total expected time is therefore $O(n^2\log V)$, matching the manifest.

In the most general analysis, the dictionary can contain $O(n^2)$ distinct reduced ratio keys, so its space is $O(n^2)$. Under this problem's explicit bound $V\le1000$, the number of possible reduced positive numerator-denominator pairs is also bounded by $O(V^2)$; a tighter combined statement is $O(\min(n^2,V^2))$ keys. The answer and loop variables use constant additional space. Dictionary operations are expected constant time; adversarial hash-collision behavior is not the normal complexity model for Python dictionaries.

## Alternatives and edge cases

- **Four nested loops:** Directly selecting $p,q,r,s$ and testing the equation is conceptually simple but takes $O(n^4)$ time, which is unusable for $n=1000$.
- **Enumerate two pairs for every \(q\):** Rebuilding all right-pair counts from scratch for each second index costs $O(n^3)$. Incremental removal is what reduces the work to quadratic.
- **Store raw products:** A map keyed by a product can help in some formulations, but here the equality pairs one value from each side. Reduced ratios provide a clean pair-matching key while avoiding floating-point arithmetic.
- **Floating-point ratios:** Using `a / b` as a floating-point key risks precision-based mismatches. GCD reduction represents equal rational values exactly.
- **Right-key orientation:** The required comparison is $a/b=d/c$. Keying the right pair as $(c/g,d/g)$ silently checks $a/b=c/d$ and is incorrect.
- **Repeated values and ratios:** The dictionary stores counts rather than a Boolean. Many different $(r,s)$ pairs can share one ratio, and every one produces a distinct index subsequence.
- **Minimum length:** At $n=7$, the only possible spaced quadruple is $(0,2,4,6)$. The loop ranges still initialize, test, and then finish correctly.
- **Strict spacing:** The boundaries `q - 2`, `q + 2`, and `r + 2` are not optional optimizations. Allowing adjacent selected indices would count sequences forbidden by the statement.
- **Positive inputs:** GCD normalization relies on the stated positive values. There is no need to define a ratio involving zero or normalize signs.
- **Large answer:** The problem asks for an ordinary count, not a modular result. Python integers grow automatically, so `ans` does not overflow even when many quadruples are valid.
