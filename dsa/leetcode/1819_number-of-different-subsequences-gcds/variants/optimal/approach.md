## General

**Test each possible GCD value directly**

Every nonempty subsequence GCD is a positive integer no larger than the largest array value `mx`. The solution tests every candidate `x` from 1 through `mx`.

The crucial question is: how can we determine whether some subsequence has GCD exactly $x$ without enumerating subsequences?

**Only multiples of `x` can participate**

If a sequence has GCD $x$, every selected number must be divisible by $x$. Therefore all possible members of such a subsequence come from input values that are multiples of $x$.

The solution stores distinct input values in set `vis` and scans potential multiples:

`x, 2*x, 3*x, ...` up to `mx`.

Whenever a multiple is present, it is folded into running GCD `g`.

**Why the GCD of all present multiples is the decisive test**

Let $A_x$ be the set of input values divisible by $x$, and let

$$
g_x=\gcd(A_x).
$$

If $g_x=x$, selecting one occurrence of every distinct value in $A_x$ forms a valid subsequence whose GCD is exactly $x$. So $x$ is achievable.

If $g_x>x$, every value in $A_x$ is divisible by $g_x$. Any subsequence using only those values also has every member divisible by $g_x$, so its GCD cannot be the smaller value $x$. Values outside $A_x$ are not divisible by $x$ and cannot belong to a sequence with GCD $x$.

Thus $x$ appears as a subsequence GCD if and only if the GCD of all present multiples of $x$ equals $x$.

**Build the running GCD**

`g` starts at zero. The identity `gcd(0, y) = y` means the first present multiple initializes it naturally.

Each later present multiple can only keep or decrease the running GCD. Because every folded value is divisible by $x$, `g` always remains a multiple of $x$.

As soon as `g == x`, the candidate is proven achievable. Adding more multiples of $x$ cannot reduce the GCD below $x$: the GCD of $x$ with any multiple of $x$ is still $x$. The solution increments `ans` and breaks early.

If no multiples are present, `g` stays zero and the candidate is not counted.

**Why duplicates can be discarded**

Including the same value several times does not change a GCD:

$$
\gcd(a,a)=a.
$$

The question asks which different GCD values are possible, not how many subsequences produce them. Set `vis` therefore retains all necessary information while avoiding duplicate membership work.

**Following the first example**

For `nums = [6,10,3]`:

- candidate 10 sees present multiple 10 and reaches GCD 10;
- candidate 6 similarly reaches 6;
- candidate 3 sees 3 and 6, whose GCD is 3;
- candidate 2 sees 6 and 10, whose GCD is 2;
- candidate 1 folds 3, 6, and 10 and eventually reaches 1.

These are the five distinct achievable GCDs.

Candidate 4 has no present multiple and is rejected. Candidate 5 sees only 10, whose GCD is 10 rather than 5, so 5 is not achievable.

**Why arbitrary subsequence order does not matter**

GCD is associative and commutative. A chosen value set can appear as a subsequence by taking its occurrences in their original array order, and reordering the mathematical GCD computation does not change its result.

Therefore reasoning with a set of present values does not violate the subsequence requirement.

**Why the answer is correct**

For every candidate $x$, the multiples scan computes $g_x$. The equivalence proof shows that `g_x == x` is necessary and sufficient for an $x$-GCD subsequence.

The outer loop examines every possible positive GCD through the maximum input value and counts each candidate once. Hence `ans` is exactly the number of different subsequence GCDs.

## Complexity detail

Let $n$ be the input length and $M=\max(\texttt{nums})$. Building `vis` and finding $M$ take expected $O(n)$ time.

Candidate $x$ scans $\lfloor M/x\rfloor$ multiples. Across all candidates, the number of iterations is

$$
\sum_{x=1}^{M}\left\lfloor\frac{M}{x}\right\rfloor
=
O(M\log M).
$$

Under the usual word-RAM treatment of bounded integer GCD as constant or logarithmically small, total time is $O(n+M\log M)$ as recorded in the manifest. A bit-complexity analysis would additionally account for Euclidean-algorithm costs.

The set holds at most $M$ distinct positive values, so space is $O(M)$, matching the manifest. Exact set usage is $O(\min(n,M))$.

## Alternatives and edge cases

- **Enumerate all subsequences:** There are $2^n-1$ nonempty subsequences, which is impossible.
- **Maintain GCDs of subsequences ending at each index:** It can also compress repeated GCD values, but the multiples test exploits the bounded value domain directly.
- **Boolean presence array:** It replaces expected hash membership with deterministic indexing at $O(M)$ space.
- **Count duplicates separately:** It is unnecessary because multiplicity does not create new GCD values.
- **Candidate appears directly:** A singleton containing value $x$ immediately proves GCD $x$.
- **Candidate absent:** It may still be achievable, such as 2 from values 6 and 10.
- **No present multiple:** Running GCD remains zero and the candidate is rejected.
- **Only one present multiple:** The candidate works only if that value equals $x$.
- **Early GCD equality:** Once `g == x`, later multiples cannot change it away from $x$.
- **Value one present:** Singleton one proves GCD one immediately.
- **GCD one without value one:** Several larger values may still reduce the running GCD to one.
- **All values equal:** Only that value is achievable as a subsequence GCD.
- **Subsequence order:** Original order never changes the GCD of chosen occurrences.
- **Positive inputs:** Candidate zero is irrelevant and never tested.
- **Maximum bound:** No subsequence GCD can exceed the largest selected value, so testing through $M$ is exhaustive.
