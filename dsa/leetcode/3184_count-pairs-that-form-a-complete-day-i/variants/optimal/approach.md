## General

**Only remainders modulo 24 matter**

A sum is a multiple of 24 exactly when

$$
(a\bmod24+b\bmod24)\bmod24=0.
$$

For current remainder $r=x\bmod24$, the required partner remainder is

$$
(24-r)\bmod24.
$$

The second modulo handles $r=0$: its complement should be 0, not 24, because remainder classes range 0 through 23.

**Count earlier complements**

`cnt` stores frequencies of remainders among values already scanned.

For current `x`, the source first adds

`cnt[(24 - (x % 24)) % 24]`

to `ans`. Each such earlier value forms a valid pair with current index as the right endpoint.

Then it increments `cnt[x % 24]` so current value is available only to later indices.

This order enforces $i<j$ and prevents pairing an element with itself.

**Example**

For `[12,12,30,24,24]`:

- first 12 finds no earlier 12, then records one;
- second 12 finds one complement and adds pair $(0,1)$;
- 30 has remainder 6 and needs 18, absent;
- first 24 has remainder 0, finds none, then records;
- second 24 finds one remainder-0 partner and adds pair $(3,4)$.

Answer is 2.

For 72, 48, and 24, all remainders are zero. Their successive contributions are 0, 1, and 2, totaling $\binom32=3$.

**Why values themselves can be discarded**

If two durations have equal remainder, they behave identically with every possible partner regarding divisibility by 24. Quotient numbers of complete days add multiples of 24 and do not affect the condition.

Thus 24, 48, and 72 all belong to remainder class zero.


When processing index $j$, `cnt[c]` equals number of earlier indices $i<j$ with remainder $c$. The complement expression selects exactly those satisfying $(hours[i]+hours[j])\bmod24=0$.

Every valid pair is counted once when its right endpoint is processed. No invalid pair is counted because only complementary classes contribute. Updating afterward preserves the invariant.

**Fixed-domain space**

Although `Counter` is dynamic, it can contain at most 24 remainder keys. Space is constant with respect to input length.

The solution is more efficient than the brute-force approach suggested by the small “I” constraint, and it is identical to the scalable “II” source.

**Algebra behind the complement**

Write hours as $24q+r$. For two values,

$$
(24q_1+r_1)+(24q_2+r_2)=24(q_1+q_2)+(r_1+r_2).
$$

The whole sum is divisible by 24 precisely when remainder sum is 0, 24, or—in the bounded range 0 through 46—equivalently zero modulo 24. This yields $r_2=(24-r_1)\bmod24$.

**Why Counter lookup does not insert useful phantom pairs**

A missing complement returns zero, so no pair is added. The code then increments only current remainder. Future values may use it, but the current value cannot pair backward with a class that had no actual earlier member.

**Alternative frequency formula**

After counting all remainders, distinct complementary classes $r$ and $24-r$ contribute `count[r] * count[24-r]`. Self-complementary classes 0 and 12 contribute $\binom{count}{2}$. One must process only one side of each distinct pair or divide duplicated totals. The streaming method avoids those special bookkeeping rules.

**Index multiplicity**

If three different indices all contain 24, they create three pairs even though the values are equal. Frequencies preserve this: their arrivals add 0, then 1, then 2. Converting input to a set would incorrectly reduce them to one value and zero pairs.

**Why the answer cannot be derived from total sum**

Pair validity is local to two remainders. The sum of all hours loses how remainders are distributed and cannot determine how many index pairs complement each other.

**Boundary examples**

Remainders 1 and 23 pair; 1 and 24 do not because their remainder sum is 1. Remainders 12 and 12 pair. Remainders 0 and 0 pair, including two different durations such as 24 and 72.

These examples cover the ordinary distinct-complement and both self-complement cases that often cause off-by-one errors.

## Complexity detail

Let $n$ be number of durations.

The loop performs expected constant-time counter operations per value, so time is $O(n)$.

At most 24 remainder counts are stored, giving $O(1)$ auxiliary space. The answer scalar is constant space.

Python integers safely hold up to $\binom n2$ pairs.

Input is not modified.

## Alternatives and edge cases

- **Check every pair:** $O(n^2)$ is feasible for length 100 but unnecessary.
- **Fixed array of 24 counts:** Avoids hash overhead and makes constant space explicit.
- **Count classes after one pass:** Combine $cnt[r]cnt[24-r]$ and use combinations for 0 and 12; correct but needs careful double-counting.
- **Remainder zero:** Complements itself.
- **Remainder twelve:** Also complements itself because $12+12=24$.
- **Other remainder:** Complements a distinct class $24-r$.
- **Single element:** No earlier partner, answer zero.
- **Repeated durations:** Each index creates distinct pairs through frequency counts.
- **Large hours:** Modulo reduces them immediately.
- **Update order:** Querying before increment prevents self-pairing.
- **i less than j:** Streaming order enforces it automatically.
- **Exact multiple:** Any positive multiple of 24 qualifies, not only 24.
