## General

Let Alice's initial total be $A$ and Bob's initial total be $B$. Suppose Alice gives a box containing $a$ candies and receives Bob's box containing $b$ candies. Their totals afterward are

$$
A-a+b
$$

and

$$
B-b+a.
$$

For the exchange to be fair, these must be equal:

$$
A-a+b=B-b+a.
$$

Rearranging gives

$$
a-b=\frac{A-B}{2}.
$$

Define

$$
\text{diff}=\frac{A-B}{2}.
$$

Then for any chosen Alice box $a$, the only Bob box value that can balance the totals is

$$
b=a-\text{diff}.
$$

This equation removes the need to test every Alice/Bob pair.

**Compute the half-difference.** The solution uses

```text
diff = (sum(aliceSizes) - sum(bobSizes)) >> 1
```

Right-shifting an integer by one is division by two with floor behavior in Python. A valid answer is guaranteed, which implies $A-B=2(a-b)$ for some integer box sizes and is therefore even. Because the difference is even, the shift computes the exact half even when the difference is negative.

If Alice initially has more candies, `diff` is positive, so she must give a box larger than the one she receives. If Bob has more, `diff` is negative, and the formula correctly asks for a Bob box larger than Alice's.

**Use a set for Bob's box sizes.** `s = set(bobSizes)` supports expected $O(1)$ membership checks. For each Alice box value `a`, the solution computes `b = a - diff` and checks whether that value occurs among Bob's boxes. The first match is returned.

The walrus expression

```text
if (b := (a - diff)) in s:
```

both assigns the required value to `b` and performs the membership test. It does not remove a box from either input. The task requests only the two sizes, so locating one occurrence is enough even when values repeat.

**Why every returned pair is valid.** If the set contains the computed $b$, then $a-b=\text{diff}=(A-B)/2$. Reversing the algebra yields $A-a+b=B-b+a$, so totals after the exchange are equal. The returned sizes correspond to boxes each person actually owns.

**Why a valid answer will be found.** The contract guarantees at least one pair $(a^*,b^*)$ that balances totals. That pair satisfies $b^*=a^*-\text{diff}$. When the loop reaches Alice's occurrence of $a^*$, Bob's set contains $b^*$, so the membership test succeeds. Multiple valid pairs are allowed, and returning the first is acceptable.

For `aliceSizes = [1,1]` and `bobSizes = [2,2]`, totals are 2 and 4. The half-difference is $-1$. For Alice's box $a=1$, the required Bob size is $1-(-1)=2$, which exists. After swapping, each owns 3 candies.

It is useful to verify the totals directly from the difference equation. Because $a-b=(A-B)/2$, Alice's new total can be rewritten as

$$
A-a+b
=A-(a-b)
=A-\frac{A-B}{2}
=\frac{A+B}{2}.
$$

Bob's new total similarly becomes

$$
B-b+a
=B+(a-b)
=B+\frac{A-B}{2}
=\frac{A+B}{2}.
$$

Thus a matching pair does not merely make the two totals equal in an abstract equation; it gives each person exactly half of the combined candy total. This also explains why an odd difference would be impossible: it would imply an odd combined total, which cannot be divided into two equal integer candy amounts by exchanging whole boxes.

This method is optimal up to reading the inputs: both sums must account for all boxes, and building or querying a hash representation avoids the $pq$ comparisons of a nested search.

## Complexity detail

Let $p$ be the number of Alice's boxes and $q$ the number of Bob's boxes. Computing sums costs $O(p+q)$. Building Bob's set costs $O(q)$ expected time, and scanning Alice costs $O(p)$ expected time.

- **Time complexity:** $O(p+q)$ expected.
- **Space complexity:** $O(q)$ for Bob's distinct box sizes.

The returned list has constant size. If desired, the smaller side could be stored with adjusted algebra to reduce extra space to $O(\min(p,q))$.

## Alternatives and edge cases

- **Nested pair search:** Test every Alice box against every Bob box and compare resulting totals. This costs $O(pq)$ time.
- **Sort and use two pointers:** Sorting both arrays can find a difference-matching pair in $O(p\log p+q\log q)$ time and may mutate inputs.
- **Store Alice instead:** Rearrange the same equation for each Bob box. This is useful when Alice has fewer boxes; the algebraic sign must be handled consistently.
- **Odd total difference:** No integer box swap can solve the equation if $A-B$ is odd. The problem's guaranteed solution rules this case out.
- **Alice has more candy:** `diff > 0` and the selected Alice box must exceed the Bob box by `diff`.
- **Bob has more candy:** `diff < 0` and `b = a - diff` correctly becomes larger than `a`.
- **Duplicate sizes:** A set discards multiplicity, but only existence of one box with the required size matters.
- **Multiple answers:** Returning the first match in Alice's iteration order satisfies the contract.
- **Negative computed candidate:** Box sizes are positive, so a negative `b` will not be in the set and is harmlessly skipped.
- **Right shift:** It is exact here only because a solution guarantees an even difference. Explicit integer division by 2 would rely on the same fact.
- **Inputs are not mutated:** Sums, set construction, and iteration leave both box lists unchanged.
- **Return sizes, not indices:** The required answer contains candy counts from the exchanged boxes.
