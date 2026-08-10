## General

**Recognize the two-denomination Frobenius problem**

An item priced $x$ can be bought exactly when there are nonnegative integers $u$ and $v$ such that

$$
x=u\cdot\texttt{primeOne}+v\cdot\texttt{primeTwo}.
$$

For two coprime positive denominations $a$ and $b$, the largest positive integer that cannot be represented this way is the Frobenius number

$$
ab-a-b.
$$

The two inputs are distinct primes. Distinct primes share no positive divisor other than one, so they are coprime and the formula applies directly. The exact implementation returns `primeOne * primeTwo - primeOne - primeTwo`.

**Why coprimality is essential**

If denominations shared a divisor $g>1$, every payable amount would also be divisible by $g$. Infinitely many positive prices not divisible by $g$ would remain impossible, so there would be no single “most expensive” impossible item. The prime guarantee prevents this situation.

The denominations do not need to be ordered. The formula is symmetric in $a$ and $b$, so swapping the two parameters changes nothing.

**Prove that the returned amount cannot be formed**

Let $F=ab-a-b$. Suppose for contradiction that $F=ua+vb$ for nonnegative integers $u,v$.

Reduce both sides modulo $a$. Since $ab$ and $a$ are divisible by $a$,

$$
F\equiv -b\pmod a.
$$

The assumed representation gives $F\equiv vb\pmod a$. Therefore,

$$
vb\equiv -b\pmod a.
$$

Because $a$ and $b$ are coprime, $b$ has a multiplicative inverse modulo $a$. Cancelling it gives $v\equiv -1\pmod a$. The smallest nonnegative integer with that residue is $a-1$, so $v\ge a-1$.

But then

$$
vb\ge(a-1)b=ab-b=F+a>F.
$$

That is impossible if $ua+vb=F$ with $u\ge0$. Hence $F$ cannot be purchased.

**Prove that every greater amount can be formed**

Take any integer $x>F$. Consider the $a$ values

$$
x,\ x-b,\ x-2b,\ \ldots,\ x-(a-1)b.
$$

Their residues modulo $a$ are all distinct. If two had the same residue, their difference $(r-s)b$ would be divisible by $a$. Coprimality would force $r-s$ to be divisible by $a$, impossible for two different indices between zero and $a-1$. Since there are exactly $a$ residue classes, one of these values is divisible by $a$.

Thus, for some $k$ with $0\le k\le a-1$, `x - kb = qa` for an integer $q$. We must show $q$ is nonnegative. Using $x>ab-a-b$,

$$
x-(a-1)b>-a.
$$

The chosen `x-kb` is at least this lower bound, is divisible by $a$, and is strictly greater than $-a$. The only multiples of $a$ in that range are zero or positive, so $q\ge0$.

Therefore $x=qa+kb$ with both coefficients nonnegative. Every price greater than $F$ is purchasable, while $F$ is not, proving it is the greatest impossible price.

**Examples through the formula**

For denominations two and five, the answer is $10-2-5=3$. Prices one and three are impossible, while four, five, six, and every greater amount can be formed.

For five and seven, the formula gives $35-5-7=23$. The proof establishes both facts needed by the problem: 23 is impossible, and no larger impossible value exists. There is no need to enumerate all combinations up to the product bound.

**Why one arithmetic expression is enough**

The constraints already prove all prerequisites of the theorem. Running dynamic programming or searching coin combinations would rediscover a result known in closed form and introduce input-dependent work. The code’s constant-time expression is not a shortcut without justification; it is the theorem’s exact conclusion.

## Complexity detail

The method performs two multiplications/subtractions at fixed input size, so its running time is $O(1)$ under the standard word-arithmetic model. It stores no data structure, giving $O(1)$ auxiliary space.

Python integers prevent overflow in the product. Under the given bounds the product is below $10^5$ anyway, so even ordinary fixed-width integer types would be safe.

## Alternatives and edge cases

- **Coin-change dynamic programming:** Marking every reachable amount up to a safe threshold works under these small bounds but takes $O(ab)$ time and space instead of using the theorem.
- **Breadth-first search over residues:** Shortest representable amounts for residue classes can establish a cutoff, but it is unnecessary for exactly two coprime denominations.
- **Brute-force coefficient pairs:** Enumerating $u$ and $v$ can identify gaps but needs an additional proof that searching has gone far enough.
- **Non-coprime denominations:** The formula does not apply and no largest impossible amount exists because infinitely many prices are unreachable.
- **Equal primes:** They would not be coprime as a pair of denominations and are explicitly excluded by “distinct.”
- **Input order:** The expression is symmetric, so either prime may be larger.
- **Smallest primes two and three:** The formula returns one; every price at least two is payable.
- **Zero coins of one type:** Coefficients are nonnegative, so representations using only one denomination are naturally included.
- **No simulation state:** The returned number follows from the complete proof that it is impossible and all larger numbers are possible.
