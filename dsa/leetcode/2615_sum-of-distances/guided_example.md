# Guided Example: Sum of Distances

## 1. The instance and the required output

Take `nums = [1, 3, 1, 1, 2]`, whose length is $n = 5$. For each index $i$, the answer asks for the total distance to every *other* index holding the same value:

$$
\text{arr}[i] = \sum_{\substack{0 \le j < n \\ \text{nums}[j] = \text{nums}[i]}} \lvert i - j \rvert ,
$$

where the term $j = i$ contributes $\lvert i - i \rvert = 0$ and may be included harmlessly, or excluded by the condition $j \neq i$. When index $i$ has no partner with the same value, the sum is empty and $\text{arr}[i] = 0$.

| `i` | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `nums[i]` | 1 | 3 | 1 | 1 | 2 |
| required `arr[i]` | 5 | 0 | 3 | 4 | 0 |

The three occurrences of the value $1$ at indices $0$, $2$ and $3$ interact with each other and with nothing else; the values $3$ and $2$ occur once each and therefore produce zeros. The whole difficulty is concentrated in the group $\{0, 2, 3\}$, which is exactly why this instance is representative.

## 2. Grouping equal values into sorted index lists

The sum for index $i$ never mentions a value different from `nums[i]`, so the array decomposes into independent groups that can be solved one at a time. Scan once from left to right and append each index to the bucket of its value; because the scan is in increasing order, every bucket is already sorted.

| value | member indices $p_0 < p_1 < \dots < p_{m-1}$ | group size $m$ | sum of indices | the bucket's answer slots |
|---|---|---|---|---|
| 1 | 0, 2, 3 | 3 | 5 | `arr[0]`, `arr[2]`, `arr[3]` |
| 3 | 1 | 1 | 1 | `arr[1]` |
| 2 | 4 | 1 | 4 | `arr[4]` |

A group of size $m$ costs $O(m)$ work if the distance sum for each of its members can be advanced from the previous member instead of recomputed from scratch. Since $\sum m = n$, the grouping pass and all group work together are linear.

## 3. Splitting a distance sum into a left part and a right part

Fix a group of sorted indices $p_0 < p_1 < \dots < p_{m-1}$ and stand at its $k$-th member, $p_k$. Every other member lies strictly to the left or strictly to the right, so the sum splits into two non-negative halves:

$$
L_k = \sum_{t < k} (p_k - p_t), \qquad R_k = \sum_{t > k} (p_t - p_k), \qquad \text{arr}[p_k] = L_k + R_k .
$$

The first member has an empty left side, and $R_0$ can be computed in closed form from the group's index total:

$$
R_0 = \sum_{t=1}^{m-1} (p_t - p_0) = \left(\sum_{t=0}^{m-1} p_t\right) - m\,p_0 .
$$

| value | $\sum p_t$ | $m$ | $p_0$ | $L_0$ | $R_0 = \sum p_t - m\,p_0$ | $\text{arr}[p_0]$ |
|---|---|---|---|---|---|---|
| 1 | 5 | 3 | 0 | 0 | $5 - 3 \cdot 0 = 5$ | 5 |
| 3 | 1 | 1 | 1 | 0 | $1 - 1 \cdot 1 = 0$ | 0 |
| 2 | 4 | 1 | 4 | 0 | $4 - 1 \cdot 4 = 0$ | 0 |

The singleton rows show a pleasant edge behaviour: for $m = 1$ the formula gives $R_0 = p_0 - p_0 = 0$, so a lonely value needs no special branch at all.

## 4. Advancing from one member to the next

Moving the viewpoint from $p_k$ to $p_{k+1}$ changes both halves. Let $\delta = p_{k+1} - p_k > 0$ be the gap.

- Every one of the $k+1$ members at or before position $k$ becomes exactly $\delta$ farther away, so $L$ grows by $(k+1)\delta$.
- The member at $p_{k+1}$ leaves the right side, and each of the $m - k - 1$ members after it becomes exactly $\delta$ closer, so $R$ shrinks by $(m - k - 1)\delta$.

Keeping $L$ and $R$ as running totals therefore costs one addition and one subtraction per member:

| move | $\delta = p_{k+1} - p_k$ | $L$ before | $\Delta L = (k+1)\delta$ | $L$ after | $R$ before | $\Delta R = (m-k-1)\delta$ | $R$ after |
|---|---|---|---|---|---|---|---|
| $k = 0 \to 1$ | $2 - 0 = 2$ | 0 | $1 \cdot 2 = 2$ | 2 | 5 | $2 \cdot 2 = 4$ | 1 |
| $k = 1 \to 2$ | $3 - 2 = 1$ | 2 | $2 \cdot 1 = 2$ | 4 | 1 | $1 \cdot 1 = 1$ | 0 |

## 5. Invariant and correctness of the running halves

**Invariant.** Immediately before the answer for $p_k$ is read off, the two running totals satisfy

$$
L = L_k = \sum_{t<k}(p_k - p_t), \qquad R = R_k = \sum_{t>k}(p_t - p_k),
$$

so the stored value $L + R$ equals $\text{arr}[p_k]$ exactly.

