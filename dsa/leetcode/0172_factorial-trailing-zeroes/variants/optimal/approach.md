## General
A decimal trailing zero is a factor of ten, and $10 = 2 \cdot 5$. In a factorial, factors of two are far more common than factors of five, so every available five can be paired with a two. The answer is therefore the exponent of five in the prime factorization of $n!$.

Counting only multiples of five is not enough: `25` contributes two factors of five, `125` contributes three, and so forth. Count the contributions in layers:

$\operatorname{floor}(n / 5) + \operatorname{floor}(n / 25) + \operatorname{floor}(n / 125) + \ldots$

The first term counts every number supplying at least one five. The second counts the extra five supplied by multiples of $5^{2}$; the third counts another extra five from multiples of $5^{3}$. Stop when the quotient is zero. Repeatedly dividing a working copy of `n` by five and adding each quotient avoids explicit powers and multiplication overflow.

For $n = 25$, $\left\lfloor 25 / 5 \right\rfloor = 5$ counts `5, 10, 15, 20, 25`, while $\left\lfloor 25 / 25 \right\rfloor = 1$ counts the second factor inside `25`. The total is six trailing zeroes.

If an integer is divisible by $5^r$, it contributes one factor of five to each of the first $r$ quotient terms and none thereafter. Thus the quotient sum includes every factor of five in every integer from $1$ through $n$ exactly once per multiplicity. Because $n!$ contains at least as many factors of two, each counted five forms one factor of ten. The sum is therefore exactly the number of trailing zeroes in $n!$.

## Complexity detail
Each iteration divides the working value by five, so there are $O(\log_{5} n)$, equivalently $O(\log n)$, iterations. The accumulator and quotient use $O(1)$ auxiliary space.

## Alternatives and edge cases
- Constructing $n!$ creates an enormous integer merely to inspect its decimal suffix and is much more expensive.
- Testing every integer's divisibility by five avoids the factorial but still takes $O(n)$ iterations.
- Counting only $\lfloor n/5 \rfloor$ misses additional factors contributed by multiples of $25$, $125$, and higher powers.
- $0! = 1$, and every $n < 5$ returns zero.
- At powers of five, the answer jumps by more than one because the boundary value contributes several factors.
