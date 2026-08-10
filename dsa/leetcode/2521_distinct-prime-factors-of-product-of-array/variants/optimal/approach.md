## General

**Factor the inputs without forming their product**

A prime divides the product of all array values if and only if it divides at least one individual value. Therefore, the set of distinct prime factors of the product is the union of the prime-factor sets of the elements.

The product itself may be enormous and is unnecessary. The method factors each number independently and inserts discovered primes into one shared set `s`.

Set insertion automatically removes duplication:

- repeated copies of a factor within one number count once;
- the same factor appearing in several array elements still counts once.

**Trial-divide the current residual**

For each array value, local `n` is a working residual and `i` begins at two.

While `i<=n//i`, the code checks whether `i` divides `n`. This condition is an overflow-safe version of $i^2\le n$.

When `n%i==0`:

1. `i` is inserted into the shared set;
2. every copy of `i` is divided out through the nested loop.

Removing all copies ensures future work considers only other prime factors and quickly shrinks the residual.

**Why a discovered divisor is prime**

Candidates are tested in increasing order. By the time `i` divides the residual, every smaller prime factor has already been completely removed.

If `i` were composite, it would have a smaller prime divisor, which would also divide the current residual. That smaller divisor should have been removed earlier, a contradiction. Thus every inserted trial divisor is prime.

The code increments through composite candidates too, but only actual divisors are added.

**Handle the final residual**

When trial division stops, any residual `n>1` must be prime. If it were composite, it would have some factor no greater than its square root, and the loop condition would still allow finding it.

The final `if n>1` inserts that residual into `s`.

For a prime input such as 997, no candidate divides it, trial division eventually stops, and 997 is inserted here.

**Trace a value with multiplicity**

For 40:

$$
40=2\cdot2\cdot2\cdot5.
$$

Candidate 2 is inserted once, then repeated division changes residual 40 to 20, 10, and 5. The square-root loop ends, and residual 5 is inserted.

The number contributes factor set $\{2,5\}$, regardless of 2's exponent three.

**Combine factors across the sample**

For `[2,4,3,7,10,6]`:

- 2 and 4 contribute 2;
- 3 contributes 3;
- 7 contributes 7;
- 10 contributes 2 and 5;
- 6 contributes 2 and 3.

The shared set becomes $\{2,3,5,7\}$ and its length is four.

**Why mutating local `n` is safe**

The `for n in nums` loop variable refers to the current integer value. Dividing and rebinding it does not modify the original list because Python integers are immutable and the list entry is never assigned.

Each next iteration receives its own original array value.


Every inserted value is a prime factor of some array element, so it divides the overall product.

Conversely, any prime factor of the product divides at least one array element. Trial division of that element either discovers it as a candidate divisor or leaves it as the final prime residual. It is therefore inserted.

The shared set equals exactly the desired distinct-prime set, and returning `len(s)` is correct.

**Avoiding overflow**

Even though each input is at most 1000, multiplying up to $10^4$ values would create an enormous integer. Factoring separately avoids that growth in any language.

**Why product exponents do not matter**

Multiplication adds prime exponents. If prime $p$ appears with exponent three in one number and exponent two in another, the product contains exponent five, but it is still only one distinct prime factor. The shared set deliberately records presence rather than accumulated exponent, matching the word “distinct.”

## Complexity detail

Let $N$ be the number of values and $M=\max(\texttt{nums})$. In the worst case, trial division checks $O(\sqrt M)$ candidates for one value, giving $O(N\sqrt M)$ time.

Successful repeated divisions add only $O(\log M)$ work per number and are covered by the looser square-root bound.

If $p$ distinct prime factors occur across all inputs, the set stores $p$ integers, so auxiliary space is $O(p)$. Under the input maximum 1000, $p$ is also bounded by the number of primes through 1000.

## Alternatives and edge cases

- **Smallest-prime-factor sieve:** Precompute factors through 1000 and factor each value faster when many inputs are processed.
- **Multiply first:** It preserves mathematical information but creates needless huge integers.
- **Prime input:** It is added as the final residual.
- **Prime power:** The prime is inserted once while all exponent copies are divided out.
- **Same prime across values:** Set insertion keeps it distinct.
- **Composite trial candidates:** They cannot divide after their smaller prime factors were removed.
- **Residual one:** Nothing remains to insert.
- **Overflow-safe loop guard:** `i<=n//i` avoids multiplying `i*i`.
- **Input list:** Local residual changes do not mutate it.
- **Distinct count:** Return set size, not the sum of factors or exponents.
