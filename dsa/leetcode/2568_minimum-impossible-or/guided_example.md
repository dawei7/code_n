# Guided Example: Minimum Impossible OR

## 1. Expressibility is reachability under bitwise OR

An integer $x$ is *expressible* when some selection of positions $i_1 < i_2 < \dots < i_k$ satisfies `nums[i_1] | ... | nums[i_k] = x`. Empty selections are allowed by the definition and produce $0$, which is why the task asks for the smallest **positive** value that no selection can reach.

The OR operation has one property that controls everything: it is **monotone in the set of contributing bits**. Adding another element to a selection can only turn more bits on, never off. There is no cancellation, no borrowing, and no way to remove a bit that a chosen element brings along.

For the instance we trace, `nums = [2,1]`, the whole reachable set is small enough to list exhaustively:

| Selected positions | Selected values | Bitwise OR reached |
|---|---|---|
| none | — | 0 |
| 0 | 2 | 2 |
| 1 | 1 | 1 |
| 0 and 1 | 2, 1 | 3 |

So $1$, $2$ and $3$ are expressible and $4$ is the smallest positive integer that is not — the authored answer for this input. The interesting question is *why* $4$ is out of reach, and the answer is not "the array is too short": `nums` contains no value with bit $2$ set at all, and no combination of $1$ and $2$ can manufacture one.

## 2. The decisive lemma: a single-bit value needs that exact value present

**Lemma.** For every exponent $p \ge 0$, the value $2^p$ is expressible from `nums` if and only if some element of `nums` equals $2^p$.

*If direction.* Choosing the single position that holds $2^p$ yields an OR of $2^p$.

*Only-if direction.* Suppose a selection ORs to exactly $2^p$, whose binary form has bit $p$ set and every other bit clear. Since the OR has bit $p$ set, at least one selected element $v$ has bit $p$ set. That same $v$ contributes all of its other set bits to the OR as well, and OR never clears them. For the result to have no bit other than $p$, $v$ must have no other set bits, so $v = 2^p$. Hence an element equal to $2^p$ must exist in the array.

The lemma is where intuition usually fails, because multi-bit values look helpful. A value like $3 = 2 + 1$ does carry bit $1$, yet it also drags bit $0$ into the result; the reachable value $3$ is not $2$, and no partner element can subtract bit $0$ back out.

| Target | Array | Elements carrying the target bit | Why the target is still unreachable |
|---|---|---|---|
| 4 | `[2,1]` | none (only bits 0 and 1 occur) | no element supplies bit 2 |
| 2 | `[1,3,5,6,7]` | 3, 6, 7 | each also carries bit 0 or bit 2, and OR keeps those bits |
| 4 | `[1,1,2,2,8,8]` | none (elements are $2^0$, $2^1$, $2^3$) | duplicates of 1 and 2 can only rebuild 1, 2, 3, 8, 9, 10, 11 |
| 32 | `[16,1,8,2,4,31]` | none (every element is below 32) | the largest possible OR is $31 = 2^5-1$ |

## 3. The answer is the smallest power of two that is absent

Let $p$ be the smallest exponent with $2^p \notin \texttt{nums}$; the claim is that the answer is exactly $2^p$.

**No smaller positive value is missing.** Take any $x$ with $1 \le x < 2^p$ and write it in binary as a sum of distinct powers,

$$x \;=\; \sum_{j=1}^{m} 2^{e_j}, \qquad e_1 < e_2 < \dots < e_m \le p-1 .$$

Every exponent appearing here is below $p$, and by minimality of $p$ each of the values $2^{e_j}$ occurs in `nums`. Choosing one occurrence per exponent gives distinct positions, and because distinct powers of two have disjoint bit sets, the OR of the chosen values *is* their sum, namely $x$. Every $x$ below $2^p$ is therefore expressible.

**The value $2^p$ itself is not expressible**, by the lemma, since no element equals it.

Combining the two halves, $2^p$ is the minimum positive non-expressible integer. The algorithm is thus a search for the first absent power of two:

$$\text{answer} \;=\; \min\{\,2^p \;:\; p \ge 0,\; 2^p \notin \texttt{nums}\,\}.$$

## 4. Tracing `nums = [2,1]` exponent by exponent

| Exponent $p$ | Power $2^p$ | Present in `nums`? | Consequence |
|---|---|---|---|
| 0 | 1 | yes, position 1 | $1$ expressible as a one-element selection |
| 1 | 2 | yes, position 0 | $2$ expressible; also $3 = 2 \mid 1$ becomes expressible |
| 2 | 4 | no | $4$ is the first absent power, so it is the answer |

The trace also shows the completeness half of the argument at work: $3 < 4$, its binary form is $2^1 + 2^0$, and both powers are present, so selecting `nums[0] = 2` together with `nums[1] = 1` reaches $3$. No selection reaches $4$: the only elements available are $1$ and $2$, their OR is $3$, and $3$ has bit $1$ and bit $0$ set but not bit $2$.

## 5. Applying the test to the awkward inputs