*Base.* At $k = 0$ the left total is genuinely empty, $L = 0 = L_0$, and the closed form $R = \sum_t p_t - m\,p_0$ equals $\sum_{t>0}(p_t - p_0) = R_0$ because each of the $m$ terms contributes $p_0$ once. Both halves match the definition.

*Step.* Assume the invariant holds at $k$ and the sweep advances to $p_{k+1}$ with gap $\delta$. Then

$$
L_{k+1} = \sum_{t \le k}\big((p_k + \delta) - p_t\big) = \sum_{t<k}(p_k - p_t) + \delta = L_k + (k+1)\delta,
$$

because the $k$ terms with $t < k$ each gain $\delta$ and the single term $t = k$ equals $\delta$; and

$$
R_{k+1} = \!\!\sum_{t > k+1}\!\!\big(p_t - (p_k + \delta)\big) = \Big(\sum_{t>k}(p_t - p_k)\Big) - \delta - (m - k - 2)\delta = R_k - (m - k - 1)\delta .
$$

The two update rules in the table above are therefore not heuristics; they are the definition of $L$ and $R$ rewritten for the next member.

*Termination.* The sweep visits $k = 0, 1, \dots, m-1$, so every member of every group receives a value, and the invariant supplies the exact sum at each visit. Members with no partner belong to a group of size one, whose single visit stores $L + R = 0$, matching the required "no such $j$" behaviour. No index is written twice, because each index belongs to exactly one value bucket.

## 6. Executing the group $\{0, 2, 3\}$ step by step

The group has $m = 3$, indices $p = (0, 2, 3)$, index total $5$, initial $L_0 = 0$ and $R_0 = 5 - 3\cdot 0 = 5$.

| probe $k$ | $p_k$ | members to the left | $L_k$ | members to the right | $R_k$ | stored $\text{arr}[p_k] = L_k + R_k$ |
|---|---|---|---|---|---|---|
| 0 | 0 | none | 0 | $\{2, 3\}$ | $(2-0) + (3-0) = 5$ | 5 |
| 1 | 2 | $\{0\}$ | $2 - 0 = 2$ | $\{3\}$ | $3 - 2 = 1$ | 3 |
| 2 | 3 | $\{0, 2\}$ | $(3-0) + (3-2) = 4$ | none | 0 | 4 |

These are precisely the required values at indices $0$, $2$ and $3$, so together with `arr[1] = 0` and `arr[4] = 0` from the singleton groups the final result is `[5, 0, 3, 4, 0]`. Note how the two halves trade magnitude: $L$ climbs $0 \to 2 \to 4$ while $R$ falls $5 \to 1 \to 0$, and their sum $5 \to 3 \to 4$ is *not* monotone. The answer for a group is unimodal in position — smallest at the centre member — which is a good sanity check on any trace.

## 7. Traps this instance exposes

| trap | what it looks like here | correct handling |
|---|---|---|
| Recomputing each sum with a nested scan | Group $\{0,2,3\}$ would rescan the whole array three times, and with $n = 10^{5}$ that is $10^{10}$ pair evaluations | Group once, then advance $L$ and $R$ incrementally |
| Treating the sum as symmetric | $\text{arr}[0] = 5$ but $\text{arr}[2] = 3$ and $\text{arr}[3] = 4$: equal values do not imply equal answers | The value is symmetric only up to the direction from which the group is scanned |
| Forgetting the empty-partner case | Values $3$ and $2$ occur once each and must give $0$, not a sentinel or an error | Singleton groups come out of the same formula as $0$ |
| Assuming equal values are contiguous | Groups can interleave arbitrarily, and indices inside a bucket stay sorted only because of the left-to-right scan | Never index a group by array order; index it by its sorted member list |
| Assuming a group's answers are consecutive positions | The bucket $\{0,2,3\}$ writes to scattered slots | Write back at the original indices |
| Width of the sum | With $n = 10^{5}$ and one group holding every index, the centre sum reaches roughly $2 \cdot (1 + 2 + \dots + 5 \cdot 10^{4}) \approx 2.5 \times 10^{9}$, beyond a 32-bit integer | Use a 64-bit or arbitrary-precision accumulator |
| Single-element input | With `nums = [5]` the array has no pair at all | The result is `[0]`; nothing in the method is undefined |

## 8. Complexity

**Time.** One linear scan builds the buckets, costing $O(n)$ expected time under hashing. Inside a group of size $m$, the closed-form start costs $O(m)$ for the index total, and each of the $m - 1$ transitions costs constant work, so the group costs $O(m)$; summing over groups gives $O(n)$. The whole method is therefore

$$
O(n)
$$

expected time, against $O(n^{2})$ for the direct double loop that evaluates every same-valued pair separately. With $n \le 10^{5}$ the linear bound is the difference between roughly $10^{5}$ and $10^{10}$ basic operations.

**Auxiliary space.** The index buckets store exactly $n$ integers in total, one per array position, and the output array holds $n$ entries, so the extra storage is $O(n)$. Group sizes and index totals are scalars updated during the scan and add no asymptotic cost.
