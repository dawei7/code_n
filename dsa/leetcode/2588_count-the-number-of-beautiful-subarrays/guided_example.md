# Guided Example: Count the Number of Beautiful Subarrays

## 1. The instance we will count

Take the first official instance:

$$
\texttt{nums} = [4, 3, 1, 2, 4],
$$

so $n = 5$ and the array has $\frac{5 \cdot 6}{2} = 15$ non-empty contiguous subarrays. The required outcome is `2`, and the two qualifying subarrays are `nums[1..3] = [3, 1, 2]` and the whole array `nums[0..4] = [4, 3, 1, 2, 4]`.

The operation is unusual enough to deserve restating carefully. One move chooses two *different* indices $i$ and $j$ together with a bit position $k$ such that the $k$-th bit is `1` in **both** $\text{nums}[i]$ and $\text{nums}[j]$, then subtracts $2^k$ from each of the two values. Subtracting $2^k$ from a value whose $k$-th bit is `1` is exactly clearing that bit, so one move clears the same bit position in two different elements at once. A subarray is **beautiful** when some sequence of such moves zeroes every one of its elements; zero moves are allowed, which is why an all-zero subarray is beautiful by definition.

## 2. What a move does, in bits

Because a move always touches one bit position in exactly two elements, it never changes any bit's *counting parity*. Look at the bit positions of the two chosen elements before and after the move, using the official reduction of `[3, 1, 2]`.

| Value (decimal) | Binary (bits `2,1,0`) | Bit `2` | Bit `1` | Bit `0` |
|---|---|---|---|---|
| `3` | `011` | 0 | 1 | 1 |
| `1` | `001` | 0 | 0 | 1 |
| `2` | `010` | 0 | 1 | 0 |
| Count of set bits per position | — | 0 | 2 | 2 |
| Parity of that count | — | even | even | even |

The move that the statement applies first chooses $k = 1$ and the elements `3` and `2`, subtracting $2^1 = 2$ from each: the subarray becomes `[1, 1, 0]`. Bit `1` was set in both of those elements and is now cleared in both, so the count of elements with bit `1` set fell from $2$ to $0$ — it changed by two, so its parity did not change. Every other bit position is untouched, and the other elements are untouched as well. The second move chooses $k = 0$ and the two elements equal to `1`, producing `[0, 0, 0]`, which again lowers a per-bit count by exactly two.

## 3. The invariant, and the condition it forces

Define, for a fixed subarray and a fixed bit position $k$,

$$
c_k \;=\; \bigl\lvert\{\, \text{element } x \text{ of the subarray} : \text{bit } k \text{ of } x \text{ is } 1 \,\}\bigr\rvert .
$$

A move either leaves $c_k$ unchanged (when bit $k$ is not the chosen position) or decreases it by exactly $2$ (when bit $k$ is chosen, since both participants had the bit set). Hence

$$
c_k \bmod 2 \quad \text{is invariant under every move},
$$

for each bit position $k$. Reaching the all-zero subarray would make every $c_k$ equal to $0$, which is even, so a subarray can only be beautiful if **every** $c_k$ is even to begin with. The parity vector $(c_2 \bmod 2, c_1 \bmod 2, c_0 \bmod 2, \dots)$ is an invariant of the move system, and the all-zero target has the parity vector of all zeros.

The parity vector has a familiar name: the bitwise XOR of the subarray has, at position $k$, the parity of the number of set bits at position $k$. Therefore

$$
\text{subarray XOR} \;=\; \text{nums}[l] \oplus \text{nums}[l+1] \oplus \dots \oplus \text{nums}[r] \;=\; 0
$$

is exactly the statement that every $c_k$ is even. The necessary condition is a single integer test.

## 4. Why the condition is also sufficient

Even parities are not merely necessary; they are enough. Suppose every $c_k$ is even. If some element is nonzero, it has a set bit at some position $k$; since $c_k$ is even and at least $1$, some *other* element also has bit $k$ set, so a legal move with that $k$ exists. Apply it: two elements lose the same bit, so the sum of the elements strictly decreases while every parity is preserved.

The argument closes by induction on the total sum $T = \sum x$ of the subarray, a non-negative integer that drops by $2^{k+1} > 0$ on each move. If $T = 0$ the subarray is already all zeros. Otherwise a legal move exists, as just shown, and after it the sum is smaller while all parities are still even — so by induction the remaining configuration can be zeroed. The construction produces at most $\tfrac{1}{2}\sum_k c_k$ moves, and it never needs a bit position to be chosen twice.

Combining the two directions gives the characterisation that the whole solution rests on:

$$
\text{subarray } \text{nums}[l..r] \text{ is beautiful} \iff \text{nums}[l] \oplus \dots \oplus \text{nums}[r] = 0 .
$$

Individual positions are irrelevant: only the XOR of the range matters.

## 5. Counting zero-XOR ranges with prefix XORs