| `nums` | Powers of two present | First absent power | Answer | Note |
|---|---|---|---|---|
| `[2,1]` | 1, 2 | 4 | 4 | small prefix, then a gap |
| `[5,3,2]` | 2 | 1 | 1 | 1 is missing, so nothing smaller can be |
| `[1,3]` | 1 | 2 | 2 | the element 3 has bit 1 set but cannot isolate it |
| `[1,2,4,8]` | 1, 2, 4, 8 | 16 | 16 | four consecutive powers |
| `[7]` | none | 1 | 1 | a lone multi-bit value never reaches 1 |
| `[1,1,2,2,8,8]` | 1, 2, 8 | 4 | 4 | duplicate powers do not fill the missing bit 2 |
| `[1,3,5,6,7]` | 1 | 2 | 2 | extra bits in larger elements do not help |
| `[16,1,8,2,4,31]` | 1, 2, 4, 8, 16 | 32 | 32 | input order is irrelevant; 31 caps every OR at 31 |
| powers $2^0$ through $2^{29}$ | 1, 2, 4, ..., $2^{29}$ | $2^{30}$ | 1073741824 | the answer exceeds every element |

Two rows deserve emphasis. In `[1,1,2,2,8,8]` the array holds three distinct powers with multiplicity, and the reachable set is exactly the set of subset sums of $\{1,2,8\}$: $\{1,2,3,8,9,10,11\}$. Four is missing because no element and no combination carries bit 2 alone; a third copy of 2 would not change that, since the multiset of *bit patterns* is what matters, not the count of elements. In `[16,1,8,2,4,31]` the element `31` contains every bit below 5, which makes it tempting as a universal building block, yet every value here is at most 31, so every OR is at most 31 and 32 remains out of reach. Presence of *bits* is not the criterion; presence of the exact power is.

## 6. Why 31 exponents already decide the answer

The constraint is $1 \le \texttt{nums}[i] \le 10^{9}$, and

$$2^{30} = 1073741824 > 10^{9},$$

so no element can equal $2^{30}$, nor any higher power. Scanning exponents $p = 0, 1, \dots, 30$ therefore always terminates with an absent power, and the answer never exceeds $2^{30}$. This is why the search can stay at machine-word width: the exponent bound comes from the element bound, not from an arbitrary limit. Note that the answer may be far larger than any element, as the final row of the previous table shows.

## 7. Why the reasoning is correct

The proof has one invariant that carries the completeness half: *before testing exponent $p$, every integer in $[1, 2^p - 1]$ is expressible.* It holds initially because the range $[1, 1]$ is empty when $p = 0$. If the invariant holds and $2^p$ is present, then every $x < 2^{p+1}$ is a sum of distinct powers below $p+1$, each of which is present, so OR-combining them reaches $x$ and the invariant advances. If instead $2^p$ is absent, the lemma shows $2^p$ itself is unreachable, so no larger value needs to be examined — every candidate smaller than $2^p$ was already shown expressible by the invariant.

Soundness of the stopping rule and completeness of the reachable prefix therefore come from the same two facts: OR cannot clear bits (so single-bit targets demand single-bit sources), and distinct powers of two OR to their sum (so binary decompositions are realizable). Nothing in the argument uses the order of `nums`, its length beyond the presence of the required positions, or the multiplicity of repeated powers.

## 8. Traps this instance exposes

| Tempting reasoning | Where it breaks | Correct view |
|---|---|---|
| "Enumerate subsequences and OR them." | `[1,1,2,2,8,8]` already has $2^6$ selections. | Only the presence of each exact power of two matters. |
| "Any element with bit $p$ set can supply $2^p$." | `[1,3,5,6,7]` returns 2, not a value built from 3. | OR retains the other bits of every contributor, so a single-bit target needs a single-bit source. |
| "Large elements act as wildcards because they contain many bits." | `[16,1,8,2,4,31]` still answers 32. | Extra bits are noise; 31 cannot create bit 5. |
| "More copies must help." | `[1,1,2,2,8,8]` answers 4 with or without extra copies. | Expressibility depends on the set of distinct bit patterns, not on frequencies. |
| "The answer is bounded by the largest element." | the all-powers input answers $2^{30}$, larger than every element. | The answer is the first absent power, which is one bit above the longest present prefix. |
| "Sorting or deduplicating would change the answer." | — | Order and duplicates are irrelevant; a membership test on 31 values is the whole decision. |

## 9. Time and auxiliary space

Let $n = \texttt{nums.length}$ and let $W = 30$ be the smallest exponent with $2^W > 10^{9}$, the first exponent no legal element can reach.

- **Time** $O(n)$ expected: one pass inserts the $n$ values into a hash set, and then at most $W + 1 = 31$ membership probes locate the first absent power. Since $W$ is a constant fixed by the element bound, the whole procedure is a linear scan with a constant-size tail.
- **Auxiliary space** $O(n)$ for the set of distinct values. A hash set is not strictly necessary: a boolean array indexed by exponent, filled during a single scan that tests whether an element is a power of two within range, uses $O(W) = O(1)$ additional space while keeping the same linear time.

Neither bound depends on the number of expressible values, because the method never enumerates subsets.
