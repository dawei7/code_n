## General

**Normalize every duration into one of 24 classes**

Whether two hours form a complete day depends only on their sum modulo 24. Write $r=x\bmod24$. A prior value must have remainder

$$
c=(-r)\bmod24=(24-r)\bmod24.
$$

The nested modulo is necessary for remainder zero, whose complement is class zero.

**Streaming pair count**

`cnt` records remainder frequencies among earlier array positions.

For each current `x`:

1. compute its complement class;
2. add the number of earlier values in that class to `ans`;
3. record current remainder for future positions.

If there are $p$ earlier complementary values, current index forms exactly $p$ new index pairs. The algorithm adds all of them at once.

**Why each pair appears once**

For valid pair $(i,j)$ with $i<j$, index $i$ is already in the counter when $j$ is processed, so the pair is added. It could not have been counted at $i$ because $j$ was not recorded yet, and it is never revisited afterward.

Invalid remainders never satisfy the complement lookup and contribute zero.

**Self-complementary classes**

Remainder 0 pairs with 0, representing durations already divisible by 24.

Remainder 12 pairs with 12 because two half-day remainders sum to 24.

The streaming method needs no special branches for these cases: querying before increment ensures a class element pairs only with earlier copies.

For $t$ values in one self-complementary class, contributions become $0+1+\cdots+(t-1)=\binom t2$.

**Example**

For `[12,12,30,24,24]`, the second 12 adds one and the second remainder-zero value adds one. Remainder 6 from 30 has no remainder-18 partner. Total is 2.

For `[72,48,24,3]`, first three values all have remainder zero and generate three unordered index pairs. Remainder 3 needs 21, absent.


Before index $j$, `cnt[r]` equals the number of $i<j$ with `hours[i] % 24 == r`, and `ans` equals valid pairs entirely before $j$.

Complement lookup adds exactly all valid pairs ending at $j$. Incrementing current remainder establishes the invariant for next index. Induction proves final answer exact.

**Relation to ID 3184**

The exact implementations are identical. ID 3185 raises length to $5\cdot10^5$, making the linear method necessary rather than merely convenient.

The fixed modulus is what keeps counter space constant even at this larger scale.

**Algebraic derivation**

Write each duration as $24q+r$. Complete-day quotients $q$ already contribute multiples of 24, so only $r$ affects divisibility. Since two remainders lie between 0 and 23, their sum is divisible by 24 only when it is 0 or 24. The complement expression captures both in one modular formula.

**Why streaming scales**

At $5\cdot10^5$ values, there can be roughly $1.25\cdot10^{11}$ index pairs. Enumerating them is impossible, but all earlier partners of one remainder are interchangeable for the current test. One counter lookup adds their entire group contribution.

The algorithm's work does not increase when the answer is huge; it depends only on number of input values.

**Post-count comparison**

A two-pass frequency method would compute:

- $\binom{c_0}{2}$ for remainder 0;
- $\binom{c_{12}}{2}$ for remainder 12;
- $c_r c_{24-r}$ for $r=1$ through 11.

That formula proves the same count. The one-pass source distributes each product over arrivals and avoids separate combination arithmetic.

**No double counting with complementary classes**

When a remainder-5 value arrives, it pairs with earlier remainder 19 values. Later, a new 19 pairs with all earlier 5s, but not with the already-counted orientation involving the earlier 19 and current 5: those are different right endpoints only when they are different index pairs. Each unordered index pair has exactly one later endpoint.

**Practical fixed array**

A 24-entry list could replace `Counter` and would have lower overhead for half a million iterations. The source remains asymptotically constant-space because even the dynamic counter can never exceed 24 keys.

**Input order does not change total**

Streaming contributions may occur at different steps after reordering, but every valid pair still has one later endpoint, so final total is invariant under permutation of `hours`.

## Complexity detail

For $n$ values, one pass with expected constant-time counter accesses takes $O(n)$ time.

Only 24 possible keys exist, so auxiliary space is $O(1)$. The counter's implementation is dynamic, but its domain is fixed.

The pair count can approach $n(n-1)/2$, which fits Python's arbitrary-precision integer.

Input array remains unchanged.

This is asymptotically optimal because every element can affect the answer and must be read.

## Alternatives and edge cases

- **24-entry list:** Faster deterministic indexing and explicitly fixed space.
- **Post-count frequency formula:** Pair complementary distinct classes once and use combinations for 0 and 12; easy to double-count without care.
- **Nested pair loops:** $O(n^2)$ is infeasible for the II constraints.
- **Remainder zero:** Pairs with earlier zero remainders.
- **Remainder twelve:** Pairs with earlier twelves.
- **Complement formula:** Outer modulo maps computed 24 back to class zero.
- **Large durations:** Quotient complete days do not matter.
- **One value:** No pair can form.
- **All values same non-self-complementary remainder:** Answer is zero unless remainder is 0 or 12.
- **All multiples of 24:** Answer is $\binom n2$.
- **Streaming order:** Naturally enforces $i<j$.
- **No input mutation:** Only remainders are stored in the counter.