Testing each of the $\Theta(n^2)$ subarrays separately is too slow for $n \le 10^5$, so the XOR condition is rewritten in terms of prefix values. Let

$$
P_0 = 0, \qquad P_i = \text{nums}[0] \oplus \text{nums}[1] \oplus \dots \oplus \text{nums}[i-1] \quad (1 \le i \le n).
$$

Then the XOR of the range $\text{nums}[l..r]$ telescopes as $P_l \oplus P_{r+1}$, because every element strictly inside the range appears in both prefix values and cancels under XOR. So

$$
\text{nums}[l] \oplus \dots \oplus \text{nums}[r] = 0 \iff P_l = P_{r+1}.
$$

Counting beautiful subarrays becomes counting pairs of *equal prefix values*: choose two distinct indices $u < v$ among $0, 1, \dots, n$ with $P_u = P_v$, and the pair corresponds to exactly one non-empty subarray, namely $\text{nums}[u..v-1]$. When a prefix value occurs $m$ times, it contributes $\binom{m}{2}$ such pairs. This is a pure counting identity, so no enumeration of subarrays is needed.

| Prefix index $i$ | Values included | Prefix XOR $P_i$ |
|---|---|---|
| 0 | none | `0` |
| 1 | `4` | `4` |
| 2 | `4, 3` | `7` |
| 3 | `4, 3, 1` | `6` |
| 4 | `4, 3, 1, 2` | `4` |
| 5 | `4, 3, 1, 2, 4` | `0` |

Reading the equal pairs off this table gives the answer immediately: $P_0 = P_5 = 0$ contributes the whole array, and $P_1 = P_4 = 4$ contributes $\text{nums}[1..3] = [3, 1, 2]$. Every other prefix value occurs once and contributes nothing. The two pairs match the two beautiful subarrays named in Section 1, and the total is $\binom{2}{2} + \binom{2}{2} = 1 + 1 = 2$.

## 6. Executing the one-pass sweep

A single left-to-right pass computes the prefix XORs and counts, for each new prefix value, how many equal prefix values were seen before it. That count is exactly the number of beautiful subarrays ending at the current position. The working state is one running XOR (the mask) plus a multiset of earlier prefix values; the empty prefix contributes the initial entry for `0`, because the empty prefix is a legitimate partner for any later prefix equal to `0`.

| Step | `nums[i]` | Mask after XOR | Earlier prefixes equal to the mask | Added to answer | Answer | Multiplicity stored for the mask |
|---|---|---|---|---|---|---|
| start | — | `0` | — | — | 0 | `0` seen once, before any element |
| 1 | `4` | `4` | none | 0 | 0 | `4` seen once |
| 2 | `3` | `7` | none | 0 | 0 | `7` seen once |
| 3 | `1` | `6` | none | 0 | 0 | `6` seen once |
| 4 | `2` | `4` | `P_1 = 4` | 1 | 1 | `4` seen twice |
| 5 | `4` | `0` | `P_0 = 0` | 1 | 2 | `0` seen twice |

Step 4 pairs the new prefix $P_4 = 4$ with the earlier $P_1 = 4$, which certifies the subarray `nums[1..3]`. Step 5 pairs $P_5 = 0$ with the initial $P_0 = 0$, which certifies the whole array. The final answer is `2`, as required. Note that the sweep never needs the subarray boundaries: the multiplicity of the mask *is* the number of valid left endpoints, and it is read before the mask is inserted so that a prefix is never paired with itself.

## 7. Where the tempting alternatives break

| Alternative | Complexity | Why it is not used here |
|---|---|---|
| Enumerate all $\Theta(n^2)$ subarrays and XOR each range by an inner loop | $O(n^3)$ | The triple loop re-derives the same XORs repeatedly; hopeless at $n = 10^5$ |
| Precompute prefix XORs, then test every pair $(u, v)$ directly | $O(n^2)$ | Still $\Theta(n^2)$ pairs, around $5 \times 10^9$ tests at the maximum length |
| Sort the prefix values and count equal neighbours | $O(n \log n)$ | Correct and deterministic, but it discards the streaming structure and stores the whole prefix array |
| Simulate the moves to decide beauty | exponential in the worst case | Unnecessary: Section 4 replaced simulation with a parity argument |
| Count only subarrays whose elements are nonzero and cancel pairwise | $O(n)$ but wrong | Ranges such as `[1, 1]` and `[1, 2, 3]` qualify for reasons that pairwise equality does not describe |

The last row is the trap this instance is chosen to expose. Subarray `[3, 1, 2]` contains no repeated value at all, yet it is beautiful because bit `1` appears twice (in `3` and `2`) and bit `0` appears twice (in `3` and `1`); the pairing is over *bits*, not over equal values. Any reasoning that looks for duplicate elements, or for a zero element, will miss it.

## 8. Boundary conditions and traps

| Situation | Instance | Outcome | Why |
|---|---|---|---|
| Single zero element | `nums = [0]` | `1` | $P_0 = P_1 = 0$, one pair; the note states that no operation is needed |
| Single nonzero element | `nums = [7]` | `0` | A move needs two different indices and the subarray has one, so a nonzero element can never be cleared |
| Two equal values | `nums = [1, 1]` | `1` | $P_0 = 0$, $P_1 = 1$, $P_2 = 0$: the pair $(P_0, P_2)$ certifies the whole array |
| Three equal values | `nums = [5, 5, 5]` | `2` | Prefixes are `0, 5, 0, 5`; the overlapping ranges `[5,5]` at offsets $0$ and $1$ are counted separately |
| Unknown values that cancel | `nums = [1, 2, 3]` | `1` | $1 \oplus 2 \oplus 3 = 0$ although all three values differ |
| A zero in the middle | `nums = [1, 0, 1]` | `2` | $P_0 = 0$, $P_1 = 1$, $P_2 = 1$, $P_3 = 0$: the range `[0]` alone and the whole array qualify |
| All elements zero | `nums = [0, 0, 0, 0]` | `10` | All five prefixes equal `0`, giving $\binom{5}{2} = 10$ ranges, i.e. every non-empty subarray |
| Values at the maximum | `nums = [1000000, 1000000]` | `1` | Equal values cancel; the prefix mask stays below $2^{20}$, so no overflow concept applies |

Three traps stand out. First, the answer counts pairs of equal prefix values *including* pairs whose common value is nonzero: the pair $P_1 = P_4 = 4$ in Section 5 is what certifies `[3, 1, 2]`, so restricting attention to prefixes equal to `0` would return `1` instead of `2`. Second, the prefix index range is $0 \le i \le n$, which is $n + 1$ values, one more than the number of elements; forgetting the empty prefix loses exactly those subarrays that start at index $0$. Third, subarrays are non-empty and are counted as distinct ranges: overlapping subarrays that share the same values, such as the two `[5, 5]` ranges inside `[5, 5, 5]`, are counted separately, so no deduplication of values is ever performed.

## 9. Why the reasoning is correct

**Soundness (every counted subarray is beautiful).** If the sweep pairs a new prefix $P_v$ with an earlier prefix $P_u$ of the same value, then the subarray $\text{nums}[u..v-1]$ has XOR $P_u \oplus P_v = 0$, because XOR is associative, commutative, and self-inverse, so each element of the range cancels against its own occurrence in the two prefixes. By Section 4, zero XOR means every per-bit count is even, which means a zeroing sequence exists. Every pair the sweep counts therefore certifies a genuinely beautiful subarray, and distinct pairs $(u, v)$ correspond to distinct ranges, so no range is counted twice.

**Completeness (every beautiful subarray is counted).** If $\text{nums}[l..r]$ is beautiful, its XOR is $0$, hence $P_l = P_{l} \oplus 0 = P_{r+1}$, and the two prefix indices $l$ and $r+1$ satisfy $l < r + 1$ because the range is non-empty. When the sweep reaches index $r+1$, the earlier prefix $P_l$ has already been inserted — insertion happens at the end of each step — so the multiplicity of the mask includes it, and the pair is added to the answer. No beautiful subarray is missed.

**Invariant of the sweep.** After processing element $i$, the multiset held by the sweep contains each prefix value $P_0, \dots, P_i$ as many times as it occurs among those indices, and the accumulated answer equals the number of pairs $u < v \le i$ with $P_u = P_v$. Both parts are established by induction: the update inserts the new mask exactly once, and the answer grows by the number of earlier occurrences, which is precisely the number of new equal pairs created by appending index $i$. At the end, $i = n$, so the accumulated count is the number of equal-prefix pairs over $0 \le u < v \le n$ — the number of beautiful subarrays.

## 10. Complexity: time and auxiliary space

**Time.** The sweep performs exactly $n$ steps, each doing one XOR, one multiset lookup, one insertion, and one addition, so the counting work is $\Theta(n)$ plus the cost of the multiset operations. With a hash table those operations are $O(1)$ expected, giving $\Theta(n)$ expected total time; with a balanced search tree they are $O(\log n)$ each, giving $O(n \log n)$ worst case. The alternative of enumerating subarrays costs $\Theta(n^2)$ or worse, which is why the prefix reformulation is decisive at $n = 10^5$. Note that a single sweep replaces the whole $\Theta(n^2)$ family of range-XOR queries.

**Auxiliary space.** The multiset stores at most $n + 1$ prefix values, so the auxiliary space is $O(n)$; the answer counter, the running mask, and the loop index are $O(1)$. Because the mask is a prefix XOR of values bounded by $10^6 < 2^{20}$, every stored key fits in $20$ bits, and the total number of beautiful subarrays can reach $\binom{10^5+1}{2} \approx 5 \times 10^{9}$, so the answer accumulator must be wide enough for values far beyond a 32-bit signed integer.